# PLANS.md

This file defines how planning documents should be produced during **Phase 0**.

## Goal

Turn a high-level project idea into a durable execution package for later long-running Codex or Commander runs.

## Phase 0 milestones

### M0.1 Repository reconnaissance
Produce a grounded repo summary:
- key directories and modules
- build, test, lint, run commands
- current test state
- configuration and env files
- obvious risk areas and shared resources

### M0.2 Scope and boundary freeze
Create `spec.md` with:
- goals
- in-scope items
- non-goals
- constraints
- assumptions
- dependencies
- risks
- open questions

### M0.3 Task graph
Create `dev_plan.yaml` as a dependency-aware task graph:
- tasks must be small enough for isolated execution
- each task must map to acceptance IDs
- touched and forbidden paths must be explicit
- DB / port / shared-resource needs must be explicit

### M0.4 Acceptance definition
Create `acceptance_spec.yaml`:
- every critical path needs success and failure checks
- acceptance must be precise enough for later automation
- evidence files must be named up front

### M0.5 Contracts and run policy
Create:
- `contracts/*.yaml` when applicable
- `run_policy.yaml`
- `implement.md`

These must define:
- contract shape
- port allocation policy
- DB migration lock policy
- retry / backoff / circuit-breaker policy
- subagent / worktree execution conventions
- verification conventions

### M0.6 Structured result
Create `phase0_result.json` with:
- completion status
- generated files
- missing files
- blockers
- risks
- readiness for next phase
- explicit next step

## Quality red lines

Do not mark Phase 0 complete if any of the following is true:

1. tasks are missing acceptance bindings
2. acceptance items are only prose with no concrete assertions
3. shared resources are undeclared
4. contracts are needed but absent
5. the result JSON is missing or fails schema validation

## Living-document rule

Plans are durable artifacts, not throwaway notes. As discoveries occur, revise the planning files so they remain usable by a fresh agent with no memory of prior chat.
