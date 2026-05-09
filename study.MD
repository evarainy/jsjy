# Study Notes

本文档用于持续记录外部参考仓库的研究结论，重点关注：

- 仓库名称与地址
- 当前阅读快照
- 项目定位
- 架构路线
- 技术栈与软件框架
- 设计思路
- 对我们当前方案的可借鉴点
- 不宜直接照搬的部分
- 后续可跟进的问题

---

## 1. bytedance/deer-flow

### 基本信息

- 名称：DeerFlow
- 地址：<https://github.com/bytedance/deer-flow>
- 本次阅读快照：
  - commit: `dbd777fe626f5c2d9afa900f38ee9d2726a53329`
  - 时间：`2026-04-22 16:48:09 +0800`
  - 最近提交：`chore(deps): bump python-dotenv from 1.2.1 to 1.2.2 in /backend (#2440)`

### 项目定位

DeerFlow 当前不是单纯的“research demo”或“prompt collection”，而是一个完整的 **super agent harness / agent runtime product**。它的目标是提供：

- 多 agent 编排
- 可配置模型接入
- 技能系统
- 沙箱执行
- 长期记忆
- MCP 工具扩展
- Web 产品化界面
- 多种部署模式

它已经具备明显的“平台化”特征，而不是只服务某一个具体业务场景。

### 架构路线

DeerFlow 的架构路线很清晰，是一条从“单体后端”演进为“可复用 harness + 面向用户的 app”的路线。

当前关键分层：

- `backend/packages/harness/deerflow/`
  - 可复用 agent 编排框架
  - 包括 agents / middleware / sandbox / tools / mcp / skills / models / memory / client
- `backend/app/`
  - 用户产品层
  - 包括 gateway API 和 channels
- `frontend/`
  - Next.js Web UI
- `docker/`
  - dev / prod / provisioner / nginx 部署层

典型运行时是三到四段式：

- Nginx
- LangGraph server
- Gateway API
- Next.js frontend

并且它专门写了 `HARNESS_APP_SPLIT.md`，明确说明：

- Harness 回答“如何构建和运行 agent”
- App 回答“如何把 agent 能力呈现给用户”
- Harness 不能反向依赖 App

这说明它把“可复用运行时内核”和“产品壳层”作为长期演进主线。

### 技术栈与软件框架

后端：

- Python 3.12+
- LangGraph
- LangChain
- FastAPI
- Uvicorn
- SSE streaming
- Pydantic
- MCP adapters
- SQLite/Postgres checkpointer 路线

前端：

- Next.js 16
- React 19
- Tailwind CSS 4
- Radix UI
- TanStack Query
- Playwright / Vitest

部署与运行：

- Docker Compose
- Nginx
- Kubernetes provisioner 可选
- host Docker socket / sandbox image / container-based execution

### 设计思路

我认为 DeerFlow 最核心的设计思路有六个：

1. **把 agent runtime 做成平台内核**
   它不是把 agent 写死在 Web 项目里，而是抽象成 harness。

2. **状态是第一等公民**
   `ThreadState` 明确管理 sandbox、thread_data、artifacts、todos、viewed_images 等运行态。

3. **middleware 化而不是堆业务逻辑**
   Summarization、Todo、Title、Memory、ViewImage、Clarification、LoopDetection 等能力都走 middleware chain。

4. **配置驱动**
   模型、工具、sandbox、memory、summarization、channels、guardrails、checkpointer 等都在 `config.yaml` 中声明。

5. **安全边界前置**
   沙箱、guardrails、tool filtering、subagent limit、loop detection 都是在控制执行风险。

6. **产品化意识很强**
   它同时提供 UI、部署模式、IM channel、artifact serving、MCP config API，不止是“能跑 agent”。

### 对我们可借鉴的点

对我们当前仓库，DeerFlow 最值得借鉴的是“系统形态”，不是具体业务功能。

可直接借鉴：

- 后续若进入执行系统阶段，应拆成 `planner-harness` 和 `planner-app`
- 规划执行需要一个明确的运行态契约，而不是只有静态 markdown/yaml
- 需要把 repo scan / contract emit / acceptance emit / verification 做成中间件或流水线节点
- 需要配置驱动，而不是只靠 prompt 文案驱动
- 需要把“可分发内核”和“交互壳层”分开，避免未来 CLI、API、UI、Bot 重复造轮子

中期可借鉴：

- checkpointer / run state / artifact path 管理
- tool system 与 sandbox 边界
- stateful execution model
- gateway API 与 runtime 的职责分离

### 不宜直接照搬的点

