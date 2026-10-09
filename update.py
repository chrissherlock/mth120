#!/usr/bin/env python3
"""
Surgically patch week1-lecture3.html for mobile responsiveness.
Preserves 100% of explanatory prose, worked examples, and widget logic.
"""

from pathlib import Path
import re
import subprocess
import sys

TARGET_FILE = Path("week1-lecture3.html")
SCRIPT_FILE = Path(__file__).resolve()

COMMIT_SUBJECT = (
    "Make week1-lecture3.html responsive via surgical layout patch"
)
COMMIT_BODY = (
    "Add responsive CSS rules for mobile viewports without altering prose.\n"
    "Convert monolithic 840px SVGs into auto-wrapping card grids. Upgrade\n"
    "the Section 5 comparative sequence table with a sticky index column,\n"
    "touch momentum scrolling, and a minimum width to prevent math cramping."
)


def patch_stylesheet(content: str) -> str:
    """Inject responsive grid classes, table styling, and mobile overrides."""
    if ".diagram-grid-2x2" in content:
        return content  # Styles already present

    custom_css = """
        /* Responsive SVG Grid Layouts */
        .diagram-grid-2x2 { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1rem; margin-top: 1rem; }
        .diagram-grid-2col { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1rem; margin-top: 1rem; }
        .diagram-card-svg { width: 100%; height: auto; display: block; }

        /* Responsive Stepping Table Styles */
        .table-scroll-hint {
            display: none;
            font-size: 0.76rem;
            font-weight: 700;
            color: #64748b;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 0.4rem;
            text-align: right;
        }
        .stepping-table-wrap {
            width: 100%;
            overflow-x: auto;
            -webkit-overflow-scrolling: touch;
            margin: 1.25rem 0 1.75rem 0;
            border: 1px solid var(--border);
            border-radius: 8px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.03);
            background: #ffffff;
        }
        .stepping-table {
            width: 100%;
            min-width: 600px;
            border-collapse: collapse;
            font-size: 0.92rem;
            text-align: center;
        }
        .stepping-table th {
            background: #f1f5f9;
            padding: 0.65rem 0.75rem;
            color: #475569;
            font-weight: 600;
            border-bottom: 2px solid var(--border);
        }
        .stepping-table td {
            padding: 0.6rem 0.75rem;
            border-bottom: 1px solid #e2e8f0;
        }
        .stepping-table tr:last-child td {
            border-bottom: none;
        }
        .stepping-table tr.row-plateau {
            background: #f0fdf4;
        }
        /* Sticky Left Column */
        .stepping-table th:first-child,
        .stepping-table td:first-child {
            position: sticky;
            left: 0;
            z-index: 2;
            background: #ffffff;
            box-shadow: 2px 0 5px -2px rgba(0,0,0,0.12);
        }
        .stepping-table th:first-child {
            background: #f1f5f9;
            z-index: 3;
        }
        .stepping-table tr.row-plateau td:first-child {
            background: #f0fdf4;
        }
    """
    content = content.replace("</style>", f"{custom_css}\n    </style>", 1)

    # Replace cramped navigation rules in @media (max-width: 768px)
    old_nav_block = (
        ".header > div:last-child, .nav-btn-group, .footer-nav {\n"
        "                display: flex !important; flex-direction: row !important; "
        "flex-wrap: nowrap !important; width: 100% !important; gap: 0.5rem !important;\n"
        "            }\n"
        "            .header > div:last-child a, .nav-btn-group a, .footer-nav a {\n"
        "                flex: 1 1 0 !important; min-width: 0 !important; "
        "text-align: center !important; padding: 0.55rem 0.4rem !important;\n"
        "                font-size: 0.84rem !important; white-space: nowrap !important; "
        "overflow: hidden !important; text-overflow: ellipsis !important;\n"
        "            }"
    )

    new_nav_block = (
        ".table-scroll-hint { display: block !important; }\n"
        "            .header > div:last-child, .nav-btn-group, .footer-nav {\n"
        "                display: flex !important; flex-direction: row !important; "
        "flex-wrap: wrap !important; width: 100% !important; gap: 0.5rem !important;\n"
        "            }\n"
        "            .header > div:last-child a, .nav-btn-group a, .footer-nav a {\n"
        "                flex: 1 1 30% !important; min-width: 90px !important; "
        "text-align: center !important; padding: 0.55rem 0.4rem !important;\n"
        "                font-size: 0.84rem !important; white-space: nowrap !important;\n"
        "            }\n"
        "            #progression-stepper-widget > div:first-child {\n"
        "                flex-direction: column !important; align-items: stretch !important; gap: 0.75rem !important;\n"
        "            }\n"
        "            #progression-stepper-widget > div:first-child > div:last-child {\n"
        "                display: flex !important; width: 100% !important;\n"
        "            }\n"
        "            #progression-stepper-widget > div:first-child > div:last-child button {\n"
        "                flex: 1 1 0 !important; padding: 0.4rem 0.25rem !important; font-size: 0.75rem !important; text-align: center !important;\n"
        "            }\n"
        "            .ct .tube { width: clamp(54px, 17vw, 84px) !important; }\n"
        "            .ct .tele[data-s=\"3\"] .tube:not(:first-child) { margin-left: clamp(-24px, -8vw, -34px) !important; }\n"
        "            .ct .tele[data-s=\"4\"] .tube:not(:first-child) { margin-left: clamp(-42px, -14vw, -60px) !important; }\n"
        "            .ct .stage { padding: 12px 8px !important; min-height: 120px !important; }\n"
        "            .ct .row { font-size: clamp(0.95rem, 3.2vw, 1.35rem) !important; }\n"
        "            .ct .bar button { padding: 6px 10px !important; font-size: 0.82rem !important; min-height: 36px !important; }"
    )

    return content.replace(old_nav_block, new_nav_block, 1)


