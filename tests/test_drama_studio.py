from __future__ import annotations

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
                    "minimax-h3",
                ],
                capture_output=True,
                text=True,
                encoding="utf-8",
            )
            self.assertEqual(r_init.returncode, 0, r_init.stderr)
            self.assertTrue((root / "00_季播总案与资产表.md").exists())
            self.assertTrue((root / "01_分集卡点纲.md").exists())

            ep1 = root / "剧本" / "第001集_不准抬头.md"
            ep1.write_text(
                "# 第001集 不准抬头\n\n"
                "## 镜号 1（3s）\n"
                "- **场景**：`@LOC-01` 高三晚自习教室\n"
                "- **画面**：黑板上突然渗出红字《晚自习守则：十点后听到点名绝不能答应》。陈默（`@CHAR-01` `[shock]`）猛地咬住笔杆。\n"
                "- **台词**：\n"
                "  - 王老师（`@CHAR-02`）：「陈默，这道送分题你选哪个？」\n"
                "  - 陈默（`@CHAR-01`）：「老师，我现在要是敢开口，咱俩都得交卷！」\n\n"
                "## 镜号 2（4s）【集末钩子】\n"
                "- **场景**：`@LOC-01` 高三晚自习教室\n"
                "- **画面**：讲台下的影子突然裂开两张嘴，倒计时弹窗【00:03】在陈默瞳孔里炸开。\n"
                "- **台词**：\n"
                "  - 陈默（`@CHAR-01`）：「等等，五年高考三年模拟里没写这题超纲啊！」\n",
                encoding="utf-8",
            )

            r_lint = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPTS_DIR / "lint_script.py"),
                    "--dir",
                    str(root / "剧本"),
                    "--genre",
                    "shadiao",
                    "--backend",
                    "minimax-h3",
                ],
                capture_output=True,
                text=True,
                encoding="utf-8",
            )
            self.assertEqual(r_lint.returncode, 0, r_lint.stdout + "\n" + r_lint.stderr)

            for fmt in ("production", "clean-script"):
                out_docx = root / "交付" / f"夜自习守则_{fmt}.docx"
                out_txt = root / "交付" / f"夜自习守则_{fmt}.txt"
                r_exp = subprocess.run(
                    [
                        sys.executable,
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


if __name__ == "__main__":
    unittest.main()