当前阶段不适合直接照搬：

- 完整 LangGraph + Gateway + Frontend + Nginx + Provisioner 栈
- IM channel 集成
- 重产品化 UI
- 容器级沙箱基础设施

原因不是这些思路不好，而是我们当前还是“规划资产系统”，不是“可执行 super-agent 产品”。

### 对我们的具体启发

最重要的启发不是“做个 DeerFlow”，而是：

- 未来如果我们从规划仓走向执行系统，必须先定义内核和外壳边界
- 未来必须有一个 `state contract`，不能只有 `spec/` 和 `planning/`
- 未来的 repo adapter / evidence pipeline / acceptance engine 应该是可插拔的，而不是绑死在一个 prompt 里

---

## 2. affaan-m/everything-claude-code

### 基本信息

- 名称：Everything Claude Code
- 地址：<https://github.com/affaan-m/everything-claude-code>
- 本次阅读快照：
  - commit: `4e66b2882da9afb9747468b08a253ca2f09c85f3`
  - 时间：`2026-04-21 18:41:36 -0400`
  - 最近提交：`docs: fix plugin quick start for continuous learning v2 (#1546)`

### 项目定位

ECC 不是传统意义上的单体应用，更像一个 **跨 AI harness 的 workflow system / installable operating layer**。

它服务的不是某一个具体产品，而是：

- Claude Code
- Codex
- Cursor
- OpenCode
- Gemini

等多个 agent harness 上的统一工作流、规则、技能、hook、agent、命令、安装与运维体系。

ECC 的两个层次需要分开看：

- `v1.x`：内容面和安装面
  - skills / agents / hooks / rules / commands / manifests / installers
- `ecc2/`：控制面 alpha
  - Rust TUI + daemon + session state + worktree orchestration scaffold

### 架构路线

ECC 的核心不是“运行时平台”，而是“内容系统 + 安装系统 + 控制面演进”。

当前可以分成三层理解：

1. **内容层**
   - `skills/`
   - `agents/`
   - `rules/`
   - `commands/`
   - `hooks/`

2. **分发/安装层**
   - `.claude-plugin/plugin.json`
   - `manifests/install-modules.json`
   - `scripts/install-plan.js`
   - `scripts/install-apply.js`
   - `scripts/install-state.js`
   - `doctor / repair / uninstall / list-installed`

3. **控制面 alpha**
   - `ecc2/`
   - Rust TUI
   - SQLite state store
   - session / daemon / worktree / dashboard

它最值得注意的是：

- 主仓并不急着把所有事情塞进控制面
- 先把“模块 catalog + install contract + lifecycle contract”做扎实
- 再逐渐向 ECC 2.0 控制面演进

### 技术栈与软件框架

主内容与安装层：

- Node.js / JavaScript
- 少量 Python
- JSON Schema
- npm package
- plugin manifest
- install-state persistence

控制面 alpha：

- Rust
- Ratatui
- Crossterm
- Tokio
- SQLite (`rusqlite`)
- Git integration (`git2`)
- Clap CLI

辅助层：

- 大量 Markdown 资产
- 多语言文档与翻译
- 测试、lint、catalog 校验

### 设计思路

ECC 最强的设计思路不在“某个 skill 很多”，而在它把 agent workflow 当成一套可治理系统来做。

我认为它最核心的设计思路有七个：

1. **skills/agents/rules/hooks 是内容资产，不是散装文件**
   它们被 catalog 化、模块化、target-aware。

2. **选择性安装比全量复制更重要**
   `install-modules.json` 和 profile 机制让它可以按目标和需求裁剪。

3. **安装状态必须持久化**
   它明确记录：
   - 请求了什么
   - 解析出了什么
   - 安装到了哪里
   - 哪些文件归 ECC 管

4. **doctor / repair / uninstall 是一等能力**
   安装之后的可维护性被正式建模了。

5. **target adapter 思维**
   Claude、Cursor、Codex、OpenCode 不是同一套文件布局，必须做目标适配。

6. **内容层和控制面分离**
   先把内容系统做扎实，再做 Rust 控制面，不反过来。

7. **统一 session contract**
   `SESSION-ADAPTER-CONTRACT.md` 表明它在为未来的多 runtime / 多 harness 观察与调度做数据标准化。

### 对我们可借鉴的点

ECC 对我们当前阶段的借鉴价值非常高，甚至高于 DeerFlow。

可直接借鉴：

