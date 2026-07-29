# Privacy Policy

Effective date: July 29, 2026

Code Ontology Explorer processes supported source files locally at the user's request.

## Data processed

The analyzer may read regular `.java` and `.py` files in a repository the user identifies and is authorized to inspect. It derives symbol names, annotations/decorators, qualified names, structural relationships, language labels, and repository-relative paths.

It does not intentionally retain source bodies, comments, string literals, absolute source paths, file hashes, credentials, API keys, environment variables, prompts, or model output.

Secret-like filenames, private-key and keystore extensions, symbolic links/reparse points, common version-control folders, dependency folders, build outputs, caches, and virtual environments are excluded.

## Local storage

Preflight creates no files. With explicit user confirmation, indexing writes JSON, RDF/Turtle, and Markdown artifacts only to the user-selected directory outside the target repository. Visualization writes a self-contained HTML file beside that index.

Generated identifiers and relative paths may still be confidential. Users control the artifacts and should not share them without authorization.

## Network, Codex processing, telemetry, and third parties

The following statements describe the bundled Python analyzer itself. The analyzer:

- makes no direct network requests;
- collects no telemetry or analytics;
- uses no accounts, cookies, advertising identifiers, or remote APIs;
- sends no source or ontology data to the developer;
- installs no packages, models, databases, or services.

When Codex invokes this skill, command output such as aggregate counts, symbol names, qualified names, parse warnings, and repository-relative paths may be processed by OpenAI to provide the requested Codex functionality. Codex is governed by OpenAI's [applicable terms](https://openai.com/policies/terms-of-use/) and [privacy policy](https://openai.com/policies/privacy-policy/). The user's operating system is governed by its provider's terms and policies.

The plugin publisher receives no analysis data directly from the bundled analyzer.

## Retention and deletion

The developer receives and retains no analysis data. Users can delete generated artifacts with their normal local file-management tools.

## Contact

Privacy questions can be filed at:

https://github.com/battle-doll/code-ontology-explorer/issues
