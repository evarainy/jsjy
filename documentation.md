# documentation.md

## Repository overview
- 仓库核心资产为 Phase0 启动包、根目录规划文档、schemas 与检查清单。
- 未发现业务源码目录，因此本轮仅进行规划资产治理。

## Build / run / test evidence
- Command: `rg --files`
  - Source file: repository filesystem
  - Observed result: 可枚举启动包、根目录文档、schemas 与 evidence 文件。
- Command: `python codex_phase0_startup_pack_v2/scripts/validate_startup_pack.py`
  - Source file: `codex_phase0_startup_pack_v2/scripts/validate_startup_pack.py`
  - Observed result: 返回 `ok: true`。
- Command: `python codex_phase0_startup_pack_v2/scripts/validate_phase0_outputs.py`
  - Source file: `codex_phase0_startup_pack_v2/scripts/validate_phase0_outputs.py`
  - Observed result: 返回 `ok: true`, `errors: {}`。

## Environment and config notes
- Python3 可用。
- 需安装 `PyYAML` 与 `jsonschema` 才能执行 Phase0 输出验证脚本。

## Shared resource notes
- DB: none
- Ports: none
- Cache / queue: none
- External services: GitHub remote

## Stable rules learned during Phase 0
- 根目录 Phase0 输出文件必须齐全。
- `dev_plan.yaml` 与 `acceptance_spec.yaml` 的引用关系必须可被 validator 验证。
- readiness 必须与 blockers/risks/next_step 保持一致，不可乐观虚报。

## Open questions / blockers
- 是否将启动包内 guidance 与根目录 guidance 收敛为单一真源。
- 是否在本仓库继续 Phase1，或迁移到业务仓库后再执行。