- 做 `manifest` 驱动的规划包模块系统
- 做 `install-state` / `planning-state` / `run-state`
- 做 `doctor / repair / uninstall`
- 做 `target adapters`
- 把“单一真源 + 生成镜像”制度化，而不是手工复制
- 用 schema 校验 + state contract 控制演进

非常适合我们当前仓库的思路：

- 先把规划内容面做成模块系统
- 再做工具面和控制面
- 先追求可验证、可分发、可修复
- 再考虑 UI / daemon / dashboard

### 不宜直接照搬的点

ECC 当前内容库非常庞大，直接照搬会有几个问题：

- 会把我们带向“大 catalog，低聚焦”
- 容易在没有清晰目标前就做过量模块
- 容易先做 distribution complexity，再做核心规划逻辑

所以不能照搬它的规模，但可以照搬它的 **合同与生命周期治理思路**。

### 对我们的具体启发

ECC 对我们当前最重要的启发有五个：

- 规划包也应该有模块 catalog，而不是一坨文档
- 镜像入口应该是生成物，不应手工双写
- 规划产物生成后必须有持久状态文件记录来源、解析、结果和 ownership
- 未来如果要支持 Codex / Claude / 其他 harness，必须有 target adapter
- 后续任何控制面都要建立在 canonical state contract 之上，而不是建立在聊天上下文之上

### 当前结论

如果只看对我们眼下最有用的部分，ECC 最值得学习的不是某个命令或某个 skill，而是：

- manifest
- install plan
- install state
- lifecycle commands
- session contract

它提供的是“如何把 agent workflow 系统做成工程化资产”的方法论。

---

## 3. shareAI-lab/learn-claude-code

### 基本信息

- 名称：Learn Claude Code
- 地址：<https://github.com/shareAI-lab/learn-claude-code>
- 本次阅读快照：
  - commit: `4b95969a03f780e8aa17340a10ff0a6d9512a2c9`
  - 时间：`2026-04-15T00:58:19+08:00`

### 项目定位

这个仓库不是一个面向生产的 agent 平台，也不是一个“大而全”的工具仓，而是一个非常明确的 **教学型 harness engineering 仓库**。

它要解决的问题不是“怎么交付一个成品 agent 产品”，而是：

- 怎么把 Claude Code 一类 coding agent 的关键机制拆开讲清楚
- 怎么从最小 agent loop 逐步演进到多任务、多队友、后台执行、worktree 隔离
- 怎么让读者理解“agent 的智能来自模型，工程师主要在构建 harness”

所以它的核心价值，在于 **抽象和讲解框架**，而不在于提供完整生产实现。

### 架构路线

它的架构路线非常清楚，是一条“渐进式教学路线”，不是“平台分层路线”。

关键结构：

- `agents/`
  - `s01` 到 `s12` 的渐进式 Python 参考实现
  - `s_full.py` 提供更完整的组合版
- `docs/en|zh|ja/`
  - 每个 session 的讲解文档，多语言对应
- `skills/`
  - `agent-builder`、`code-review`、`mcp-builder`、`pdf`
- `web/`
  - Next.js 学习展示站点，用于把课程内容做成可浏览界面
- `tests/`
  - 当前测试以 smoke/编译级验证为主

它不是按“控制面 / 数据面 / 网关 / runtime”拆，而是按 **session 能力堆栈** 拆：

1. 最小 loop
2. 工具扩展
3. planning
4. subagents
5. on-demand knowledge
6. context compression
7. task graph
8. background jobs
9. teammate delegation
10. communication protocol
11. autonomous claiming
12. worktree isolation

这是典型的“先讲一条最小主线，再一层层加 harness 机制”的路线。

### 技术栈与软件框架

主实现层：

- Python
- Anthropic SDK
- dotenv
- YAML/Markdown 驱动的内容组织

Web 内容层：

- Next.js 16
- React 19
- TypeScript
- Tailwind 4
- Markdown 提取与渲染链路

测试层：

- `pytest`
- `unittest`
- 当前以脚本可编译、核心模块可加载为主

这里最值得注意的是：**技术栈很轻，目的不是构建复杂平台，而是让“机制本身”尽可能透明。**

### 设计思路

我认为这个仓库最核心的设计思路有六个：

1. **把 Claude Code 拆成一组可讲授的 harness 机制**
   它不是复刻 Claude Code 全貌，而是抽出 loop、tool、plan、subagent、task、worktree 这些可迁移机制。

2. **保持最小 loop 不变，新增能力只作为外围 harness 增量**
   README 和 session 文档都在强调：agent loop 是稳定内核，其他都是围绕它叠加的 harness 机制。

