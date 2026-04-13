# implement.md

## Phase boundary
- This run is limited to Phase 0/0.5 planning and repository cleanup.
- Broad feature implementation is prohibited.

## Task execution contract
Each task execution result must include:
- `task_id`
- `status` (`success|partial|failed`)
- `attempt`
- `layer`
- `changed_files`
- `tests_run`
- `verification_commands`
- `acceptance_ids_planned`
- `acceptance_ids_passed`
- `acceptance_ids_failed`
- `evidence_paths`
- `invariants_preserved`
- `blockers`
- `risks`
- `needs_human`
- `error_code`
- `next_action`

## Thick receipt example schema
```yaml
result:
  task_id: T-PLAN-004
  status: success
  attempt: 1
  layer: docs
  changed_files:
    - planning/implement.md
  tests_run:
    - test -f planning/implement.md
  verification_commands:
    - test -f planning/implement.md
  acceptance_ids_planned: [AC-012]
  acceptance_ids_passed: [AC-012]
  acceptance_ids_failed: []
  evidence_paths:
    - planning/implement.md
  invariants_preserved: [INV-001, INV-004]
  blockers: []
  risks: []
  needs_human: false
  error_code: null
  next_action: proceed_to_T-PLAN-005
```

## Merge gate
- No task may claim completion without evidence paths.
- No run may flip `execution_ready` to true unless blockers are cleared by human gate.