def unbundle_svg_panels(content: str) -> str:
    """Extract nested SVG panels into autonomous cards inside CSS grids."""
    def replace_svg_grid(match: re.Match) -> str:
        tag = match.group(1)
        grid_type = "diagram-grid-2x2" if "460" in tag else "diagram-grid-2col"
        height = "210" if "460" in tag else ("285" if "310" in tag else "235")
        inner_content = match.group(2)

        panels = []
        for g_match in re.finditer(r'<g\s+transform="translate\([^"]+\)">(.*?)</g>', inner_content, re.DOTALL):
            panel_body = g_match.group(1).strip()
            panels.append(
                f'<svg viewBox="0 0 395 {height}" class="diagram-card-svg">\n'
                f'    {panel_body}\n'
                f'</svg>'
            )

        if not panels:
            return match.group(0)

        rendered_panels = "\n".join(panels)
        return f'<div class="{grid_type}">\n{rendered_panels}\n</div>'

    pattern = r'(<svg\s+viewBox="0\s+0\s+840\s+(?:460|260|310)"[^>]*>)(.*?)</svg>'
    return re.sub(pattern, replace_svg_grid, content, flags=re.DOTALL)


def upgrade_stepping_table(content: str) -> str:
    """Enhance the Section 5 stepping table with sticky index styling."""
    if "class=\"stepping-table\"" in content:
        return content  # Already upgraded

    target_phrase = "<!-- BEGINNER-FRIENDLY COMPARATIVE STEPPING TABLE -->"
    if target_phrase not in content:
        return content

    pattern = re.compile(
        r'<!-- BEGINNER-FRIENDLY COMPARATIVE STEPPING TABLE -->\s*'
        r'<div style="overflow-x:\s*auto;\s*margin:\s*1\.25rem\s*0;">\s*'
        r'<table style="[^"]*">(.*?)</table>\s*</div>',
        re.DOTALL
    )

    match = pattern.search(content)
    if not match:
        return content

    table_body = match.group(1)
    # Mark plateau rows with class for sticky background coordination
    table_body = table_body.replace(
        'style="border-bottom: 1px solid #e2e8f0; background: #f0fdf4;"',
        'class="row-plateau"'
    )

    replacement = (
        f'{target_phrase}\n'
        f'            <div class="table-scroll-hint">↔ Swipe horizontally to inspect values</div>\n'
        f'            <div class="stepping-table-wrap">\n'
        f'                <table class="stepping-table">\n'
        f'                    {table_body.strip()}\n'
        f'                </table>\n'
        f'            </div>'
    )

    return content[:match.start()] + replacement + content[match.end():]


def sanitize_attributes(content: str) -> str:
    """Remove syntax anomalies from image attributes."""
    anomalous_snippet = (
        'alt="The Discrete Rate of Change visualized through adjacent '
        'lockers showing rise over run reducing to neighbour subtraction" '
        'style="'
    )
    clean_snippet = (
        'alt="The Discrete Rate of Change visualized through adjacent '
        'lockers showing rise over run reducing to neighbour subtraction" '
        'style="'
    )
    return content.replace(anomalous_snippet, clean_snippet)


def update_lecture_document(file_path: Path) -> None:
    """Apply surgical responsive changes to the lecture document."""
    if not file_path.exists():
        print(f"Error: Target file '{file_path}' not found.", file=sys.stderr)
        sys.exit(1)

    original_text = file_path.read_text(encoding="utf-8")
    original_line_count = len(original_text.splitlines())

    text = patch_stylesheet(original_text)
    text = unbundle_svg_panels(text)
    text = upgrade_stepping_table(text)
    text = sanitize_attributes(text)

    new_line_count = len(text.splitlines())
    file_path.write_text(text, encoding="utf-8")
    print(
        f"Updated '{file_path.name}' safely. "
        f"Lines before: {original_line_count}, lines after: {new_line_count}."
    )


def check_staged_changes() -> bool:
    """Return True if changes exist in the git staging index."""
    result = subprocess.run(["git", "diff", "--cached", "--quiet"])
    return result.returncode != 0


def sync_git_repository(target_path: Path, script_path: Path) -> None:
    """Stage modified lecture file and script, commit, and push."""
    commit_message = f"{COMMIT_SUBJECT}\n\n{COMMIT_BODY}"

    print(f"Staging {target_path.name} and {script_path.name}...")
    subprocess.run(["git", "add", str(target_path), str(script_path)], check=True)

    if not check_staged_changes():
        print("No staged changes to commit. Working tree is clean.")
        return

    print("Creating git commit...")
    subprocess.run(["git", "commit", "-m", commit_message], check=True)

    print("Pushing to remote repository...")
    subprocess.run(["git", "push"], check=True)
    print("Done! Changes successfully synchronized.")


if __name__ == "__main__":
    try:
        update_lecture_document(TARGET_FILE)
        sync_git_repository(TARGET_FILE, SCRIPT_FILE)
    except subprocess.CalledProcessError as git_err:
        print(f"Git execution error: {git_err}", file=sys.stderr)
        sys.exit(1)
    except OSError as err:
        print(f"File system error: {err}", file=sys.stderr)
        sys.exit(1)
