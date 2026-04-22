# JSJY Repository README

## 仓库定位

这个仓库**不是业务系统源码仓**，而是一个面向真实业务仓库的 **spec-first 规划资产仓**。它当前承载的是：

- 现行规划包 `codex_business_repo_plan_pack_v2/`
- 根目录执行入口镜像 `prompts/`、`templates/`、`checklists/`
- 已生成的规划产物 `spec/`、`planning/`、`contracts/`
- 证据文件 `artifacts/evidence/`
- 历史归档 `planning_archive/legacy_bootstrap/`

它的核心用途，是把规划包放进一个**真实业务仓库根目录**，然后由 Codex 在 PLAN 模式下深读该业务仓库，输出后续 Phase 0 / 0.5 所需的机器可消费规划文件，而不是直接在本仓库里开发业务功能。

## 当前结论

基于仓库现有内容，这个仓库的真实状态是：

- 当前主内容是 Markdown、YAML、JSON 和少量 Python 校验脚本
- 没有发现业务应用源码目录，也没有发现可直接运行的业务构建入口
- 当前可确认的是“规划资产完整”，不能确认“业务执行就绪”
- 当前 `planning/phase0_result.json` 的结论是：
  - `planning_ready: true`
  - `execution_ready: false`

这意味着仓库已经适合继续做**规划、审查、归档和迁移**，但**不适合把它误认为可直接进入 Phase 1 的业务实现仓**。

## 推荐阅读顺序

如果你第一次接手这个仓库，建议按下面顺序理解：

1. [README.md](README.md)
2. [ARCHITECTURE.md](ARCHITECTURE.md)
3. [codex_business_repo_plan_pack_v2/README.md](codex_business_repo_plan_pack_v2/README.md)
4. [prompts/business_repo_plan_prompt.md](prompts/business_repo_plan_prompt.md)
5. [templates/business_repo_output_contract.md](templates/business_repo_output_contract.md)
6. [checklists/business_repo_review_checklist.md](checklists/business_repo_review_checklist.md)
7. [planning/phase0_result.json](planning/phase0_result.json)
8. [planning/repo_cleanup_report.md](planning/repo_cleanup_report.md)
9. `planning_archive/legacy_bootstrap/` 下的历史资产

## 目录结构

```text
.
├─ artifacts/
│  └─ evidence/                     # 当前仓库状态、远端状态、清理后树形证据
├─ checklists/
│  └─ business_repo_review_checklist.md
├─ codex_business_repo_plan_pack_v2/
│  ├─ README.md
│  ├─ prompts/
│  ├─ templates/
│  └─ checklists/                  # 现行规划包的完整可分发版本
├─ contracts/
│  └─ README.md                    # 合同尚未落地时的诚实基线说明
├─ planning/
│  ├─ acceptance_spec.yaml
│  ├─ dev_plan.yaml
│  ├─ documentation.md
│  ├─ implement.md
│  ├─ phase0_result.json
│  ├─ plan_review_checklist.md
│  ├─ repo_cleanup_report.md
│  └─ run_policy.yaml              # 当前规划输出区
├─ planning_archive/
│  └─ legacy_bootstrap/            # 历史 Phase0 启动包与旧规划结果归档
├─ prompts/
│  └─ business_repo_plan_prompt.md # 当前根目录执行入口
├─ spec/
│  ├─ invariant_spec.yaml
│  ├─ module_spec.yaml
│  ├─ product_spec.md
│  ├─ product_spec.yaml
│  └─ resource_spec.yaml           # 当前分层规格输出区
├─ templates/
│  └─ business_repo_output_contract.md
└─ codex_business_repo_plan_pack_v2.zip
```

## 核心组件说明

### 1. 现行规划包

`codex_business_repo_plan_pack_v2/` 是当前仓库最重要的分发单元，面向“真实业务仓库”的 PLAN 模式使用。它定义了：

- 应该先读哪些仓库证据
- 必须输出哪些规划文件
- 任务、验收、运行策略、厚回执应达到什么粒度
- 遇到未知项时如何诚实标记，而不是编造

### 2. 根目录入口镜像

根目录下这三份文件是当前执行入口：

