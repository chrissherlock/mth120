#!/usr/bin/env python3
"""
fix_mobile_nav_buttons_and_push.py

Ensures top and bottom navigation buttons stay side-by-side on mobile screens
by applying equal flex-grow, preventing wrapping, and adjusting font/padding.
Stages, commits, and pushes the changes.
"""

from pathlib import Path
import re
import subprocess
import sys

MOBILE_NAV_CSS = """
            /* Keep header and footer navigation buttons side-by-side on mobile */
            .header > div:last-child,
            .nav-btn-group {
                display: flex !important;
                flex-direction: row !important;
                flex-wrap: nowrap !important;
                width: 100% !important;
                gap: 0.5rem !important;
            }

            .header > div:last-child a,
            .nav-btn-group a {
                flex: 1 1 0 !important;
                min-width: 0 !important;
                text-align: center !important;
                padding: 0.55rem 0.4rem !important;
                font-size: 0.82rem !important;
                white-space: nowrap !important;
                overflow: hidden !important;
                text-overflow: ellipsis !important;
            }
"""

def patch_file(file_path: Path) -> bool:
    content = file_path.read_text(encoding="utf-8")
    original = content

    # Add class="nav-btn-group" to header and footer button wrappers if missing
    content = re.sub(
        r'<div style="display: flex; gap: 0\.5rem; align-items: center; flex-wrap: wrap;">',
        '<div class="nav-btn-group" style="display: flex; gap: 0.5rem; align-items: center;">',
        content
    )

    # Inject the side-by-side mobile rules if not already present
    if "/* Keep header and footer navigation buttons side-by-side on mobile */" not in content:
        mq_pos = content.find("@media (max-width: 768px)")
        if mq_pos != -1:
            # Find the closing brace of the @media block
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
                content = content[:insert_pos] + f"{MOBILE_NAV_CSS}\n        " + content[insert_pos:]

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

def commit_and_push(changed_files: list[str]) -> None:
    run_git(["git", "rev-parse", "--is-inside-work-tree"])

    for filename in changed_files:
        run_git(["git", "add", filename])

    diff_check = subprocess.run(["git", "diff", "--cached", "--quiet"])
    if diff_check.returncode == 0:
        print("No staged changes detected. Nothing to commit or push.")
        return

    commit_subject = "Ensure navigation buttons remain side by side on mobile"
    commit_body = (
        "Prevent navigation button wrapping on narrow screens by applying\n"
        "flex-wrap: nowrap, equal flex sizing (flex: 1 1 0), and compact\n"
        "padding with text-overflow protection."
    )
    full_message = f"{commit_subject}\n\n{commit_body}"

    run_git(["git", "commit", "-m", full_message])
    print("Changes committed successfully.")

    print("Pushing commits to remote...")
    run_git(["git", "push"])
    print("Push complete.")

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
        print(f"\n{len(modified_files)} file(s) updated. Proceeding with Git workflow...")
        commit_and_push(modified_files)
    else:
        print("\nAll files already have side-by-side button styling.")

if __name__ == "__main__":
    main()
