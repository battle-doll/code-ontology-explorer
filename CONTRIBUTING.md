# Contributing

Contributions should preserve the analyzer-local, static, least-privilege defaults.

Before proposing a change:

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_package.py
```

Use synthetic fixtures. Do not commit private repositories, source excerpts from third parties, credentials, generated ontology artifacts from real projects, model weights, or copied vendor schemas.

Changes that add network access, target-code execution, package installation, authentication, telemetry, background services, hooks, MCP, or an external database require a separate design and updated privacy, security, threat-model, test, and submission review.

By submitting a contribution, you represent that you have the right to license it under Apache-2.0.
