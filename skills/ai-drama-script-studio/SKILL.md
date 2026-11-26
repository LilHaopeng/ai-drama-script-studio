---
name: ai-drama-script-studio
description: 专攻 AI 短剧、AI 漫剧与沙雕短剧的一体化编剧与改编工作室。支持「从零独立原创完整剧本」与「基于短篇/商业长篇/传统出版长篇小说或大纲改编剧本」双入口（兼容 `webnovel-short-studio`、`webnovel-long-studio` 与长篇三件套）；开写前强制执行节奏与逻辑 5 问预匹配，内置三大剧种模板——MiniMax-H3 仿真人 AI 短剧（ai-drama）、高奇观多季 AI 漫剧（comic-drama）、高频反转沙雕短剧（shadiao）。涵盖控算力资产表、黄金前3集与单集秒级卡点纲、视听分集剧本、按需分镜表、视听体检与纯净 DOCX/TXT 导出。默认简体中文。不用于纯文字小说正文撰写。
metadata:
  version: "1.3.0"
---

# AI 短剧与沙雕短剧编剧工作室

面向红果、抖音等竖屏/横屏生态的 AI 短剧编剧与小说改编工作流。既可从零原创整季完整剧本，也可吃进 `webnovel-short-studio`、`webnovel-long-studio`、传统出版长篇三件套（`story-world-architect` / `story-outline-architect` / `story-prose-writer`）或外部任意底稿完成视听重构。

## 核心原则

1. **先过写前「节奏与逻辑 5 问预匹配」**：不把小说直接缩成对话，也不盲写第 1 集。动笔前对齐剧种、前 3–5 秒钩子、黄金前 3 集闭环、逻辑自洽（拒憋屈烧心）与集末卡点。
2. **按平台守红线，不机械一刀切**：冲红果 `40×` 分成时控单集旁白/OS ≤20%（详见 [genre-templates.md](references/genre-templates.md)），抖音解说流可显式豁免；零版权 BGM 不排斥剧情内自然声源。
3. **硬资产硬卡点，松台词声口**：锁死控算力资产上限（常驻核心角色 `3–8 人`，单镜建议 `2–3 人`、上限 `4 人`，单集主场景 `1–2 处`、上限 `3 处`），每部剧独立定调 1 段声口切片，拒绝跨剧 AI 翻译腔。

## 阶段路由

按用户已有材料切入对应阶段（默认简体中文）：

| 阶段 | 适用场景 | 核心动作 | 必读参考 |
|---|---|---|---|
| `intake` | 创意、`webnovel-market-radar` 选题简报，或已有短/长篇小说与大纲 | 判定入口（`original` / `adapt-short` / `adapt-long`）与剧种（`ai-drama` / `comic-drama` / `shadiao`），过**写前节奏与逻辑 5 问预匹配** | [adaptation-and-pacing.md](references/adaptation-and-pacing.md) |
| `bible` | 逻辑与节奏已拍板 | 填妥 `00_季播总案与资产表.md`：剧集总案、异构 3 备选剧名、控算力固定资产表（`@CHAR/@LOC/@PROP/@VOICE`）与单剧声口切片 | [genre-templates.md](references/genre-templates.md)、[production-and-assets.md](references/production-and-assets.md)、[naming-and-titling.md](references/naming-and-titling.md) |
| `outline` | 资产已定，排整季分集 | 产出 `01_分集卡点纲.md`：黄金前 3 集详卡 + 全季每集冲突、爽点/笑点维度轮换与集末硬钩子 | [adaptation-and-pacing.md](references/adaptation-and-pacing.md)、[naming-and-titling.md](references/naming-and-titling.md) |
| `script` | 撰写视听分集剧本 | 写 `剧本/第XXX集_集名.md`（集名用 `2–6 字` 画面锚点或 `4–8 字` 短钩子；先试写第 1–3 集校准时长与嘴感后再批量推进） | [genre-templates.md](references/genre-templates.md)、[naming-and-titling.md](references/naming-and-titling.md) |
| `storyboard` | 需喂给 MiniMax-H3 / 即梦 / 火山剧创 | 按需将指定集数拆为逐镜视听与资产槽位表 | [production-and-assets.md](references/production-and-assets.md) |
| `check` & `export` | 体检与交付送审/进组 | 运行 `lint_script.py` 体检，用 `export_drama.py` 导出产线版或红果送审纯净版 `.docx` / `.txt` | [production-and-assets.md](references/production-and-assets.md) |

## 三大内置剧种速查

| 剧种 (`--genre`) | 典型平台与气质 | 节奏与季播区间 | 默认后端 (`--backend auto`) |
|---|---|---|---|
| **`ai-drama`**（写实 AI 短剧） | 红果 AI 剧：年代创业、乡土生活流、历史团队、都市轻逆袭/萌宝 | 60–90 秒/集（生活流 75–110 秒），8–14 镜；常规 **30–60 集**（长线可延至 60–120 集） | `minimax-h3` |
| **`comic-drama`**（高奇观 AI 漫剧） | 红果漫剧：规则怪谈、末世求生、玄幻修仙、系统脑洞 | 60–120 秒/集，强奇观定格与 UI 弹窗；多季连载 **60–120 集/季** | `jimeng`（或 `general`） |
| **`shadiao`**（沙雕短剧双子轨） | 子轨 A：红果 40× 快切沙雕漫（旁白≤20%）；<br>子轨 B：抖音/推文旁白沙雕动画 | 子轨 A：70–95 秒/集，**15–40 集**（10–15 秒一包袱）；<br>子轨 B：**2–15 分钟合集**（传 `--compilation --allow-high-narration`） | `general` |

## 快速工作流命令

### 1. 初始化短剧项目

```text
python <skill-dir>/scripts/init_drama_project.py \
  --root <项目根> \
  --title <剧名> \
  --genre <ai-drama|comic-drama|shadiao> \
  --entry <original|adapt-short|adapt-long> \
  --backend <auto|minimax-h3|jimeng|general>
```

（上游有 `webnovel-market-radar` 的 `选题简报.md` 或小说/大纲路径时，用 `--source-ref <路径>` 记录溯源。）

### 2. 剧本视听体检（客观镜子，仅出 `[ADVISORY]`）

```text
python <skill-dir>/scripts/lint_script.py --dir <项目根>/剧本 --genre <ai-drama|comic-drama|shadiao> --backend auto
```

（抖音旁白合集可加 `--allow-high-narration --compilation`。）

### 3. 产线版 / 红果送审纯净版导出

```text
python <skill-dir>/scripts/export_drama.py --root <项目根> --out-docx <交付>/<剧名>_剧本.docx --out-txt <交付>/<剧名>_纯文本.txt --title <剧名> --format <production|clean-script>
```
