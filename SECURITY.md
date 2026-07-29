# Security Policy

## Supported version

Security fixes are provided for the latest released version.

## Report a vulnerability

Do not include private source code, secrets, credentials, or generated ontology artifacts in a public issue.

Report a vulnerability through GitHub's private vulnerability reporting for:

https://github.com/battle-doll/code-ontology-explorer

If private reporting is unavailable, open a minimal public issue asking the maintainer to enable a private channel. Include no exploit details or confidential data.

## Security model

Version 0.1:

- uses static parsing only;
- never imports or executes target code;
- does not follow symlinks;
- enforces file-size and path exclusions;
- makes no direct network requests;
- has no authentication or secret inputs;
- starts no server or background process;
- writes indexes only outside the target repository and visualizations only beside an index.

The output is not automatically safe to publish. Symbol names and relative paths may reveal confidential architecture.
