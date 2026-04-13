# plan_review_checklist.md

## A. Scope & evidence grounding
- [ ] Plan decisions map to explicit repository evidence paths.
- [ ] No fabricated modules/endpoints/commands are introduced.
- [ ] True-source entry files are present at root paths.
- [ ] Legacy cleanup actions are documented in `planning/repo_cleanup_report.md`.

## B. Spec-first completeness
- [ ] `spec/product_spec.md` has all required sections.
- [ ] `spec/product_spec.yaml` includes required machine-readable keys.
- [ ] `spec/module_spec.yaml` module boundaries match evidence.
- [ ] `spec/resource_spec.yaml` distinguishes detected vs unknown resources.
- [ ] `spec/invariant_spec.yaml` contains readiness and cleanup invariants.

## C. Task graph integrity (planning/dev_plan.yaml)
- [ ] No duplicate task IDs.
- [ ] Every task uses allowed `layer` values.
- [ ] No unresolved dependency IDs.
- [ ] No obvious DAG cycle risk.
- [ ] Tasks are fine-grained, not broad epics.
- [ ] Overlap in `touched_paths` is intentional and justified.
- [ ] `shared_resources_touched` identifies contention points.
- [ ] Human gates are declared where required.

## D. Acceptance rigor (planning/acceptance_spec.yaml)
- [ ] No duplicate acceptance IDs.
- [ ] Every acceptance item has trigger + expect + evidence.
- [ ] Assertions are automatable (status/field/path/existence checks).
- [ ] Cleanup, readiness, and invariant-related checks are covered.
- [ ] Evidence paths are non-empty and realistic.

## E. Execution contract robustness
- [ ] `planning/implement.md` defines thick receipt fields.
- [ ] Receipt includes pass/fail acceptance IDs.
- [ ] Receipt includes blockers/risks/needs_human/error_code.
- [ ] Merge gates are explicit and enforce readiness honesty.

## F. Readiness honesty
- [ ] `planning/phase0_result.json` has both planning_ready and execution_ready.
- [ ] execution_ready is false when business evidence is insufficient.
- [ ] blockers/risks/next_step are consistent and actionable.

## G. Scheduler failure anticipation
- [ ] Duplicate IDs are checked.
- [ ] DAG cycle risk is checked.
- [ ] touched-path overlap risk is checked.
- [ ] shared resource collision risk is checked.
- [ ] missing-contract risk is tracked.
