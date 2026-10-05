#!/usr/bin/env python3
from pathlib import Path
import re
import subprocess
import sys

TARGET_LONG_MATH = (
    r"= (k + 1)\left(\frac{k}{2} + 1\right) = (k + 1)\left(\frac{k+2}{2}\right) = \frac{(k+1)(k+2)}{2}"
)

SPLIT_MATH_REPLACEMENT = (
    r"""= (k + 1)\left(\frac{k}{2} + 1\right) \\
= (k + 1)\left(\frac{k+2}{2}\right) = \frac{(k+1)(k+2)}{2}"""
)

KATEX_OVERFLOW_CSS = """
            /* Allow long formulas to scroll horizontally on small viewports */
            .katex-display {
                overflow-x: auto !important;
                overflow-y: hidden !important;
                -webkit-overflow-scrolling: touch !important;
                max-width: 100% !important;
                padding: 0.25rem 0 !important;
            }
"""

def patch_file(file_path: Path) -> bool:
    content = file_path.read_text(encoding="utf-8")
    original = content

    # 1. Split the long induction line if present
    content = content.replace(
        r"= (k+1)\left(\frac{k}{2} + 1\right) = (k+1)\left(\frac{k+2}{2}\right) = \frac{(k+1)(k+2)}{2}",
        r"= (k+1)\left(\frac{k}{2} + 1\right) \\\n            = (k+1)\left(\frac{k+2}{2}\right) = \frac{(k+1)(k+2)}{2}"
    )

    # 2. Add katex-display containment inside the media query if missing
    if ".katex-display {" not in content:
        mq_pos = content.find("@media (max-width: 768px)")
        if mq_pos != -1:
            open_brace = content.find("{", mq_pos)
            if open_brace != -1:
                content = content[:open_brace + 1] + KATEX_OVERFLOW_CSS + content[open_brace + 1:]

    if content != original:
        file_path.write_text(content, encoding="utf-8")
        return True
    return False

def run_git(args: list[str]) -> subprocess.CompletedProcess:
    result = subprocess.run(args, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Git command failed: {' '.join(args)}", file=sys.stderr)
        print(result.stderr.strip(), file=sys.stderr)
        sys.exit(result.returncode)
    return result

def main() -> None:
    directory = Path(".")
    html_files = sorted(directory.glob("*.html"))
    modified_files = []

    for file_path in html_files:
        if patch_file(file_path):
            print(f"Patched: {file_path.name}")
            modified_files.append(file_path.name)
        else:
            print(f"Unchanged: {file_path.name}")

    if modified_files:
        print(f"\n{len(modified_files)} file(s) updated. Running Git workflow...")
        run_git(["git", "rev-parse", "--is-inside-work-tree"])

        for name in modified_files:
            run_git(["git", "add", name])

        diff_check = subprocess.run(["git", "diff", "--cached", "--quiet"])
        if diff_check.returncode == 0:
            print("No staged changes. Working tree clean.")
            return

        commit_subject = "Wrap wide induction math step to eliminate mobile overflow"
        commit_body = (
            "Split long inductive algebra chain across two lines and apply\n"
            "overflow-x scrolling to .katex-display to eliminate the right gutter."
        )
        full_message = f"{commit_subject}\n\n{commit_body}"

        run_git(["git", "commit", "-m", full_message])
        print("Committed successfully.")

        print("Pushing to remote...")
        run_git(["git", "push"])
        print("Push complete.")
    else:
        print("\nAll files are already up to date.")

if __name__ == "__main__":
    main()
