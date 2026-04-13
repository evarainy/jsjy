You are executing **Phase 0: planning and pre-execution document generation**.

Before doing any work, read and follow:

1. `AGENTS.md`
2. `planning/PLANS.md`
3. `schemas/output_schema_phase0.json`
4. `schemas/dev_plan.schema.json`
5. `schemas/acceptance_spec.schema.json`
6. `schemas/run_policy.schema.json`
7. `templates/` and `templates/contracts/`
8. the relevant repository source code, configs, docs, tests, scripts, and build files

## Objective

Do **not** start broad product implementation.

Your objective is to generate a complete, machine-readable planning package for later long-running execution.

## Required outputs

Generate or update at repo root:

- `spec.md`
- `dev_plan.yaml`
- `acceptance_spec.yaml`
- `run_policy.yaml`
- `implement.md`
- `documentation.md`
- `phase0_result.json`

Generate `contracts/*.yaml` if the repository needs them.

## Required working order

1. Inspect the repository
2. Write `spec.md`
3. Write `dev_plan.yaml`
4. Write `acceptance_spec.yaml`
5. Write `run_policy.yaml`
6. Write `implement.md`
7. Write `documentation.md`
8. Write `contracts/*.yaml` if applicable
9. Validate internal consistency
10. Write `phase0_result.json`

## Hard requirements

### 1) Tasks must be split finely
Do not create vague tasks like “implement login”.

Instead split work into bounded tasks such as:
- contract definition
- backend response implementation
- frontend form handling
- session persistence
- failure-path handling
- E2E verification

Each task must include:
- unique `id`
- `goal`
- `deps`
- `touched_paths`
- `forbidden_paths`
- `acceptance_ids`
- `parallel_safe`
- `needs_db`
- `needs_ports`
- `verification_commands`
- `evidence_paths`

### 2) Acceptance must be concrete
Do not write “login works”.

Prefer assertions like:
- `POST /api/login` with valid credentials returns `200`
- `$.code == 0`
- `$.data.accessToken` exists
- `$.data.user.id` exists
- invalid credentials return `401`
- `accessToken` must be absent
- evidence saved to `artifacts/evidence/login_success_response.json`

### 3) Keep uncertainty explicit
If information is missing:
- record evidence and reasoning in `documentation.md`
- record blockers in `phase0_result.json`
- continue with the parts you can determine
- never disguise unknowns as finished work

### 4) Keep outputs automation-friendly
Populate the planning files using the provided schemas and templates.
Prefer stable keys, bounded lists, and explicit evidence paths over long prose.

## Validation step

Before finishing:
- ensure the generated files exist
- ensure task IDs and acceptance IDs cross-reference correctly
- ensure shared resources are declared
- ensure `phase0_result.json` conforms to `schemas/output_schema_phase0.json`

## Final note

Do not begin Phase 1 or large-scale code implementation.
Your last act must be to write `phase0_result.json` and set `readiness.ready_for_phase1` truthfully.