- `prompts/business_repo_plan_prompt.md`
- `templates/business_repo_output_contract.md`
- `checklists/business_repo_review_checklist.md`

它们与 `codex_business_repo_plan_pack_v2/` 内同名文件当前是**哈希一致的镜像副本**。这样做的目的，是兼顾：

- 包目录的可分发性
- 根目录入口的低摩擦执行

代价是存在**双入口漂移风险**，这也是当前仓库明确记录的开放问题之一。

### 3. 当前规划产物区

`spec/`、`planning/`、`contracts/` 是本轮已生成的规划结果：

- `spec/`：产品级、模块级、资源级、不变量级规格
- `planning/`：任务图、验收规格、运行策略、文档化证据、回执契约、最终状态
- `contracts/`：合同基线；在没有业务接口证据前只保留 README 说明

### 4. 历史归档区

`planning_archive/legacy_bootstrap/` 保存的是旧版 `codex_phase0_startup_pack_v2` 及其历史产物。它的特点是：

- 包含 `AGENTS.md`、`planning/PLANS.md`
- 包含 JSON Schema
- 包含 Python 校验脚本
- 有旧版 `spec.md / dev_plan.yaml / acceptance_spec.yaml / run_policy.yaml / phase0_result.json`

这些内容现在的角色是**审计与演进参考**，而不是当前默认执行入口。

## 当前工作流

### 使用当前规划包的标准路径

1. 把 `codex_business_repo_plan_pack_v2/` 放到目标业务仓库根目录
2. 在 Codex PLAN 模式中执行 `prompts/business_repo_plan_prompt.md`
3. 同时参考：
   - `templates/business_repo_output_contract.md`
   - `checklists/business_repo_review_checklist.md`
4. 让 Codex 基于真实业务仓库源码、配置、测试、脚本、文档产出：
   - `spec/*`
   - `planning/*`
   - `contracts/*`
5. 只有在真实业务证据充分时，才允许将执行状态推进到下一阶段

### 当前仓库自身能做什么

当前仓库适合做：

- 规划包维护
- 规划文档审查
- 规划结果归档
- 历史演进对比
- 未来迁移到真实业务仓前的准备

当前仓库不适合做：

- 直接当作业务后端/前端仓库开发
- 编造接口、数据库、消息队列合同
- 在没有真实业务证据的情况下宣称可执行 Phase 1

## 现行输出模型

当前现行模型比旧版更严格，主要体现在：

- 从单一 `spec.md` 升级为多层规格：
  - `spec/product_spec.md`
  - `spec/product_spec.yaml`
  - `spec/module_spec.yaml`
  - `spec/resource_spec.yaml`
  - `spec/invariant_spec.yaml`
- 从旧版单布尔值 `ready_for_phase1`，升级为：
  - `planning_ready`
  - `execution_ready`
- 更强调：
  - 基于真实业务仓证据
  - 对未知项显式建模
  - 对合同缺失、执行边界和人工闸门进行诚实声明

## 已确认的关键事实

- `contracts/README.md` 明确说明：当前没有足够业务证据生成 API / event / queue / RPC 合同
- `planning/documentation.md` 明确把仓库判断为规划资产仓，而不是业务实现仓
- `planning/repo_cleanup_report.md` 明确旧资产是**归档**而不是**粗暴删除**
- `planning/phase0_result.json` 明确：
  - 规划文件已齐
  - 但真实业务仓、业务模块、真实合同仍然缺失

## 风险与开放问题

- 根目录镜像入口与包内入口长期并存，可能发生语义漂移
- 当前仓库缺乏真实业务源码，导致合同、资源、端口、数据库、队列等只能保守建模
- 是否长期保留双入口，还是收敛为单一真源路径，仍未定
- 后续真正的 Phase 1 应该在本仓库进行，还是迁移到真实业务仓后再进行，仍未定

## 架构图

详细架构图和演进说明见：

- [ARCHITECTURE.md](ARCHITECTURE.md)

## 补充说明

- 当前仓库一共包含 64 个文件，主体是文档与规划资产
- 当前分支为 `main`
- 根目录尚无业务运行入口，README 不提供“启动服务”类命令，是因为仓库现状并不支持这种说法
