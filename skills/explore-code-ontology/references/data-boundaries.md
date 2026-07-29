# Data boundaries

## Authorized inputs

Analyze only a local repository the user owns, administers, or is explicitly permitted to inspect. A path supplied by another person is not proof of authorization.

## Data read

Version 0.1 reads regular `.java` and `.py` files up to 2 MiB. It does not follow symbolic links or Windows reparse points. It skips common dependency, VCS, generated-output, IDE, virtual-environment, and cache directories.

Files whose names suggest credentials, secrets, tokens, private keys, keystores, or `.env` configuration are excluded even if they use a supported extension.

## Data retained

Artifacts may retain:

- symbol and annotation names;
- language and node/relationship types;
- qualified names;
- repository-relative source paths;
- aggregate counts and parse warnings.

Artifacts do not intentionally retain:

- source bodies, string literals, or comments;
- absolute source paths;
- file contents or hashes;
- environment variables, credentials, API keys, or tokens;
- prompts or model outputs.

Identifiers and relative paths can still be confidential. Keep artifacts local by default and obtain separate authorization before sharing them.

## Writes

Preflight writes nothing. Indexing writes only to an explicit output directory that is neither inside nor a parent of the target repository. Visualization writes only to an explicit `.html` destination in the existing index directory. Existing artifacts are not replaced without a separate overwrite flag and confirmation.

## Network and execution

The bundled analyzer makes no direct network requests and does not import, compile, build, test, or execute target code. It installs no packages and starts no services.

Codex may process analyzer command output to provide the requested workflow. That platform processing is governed by OpenAI's applicable terms and privacy policy. The v0.1 skill does not invoke a separate remote data service or upload generated artifacts.

## Interpretation

The graph is static evidence. Reflection, runtime bean conditions, generated proxies, external configuration, dynamic imports, monkey-patching, dependency injection containers, and generated code may change actual runtime behavior.
