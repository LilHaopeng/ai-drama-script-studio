![AI短剧编剧室 · AI Drama Script Studio](assets/drama-script-hero.png)

# AI 短剧与沙雕短剧编剧室 · AI Drama Script Studio

**简体中文** | [English](README_EN.md)

专攻 **AI 短剧（MiniMax-H3 仿真人/3D 剧情向）**、**AI 漫剧（2D/3D 高奇观多季连载）**与**沙雕短剧/沙雕漫（红果 40× 快切对白轨 & 抖音/推文高旁白合集轨）**的一体化编剧与改编 Agent Skill。支持「从零独立原创完整剧本」与「基于短篇/商业长篇/传统出版长篇小说或大纲改编剧本」双入口；开写前强制执行**节奏与逻辑 5 问预匹配**，内置控算力固定资产表、人物命名与剧名/分集名去 AI 味规范、黄金前 3 集与单集秒级卡点纲、视听分集剧本、按需分镜表、红果 40× 旁白占比红线体检及双模式 DOCX/TXT 导出。当前版本 **v1.3.0**。

默认采用**简体中文**创作；原生兼容上游 [Webnovel Market Radar](https://github.com/LilHaopeng/webnovel-market-radar)、[Webnovel Short Studio](https://github.com/LilHaopeng/webnovel-short-studio)、[Webnovel Long Studio](https://github.com/LilHaopeng/webnovel-long-studio) 及传统出版长篇三件套底稿。

## 核心特性

- **写前必过「节奏与逻辑 5 问预匹配门」**：拒绝把小说机械缩写成对话，也拒绝钩子发虚就盲目开写第 1 集。动笔前先核对剧种载体、前 3–5 秒视觉强钩子、黄金前 3 集留存闭环、爽点/笑点反杀逻辑与集末硬卡点。
- **守住红果 `40×` 分成生死线**：针对冲击红果/短剧创作者中心最高分成系数（`40×` 仿真人 AI 短剧、2D/3D 漫剧、表情包沙雕漫）的项目，`lint_script.py` 自动监控**单集旁白/心理独白（OS）字数占比 ≤ 20%（全季超 20% 集数 < 3 集）**，防止因旁白超标被降档为 `10×` 动态解说漫剧（收益相差 4 倍）；抖音/推文旁白合集流可通过 `--allow-high-narration --compilation` 显式适配。
- **三大内置剧种与智能后端路由（`--backend auto`）**：
  - **`ai-drama`（默认 `minimax-h3`）**：60–90 秒/集（生活流可至 75–110 秒，约 8–14 镜），贴合 MiniMax-H3 **5–15 秒原生音画同步与中文口型直出**，严格执行**多人同框口型隔离**（单镜至多 1 人开口，多人交锋自动切正反打）与单镜台词 ≤18–22 字约束。
  - **`comic-drama`（默认 `jimeng` / `general`）**：60–120 秒/集，支持屏幕可读特效字/系统 HUD 弹窗、战力/规则可视化与 60–120 集/季多季连载钩子。
  - **`shadiao`（默认 `general`）**：双子轨支持——子轨 A **红果 40× 快切沙雕漫**（70–95 秒/集，固定切脸码 `normal/shock/smirk/rage/cry/sweat` + HUD 贴纸，旁白 ≤20%）与子轨 B **抖音/推文 2–15 分钟高旁白沙雕合集**（传 `--compilation --allow-high-narration`）。
- **控算力固定资产表、去 AI 味命名与精短分集名**：`00_季播总案与资产表.md` 锁死 `@CHAR-*`、`@LOC-*`、`@PROP-*`、`@VOICE-*` 固定槽位（常驻核心角色 3–8 人，单集主场景 1–2 处）与单剧声口切片；依据 [naming-and-titling.md](skills/ai-drama-script-studio/references/naming-and-titling.md) 约束姓氏配额与配音防同音，剧名提供跨型谱 3 风格备选，分集名保持 2–6 字画面锚点或 4–8 字短钩子。
- **双模式纯净导出（进组制作版 vs 红果送审纯净版）**：`export_drama.py` 支持 `--format production`（保留分镜/资产槽位供 AI 视频产线使用）与 `--format clean-script`（自动从资产圣经还原 `@CHAR` / `@LOC` / `@PROP` / `@VOICE` 真实名称、剥离 `[Visual Prompt]` / `[Audio Prompt]` / 纯 `[音效]` 等工程提示词同时保留同行台词，并校验红果剧名规范，一键生成送审定稿）。

## 版本亮点

### v1.3.0：商业长篇适配、智能后端路由与纯净导出修复

- **全面打通商业长篇改编入口**：适配 `webnovel-long-studio` 的四表工作台与滚动阶段细纲，实现从短篇、商业连载长篇到传统出版长篇的全谱系小说视听化改编。
- **智能后端路由与合集模式**：`init_drama_project.py` 与 `lint_script.py` 新增 `--backend auto`（按剧种自动匹配 `minimax-h3` / `jimeng` / `general`）及 `--compilation`（精准适配 2–15 分钟沙雕动画合集，不再误报超长时长）。
- **体检与送审导出精度提升**：`lint_script.py` 准确识别带 `[音效]` 前缀的短台词与 `画外音` 旁白；`export_drama.py --format clean-script` 修复 `@PROP-*` 道具槽位还原，并在剥离纯拟音/环境声标签时精准保留同行角色对白。

## 配套创作工作流（七大技能全生态）

同系列七大技能既可独立使用，也可串联成从市场扫榜、小说创作到 AI 短剧剧本落地的完整管线：

- **商业网文与 AI 短剧套件**
  1. [网文与短剧市场雷达 · Webnovel Market Radar](https://github.com/LilHaopeng/webnovel-market-radar)：扫描红果短剧榜、抖音短剧创作者中心供需/飙升榜与网文热榜，输出 `选题简报.md`。
  2. [短篇网文与微短剧爽文创作室 · Webnovel Short Studio](https://github.com/LilHaopeng/webnovel-short-studio)：5 万字以内高概念脑洞短篇与微短剧向爽文创作。
  3. [商业连载长篇网文创作室 · Webnovel Long Studio](https://github.com/LilHaopeng/webnovel-long-studio)：5 万–200 万字+ 商业连载长篇网文一体化创作与防崩文工作台。
  4. **AI 短剧与沙雕短剧编剧室 · AI Drama Script Studio**：既可根据 `选题简报.md` 独立原创整季 AI 短剧/漫剧/沙雕剧，也可将短篇/商业长篇/传统出版小说或大纲改编为视听分集剧本。
- **传统出版与精品长篇三件套**
  5. [小说世界观架构师 · Story World Architect](https://github.com/LilHaopeng/story-world-architect)
  6. [小说大纲架构师 · Story Outline Architect](https://github.com/LilHaopeng/story-outline-architect)
  7. [小说正文写作 · Story Prose Writer](https://github.com/LilHaopeng/story-prose-writer)

## 安装方式

1. **通过 `skill-installer` 安装（Codex 等）**
   ```text
   $skill-installer 请从 https://github.com/LilHaopeng/ai-drama-script-studio 安装 skills/ai-drama-script-studio
   ```
2. **手动复制到本地技能目录（Antigravity / Claude Code / Codex / Cursor）**
   克隆本仓库，将 `skills/ai-drama-script-studio/` 完整复制到对应客户端的技能目录：
   - **Antigravity**：`~/.gemini/config/skills/ai-drama-script-studio`
   - **Claude Code**：`~/.claude/skills/ai-drama-script-studio`
   - **Codex**：`~/.codex/skills/ai-drama-script-studio` 或 `~/.agents/skills/ai-drama-script-studio`
   - **Cursor**：`~/.cursor/skills/ai-drama-script-studio`

初始化与视听体检脚本仅依赖 Python 3.10+ 标准库；如需使用 `export_drama.py` 导出 `.docx` 剧本，可执行 `python -m pip install -r requirements.txt` 安装 `python-docx`。

## 快速上手

**从零原创红果 40× 沙雕漫剧 / AI 短剧**：

```text
$ai-drama-script-studio
我想做一部面向红果 40× 赛道的规则怪谈校园微恐沙雕漫剧。
先带我过写前节奏与逻辑 5 问预匹配，建好控算力资产表和前 10 集卡点纲，再试写黄金前 3 集分镜剧本。
```

**将现有短篇/商业长篇小说或大纲改编为 MiniMax-H3 AI 短剧剧本**：

```text
$ai-drama-script-studio
把 <小说项目目录>/正文/ 下的作品改编成 30 集 MiniMax-H3 AI 短剧剧本。
先诊断原著哪些慢热段落需要前置或视听化改造，确认写前 5 问预匹配方案后再排资产表和分集卡点纲。
```

## 配套辅助脚本

| 脚本 | 功能说明 |
|---|---|
| `init_drama_project.py` | 初始化 `00_季播总案与资产表.md`、`01_分集卡点纲.md`、`剧本/`、`分镜/`、`交付/`（支持 `--genre ai-drama\|comic-drama\|shadiao`、`--entry original\|adapt-short\|adapt-long`、`--backend auto\|minimax-h3\|jimeng\|general`、`--source-ref`）。 |
| `lint_script.py` | 视听可执行性与红果 40× 合规体检镜子（纯 `[ADVISORY]`）：兼容中文标准剧本与英文 Shot-block（`### Shot N` / `ep_XX.md`），统计镜数、台词字数、预估秒数、单集与全季旁白/OS/画外音占比、MiniMax-H3 单镜超长台词、不可拍心理词与集末钩子（支持 `--backend auto`、`--allow-high-narration`、`--compilation`、`--json`）。 |
| `export_drama.py` | 双格式剧本导出器：支持 `--format production`（带完整分镜与资产表，`--include-bible`）与 `--format clean-script`（自动还原资产圣经中的角色/场景/道具/声线名、剥离 AI 生成提示词与纯音效标签、保留同行对白并校验红果剧名规范，一键输出送审纯净剧本 `.docx` / `.txt`）。 |

常用命令示例：

```bash
# 1. 初始化项目（--backend auto 按剧种自动路由）
python skills/ai-drama-script-studio/scripts/init_drama_project.py --root <项目根> --title "夜自习守则" --genre shadiao --entry original --backend auto

# 2. 视听与红果 40x 旁白红线体检（抖音旁白合集可加 --allow-high-narration --compilation）
python skills/ai-drama-script-studio/scripts/lint_script.py --dir <项目根>/剧本 --genre shadiao --backend auto

# 3. 导出产线完整版或红果送审纯净剧本
python skills/ai-drama-script-studio/scripts/export_drama.py --root <项目根> --format clean-script --out-docx <项目根>/交付/夜自习守则_送审剧本.docx --out-txt <项目根>/交付/夜自习守则_送审剧本.txt --title "夜自习守则"
```

运行回归测试：

```bash
python -B -m unittest discover -s tests -v
```

## 参考文档

- [改编诊断与写前节奏逻辑预匹配](skills/ai-drama-script-studio/references/adaptation-and-pacing.md)：写前 5 问门禁、黄金前 3 集 30-30-30 法则、短篇扩容与商业/出版长篇切片改编策略。
- [三大剧种剧本规范与范例](skills/ai-drama-script-studio/references/genre-templates.md)：`ai-drama`（MiniMax-H3）、`comic-drama`（高奇观漫剧）、`shadiao`（快切对白轨 & 高旁白合集轨）双格式剧本模板。
- [控算力资产表、视听体检与双模式交付](skills/ai-drama-script-studio/references/production-and-assets.md)：固定资产槽位、MiniMax-H3 音画直出纪律、红果 40× vs 10× 规则与送审导出规范。
- [人物命名平衡与剧名/分集命名规范](skills/ai-drama-script-studio/references/naming-and-titling.md)：六大题材姓氏配额、配音防同音与龙套降噪、五大剧名型谱与精短反剧透分集命名。

## 隐私与许可证

所有辅助脚本均在本地工作区内读写文件，不会上传任何剧本原稿。本仓库采用 [MIT License](LICENSE) 开源（Copyright © 2026 LilHaopeng）。
