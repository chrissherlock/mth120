#!/usr/bin/env python3
r"""
fix_lecture3_mobile_images.py

Injects responsive biography card CSS into week1-lecture3.html so that
portrait images expand to full width on mobile viewports matching the other lectures.
"""

import sys
import subprocess
from pathlib import Path

BIOGRAPHY_MOBILE_CSS = """
            /* Full-width responsive biography cards on mobile */
            .biography-box {
                padding: 1.25rem 1rem !important;
            }
            .biography-box > div {
                flex-direction: column !important;
                align-items: stretch !important;
                gap: 1.25rem !important;
            }
            .biography-box > div > div:first-child {
                flex: 0 0 100% !important;
                width: 100% !important;
                max-width: 100% !important;
                margin: 0 0 0.5rem 0 !important;
            }
            .biography-box > div > div:first-child img {
                width: 100% !important;
                max-height: 380px !important;
                object-fit: cover !important;
                border-radius: 6px !important;
                display: block !important;
            }
            .biography-box > div > div:last-child {
                width: 100% !important;
                min-width: 0 !important;
            }
"""

def execute_git(args: list[str]) -> None:
    res = subprocess.run(args, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Git execution error: {' '.join(args)}\n{res.stderr.strip()}", file=sys.stderr)
        sys.exit(res.returncode)

def main() -> None:
    target = Path("week1-lecture3.html")
    if not target.exists():
        print(f"Error: {target.name} not found.", file=sys.stderr)
        sys.exit(1)

    content = target.read_text(encoding="utf-8")

    if "max-height: 380px !important" in content:
        print(f"{target.name} already has the mobile biography image styling.")
        return

    # Insert inside the @media (max-width: 768px) block right before </style>
    media_query = "@media (max-width: 768px) {"
    if media_query in content:
        insert_pos = content.find(media_query) + len(media_query)
        updated_content = content[:insert_pos] + BIOGRAPHY_MOBILE_CSS + content[insert_pos:]
    elif "</style>" in content:
        wrapper = f"\n        @media (max-width: 768px) {{{BIOGRAPHY_MOBILE_CSS}\n        }}\n"
        updated_content = content.replace("</style>", f"{wrapper}    </style>", 1)
    else:
        print(f"Error: Could not locate <style> section in {target.name}", file=sys.stderr)
        sys.exit(1)

    target.write_text(updated_content, encoding="utf-8")
    print(f"Successfully injected responsive biography image CSS into {target.name}")

    py_files = [str(p) for p in Path(".").glob("*.py")]
    stage_targets = list(set([str(target)] + py_files))

    execute_git(["git", "add"] + stage_targets)
    diff_status = subprocess.run(["git", "diff", "--cached", "--quiet"])
    if diff_status.returncode != 0:
        commit_subject = "Fix biography card mobile image sizing in Week 1 Lecture 3"
        commit_body = (
            "Add responsive CSS rules for .biography-box on mobile viewports in\n"
            "week1-lecture3.html, ensuring portrait photos expand to full container\n"
            "width rather than remaining pinned to 135px."
        )
        execute_git(["git", "commit", "-m", f"{commit_subject}\n\n{commit_body}"])
        execute_git(["git", "push"])
        print("Successfully committed and pushed mobile image fix.")
    else:
        print("No staged changes detected to commit.")

if __name__ == "__main__":
    main()
