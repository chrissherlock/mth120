#!/usr/bin/env python3
"""
fix_mobile_list_indentation.py

Ensures ordered (<ol>) and unordered (<ul>) lists have tightened left indentation
EXCLUSIVELY on mobile viewports (<= 768px), leaving desktop layout untouched.
"""

from pathlib import Path
import re

RULE = """
            /* Tighten list indentation exclusively on mobile */
            ol, ul {
                padding-left: 1.25rem !important;
                margin-left: 0 !important;
            }
"""

def patch_file(file_path: Path) -> bool:
    content = file_path.read_text(encoding="utf-8")
    original = content

    if "padding-left: 1.25rem !important;" in content:
        return False  # Already present

    # Find the closing brace of the @media (max-width: 768px) block
    mq_pos = content.find("@media (max-width: 768px)")
    if mq_pos != -1:
        brace_count = 0
        insert_pos = -1
        for idx in range(mq_pos, len(content)):
            if content[idx] == '{':
                brace_count += 1
            elif content[idx] == '}':
                brace_count -= 1
                if brace_count == 0:
                    insert_pos = idx
                    break

        if insert_pos != -1:
            content = content[:insert_pos] + f"{RULE}\n        " + content[insert_pos:]

    if content != original:
        file_path.write_text(content, encoding="utf-8")
        return True
    return False

def main() -> None:
    directory = Path(".")
    html_files = sorted(directory.glob("*.html"))
    count = 0

    for file_path in html_files:
        if patch_file(file_path):
            print(f"Added mobile list rule to: {file_path.name}")
            count += 1
        else:
            print(f"Skipped / Already patched: {file_path.name}")

    print(f"\nDone. Updated {count} file(s).")

if __name__ == "__main__":
    main()
