# product_spec.md

## Goals
- 基于真实仓库证据产出 spec-first 规划包，供后续受控执行。
- 建立可机器消费的任务图、验收标准、运行策略与回执契约。
- 在未发现业务源码的情况下，明确“先补业务上下文再执行 Phase 1”的安全边界。

## In scope
- 仓库整理：确立 business_repo_plan_pack 为规划真源并归档旧规划资产。
- 生成 `spec/`, `planning/`, `contracts/` 下的 Phase 0/0.5 规划文件。
- 形成对当前仓库资产的模块、资源、不变量与风险建模。

## Non-goals
- 不进入任何后端/前端/数据库功能实现。
- 不修改真实业务逻辑（当前仓库未发现业务逻辑代码）。
- 不执行破坏性仓库清空操作。

## Constraints
- 仅以仓库现有证据为依据，未知项必须显式标注。
- `execution_ready` 不得因“文档写完”而误判为 true。
- 真实业务资产必须保留；旧规划资产优先归档而非删除。

## Assumptions
- 当前仓库暂为“规划资产仓”，并非已落地业务系统仓。
- `codex_business_repo_plan_pack_v2/` 与根目录入口文件保持同源语义。
- 后续若迁移到真实业务仓，需复用本规划骨架并重采证据。

## Dependencies
- Git 仓库可读写能力。
- Markdown/YAML 规划资产。
- 后续可用的真实业务源码、配置与测试资产（当前缺失）。

## Risks
- 缺乏业务源码导致模块、接口、数据流只能给出“待采证”级规划。
- 双入口（包内+根目录）长期并存可能出现语义漂移。
- 若直接进入 Phase 1，存在高概率任务空转或误实现风险。

## Open questions
- 真实业务代码仓是否就是当前仓库？若不是，目标仓地址是什么？
- 业务系统主技术栈（Node/Java/Python/Go）与运行入口为何？
- 是否已有 API 约定、数据库迁移规范、CI/CD 规则可继承？

## Current repository evidence
- 现存主要内容为 planning pack 文件、旧规划归档、少量 evidence 文件。
- 未发现应用源码目录（如 `src/`, `app/`, `services/`, `backend/`, `frontend/` 等）。
- 未发现可执行业务测试目录与业务构建脚本（package.json/pyproject/pom/gradle 等）。
