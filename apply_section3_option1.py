#!/usr/bin/env python3
r"""
apply_section3_option1.py

Replaces Section 3's introductory prose in week1-lecture3.html with the
pacing vs zoom lens metaphor (Option 1) to build physical intuition for
arithmetic and geometric dynamics.
"""

import sys
import subprocess
from pathlib import Path

OPTION_1_HTML = """            <h3 style="color: #0f172a; font-size: 1.15rem; margin-top: 1.25rem;">1. Unpacking the Two Great Motions: Strides vs. Zoom</h3>
            <p style="font-size: 1.02rem; line-height: 1.75; color: #334155; margin-bottom: 1rem;">
                Think about the two fundamentally different ways you can travel along our infinite locker hallway:
            </p>
            <ul style="font-size: 0.98rem; line-height: 1.75; color: #334155; padding-left: 1.25rem; margin-bottom: 1.25rem;">
                <li style="margin-bottom: 0.6rem;">
                    <strong>The Paced Walk (Arithmetic):</strong> You lock your stride to a wooden ruler. Every single step forward adds the exact same physical distance to your odometer—one foot, two feet, three feet. You advance through pure <strong>addition</strong>.
                </li>
                <li>
                    <strong>The Magnifying Glass (Geometric):</strong> You stay stationary, but you twist a camera's zoom lens. A $2\\times$ twist doubles your field of view; another twist doubles that again, exploding fourfold, eightfold, sixteenfold. You advance through compounding <strong>multiplication</strong>.
                </li>
            </ul>
            <p style="font-size: 1.02rem; line-height: 1.75; color: #334155; margin-bottom: 1.25rem;">
                School algebra often presents formulas like <span class="nobr">$c_n = an + b$</span> and <span class="nobr">$c_n = a q^n$</span> as arbitrary recipes to memorize for exams. But they are really the mathematical transcripts of these two distinct physical rhythms: steady linear pacing versus explosive compounding magnification.
            </p>"""

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

    start_token = '<h3 style="color: #0f172a; font-size: 1.15rem; margin-top: 1.25rem;">1. Unpacking the Two Great Motions: Strides vs. Zoom</h3>'
    end_token = '<h4 style="color: #1e293b; margin-top: 1.5rem;">The Arithmetic Progression: Walking with Constant Strides</h4>'

    start_idx = content.find(start_token)
    end_idx = content.find(end_token)

    if start_idx == -1 or end_idx == -1 or start_idx >= end_idx:
        print("Error: Could not locate Section 3 introductory boundaries in week1-lecture3.html", file=sys.stderr)
        sys.exit(1)

    updated_content = content[:start_idx] + OPTION_1_HTML.strip() + "\n\n            " + content[end_idx:]
    target.write_text(updated_content, encoding="utf-8")
    print(f"Successfully applied Option 1 intro to {target.name}")

    py_files = [str(p) for p in Path(".").glob("*.py")]
    stage_targets = list(set([str(target)] + py_files))

    execute_git(["git", "add"] + stage_targets)
    diff_status = subprocess.run(["git", "diff", "--cached", "--quiet"])
    if diff_status.returncode != 0:
        commit_subject = "Adopt paced walk vs zoom lens metaphor for Section 3 intro"
        commit_body = (
            "Replace Section 3 opening in week1-lecture3.html with the paced walk\n"
            "and camera zoom lens analogies (Option 1) to contrast additive strides\n"
            "against multiplicative scaling intuitively."
        )
        execute_git(["git", "commit", "-m", f"{commit_subject}\n\n{commit_body}"])
        execute_git(["git", "push"])
        print("Successfully committed and pushed Option 1 intro update.")
    else:
        print("No staged changes detected to commit.")

if __name__ == "__main__":
    main()
