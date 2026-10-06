cat << 'EOF' > update.py
#!/usr/bin/env python3
r"""
update.py

Safely normalizes top and bottom navigation panes across all week hubs
and lecture files using a self-healing structural tag balancer.

Implements a stacked header layout (buttons centered on top of the title)
to guarantee mobile responsiveness regardless of title length.
Stages all modified HTML and Python automation scripts to Git.
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
        print("Error: Could not locate safe structural boundaries. Skipping.", file=sys.stderr)
        return content

    header_block = content[idx_start:idx_end]

    h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', header_block, re.IGNORECASE | re.DOTALL)
    title = h1_match.group(1).strip() if h1_match else "MTHS120 Module"

    top_header = (
        '<div class="container">\n'
        '        <!-- TOP NAVIGATION HEADER -->\n'
        '        <div class="header" style="border-bottom: 2px solid var(--border); padding-bottom: 1.5rem; margin-bottom: 2rem; display: flex; flex-direction: column; align-items: center; gap: 1.25rem;">\n'
        '            <div class="nav-btn-group" style="display: flex; gap: 0.5rem; justify-content: center; flex-wrap: wrap; width: 100%;">\n'
        f'                {prev_btn}\n'
        f'                {center_btn}\n'
        f'                {next_btn}\n'
        '            </div>\n'
        '            <div style="text-align: center; width: 100%; min-width: 0;">\n'
        f'                <h1 style="margin: 0; line-height: 1.3; font-size: 1.5rem;">{title}</h1>\n'
        '            </div>\n'
        '        </div>\n\n        '
    )

    new_content = content[:idx_start] + top_header + content[idx_end:]

    new_content = re.sub(r'<!-- FOOTER NAVIGATION -->.*', '', new_content, flags=re.DOTALL | re.IGNORECASE)
    new_content = re.sub(r'<!-- BOTTOM NAVIGATION FOOTER -->.*', '', new_content, flags=re.DOTALL | re.IGNORECASE)
    new_content = re.sub(r'<div class="footer-nav".*', '', new_content, flags=re.DOTALL | re.IGNORECASE)
    new_content = re.sub(r'</body>\s*</html>\s*$', '', new_content, flags=re.DOTALL | re.IGNORECASE).rstrip()

    body_idx = new_content.find(container_marker)
    if body_idx == -1:
        body_idx = 0

    body_content = new_content[body_idx:]
    body_content_no_svg = re.sub(r'<svg.*?</svg>', '', body_content, flags=re.DOTALL | re.IGNORECASE)

    open_divs = len(re.findall(r'<div\b[^>]*>', body_content_no_svg, flags=re.IGNORECASE))
    close_divs = len(re.findall(r'</div>', body_content_no_svg, flags=re.IGNORECASE))

    missing_divs = open_divs - close_divs
    divs_to_close_before_footer = missing_divs - 2

    if divs_to_close_before_footer > 0:
        new_content += '\n' + '                    </div>\n' * divs_to_close_before_footer

    bottom_footer = (
        '\n            <!-- FOOTER NAVIGATION -->\n'
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
    py_files = [str(p) for p in Path('.').glob('*.py')]

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

        if w == 1 and l == 2:
            old_line = '<line x1="120" y1="45" x2="470" y2="45" stroke="#0284c7" stroke-width="3"/>'
            new_line = '<line x1="120" y1="22" x2="470" y2="22" stroke="#0284c7" stroke-width="3"/>'
            content = content.replace(old_line, new_line)

            old_text = '<text x="295" y="38" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0284c7" text-anchor="middle">length |a| = 7</text>'
            new_text = '<text x="295" y="15" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0284c7" text-anchor="middle">length |a| = 7</text>'
            content = content.replace(old_text, new_text)

        if content != original:
            file_path.write_text(content, encoding='utf-8')
            if str(file_path) not in updated_files:
                updated_files.append(str(file_path))
            print(f"Safely normalized & healed {file_path.name}")

    # Stage both updated HTML pages and all Python scripts
    all_staging_targets = list(set(updated_files + py_files))

    if all_staging_targets:
        execute_git(["git", "add"] + all_staging_targets)
        diff_status = subprocess.run(["git", "diff", "--cached", "--quiet"])
        if diff_status.returncode != 0:
            commit_subject = "Stack header nav and track migration python scripts"
            commit_body = (
                "Change header flexbox layout from row to column to ensure long titles\n"
                "never break on mobile devices. Stage and commit Python automation\n"
                "scripts alongside updated HTML documents."
            )
            execute_git(["git", "commit", "-m", f"{commit_subject}\n\n{commit_body}"])
            execute_git(["git", "push"])
            print("Successfully committed and pushed HTML and Python files.")
        else:
            print("No staged changes detected to commit.")
    else:
        print("Working tree clean; no files to stage.")

if __name__ == '__main__':
    main()
EOF
chmod +x update.py
./update.py
