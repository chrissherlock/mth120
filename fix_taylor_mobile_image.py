#!/usr/bin/env python3
r"""
fix_taylor_mobile_image.py

Re-architects the biography / profile card for Brook Taylor in
week1-lecture3.html to ensure the portrait spans the full container width
on mobile viewports, matching the styling in Week 1 Lecture 2 and Week 2.
"""

import re
import sys
import subprocess
from pathlib import Path

ROBUST_MOBILE_CSS = """
        /* Full-width responsive biography cards on mobile */
        @media (max-width: 768px) {
            .biography-box, [class*="biography"], [class*="profile"] {
                padding: 1.25rem 1rem !important;
            }
            .biography-box > div, [class*="biography"] > div {
                display: flex !important;
                flex-direction: column !important;
                align-items: stretch !important;
                gap: 1.25rem !important;
            }
            .biography-box div:has(> img),
            .biography-box > div > div:first-child,
            [class*="biography"] div:has(> img) {
                flex: 0 0 100% !important;
                width: 100% !important;
                max-width: 100% !important;
                margin: 0 0 0.5rem 0 !important;
            }
            .biography-box img,
            [class*="biography"] img {
                width: 100% !important;
                max-width: 100% !important;
                max-height: 380px !important;
                object-fit: cover !important;
                border-radius: 6px !important;
                display: block !important;
            }
            .biography-box > div > div:last-child,
            [class*="biography"] > div > div:last-child {
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

    # 1. Clean out any previous partial mobile biography overrides
    content = re.sub(
        r'/\*\s*Full-width responsive biography cards on mobile\s*\*/.*?(\n\s*\}\s*\n|\n\s*</style>)',
        '\n</style>',
        content,
        flags=re.DOTALL
    )

    # 2. Inject the comprehensive mobile override right before </style>
    if "</style>" in content:
        content = content.replace("</style>", f"{ROBUST_MOBILE_CSS}\n    </style>", 1)
    else:
        print(f"Error: No </style> found in {target.name}", file=sys.stderr)
        sys.exit(1)

    # 3. Ensure the biography box HTML itself has the canonical class name
    # Search for Brook Taylor's image wrapper
    content = re.sub(
        r'(<div[^>]*class="[^"]*biography[^"]*"[^>]*>)',
        r'<div class="biography-box" style="margin-top: 2rem;">',
        content,
        flags=re.IGNORECASE
    )

    target.write_text(content, encoding="utf-8")
    print(f"Successfully repaired mobile portrait styling in {target.name}")

    py_files = [str(p) for p in Path(".").glob("*.py")]
    stage_targets = list(set([str(target)] + py_files))

    execute_git(["git", "add"] + stage_targets)
    diff_status = subprocess.run(["git", "diff", "--cached", "--quiet"])
    if diff_status.returncode != 0:
        commit_subject = "Fix Brook Taylor portrait sizing on mobile in Lecture 3"
        commit_body = (
            "Refactor biography CSS selectors in week1-lecture3.html to ensure\n"
            "Brook Taylor portrait container expands to full width on mobile\n"
            "viewports instead of remaining pinned to fixed image dimensions."
        )
        execute_git(["git", "commit", "-m", f"{commit_subject}\n\n{commit_body}"])
        execute_git(["git", "push"])
        print("Successfully committed and pushed mobile portrait fix.")
    else:
        print("No changes staged to commit.")

if __name__ == "__main__":
    main()