3. **用“渐进式 session”替代“大一统框架”**
   每个 session 只讲一个新增机制，降低理解门槛，也让设计取舍非常清楚。

4. **把任务系统和目录隔离显式分开**
   `s12` 里已经明确提出：task 是 control plane，worktree 是 execution plane，这个抽象很有价值。

5. **强调 durability，但只做到教学需要的程度**
   它开始把 `.tasks/`、`.worktrees/index.json`、`events.jsonl` 做成文件级持久层，但没有进一步演进成完整运行时平台。

6. **先把“思想模型”讲明白，再谈工具堆砌**
   它非常强烈地反对 prompt plumbing，把工程焦点放回工具、知识、观察、动作接口、权限边界。

### 对我们可借鉴的点

这个仓库对我们最有价值的，不是代码复用，而是 **方法论和讲解结构**。

可直接借鉴：

- 用渐进式能力分层重新整理我们自己的方案说明
- 把“最小闭环”与“后续增强机制”清晰拆开，不再在同一份文档里混写
- 明确区分：
  - core loop / core contract
  - task system
  - evidence loading
  - context management
  - worktree / execution isolation
- 在我们的设计文档里显式引入：
  - control plane
  - execution plane
  - durable file state
  这几个概念
- 如果后续要做培训、交付、团队共识沉淀，它这种 session 化教学结构非常适合借鉴

### 不宜直接照搬的点

不适合直接照搬的地方也很明确：

- 它是教学仓，不是生产级工程仓
- 测试、状态契约、错误恢复、分发治理都还不是重点
- 很多实现故意保持轻量，便于理解，但不足以支撑长期运行
- `web/` 当前更像学习内容展示层，不是运行时产品前端

所以不能把它当成“我们系统应该长成什么样”的直接蓝图，只能把它当成“怎样把复杂系统解释清楚”的优秀样本。

### 对我们的具体启发

它对我们的具体启发主要有五个：

- 我们的方案文档应该按能力演进来写，而不是只按目录树罗列
- 应该把“最小闭环”定义得更硬，让后续扩展围绕最小闭环叠加
- 应该把 `task / state / worktree / artifacts` 这些概念在文档里拆得更清楚
- 如果将来要让别人理解和复用我们的系统，必须提供教学式路径，而不能只有“最终形态文档”
- 我们后续做多仓对比时，可以借它这套框架，把参考仓按“从最小 loop 到复杂系统”的维度归类

### 当前结论

`learn-claude-code` 的价值不在于“工程重”，而在于“抽象准、路径清、教学强”。

如果 DeerFlow 代表“产品化 runtime 路线”，ECC 代表“内容系统 + 安装治理路线”，那么这个仓库代表的是：

- harness 思想启蒙
- 渐进式机制拆解
- 最小 loop 优先
- 教学型架构表达

它非常适合成为我们后续整理自己方法论时的表达参考。

---

## 4. harness/harness

### 基本信息

- 名称：Harness Open Source
- 地址：<https://github.com/harness/harness>
- 本次阅读快照：
  - commit: `43b982e187d31ec011f376596bcd43f01151f684`
  - 时间：`2026-04-22T15:04:07Z`

### 项目定位

这个仓库和前面三个完全不是同一类问题域。

它不是 agent harness，也不是 prompt/workflow 资产仓，而是一个 **端到端开发平台 / DevOps 平台控制面仓库**。  
官方定位是把：

- 代码托管
- DevOps pipelines
- Gitspaces
- Artifact registries

放到一个统一平台里。

从 README、官方文档和源码看，它本质上是在做一套 **工程平台型 control plane**，只是服务对象是软件开发生命周期，而不是 AI agent。

### 架构路线

它的架构路线不是“轻量插件式组合”，而是明显的 **大型平台单仓演进路线**。

当前关键结构：

- `cmd/gitness/`
  - 主程序入口
  - CLI 子命令注册
  - wire 依赖注入装配
  - 数据库驱动装配
- `app/`
  - 平台主业务层
  - `api` / `auth` / `router` / `server` / `services` / `store`
  - `pipeline` / `gitspace` / `connector` / `events` 等领域模块
- `registry/`
  - Artifact registry 相关能力
- `pubsub` / `job` / `events` / `stream`
  - 平台异步与事件机制
- `web/`
  - 完整前端 UI
- `charts/gitness`
  - Helm/Kubernetes 部署面

从 `cmd/gitness/main.go` 和 `wire.go` 看得很清楚：

- `main.go` 负责 CLI / server / login / migrate / swagger 等统一入口
- `wire.go` 把 controller、service、store、events、pubsub、job、registry、gitspace、pipeline 等大量模块装配成一个系统

