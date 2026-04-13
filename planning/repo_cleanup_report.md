# repo_cleanup_report.md

## 1) 保留的关键业务目录/文件（含仓库关键资产）
- `.git/`（版本历史与远端关联保留，未做破坏性改动）
- `codex_business_repo_plan_pack_v2.zip`（当前规划包压缩源）
- `codex_business_repo_plan_pack_v2/`（解压后的完整规划包）
- `prompts/business_repo_plan_prompt.md`（当前真源入口镜像）
- `templates/business_repo_output_contract.md`（当前真源契约镜像）
- `checklists/business_repo_review_checklist.md`（当前真源检查清单镜像）
- `artifacts/evidence/remote_heads_after_push.txt`（远端状态证据）

## 2) 已归档的旧规划文件
归档根目录：`planning_archive/legacy_bootstrap/`

主要归档类别：
- 旧 Phase0 输出：
  - `spec.md`
  - `dev_plan.yaml`
  - `acceptance_spec.yaml`
  - `run_policy.yaml`
  - `implement.md`
  - `documentation.md`
  - `phase0_result.json`
- 旧 prompt/template/checklist：
  - `prompts/codex_plan_mode_prompt.md`
  - `templates/phase0_output_contract.md`
  - `checklists/phase0_review_checklist.md`
- 旧 startup pack：
  - `codex_phase0_startup_pack_v2.zip`
  - `codex_phase0_startup_pack_v2/`（含 prompts/templates/schemas/scripts/planning）
- 旧 schema 与验证产物：
  - `schemas/*.json`（旧 phase0 schema）
  - `artifacts/evidence/repo_inventory.txt`
  - `artifacts/evidence/startup_pack_validation.log`
  - `artifacts/evidence/phase0_validation.log`
  - `artifacts/evidence/git_status_before.txt`

## 3) 删除的临时或重复文件
- 本轮未执行物理删除（0 个）。
- 原则：旧规划资产优先归档，不直接删除。

## 4) 冲突但暂未处理
- `codex_business_repo_plan_pack_v2/*` 与根目录 `prompts/templates/checklists/*` 语义重复。
- 当前策略：保留两份，业务包目录作为来源，根目录作为执行入口。
- 待后续决策是否只保留单一真源路径。

## 5) 当前认定的唯一真源规划入口文件
- `prompts/business_repo_plan_prompt.md`
- `templates/business_repo_output_contract.md`
- `checklists/business_repo_review_checklist.md`
- 同包配套：`codex_business_repo_plan_pack_v2/README.md`、`codex_business_repo_plan_pack_v2/*`
