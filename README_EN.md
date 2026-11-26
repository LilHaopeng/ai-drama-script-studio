![AI Drama Script Studio · AI短剧编剧室](assets/drama-script-hero.png)

# AI Drama Script Studio · AI 短剧与沙雕短剧编剧室

[简体中文](README.md) | **English**

An all-in-one scriptwriting and novel-adaptation Agent Skill purpose-built for **AI Short Dramas (`ai-drama`, MiniMax-H3 photoreal/3D vertical dramas)**, **AI Comic Dramas (`comic-drama`, 2D/3D high-spectacle multi-season series)**, and **Comedy Short Dramas (`shadiao`, Hongguo 40× fast-cut dialogue memes & Douyin narrator-led comedy compilations)**. Supports both **original full-season scriptwriting from scratch** and **visual adaptation from short webnovels, commercial serialized long webnovels, or traditional long-form novels/outlines**. Current version: **v1.3.0**.

By default, the skill writes in **Simplified Chinese (`简体中文`)** and seamlessly ingests source projects from [Webnovel Market Radar](https://github.com/LilHaopeng/webnovel-market-radar), [Webnovel Short Studio](https://github.com/LilHaopeng/webnovel-short-studio), [Webnovel Long Studio](https://github.com/LilHaopeng/webnovel-long-studio), and the traditional long-form novel trio.

## Key Capabilities

- **Pre-Writing Pacing & Logic Gate (5-Question Alignment)**: Prevents dumping prose summaries straight into dialogue. Before writing Episode 1, aligns genre format, 3–5 second visual opening hook, Golden Episodes 1–3 retention loop, non-contrived payoff logic, and episode-end cliffhangers.
- **Hongguo `40×` Revenue Multiplier Guardrail**: Automatically monitors **narrator / inner-monologue (`OS/VO/画外音`) share ≤ 20% per episode (and < 3 episodes over 20% per season)** so dialogue-driven AI dramas, comic dramas, and meme dramas qualify for Hongguo's top `40×` revenue tier instead of being downgraded to the `10×` narrated-comic tier. Douyin/social narrator-led compilations can opt in via `--allow-high-narration --compilation`.
- **Three Built-in Genre Templates & Smart Backend Routing (`--backend auto`)**:
  - **`ai-drama` (default `minimax-h3`)**: 60–90s per episode (75–110s for slice-of-life, 8–14 shots), tuned for MiniMax-H3's 5–15s native audio-visual lip-sync generation with strict **single-speaker-per-shot lip-sync isolation** and ≤18–22 CJK characters per shot line.
  - **`comic-drama` (default `jimeng` / `general`)**: 60–120s per episode with on-screen HUD/system popups, power/rule visualization, and 60–120 episode multi-season world hooks.
  - **`shadiao` (default `general`, Dual-Track)**: Supports both **Hongguo 40× fast-cut dialogue comedy** (70–95s/ep, fixed expression swap codes `normal/shock/smirk/rage/cry/sweat` + HUD stickers, narration ≤20%) and **Douyin 2–15 min high-narration comedy compilations** (`--compilation --allow-high-narration`).
- **Compute-Controlled Asset Bible, Anti-AI Naming & Punchy Episode Titles**: `00_季播总案与资产表.md` locks reusable `@CHAR-*`, `@LOC-*`, `@PROP-*`, and `@VOICE-*` slots (3–8 recurring cast, 1–2 primary sets/ep) while enforcing genre-calibrated surname quotas, TTS homophone collision checks, 3-style heterogeneous series titles, and concise 2–8 character visual episode titles.
- **Dual-Format Clean Export (`production` vs. `clean-script`)**: `export_drama.py` exports either full production scripts (with visual/audio prompts, asset slots, and optional `--include-bible`) or platform-submission `clean-script` files (automatically mapping `@CHAR` / `@LOC` / `@PROP` / `@VOICE` IDs from the asset bible to real names, stripping `[Visual Prompt]` / `[Audio Prompt]` / standalone Foley blocks while keeping inline spoken lines, and validating Hongguo title compliance).

## What's New in v1.3.0

- **Commercial Long-Form Novel Adaptation**: Directly ingests `webnovel-long-studio` 4-ledger workbenches and rolling stage outlines alongside `webnovel-short-studio` and the traditional novel trio.
- **Smart `--backend auto` & `--compilation` Support**: Automatically routes each genre to its optimal video backend and supports 2–15 minute Douyin comedy compilations cleanly in `lint_script.py`.
- **Higher-Precision Linter & Submission Export**: Accurately parses `[音效]`-prefixed spoken lines and `画外音` voiceovers in `lint_script.py`, and fixes `@PROP-*` resolution plus clean Foley stripping without dropping inline dialogue in `export_drama.py --format clean-script`.

## Companion Studio Pipeline (7-Skill Ecosystem)

- **Commercial Webnovel & AI Drama Suite**
  1. [Webnovel Market Radar](https://github.com/LilHaopeng/webnovel-market-radar): Scans Hongguo AI drama charts, Douyin Short Drama Creator Center supply/demand & soaring charts, and webnovel rankings to produce `选题简报.md`.
  2. [Webnovel Short Studio](https://github.com/LilHaopeng/webnovel-short-studio): Writes high-concept short webnovels and micro-drama fiction under 50k words.
  3. [Webnovel Long Studio](https://github.com/LilHaopeng/webnovel-long-studio): Writes commercial serialized long-form webnovels (50k–2M+ words) with anti-derailment ledgers.
  4. **AI Drama Script Studio**: Writes original AI short drama scripts or adapts novels/outlines from `Webnovel Short Studio`, `Webnovel Long Studio`, and the traditional long-form suite.
- **Traditional & Literary Long-Form Novel Suite**
  5. [Story World Architect](https://github.com/LilHaopeng/story-world-architect) → 6. [Story Outline Architect](https://github.com/LilHaopeng/story-outline-architect) → 7. [Story Prose Writer](https://github.com/LilHaopeng/story-prose-writer)

## Installation

1. **Via `skill-installer` (Codex, etc.)**
   ```text
   $skill-installer Install skills/ai-drama-script-studio from https://github.com/LilHaopeng/ai-drama-script-studio
   ```
2. **Manual Local Installation (Antigravity / Claude Code / Codex / Cursor)**
   Clone this repository and copy `skills/ai-drama-script-studio/` into your client's skills directory:
   - **Antigravity**: `~/.gemini/config/skills/ai-drama-script-studio`
   - **Claude Code**: `~/.claude/skills/ai-drama-script-studio`
   - **Codex**: `~/.codex/skills/ai-drama-script-studio` or `~/.agents/skills/ai-drama-script-studio`
   - **Cursor**: `~/.cursor/skills/ai-drama-script-studio`

Core scripts use Python 3.10+ standard library only; install `python-docx` via `python -m pip install -r requirements.txt` for `.docx` export.

## Quick Start

```text
$ai-drama-script-studio
I want to create a campus rule-horror comedy drama targeting Hongguo's 40× revenue tier.
Walk me through the 5-question pre-writing pacing & logic gate, build the compute-controlled asset bible and 10-episode beat outline, and draft the Golden Episodes 1–3 scripts.
```

## Helper Scripts

| Script | Purpose |
|---|---|
| `init_drama_project.py` | Scaffolds `00_季播总案与资产表.md`, `01_分集卡点纲.md`, `剧本/`, `分镜/`, and `交付/` (`--genre`, `--entry`, `--backend auto\|minimax-h3\|jimeng\|general`, `--source-ref`). |
| `lint_script.py` | Audits shot counts, spoken dialogue length, estimated duration, per-episode and season-wide narration/OS/VO share (`≤20%` Hongguo `40×` guardrail), MiniMax-H3 lip-sync constraints, unfilmable mental exposition, and cliffhangers (`--backend auto`, `--allow-high-narration`, `--compilation`, `--json`). |
| `export_drama.py` | Compiles episodes into `.docx` and `.txt` in either `production` mode (`--include-bible`) or `clean-script` submission mode (automatic `@CHAR/@LOC/@PROP/@VOICE` resolution + clean Foley stripping + Hongguo title check). |

Common CLI examples:

```bash
python skills/ai-drama-script-studio/scripts/init_drama_project.py --root <project-dir> --title "夜自习守则" --genre shadiao --entry original --backend auto
python skills/ai-drama-script-studio/scripts/lint_script.py --dir <project-dir>/剧本 --genre shadiao --backend auto
python skills/ai-drama-script-studio/scripts/export_drama.py --root <project-dir> --format clean-script --out-docx <project-dir>/交付/夜自习守则_送审剧本.docx --out-txt <project-dir>/交付/夜自习守则_送审剧本.txt --title "夜自习守则"
```

Run unit tests:

```bash
python -B -m unittest discover -s tests -v
```

## Reference Guides

- [Adaptation Diagnosis & Pre-Writing Pacing Gate](skills/ai-drama-script-studio/references/adaptation-and-pacing.md)
- [Genre Script Templates & Examples](skills/ai-drama-script-studio/references/genre-templates.md)
- [Compute-Controlled Asset Bible, Linting & Dual-Mode Export](skills/ai-drama-script-studio/references/production-and-assets.md)
- [Anti-AI Naming & Title / Episode Titling Standards](skills/ai-drama-script-studio/references/naming-and-titling.md)

## Privacy & License

All helper scripts operate strictly on local workspace files and never upload scripts. Released under the [MIT License](LICENSE) (Copyright © 2026 LilHaopeng).
