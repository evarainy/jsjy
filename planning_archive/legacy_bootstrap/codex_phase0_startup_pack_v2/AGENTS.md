# AGENTS.md

## Scope

This repository is currently in **Phase 0: planning and pre-execution document generation**.

Your primary job is **not** to implement large product changes yet. Your primary job is to inspect the repository, identify constraints, and generate the machine-readable planning package required for later long-running execution.

## Non-negotiable rules

1. Plan first. Do not begin broad implementation before a task graph and acceptance criteria exist.
2. Keep guidance durable. When you learn a stable constraint, workflow, or pitfall, write it back into `documentation.md`.
3. Be concrete. Avoid vague statements such as “works”, “looks good”, or “login succeeds”.
4. Be machine-readable. Phase 0 is not complete until the required YAML / JSON files exist and are internally consistent.
5. Do not widen scope on your own. Unknowns belong in blockers, assumptions, and risk notes.
6. Preserve evidence. When you infer build, lint, test, env, or deployment behavior, record the evidence path or command source in `documentation.md`.
7. Do not modify `.git/`, remote branches, shared infrastructure, or production credentials.

## Required outputs

Generate or update these files in the repository root:

- `spec.md`
- `dev_plan.yaml`
- `acceptance_spec.yaml`
- `run_policy.yaml`
- `implement.md`
- `documentation.md`
- `phase0_result.json`

Generate `contracts/*.yaml` when the project has API contracts, event/message contracts, queue contracts, storage contracts, or service-to-service contracts.

## Planning quality bar

A task in `dev_plan.yaml` is incomplete unless it has:

- `id`
- `title`
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
- `notes`

A task must be split further if it spans two or more of:

- contract definition
- backend implementation
- frontend implementation
- database migration
- integration wiring
- end-to-end validation

## Acceptance quality bar

Every acceptance item in `acceptance_spec.yaml` must be pass/fail testable.

At minimum, describe applicable fields such as:

- trigger or request
- preconditions
- expected status code / exit code
- required response fields
- prohibited response fields
- expected file / DB / log / UI change
- evidence artifact path

## Phase 0 completion rule

Phase 0 is complete only when:

- the required planning files exist,
- the task graph is schedulable,
- acceptance items are machine-readable,
- shared resource policies are declared,
- blockers and risks are explicit,
- and `phase0_result.json` matches `schemas/output_schema_phase0.json`.
