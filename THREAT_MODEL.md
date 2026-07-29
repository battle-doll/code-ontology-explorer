# Threat Model

## Assets to protect

- target source code and architecture;
- credentials and configuration near the source tree;
- integrity of the target repository;
- integrity of existing local artifacts;
- user control over network transfer, software installation, and background processes.

## Trust boundaries

Repository contents are untrusted even when the repository is authorized. Filenames, package names, symbols, annotations, decorators, and syntax errors may be adversarial or instruction-like. Generated ontology artifacts are data, not instructions.

Codex orchestrates the workflow, but the analyzer independently enforces core filesystem and execution boundaries.

## Main threats and mitigations

| Threat | Mitigation |
| --- | --- |
| Prompt injection in source or paths | Source bodies, comments, and strings are not emitted; skill instructs Codex to treat all identifiers and artifacts as untrusted data |
| Secret collection | Secret-like filenames/extensions and common sensitive/generated directories are excluded |
| Symlink escape | Directory walking does not follow symbolic links; symlink files and directories are skipped |
| Target-code execution | No import/build/test/runtime path; analyzer rejects process/network primitives in package validation |
| Repository modification | Index output must be outside and not a parent of the target repository; visualization must stay beside that index |
| Artifact overwrite | Existing outputs require a separate `--overwrite` flag and user confirmation |
| Data exfiltration | Analyzer has no network imports or requests; plugin has no MCP, app, hook, auth, or telemetry |
| Resource exhaustion | Supported extensions only, 2 MiB per-file limit, bounded query and graph limits |
| HTML injection | Visualization escapes the document title and safely embeds JSON; it loads no remote scripts |
| False runtime conclusions | Documentation labels findings as incomplete static evidence |

## Residual risks

- Symbol names and repository-relative paths may reveal confidential architecture.
- Very large repositories may consume noticeable CPU and memory despite per-file limits.
- Static parsing may miss or misclassify dynamic behavior.
- A compromised Python runtime or Codex host is outside this plugin's security boundary.
- Users can choose to share generated artifacts after creation; the plugin cannot control downstream copies.

## Security-changing extensions

Network access, target execution, local models, databases, watchers, servers, MCP endpoints, authentication, telemetry, or automatic package installation require a new threat-model and privacy review before release.
