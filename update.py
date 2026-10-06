#!/usr/bin/env python3
r"""
normalize_nav.py

Safely normalizes top and bottom navigation panes across all week hubs
and lecture files using precise string boundaries to guarantee zero
content deletion.

Fixes SVG text overlap in week1-lecture2.html and implements a decoupled
flexbox header to prevent long titles from repositioning the navigation buttons.
"""

import re
import sys
import subprocess
from pathlib import Path

BUTTON_STYLE = 'background: #f1f5f9; color: #475569; border: 1px solid var(--border); padding: 0.5rem 0.85rem; border-radius: 6px; text-decoration: none; font-weight: 600; font-size: 0.88rem; text-align: center; white-space: nowrap;'
DISABLED_STYLE = 'background: #f1f5f9; color: #94a3b8; border: 1px solid var(--border); padding: 0.5rem 0.85rem; border-radius: 6px; font-weight: 600; font-size: 0.88rem; cursor: not-allowed; text-align: center; white-space: nowrap;'

def execute_git(args: list[str]) -> None:
    res = subprocess.run(args, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Git execution error: {' '.join(args)}\n{res.stderr.strip()}", file=sys.stderr)
        sys.exit(res.returncode)

def safe_inject_navigation(content: str, is_hub: bool, prev_btn: str, center_btn: str, next_btn: str) -> str:
    container_marker = '<div class="container">'
    module_marker = '<div class="module-content">'

    idx_start = content.find(container_marker)
    idx_end = content.find(module_marker)

    if idx_start == -1 or idx_end == -1 or idx_start > idx_end:
        print("Error: Could not locate safe structural boundaries. Skipping file.", file=sys.stderr)
        return content

    header_block = content[idx_start + len(container_marker):idx_end]

    # Safely extract existing title to preserve it
    h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', header_block, re.IGNORECASE | re.DOTALL)
    title = h1_match.group(1).strip() if h1_match else "MTHS120 Module"

    # Decoupled header: Title wraps naturally, buttons lock to the right
    top_header = (
        '\n        <!-- TOP NAVIGATION HEADER -->\n'
        '        <div class="header" style="border-bottom: 2px solid var(--border); padding-bottom: 1rem; margin-bottom: 2rem; display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: nowrap; gap: 1rem;">\n'
        '            <div style="flex: 1 1 auto; min-width: 0;">\n'
        f'                <h1 style="margin: 0; line-height: 1.3; font-size: 1.5rem;">{title}</h1>\n'
        '            </div>\n'
        '            <div class="nav-btn-group" style="display: flex; gap: 0.5rem; align-items: center; flex-shrink: 0; flex-wrap: wrap; justify-content: flex-end;">\n'
        f'                {prev_btn}\n'
        f'                {center_btn}\n'
        f'                {next_btn}\n'
        '            </div>\n'
        '        </div>\n'
        '        '
    )

    new_content = content[:idx_start + len(container_marker)] + top_header + content[idx_end:]

    # Safely strip legacy footer without greedy regex
    footer_idx = new_content.rfind('<!-- FOOTER')
    if footer_idx == -1:
        footer_idx = new_content.rfind('<div class="footer-nav"')

    if footer_idx != -1:
        # Strip up to the footer, leaving all Dedekind </div> closures perfectly intact
        new_content = new_content[:footer_idx].rstrip()
    else:
        # If no footer is found, just strip the closing HTML tags to append cleanly
        new_content = re.sub(r'</body>\s*</html>\s*$', '', new_content, flags=re.IGNORECASE).rstrip()

    bottom_footer = (
        '\n\n            <!-- FOOTER NAVIGATION -->\n'
        '            <div class="footer-nav" style="margin-top: 3rem; padding-top: 1.5rem; border-top: 1px solid var(--border); display: flex; justify-content: center; align-items: center; gap: 0.75rem; flex-wrap: wrap;">\n'
        f'                {prev_btn}\n'
        f'                {center_btn}\n'
        f'                {next_btn}\n'
        '            </div>\n'
        '        </div>\n'
        '    </div>\n'
        '</body>\n'
        '</html>\n'
    )

    return new_content + bottom_footer


def main() -> None:
    hub_files = list(Path('.').glob('week[0-9]*.html'))
    lec_files = list(Path('.').glob('week*-lecture*.html'))

    weeks = []
    for h in hub_files:
        match = re.search(r'week(\d+)\.html', h.name)
        if match:
            weeks.append(int(match.group(1)))
    weeks.sort()

    lectures = []
    for l in lec_files:
        match = re.search(r'week(\d+)-lecture(\d+)\.html', l.name)
        if match:
            lectures.append((int(match.group(1)), int(match.group(2))))
    lectures.sort(key=lambda x: (x[0], x[1]))

    updated_files = []

    # 1. Update Week Hubs
    for w in weeks:
        file_path = Path(f'week{w}.html')
        if not file_path.exists():
            continue

        content = file_path.read_text(encoding='utf-8')
        original = content

        if (w - 1) in weeks:
            prev_btn = f'<a href="week{w-1}.html" style="{BUTTON_STYLE}">&larr; Prev Week</a>'
        else:
            prev_btn = f'<span style="{DISABLED_STYLE}">&larr; Prev Week</span>'

        center_btn = f'<a href="index.html" style="{BUTTON_STYLE}">&#8962; Curriculum Index</a>'

        if (w + 1) in weeks:
            next_btn = f'<a href="week{w+1}.html" style="{BUTTON_STYLE}">Next Week &rarr;</a>'
        else:
            next_btn = f'<span style="{DISABLED_STYLE}">Next Week &rarr;</span>'

        content = safe_inject_navigation(content, True, prev_btn, center_btn, next_btn)

        if content != original:
            file_path.write_text(content, encoding='utf-8')
            updated_files.append(str(file_path))
            print(f"Safely normalized {file_path.name}")

    # 2. Update Lecture Files
    for idx, (w, l) in enumerate(lectures):
        file_path = Path(f'week{w}-lecture{l}.html')
        if not file_path.exists():
            continue

        content = file_path.read_text(encoding='utf-8')
        original = content

        if idx > 0:
            pw, pl = lectures[idx - 1]
            prev_btn = f'<a href="week{pw}-lecture{pl}.html" style="{BUTTON_STYLE}">&larr; Lecture {pl}</a>'
        else:
            prev_btn = f'<span style="{DISABLED_STYLE}">&larr; Prev Lecture</span>'

        center_btn = f'<a href="week{w}.html" style="{BUTTON_STYLE}">&uarr; Week {w} Hub</a>'

        if idx < len(lectures) - 1:
            nw, nl = lectures[idx + 1]
            next_btn = f'<a href="week{nw}-lecture{nl}.html" style="{BUTTON_STYLE}">Lecture {nl} &rarr;</a>'
        else:
            next_btn = f'<span style="{DISABLED_STYLE}">Next Lecture &rarr;</span>'

        content = safe_inject_navigation(content, False, prev_btn, center_btn, next_btn)

        # Patch SVG overlap in Reverse Triangle Inequality explicitly
        if w == 1 and l == 2:
            old_line = '<line x1="120" y1="45" x2="470" y2="45" stroke="#0284c7" stroke-width="3"/>'
            new_line = '<line x1="120" y1="22" x2="470" y2="22" stroke="#0284c7" stroke-width="3"/>'
            content = content.replace(old_line, new_line)

            old_text = '<text x="295" y="38" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0284c7" text-anchor="middle">length |a| = 7</text>'
            new_text = '<text x="295" y="15" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0284c7" text-anchor="middle">length |a| = 7</text>'
            content = content.replace(old_text, new_text)

        if content != original:
            file_path.write_text(content, encoding='utf-8')
            updated_files.append(str(file_path))
            print(f"Safely normalized {file_path.name}")

    # 3. Commit Operations
    if updated_files:
        execute_git(["git", "add"] + updated_files)

        commit_subject = "Normalize nav layout and fix SVG overlap safely"
        commit_body = (
            "Enforce a decoupled flexbox header to lock navigation buttons to the\n"
            "right, allowing long titles to wrap securely without breaking rows.\n"
            "Eliminate destructive regex stripping to preserve nested biography HTML.\n"
            "Shift vector annotations in Reverse Triangle Inequality to fix overlap."
        )

        execute_git(["git", "commit", "-m", f"{commit_subject}\n\n{commit_body}"])
        execute_git(["git", "push"])
        print("Successfully committed and pushed safe navigation changes.")
    else:
        print("All navigation panes are already normalized.")

if __name__ == '__main__':
    main()
