#!/usr/bin/env python3
r"""
fix_profiles_lecture3.py

Normalizes Brook Taylor and Carl Friedrich Gauss profile cards in
week1-lecture3.html to use the standard .biography-box class and responsive
styling, ensuring photos expand to full container width on mobile.
"""

import re
import sys
import subprocess
from pathlib import Path

BIOGRAPHY_CSS = """
        .biography-box { background: #f5f3ff; border: 1px solid #ddd6fe; border-left: 5px solid #6366f1; padding: 1.25rem 1.5rem; margin: 2rem 0; border-radius: 0 6px 6px 0; }
        .biography-box h4 { margin-top: 0; color: #3730a3; font-size: 1.05rem; display: flex; align-items: center; gap: 0.5rem; }
        .biography-box p, .biography-box li { color: #0f172a !important; }

        /* Full-width responsive biography cards on mobile */
        @media (max-width: 768px) {
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

    # 1. Clean up duplicated </style> tags and old mobile rules in <head>
    content = re.sub(r'</style>\s*</style>', '</style>', content, flags=re.IGNORECASE)
    content = re.sub(
        r'/\*\s*Full-width responsive biography cards on mobile\s*\*/.*?(?=\n\s*</style>)',
        '',
        content,
        flags=re.DOTALL
    )

    # 2. Inject clean biography CSS before </style>
    if ".biography-box {" not in content:
        content = content.replace("</style>", f"{BIOGRAPHY_CSS}    </style>", 1)
    else:
        # Replace existing .biography-box definitions with canonical block
        content = content.replace("</style>", f"{BIOGRAPHY_CSS}    </style>", 1)

    # 3. Transform Brook Taylor card to standard .biography-box
    taylor_old_pattern = (
        r'<!-- HISTORICAL PROFILE: BROOK TAYLOR -->\s*'
        r'<div class="infobox"[^>]*>'
    )
    content = re.sub(
        taylor_old_pattern,
        '<!-- HISTORICAL PROFILE: BROOK TAYLOR -->\n            <div class="biography-box" style="margin-top: 2rem;">',
        content
    )

    # 4. Transform Carl Friedrich Gauss card to standard .biography-box
    gauss_old_pattern = (
        r'<!-- HISTORICAL PROFILE: CARL FRIEDRICH GAUSS -->\s*'
        r'<div class="infobox"[^>]*>'
    )
    content = re.sub(
        gauss_old_pattern,
        '<!-- HISTORICAL PROFILE: CARL FRIEDRICH GAUSS -->\n            <div class="biography-box" style="margin-top: 2rem;">',
        content
    )

    # 5. Fix image column wrappers (from flex: 0 0 130px to flex: 0 0 135px)
    content = re.sub(
        r'<div style="flex:\s*0\s*0\s*130px;\s*text-align:\s*center;">',
        '<div style="flex: 0 0 135px; max-width: 135px;">',
        content
    )

    # 6. Fix image inline width from fixed 130px to responsive 100%
    content = content.replace(
        'style="width: 130px; height: auto;',
        'style="width: 100%; height: auto;'
    )

    target.write_text(content, encoding="utf-8")
    print(f"Successfully converted Taylor and Gauss cards in {target.name}")

    py_files = [str(p) for p in Path(".").glob("*.py")]
    stage_targets = list(set([str(target)] + py_files))

    execute_git(["git", "add"] + stage_targets)
    diff_status = subprocess.run(["git", "diff", "--cached", "--quiet"])
    if diff_status.returncode != 0:
        commit_subject = "Standardize Taylor and Gauss biography cards in Lecture 3"
        commit_body = (
            "Convert Taylor and Gauss profile cards from .infobox to\n"
            ".biography-box in week1-lecture3.html, remove hardcoded 130px image\n"
            "widths, and restore mobile responsive styles."
        )
        execute_git(["git", "commit", "-m", f"{commit_subject}\n\n{commit_body}"])
        execute_git(["git", "push"])
        print("Successfully committed and pushed biography card updates.")
    else:
        print("No staged changes detected to commit.")

if __name__ == "__main__":
    main()
