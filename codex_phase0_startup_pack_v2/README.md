# Codex Phase 0 Startup Pack v2

This pack is designed to be copied into the target repository root **before** running Phase 0.

## What changed in v2

- Added the missing `templates/` directory that the prompt already referenced.
- Added schemas for `dev_plan.yaml`, `acceptance_spec.yaml`, and `run_policy.yaml`.
- Added a repo-scoped Codex config example at `.codex/config.toml.example`.
- Added a startup-pack validator script.
- Added a concrete README with recommended run commands.

## Recommended use

1. Copy this pack into your repository root.
2. Review `.codex/config.toml.example` and rename it to `.codex/config.toml` if you want repo-scoped defaults.
3. Run the validator:

```bash
python scripts/validate_startup_pack.py
```

4. Start Phase 0 with Codex.

### Example (bash)

```bash
codex exec   --config approval_policy=never   --config sandbox_mode=workspace-write   --output-schema schemas/output_schema_phase0.json   -o phase0_result.json   "$(cat prompts/phase0_prompt.md)"
```

### Example (PowerShell)

```powershell
$prompt = Get-Content -Raw prompts/phase0_prompt.md
codex exec `
  --config approval_policy=never `
  --config sandbox_mode=workspace-write `
  --output-schema schemas/output_schema_phase0.json `
  -o phase0_result.json `
  $prompt
```

## Notes

- Phase 0 should generate planning artifacts, not broad implementation.
- If the repo truly needs API / queue / message contracts, create files under `contracts/`.
- Use `documentation.md` as the durable place to record discovered repo commands, caveats, and environment behavior.


## After Phase 0 finishes

Validate the generated planning artifacts:

```bash
python scripts/validate_phase0_outputs.py
```

A successful run confirms:
- required output files exist
- `dev_plan.yaml` matches schema
- `acceptance_spec.yaml` matches schema
- `run_policy.yaml` matches schema
- `phase0_result.json` matches schema
- task `acceptance_ids` correctly point to declared acceptance items
