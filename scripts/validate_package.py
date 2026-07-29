#!/usr/bin/env python3
"""Validate the public plugin source without third-party dependencies."""

from __future__ import annotations

import ast
import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / ".codex-plugin" / "plugin.json"
SKILL_PATH = ROOT / "skills" / "explore-code-ontology"
ANALYZER_PATH = SKILL_PATH / "scripts" / "code_ontology.py"
VERSION = "0.1.0"
REQUIRED_FILES = [
    "LICENSE",
    "NOTICE",
    "README.md",
    "PRIVACY.md",
    "TERMS.md",
    "SECURITY.md",
    "THREAT_MODEL.md",
    "SUPPORT.md",
    "THIRD_PARTY_NOTICES.md",
    "TRADEMARKS.md",
    "SBOM.spdx.json",
    "evals/cases.json",
    "assets/logo.png",
    "assets/logo-dark.png",
    "assets/composer-icon.png",
    "skills/explore-code-ontology/SKILL.md",
    "skills/explore-code-ontology/agents/openai.yaml",
    "skills/explore-code-ontology/references/data-boundaries.md",
    "skills/explore-code-ontology/references/ontology-model.md",
    "skills/explore-code-ontology/references/schema.ttl",
    "skills/explore-code-ontology/scripts/code_ontology.py",
]
FORBIDDEN_IMPORT_ROOTS = {
    "requests",
    "httpx",
    "aiohttp",
    "boto3",
    "paramiko",
    "socket",
    "subprocess",
    "urllib.request",
}


def fail(message: str) -> None:
    raise AssertionError(message)


def validate_required_files() -> None:
    missing = [relative for relative in REQUIRED_FILES if not (ROOT / relative).is_file()]
    if missing:
        fail(f"Missing required files: {', '.join(missing)}")


def validate_manifest() -> None:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    if manifest["name"] != "code-ontology-explorer":
        fail("Unexpected manifest name")
    if manifest["version"] != VERSION:
        fail("Manifest version mismatch")
    if manifest["license"] != "Apache-2.0":
        fail("Unexpected license identifier")
    if set(manifest).intersection({"hooks", "mcpServers", "apps"}):
        fail("Version 0.1 must remain skills-only")
    prompts = manifest["interface"]["defaultPrompt"]
    if not 1 <= len(prompts) <= 3 or any(len(prompt) > 128 for prompt in prompts):
        fail("Default prompt count or length is invalid")
    for field in ("websiteURL", "privacyPolicyURL", "termsOfServiceURL"):
        if not manifest["interface"][field].startswith("https://"):
            fail(f"{field} must use HTTPS")
    for field in ("composerIcon", "logo", "logoDark"):
        asset = (ROOT / manifest["interface"][field]).resolve()
        if not asset.is_file() or ROOT not in asset.parents:
            fail(f"Invalid manifest asset: {field}")


def validate_evals() -> None:
    cases = json.loads((ROOT / "evals" / "cases.json").read_text(encoding="utf-8"))
    if cases["plugin_version"] != VERSION:
        fail("Eval version mismatch")
    if len(cases["positive_cases"]) < 5:
        fail("At least five positive evaluation cases are required")
    if len(cases["negative_cases"]) < 3:
        fail("At least three negative evaluation cases are required")
    identifiers = [
        item["id"] for group in ("positive_cases", "negative_cases") for item in cases[group]
    ]
    if len(identifiers) != len(set(identifiers)):
        fail("Evaluation case IDs must be unique")


def imported_modules(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    modules: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            modules.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            modules.add(node.module)
    return modules


def validate_analyzer_boundaries() -> None:
    imports = imported_modules(ANALYZER_PATH)
    forbidden = {
        module
        for module in imports
        if module in FORBIDDEN_IMPORT_ROOTS
        or module.split(".", 1)[0] in FORBIDDEN_IMPORT_ROOTS
    }
    if forbidden:
        fail(f"Network or process imports are not allowed: {sorted(forbidden)}")
    source = ANALYZER_PATH.read_text(encoding="utf-8")
    if f'PLUGIN_VERSION = "{VERSION}"' not in source:
        fail("Analyzer version mismatch")
    for token in ("eval(", "exec(", "os.system(", "Popen(", "shell=True"):
        if token in source:
            fail(f"Target execution primitive found: {token}")


def validate_text_hygiene() -> None:
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in {".git", "dist", "__pycache__"} for part in path.parts):
            continue
        if path.suffix.lower() not in {".md", ".json", ".yaml", ".yml", ".py", ".ttl", ".svg", ""}:
            continue
        text = path.read_text(encoding="utf-8", errors="strict")
        placeholder = "TO" + "DO"
        if re.search(rf"\[{placeholder}(?::|\])|{placeholder}:", text, flags=re.IGNORECASE):
            fail(f"Unresolved placeholder found: {path.relative_to(ROOT)}")
        local_posix = "/Users/" + "aether/"
        local_windows = "\\Users\\" + "aether\\"
        if local_posix in text or local_windows in text:
            fail(f"Local absolute path leaked: {path.relative_to(ROOT)}")


def run(command: list[str]) -> None:
    process = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=False)
    if process.returncode:
        sys.stderr.write(process.stdout)
        sys.stderr.write(process.stderr)
        fail(f"Command failed: {' '.join(command)}")


def validate_skill_metadata() -> None:
    openai_yaml = (SKILL_PATH / "agents" / "openai.yaml").read_text(encoding="utf-8")
    if "$explore-code-ontology" not in openai_yaml:
        fail("openai.yaml default prompt must mention $explore-code-ontology")
    skill_text = (SKILL_PATH / "SKILL.md").read_text(encoding="utf-8")
    if not skill_text.startswith("---\nname: explore-code-ontology\n"):
        fail("Unexpected skill frontmatter")


def main() -> int:
    validate_required_files()
    validate_manifest()
    validate_evals()
    validate_analyzer_boundaries()
    validate_text_hygiene()
    validate_skill_metadata()
    run([sys.executable, "-m", "py_compile", str(ANALYZER_PATH)])
    run([sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"])
    print("PASS: source package, safety boundaries, metadata, evals, and tests")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, KeyError, json.JSONDecodeError, SyntaxError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
