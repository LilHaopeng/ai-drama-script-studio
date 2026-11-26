from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = REPO_ROOT / "skills" / "ai-drama-script-studio"
SCRIPTS_DIR = SKILL_DIR / "scripts"


class AIDramaScriptStudioTests(unittest.TestCase):
    def test_init_lint_and_export_both_modes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "drama_proj"
            r_init = subprocess.run(
                [
                    sys.executable,
                    "-B",
                    str(SCRIPTS_DIR / "init_drama_project.py"),
                    "--root",
                    str(root),
                    "--title",
                    "夜自习守则",
                    "--genre",
                    "shadiao",
                    "--entry",
                    "original",
                    "--backend",
                    "auto",
                ],
                capture_output=True,
                text=True,
                encoding="utf-8",
            )
            self.assertEqual(r_init.returncode, 0, r_init.stderr)
            self.assertTrue((root / "00_季播总案与资产表.md").exists())
            self.assertTrue((root / "01_分集卡点纲.md").exists())

            # Populate asset bible with @CHAR / @LOC / @PROP entries for clean-script resolution
            bible = root / "00_季播总案与资产表.md"
            bible.write_text(
                "# 季播总案与资产表\n\n"
                "| 资产槽位 | 名称 | 说明 |\n|---|---|---|\n"
                "| `@CHAR-01` | 陈默 | 高三学生 |\n"
                "| `@CHAR-02` | 王老师 | 班主任 |\n"
                "| `@LOC-01` | 高三晚自习教室 | 主场景 |\n"
                "| `@PROP-01` | 红色模拟卷 | 关键道具 |\n",
                encoding="utf-8",
            )

            ep1 = root / "剧本" / "第001集_不准抬头.md"
            ep1.write_text(
                "# 第001集 不准抬头\n\n"
                "## 场 1 | `@LOC-01` 高三晚自习教室 日/内\n\n"
                "### 镜头 1（3s）\n"
                "- 画面：黑板上渗出红字，陈默（`@CHAR-01` `[shock]`）捏紧 `@PROP-01`。\n"
                "- **声音**：[音效] 粉笔折断声清脆响起；王老师（`@CHAR-02`）：「陈默，这道送分题你选哪个？」\n\n"
                "### 镜头 2（4s）【集末钩子】\n"
                "- 画面：讲台下的影子裂开两张嘴，陈默（`@CHAR-01`）瞪大眼睛。\n"
                "- **声音**：[音效] 拍桌，陈默（`@CHAR-01`）：「老师，这题超纲了，五年高考三年模拟里没写这题啊！」\n",
                encoding="utf-8",
            )

            r_lint = subprocess.run(
                [
                    sys.executable,
                    "-B",
                    str(SCRIPTS_DIR / "lint_script.py"),
                    "--dir",
                    str(root / "剧本"),
                    "--genre",
                    "shadiao",
                    "--backend",
                    "auto",
                    "--json",
                ],
                capture_output=True,
                text=True,
                encoding="utf-8",
            )
            self.assertEqual(r_lint.returncode, 0, r_lint.stdout + "\n" + r_lint.stderr)
            lint_data = json.loads(r_lint.stdout)
            ep_metrics = lint_data["results"][0]["metrics"]
            self.assertEqual(ep_metrics["backend"], "general")
            self.assertGreater(ep_metrics["spoken_cjk"], 20)

            for fmt in ("production", "clean-script"):
                out_docx = root / "交付" / f"夜自习守则_{fmt}.docx"
                out_txt = root / "交付" / f"夜自习守则_{fmt}.txt"
                r_exp = subprocess.run(
                    [
                        sys.executable,
                        "-B",
                        str(SCRIPTS_DIR / "export_drama.py"),
                        "--root",
                        str(root),
                        "--format",
                        fmt,
                        "--out-docx",
                        str(out_docx),
                        "--out-txt",
                        str(out_txt),
                        "--title",
                        "夜自习守则",
                    ],
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                )
                self.assertEqual(r_exp.returncode, 0, r_exp.stdout + "\n" + r_exp.stderr)
                self.assertTrue(out_docx.exists())
                self.assertTrue(out_txt.exists())
                if fmt == "clean-script":
                    clean_txt = out_txt.read_text(encoding="utf-8")
                    self.assertNotIn("@PROP-01", clean_txt)
                    self.assertIn("红色模拟卷", clean_txt)
                    self.assertNotIn("[音效]", clean_txt)
                    self.assertIn("老师，这题超纲了", clean_txt)


if __name__ == "__main__":
    unittest.main()