这意味着它的路线是：

1. 一个大一统平台内核
2. 按领域拆模块
3. 通过依赖注入和服务装配整合
4. 同时输出 CLI、HTTP API、Web UI、Swagger、部署制品

另外一个很重要的细节是：

- 仓库名已经是 `harness/harness`
- 但 Go module 和大量代码路径仍然是 `github.com/harness/gitness`

这说明它处在“产品品牌/仓库命名已更新，内核代码仍保留历史命名与兼容层”的演进状态。

### 技术栈与软件框架

核心后端：

- Go
- Google Wire 依赖注入
- Kingpin CLI
- Swagger/OpenAPI
- SQLite / Postgres 驱动装配
- pubsub / jobs / events / stream

前端：

- React 17
- TypeScript
- Webpack
- Jest
- Harness 自有设计系统与 UI 库

平台能力：

- Pipeline execution
- Gitspaces
- Artifact registry
- Repository hosting
- Auth / token / service principal
- Helm chart / Docker 交付

从工程形态看，这是标准的“平台型大仓库”技术选型，不追求时髦，而追求模块覆盖和产品能力闭环。

### 设计思路

我认为它最值得研究的设计思路有七个：

1. **把整个开发平台当成统一 control plane 来做**
   代码仓、流水线、开发环境、制品库都不是散工具，而是平台内协同模块。

2. **统一入口，多能力装配**
   `gitness` 二进制既是 server 入口，也是 CLI 能力总入口，便于交付和运维。

3. **依赖注入治理复杂度**
   `wire.go` 虽然庞大，但至少把复杂依赖图显式化了，利于大系统装配。

4. **领域模块化而不是微服务优先**
   它更多是在单仓内做清晰领域划分，而不是一开始拆成大量网络级微服务。

5. **平台级 bootstrap 设计**
   `bootstrap.go` 里把 admin user、system service、pipeline service、gitspace service 这些系统主体初始化成一等流程。

6. **CLI / API / UI / 部署面同时存在**
   这不是“先有后端再补别的”，而是从一开始就按完整平台交付面考虑。

7. **兼容历史路径的渐进演进**
   从 Drone 到 Harness，从 `gitness` 到新品牌，说明它接受“演进中的历史包袱”，而不是强行一次性重写。

### 对我们可借鉴的点

这个仓库虽然不属于 agent 方向，但对我们仍然有几个高价值启发。

可借鉴的不是具体业务，而是 **平台化治理方式**：

- 如果我们未来从“规划仓”演进到“执行平台”，需要更认真地定义 control plane
- 需要区分：
  - bootstrap
  - runtime services
  - API surface
  - background jobs
  - event bus
  - storage layer
- 需要考虑统一入口，而不是零散脚本拼装
- 大型系统不一定先拆微服务，先做清晰领域模块和装配边界往往更务实
- service principal / system actor / admin bootstrap 这类“系统主体”初始化值得提前建模

### 不宜直接照搬的点

对我们当前阶段来说，绝大部分内容都不适合直接照搬：

- 它的问题规模和我们完全不在一个量级
- 它是完整开发平台，不是 agent planning 系统
- 大一统平台内核会带来很高复杂度和维护成本
- 前后端、部署、registry、pipeline 一起推进的节奏不适合我们现在

所以这里真正值得借鉴的是 **平台治理抽象**，而不是产品版图。

### 对我们的具体启发

这个仓库对我们的具体启发主要有六个：

- 以后如果系统继续长大，不能只靠文档和 prompt，要出现清晰的装配入口
- 要提前思考 bootstrap：谁是 system actor，谁负责初始化默认状态
- 要把服务边界、事件边界、存储边界写清楚，避免后续越做越乱
- 如果未来做 API/CLI/UI，不应分别长成三套逻辑，而应共享同一个核心系统
- 不要过早执着微服务化，先把领域边界和依赖图做对
- 历史包袱不可避免，所以我们要尽量尽早建立 canonical 命名与真源

### 当前结论

`harness/harness` 不是我们要模仿的产品形态，但它是一个很好的“平台级系统如何收敛复杂度”的样本。

对我们来说，它最值得学习的不是某个技术点，而是：

- 平台控制面的抽象方式
- 大系统模块装配方式
- bootstrap 与系统主体初始化
- 统一入口与多交付面协同

如果说前面三个仓库更接近“AI harness / workflow / planning”世界，那么 `harness/harness` 提供的是更上层的 **平台工程视角**。
