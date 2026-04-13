# documentation.md

## Evidence inventory
- `rg --files` output shows repository primarily contains planning assets, archived legacy bootstrap assets, and no business runtime code tree.
- Root truth-source entries for current planning are present at:
  - `prompts/business_repo_plan_prompt.md`
  - `templates/business_repo_output_contract.md`
  - `checklists/business_repo_review_checklist.md`
- Legacy phase0 assets were moved into `planning_archive/legacy_bootstrap/`.

## Major conclusions and evidence mapping
1. **Conclusion:** Current repository is planning-centric, not business implementation-centric.
   - Evidence: absence of typical app/service directories and manifests in repo file list.
2. **Conclusion:** It is unsafe to mark execution readiness as true.
   - Evidence: no API routes, no DB migrations, no service runtime entrypoints.
3. **Conclusion:** Legacy planning assets can be preserved without deletion by archiving.
   - Evidence: archived files and directories under `planning_archive/legacy_bootstrap/`.

## Build / run / test command evidence
- Command: `rg --files > artifacts/evidence/repo_tree_after_cleanup.txt`
  - Observed result: root truth-source files + archived legacy assets + new planning outputs are present.
- Command: `test -f prompts/business_repo_plan_prompt.md`
  - Observed result: pass.
- Command: `test -f planning/phase0_result.json`
  - Observed result: pass.

## Cleanup notes
- Archived legacy startup-pack and old phase0 outputs instead of deletion.
- Kept both package-internal files and root entry mirrors to avoid accidental source loss.
- Recorded unresolved mirror-conflict policy as open question.

## Open questions / blockers
- Blocker: target business repository identity is still unconfirmed.
- Blocker: business runtime stack and interfaces remain unknown.
- Open question: long-term single source-of-truth strategy for duplicated guidance paths.
- Open question: whether to generate concrete contracts after business code import.
