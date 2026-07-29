# Public Plugin Submission Notes

## Listing

- Name: Code Ontology Explorer
- Version: 0.1.0
- Developer: battle-doll
- Category: Developer Tools
- Distribution: Public
- Component type: Skills only
- License: Apache-2.0

Short description:

> Local-first code knowledge graphs

Long description:

> Statically map an authorized Java, Spring, or Python repository into a local knowledge graph. Search symbols, inspect possible change impact, export portable RDF/Turtle, and create a self-contained visualization. The bundled analyzer does not execute target code or make direct network requests; normal Codex processing remains governed by OpenAI's terms and privacy policy.

## Access and data-use declaration

| Area | Version 0.1 behavior |
| --- | --- |
| Authentication | None |
| Network access | Bundled analyzer: none; normal Codex platform processing is disclosed separately |
| External APIs | None |
| Telemetry/analytics | None |
| Target code execution | None |
| Reads | Authorized regular `.java` and `.py` files under explicit repository path |
| Exclusions | Secrets, keys, env files, symlinks, VCS, dependencies, build outputs, caches |
| Writes | Explicit index path outside the target repository; visualization beside that index |
| Local artifacts | Symbols, relationships, language labels, qualified names, relative paths, counts |
| Not retained | Source bodies, comments, strings, absolute paths, hashes, credentials, prompts |
| Separate uploads | None |
| Background services | None |
| Hooks | None |
| MCP servers | None |
| Apps/widgets | None |
| Package installation | None |
| Models/model weights | None |

## Review rationale

The first public release intentionally excludes automatic installers, local models, graph databases, Tomcat, watchers, MCP servers, and remote AI calls. Those features materially expand permissions, supply-chain exposure, resource use, privacy disclosures, and licensing obligations.

The plugin asks Codex to:

1. verify repository authorization;
2. run a no-write preflight;
3. display the safety summary;
4. obtain confirmation before writing artifacts;
5. keep artifacts outside the target repository;
6. describe output as static evidence, not runtime truth.

The analyzer enforces key boundaries independently of the prompt: authorization flag, outside-repository output, link/reparse-point avoidance, sensitive-path exclusions, source-size limit, no direct network requests, and no target execution.

## Evaluation cases

The machine-readable review set is [evals/cases.json](evals/cases.json). It includes five positive cases and three negative/abuse cases covering authorization, analyzer-local behavior, Spring/Python analysis, visualization, secret exfiltration, and silent software installation.

## Legal and policy materials

- [LICENSE](LICENSE)
- [NOTICE](NOTICE)
- [PRIVACY.md](PRIVACY.md)
- [TERMS.md](TERMS.md)
- [SECURITY.md](SECURITY.md)
- [THREAT_MODEL.md](THREAT_MODEL.md)
- [SUPPORT.md](SUPPORT.md)
- [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)
- [TRADEMARKS.md](TRADEMARKS.md)
- [SBOM.spdx.json](SBOM.spdx.json)

Final publisher attestations must be reviewed and accepted by the publisher personally. They are not delegated to an automated agent.
