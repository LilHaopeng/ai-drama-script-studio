# AI Drama Script Studio · AI 短剧与沙雕短剧编剧室

[简体中文](README.md) | **English**

An all-in-one scriptwriting and novel-adaptation Agent Skill purpose-built for **AI Short Dramas (`ai-drama`, MiniMax-H3 photoreal/3D vertical dramas)**, **AI Comic Dramas (`comic-drama`, 2D/3D high-spectacle multi-season series)**, and **Comedy Short Dramas (`shadiao`, fast-cut dialogue memes & narrator-driven comedy animations)**. Supports both **original full-season scriptwriting from scratch** and **visual adaptation from short/long webnovels or outlines**. Current version: **v1.2.0**.

## Key Capabilities

- **Pre-Writing Pacing & Logic Gate (5-Question Alignment)**: Prevents dumping prose summaries straight into dialogue. Before writing Episode 1, aligns genre format, 3-second visual opening hook, Golden Episodes 1–3 retention loop, non-contrived payoff logic, and episode-end cliffhangers.
- **Hongguo `40×` Revenue Multiplier Guardrail**: Automatically monitors **narrator / inner-monologue (`OS/VO`) share ≤ 20% per episode (and < 3 episodes over 20% per season)** so dialogue-driven AI dramas, comic dramas, and meme dramas qualify for Hongguo's top `40×` revenue tier instead of being downgraded to the `10×` narrated-comic tier. (Douyin/social narrator-led compilations can opt out via `--allow-high-narration`.)
- **Three Built-in Genre Templates & Backend Rules**:
  - **`ai-drama` (MiniMax-H3 Photoreal / 3D Drama)**: 60–90s per episode (8–14 shots), tuned for MiniMax-H3's 5–15s native audio-visual lip-sync generation with strict **single-speaker-per-shot lip-sync isolation** and ≤18–22 CJK characters per shot line.
  - **`comic-drama` (2D/3D High-Spectacle Comic Drama)**: 60–120s per episode with on-screen HUD/system popups, power/rule visualization, and multi-season world hooks.
  - **`shadiao` (Comedy Short Drama Dual-Track)**: Supports both **Hongguo 40× fast-cut dialogue comedy** (2–4s shots, fixed expression swap codes `normal/shock/smirk/rage/cry/sweat` + HUD stickers, narration ≤20%) and **Douyin high-narration panda-meme comedy compilations**.
- **Compute-Controlled Asset Bible, Anti-AI Naming & Punchy Episode Titles**: `00_季播总案与资产表.md` locks reusable `@CHAR-*`, `@LOC-*`, `@PROP-*`, and `@VOICE-*` slots while applying genre-calibrated surname quotas, TTS homophone collision checks, 3-style heterogeneous series title options, and concise 2–8 character visual episode titles ([naming-and-titling.md](skills/ai-drama-script-studio/references/naming-and-titling.md)).
- **Dual-Format Clean Export (`production` vs. `clean-script`)**: `export_drama.py` exports either full production scripts (with visual/audio prompts and asset slots) or platform-submission `clean-script` files (automatically mapping `@CHAR_01` IDs from `series_bible.md` to real character names, stripping `[Visual Prompt]` / `[Audio Prompt]` / `[SFX]` blocks, and validating title compliance).

## Companion Studio Pipeline

1. [Webnovel Market Radar](https://github.com/LilHaopeng/webnovel-market-radar): Scans Hongguo AI drama charts, Douyin Short Drama Creator Center supply/demand & soaring charts, and webnovel rankings to produce `选题简报.md`.
2. [Webnovel Short Studio](https://github.com/LilHaopeng/webnovel-short-studio): Writes high-concept short webnovels and micro-drama fiction under 50k words.
3. **AI Drama Script Studio**: Writes original AI short drama scripts or adapts novels/outlines from `Webnovel Short Studio` and the long-form novel suite.
4. [Story World Architect](https://github.com/LilHaopeng/story-world-architect) → [Story Outline Architect](https://github.com/LilHaopeng/story-outline-architect) → [Story Prose Writer](https://github.com/LilHaopeng/story-prose-writer): Full long-form novel studio suite.

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

## Helper Scripts

| Script | Purpose |
|---|---|
| `init_drama_project.py` | Scaffolds `00_季播总案与资产表.md`, `01_分集卡点纲.md`, `剧本/`, `分镜/`, and `交付/` (`--genre`, `--entry`, `--backend`). |
| `lint_script.py` | Audits shot counts, spoken dialogue length, estimated duration, per-episode and season-wide narration/OS share (`≤20%` Hongguo `40×` guardrail), MiniMax-H3 lip-sync constraints, unfilmable mental exposition, and cliffhanger hooks. |
| `export_drama.py` | Compiles episodes into `.docx` and `.txt` in either `production` mode or `clean-script` submission mode (with automatic `series_bible.md` character-ID resolution). |

Run unit tests:

```bash
python -B -m unittest discover -s tests -v
```

## Privacy & License

All helper scripts operate strictly on local workspace files and never upload scripts. Released under the [MIT License](LICENSE) (Copyright © 2026 LilHaopeng).
