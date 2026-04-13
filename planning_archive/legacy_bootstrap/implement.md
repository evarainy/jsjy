# implement.md

## Execution principles
- 严格执行 `dev_plan.yaml` 中声明任务，不越界实现业务功能。
- 仅修改任务 `touched_paths`，禁止触碰 `forbidden_paths`。
- 每个任务必须产出证据，并可被验收项回溯。

## Per-task contract
每个任务执行必须输出：
1. 任务输入（task_id, deps, acceptance_ids）
2. 变更文件列表（changed_files）
3. 验证命令与结果（tests_run / verification_commands）
4. 证据路径（evidence_paths）
5. 阻塞与风险（blockers / risks）
6. 下一步动作（next_action）

## Structured task result
最小结果结构字段：
- `task_id`
- `status`
- `changed_files`
- `tests_run`
- `verification_commands`
- `evidence_paths`
- `blockers`
- `risks`
- `next_action`

## Phase0 merge gate
- `python codex_phase0_startup_pack_v2/scripts/validate_phase0_outputs.py` 必须通过。
- `python codex_phase0_startup_pack_v2/scripts/validate_startup_pack.py` 必须通过。
- `phase0_result.json` 的 readiness 与 next_step 必须真实、可执行。
