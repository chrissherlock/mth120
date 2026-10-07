#!/usr/bin/env python3
r"""
add_progression_image.py

Embeds the 'images/arithmetic-vs-geometric.png' illustration into Section 3.1
of week1-lecture3.html directly beneath the paced walk vs zoom lens metaphor.
"""

import sys
import subprocess
from pathlib import Path

FIGURE_HTML = """            <!-- ILLUSTRATION: ARITHMETIC VS GEOMETRIC -->
            <div style="margin: 1.75rem 0 2rem 0; text-align: center;">
                <div style="border-radius: 8px; overflow: hidden; border: 1px solid var(--border); box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05), 0 2px 4px -1px rgba(0,0,0,0.03); background: #ffffff;">
                    <img src="images/arithmetic-vs-geometric.png" alt="Comparison of Arithmetic Paced Walk versus Geometric Zoom Magnification" style="width: 100%; height: auto; display: block;">
                </div>
                <p style="font-size: 0.88rem; color: #64748b; margin-top: 0.6rem; line-height: 1.5;">
                    <em>Figure 3.2:</em> The two fundamental engines of discrete dynamics. <strong>1. The Paced Walk (Arithmetic):</strong> Advancing by fixed measuring-tape strides (+1 each step). <strong>2. The Magnifying Glass (Geometric):</strong> Compounding field-of-view magnification (&times;2 each twist).
                </p>
            </div>"""

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

    if "images/arithmetic-vs-geometric.png" in content:
        print(f"Figure is already present in {target.name}.")
        return

    # Locate the anchor paragraph right before arithmetic definition
    search_token = "steady linear pacing versus explosive compounding magnification."
    token_pos = content.find(search_token)

    if token_pos == -1:
        # Fallback to alternate intro closing line
        search_token = "steady linear pacing versus explosive compounding zoom."
        token_pos = content.find(search_token)

    if token_pos == -1:
        print("Error: Could not locate Section 3.1 introductory paragraph.", file=sys.stderr)
        sys.exit(1)

    close_p_pos = content.find("</p>", token_pos)
    if close_p_pos == -1:
        print("Error: Could not find closing </p> tag for Section 3.1 intro.", file=sys.stderr)
        sys.exit(1)

    insert_idx = close_p_pos + len("</p>")
    updated_content = content[:insert_idx] + "\n\n" + FIGURE_HTML + content[insert_idx:]

    target.write_text(updated_content, encoding="utf-8")
    print(f"Successfully added arithmetic-vs-geometric.png to {target.name}")

    py_files = [str(p) for p in Path(".").glob("*.py")]
    stage_targets = list(set([str(target)] + py_files))

    execute_git(["git", "add"] + stage_targets)
    diff_status = subprocess.run(["git", "diff", "--cached", "--quiet"])
    if diff_status.returncode != 0:
        commit_subject = "Add Figure 3.2 arithmetic vs geometric progression visual"
        commit_body = (
            "Embed images/arithmetic-vs-geometric.png into Section 3.1 of\n"
            "week1-lecture3.html illustrating the contrast between measuring-tape\n"
            "addition and camera-lens magnification."
        )
        execute_git(["git", "commit", "-m", f"{commit_subject}\n\n{commit_body}"])
        execute_git(["git", "push"])
        print("Successfully committed and pushed figure update.")
    else:
        print("No staged changes detected to commit.")

if __name__ == "__main__":
    main()
