#!/usr/bin/env python3
r"""
patch_biography_css.py

Injects the missing responsive CSS for biography boxes into all HTML files.
This forces the rigid 135px image columns (like Taylor and Gauss) to
expand to 100% width and stack vertically on mobile screens.
"""

import sys
import subprocess
from pathlib import Path

MOBILE_CSS = """
        /* Full-width responsive biography cards on mobile */
        @media (max-width: 768px) {
            .biography-box { padding: 1.25rem 1rem !important; }
            .biography-box > div { flex-direction: column !important; align-items: stretch !important; gap: 1.25rem !important; }
            .biography-box > div > div:first-child { flex: 0 0 100% !important; width: 100% !important; max-width: 100% !important; margin: 0 0 0.5rem 0 !important; }
            .biography-box > div > div:first-child img { width: 100% !important; max-height: 380px !important; object-fit: cover !important; border-radius: 6px !important; display: block !important; }
            .biography-box > div > div:last-child { width: 100% !important; min-width: 0 !important; }
        }
"""

def execute_git(args: list[str]) -> None:
    res = subprocess.run(args, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Git execution error: {' '.join(args)}\n{res.stderr.strip()}", file=sys.stderr)
        sys.exit(res.returncode)

def main() -> None:
    html_files = list(Path('.').glob('*.html'))
    updated_files = []

    for file_path in html_files:
        content = file_path.read_text(encoding='utf-8')

        # Skip if the file already has the mobile image override
        if 'max-height: 380px !important' in content:
            continue

        # Inject right before the closing style tag
        if '</style>' in content:
            new_content = content.replace('</style>', f'{MOBILE_CSS}    </style>')
            file_path.write_text(new_content, encoding='utf-8')
            updated_files.append(str(file_path))
            print(f"Patched mobile CSS in {file_path.name}")
        else:
            print(f"Warning: No <style> tag found in {file_path.name}. Skipping.", file=sys.stderr)

    if updated_files:
        execute_git(["git", "add"] + updated_files + [str(Path(__file__).resolve())])

        commit_subject = "Apply mobile-responsive biography CSS across all files"
        commit_body = (
            "Inject a @media query into the stylesheets of all remaining files to\n"
            "override the rigid 135px flex layout on biography boxes. This ensures\n"
            "images for figures like Gauss and Brook Taylor scale to 100% width\n"
            "and stack vertically on mobile devices."
        )

        execute_git(["git", "commit", "-m", f"{commit_subject}\n\n{commit_body}"])
        execute_git(["git", "push"])
        print("Successfully committed and pushed biography CSS patches.")
    else:
        print("All files already have the responsive biography CSS.")

if __name__ == '__main__':
    main()
