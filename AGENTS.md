# Working on Otterpack

Otterpack curates independent projects. Keep changes focused on this repository unless the user explicitly includes an upstream project.

- Preserve upstream authors, licenses and pinned source references. Root MIT does not relicense the AGPL Herdr Remote patch.
- Never collect credentials, private endpoints, sessions, logs or complete personal configurations into the pack.
- Treat presets as fragments. Do not silently overwrite user configuration or install/start services.
- Distinguish screenshots, actual terminal-output renders and illustrations. Use synthetic demonstration data and record how each image was captured.
- Record actual verification and its limits. Do not reuse historical claims as proof of the current bundle.
- Use Python 3.11+ for the helpers. Run `python3 scripts/verify.py` and `python3 -m unittest discover -s tests -v` after relevant changes.
- Keep source reconstruction pinned and checksummed. Never accept an existing destination or execute downloaded source automatically.
