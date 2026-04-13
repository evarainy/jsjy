# spec.md

## Goals
- 产出完整、可机读、可调度、可复核的 Phase 0 文档包，供后续自动执行直接消费。
- 明确仓库当前为“启动包+规划资产”形态下的边界、风险与执行约束。
- 形成可用于后续多 agent 并行执行的任务图、验收规格和运行策略。

## In scope
- 生成并维护 Phase 0 必需文件：`spec.md`、`dev_plan.yaml`、`acceptance_spec.yaml`、`run_policy.yaml`、`implement.md`、`documentation.md`、`phase0_result.json`。
- 基于 Schema 与验证脚本建立可自动检查链路（文件存在、Schema 合规、交叉引用合规）。
- 固化根目录 guidance 入口：`prompts/codex_plan_mode_prompt.md`、`templates/phase0_output_contract.md`、`checklists/phase0_review_checklist.md`。

## Non-goals
- 不进行 Phase 1 功能开发。
- 不进行后端接口、前端页面、数据库迁移等业务实现。
- 不修改 `.git/` 内部对象或远端基础设施配置。

## Constraints
- 必须遵守 `codex_phase0_startup_pack_v2/AGENTS.md` 的 Phase 0 规则。
- 所有输出必须可被 `codex_phase0_startup_pack_v2/scripts/validate_phase0_outputs.py` 验证。
- 任务设计必须细粒度、可并行标注、并具备 acceptance 绑定。

## Assumptions
- 当前仓库即本轮 Phase 0 的执行仓库。
- 启动包目录下 `prompts/schemas/templates/scripts` 为规范真源，根目录入口文件用于简化消费路径。
- Python 运行时可安装并使用 `PyYAML`、`jsonschema`。

## Dependencies
- Python3。
- `PyYAML`、`jsonschema`。
- `codex_phase0_startup_pack_v2/scripts/validate_startup_pack.py`。
- `codex_phase0_startup_pack_v2/scripts/validate_phase0_outputs.py`。

## Risks
- 仓库缺少业务代码，Phase 1 的业务价值取决于是否确认本仓库为目标业务仓。
- 启动包目录与根目录 guidance 双入口可能发生语义漂移。
- 环境依赖变化（Python 包版本）可能导致验证脚本结果不稳定。

## Open questions
- 是否保留双入口（启动包内 + 根目录）还是收敛到单一真源路径。
- 后续 Phase 1 是否继续在本仓库执行，或迁移到业务仓库后再执行。
- 是否需要追加 contracts/（当前无 API/消息/队列证据）。

## Current repository evidence
- 存在启动包目录、根目录规划文档、schema 文件、checklist 与 evidence 目录。
- `validate_startup_pack.py` 与 `validate_phase0_outputs.py` 可执行并可产出成功结果。
