#!/usr/bin/env python3
r"""
update.py

Ensures all Notation Reference infoboxes feature properly centered and
accent-colored notation symbols, standardizing the notation grid layout.
"""

from pathlib import Path
import re
import subprocess
import sys

TARGET_HTML = Path("week1-lecture3.html")
SCRIPT_FILE = Path(__file__).resolve()

def execute_git(args: list[str]) -> subprocess.CompletedProcess:
    res = subprocess.run(args, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Git execution error: {' '.join(args)}", file=sys.stderr)
        print(res.stderr.strip(), file=sys.stderr)
        sys.exit(res.returncode)
    return res

def main() -> None:
    if not TARGET_HTML.exists():
        print(f"Error: {TARGET_HTML} not found in workspace.", file=sys.stderr)
        sys.exit(1)

    content = TARGET_HTML.read_text(encoding="utf-8")
    original = content

    # Ensure .notation-sym is robustly centered and styled in CSS
    old_css_rule = ".notation-sym { font-weight: 600; color: var(--accent); white-space: nowrap; display: flex; justify-content: center; align-items: center; text-align: center; }"

    # If the CSS block needs ensuring, let's inject or update it
    if ".notation-sym" in content:
        content = re.sub(
            r'\.notation-sym\s*\{[^}]*\}',
            '.notation-sym { font-weight: 600; color: var(--accent); white-space: nowrap; display: flex; justify-content: center; align-items: center; text-align: center; background: #fef3c7; padding: 0.3rem 0.6rem; border-radius: 4px; border: 1px solid #fde68a; }',
            content
        )

    if content != original:
        TARGET_HTML.write_text(content, encoding="utf-8")
        print("Updated notation symbol styling in CSS.")

    execute_git(["git", "add", str(TARGET_HTML), str(SCRIPT_FILE)])

    diff_check = subprocess.run(["git", "diff", "--cached", "--quiet"])
    if diff_check.returncode == 0:
        print("No staged changes detected. Working tree clean.")
        return

    execute_git(["git", "commit", "-m", "Center and color notation reference symbols in CSS\n\nUpdate .notation-sym class definition in style block to ensure notation symbols are centered, highlighted, and visually distinct."])
    execute_git(["git", "push"])
    print("Committed and pushed notation styling fix.")

if __name__ == "__main__":
    main()
