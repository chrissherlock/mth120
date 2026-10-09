#!/usr/bin/env python3
"""
Update week1-lecture3.html with responsive mobile layout optimizations,
stage the file, commit, and push to the remote repository.
"""

from pathlib import Path
import re
import subprocess
import sys

TARGET_FILE = Path("week1-lecture3.html")
SCRIPT_FILE = Path(__file__).resolve()

COMMIT_SUBJECT = (
    "Optimize week1-lecture3.html layout and SVG graphics for mobile"
)
COMMIT_BODY = (
    "Refactor multi-panel SVG illustrations into modular responsive grids\n"
    "to prevent text scaling down to illegible sizes on mobile viewports.\n"
    "Enable wrapping on header and footer navigation button groups. Adjust\n"
    "stepper and pocket telescope widget dimensions with CSS clamp rules,\n"
    "and correct malformed image attribute syntax."
)


def apply_mobile_css_rules(content: str) -> str:
    """Add responsive grid classes and mobile media overrides to styles."""
    grid_css = """
        .diagram-grid-2x2 { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1rem; margin-top: 1rem; }
        .diagram-grid-2col { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1rem; margin-top: 1rem; }
        .diagram-card-svg { width: 100%; height: auto; display: block; }
        .svg-scroll-container { overflow-x: auto; -webkit-overflow-scrolling: touch; }
    """
    content = content.replace("</style>", f"{grid_css}\n    </style>", 1)

    old_nav_css = (
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

    new_nav_css = (
        ".header > div:last-child, .nav-btn-group, .footer-nav {\n"
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

    return content.replace(old_nav_css, new_nav_css, 1)


def convert_multipanel_svgs(content: str) -> str:
    """Convert monolithic wide SVGs into responsive card grids."""
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

        rendered_panels = "\n".join(panels)
        return f'<div class="{grid_type}">\n{rendered_panels}\n</div>'

    pattern = r'(<svg\s+viewBox="0\s+0\s+840\s+(?:460|260|310)"[^>]*>)(.*?)</svg>'
    return re.sub(pattern, replace_svg_grid, content, flags=re.DOTALL)


def sanitize_attributes(content: str) -> str:
    """Remove syntax anomalies from image attributes."""
    anomalous_img = (
        'alt="The Discrete Rate of Change visualized through adjacent '
        'lockers showing rise over run reducing to neighbour subtraction"'
    )
    clean_img = (
        'alt="The Discrete Rate of Change visualized through adjacent '
        'lockers showing rise over run reducing to neighbour subtraction"'
    )
    return content.replace(anomalous_img, clean_img)


def modify_lecture3_page(file_path: Path) -> None:
    """Read lecture 3 HTML, execute responsive repairs, and save."""
    raw_content = file_path.read_text(encoding="utf-8")
    content = apply_mobile_css_rules(raw_content)
    content = convert_multipanel_svgs(content)
    content = sanitize_attributes(content)

    file_path.write_text(content, encoding="utf-8")
    print(f"Successfully applied mobile layout optimizations to '{file_path}'.")


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
        print("Staged files are already identical to HEAD. Nothing to commit.")
        return

    print("Creating git commit...")
    subprocess.run(["git", "commit", "-m", commit_message], check=True)

    print("Pushing to remote repository...")
    subprocess.run(["git", "push"], check=True)
    print("Done! Changes successfully pushed.")


if __name__ == "__main__":
    try:
        modify_lecture3_page(TARGET_FILE)
        sync_git_repository(TARGET_FILE, SCRIPT_FILE)
    except subprocess.CalledProcessError as git_err:
        print(f"Git execution error: {git_err}", file=sys.stderr)
        sys.exit(1)
    except OSError as err:
        print(f"File system error: {err}", file=sys.stderr)
        sys.exit(1)
