# Code Ontology Explorer

Code Ontology Explorer is an independent Codex plugin that creates a local-first knowledge graph from an authorized Java/Spring or Python repository.

Its bundled Python analyzer performs deterministic static analysis, exports RDF 1.1 Turtle, searches symbols, explores possible change impact, and creates a self-contained graph. The analyzer does not execute target code, make direct network requests, install dependencies, or upload source.

Codex may process command output—such as symbols, counts, and repository-relative paths—to carry out the requested workflow. That platform processing is governed by OpenAI's [applicable terms](https://openai.com/policies/terms-of-use/) and [privacy policy](https://openai.com/policies/privacy-policy/). This plugin does not make Codex an offline product.

## What version 0.1 does

- Maps Java packages, imports, classes, interfaces, methods, inheritance, and basic dependencies.
- Recognizes common Spring stereotypes, bean factories, constructor/field injection, AOP advice, and proxy/interceptor annotations.
- Maps Python modules, imports, classes, functions, decorators, calls, inheritance, and heuristic data-pipeline roles.
- Produces `ontology.json`, portable `ontology.ttl`, and a privacy/coverage report.
- Searches the local graph and explores a bounded static relationship neighborhood.
- Generates a standalone HTML/SVG visualization with no CDN or plugin telemetry.

## Privacy and safety defaults

- Analyze only code you own or are authorized to inspect.
- Preflight is read-only and creates no files.
- Indexing requires an explicit `--authorized` confirmation.
- Artifacts must be written outside the target repository.
- Source bodies, comments, strings, absolute paths, and file hashes are not retained.
- Secret-like files, symlinks/reparse points, dependencies, VCS data, and generated outputs are excluded.
- Target projects are never imported, built, tested, or run.

Symbol names and repository-relative paths can still be confidential. Keep generated artifacts local unless you separately approve sharing them.

## Requirements

- Codex with plugin/skill support
- Python 3.10 or newer
- No Python packages, database, local model, or server

## Manual quick start

```bash
python3 skills/explore-code-ontology/scripts/code_ontology.py \
  preflight --repo "/path/to/authorized/repository"
```

After reviewing preflight and confirming artifact creation:

```bash
python3 skills/explore-code-ontology/scripts/code_ontology.py \
  index \
  --repo "/path/to/authorized/repository" \
  --output "/path/outside/repository/code-ontology" \
  --authorized
```

Search:

```bash
python3 skills/explore-code-ontology/scripts/code_ontology.py \
  query \
  --index "/path/code-ontology/ontology.json" \
  --term "OrderService"
```

Visualize:

```bash
python3 skills/explore-code-ontology/scripts/code_ontology.py \
  visualize \
  --index "/path/code-ontology/ontology.json" \
  --output "/path/code-ontology/graph.html"
```

## RDF portability

The Turtle export uses stable URNs for entities and a documented `co:` namespace. It can be imported into RDF 1.1-compatible stores. Store installation, remote endpoints, SPARQL services, automatic watchers, local LLMs, and MCP servers are intentionally not included in version 0.1.

Those features are possible future extensions, but each adds meaningful permissions, licenses, resource use, or data-transfer decisions. They should remain opt-in components with their own review.

## Static-analysis limits

The graph is evidence for navigation and planning, not a runtime trace or correctness proof. Reflection, generated code, runtime Spring conditions, dynamic proxies, configuration, dependency versions, and Python metaprogramming may be incomplete.

## Development

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_package.py
```

Security issues: see [SECURITY.md](SECURITY.md). General support: see [SUPPORT.md](SUPPORT.md).

## License and independence

Source code is licensed under Apache-2.0. This project is independent and is not affiliated with or endorsed by OpenAI, Broadcom, VMware, the Spring project, Oracle, or the Python Software Foundation. Product names are used only to describe compatibility.
