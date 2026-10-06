#!/usr/bin/env python3
r"""
fix_bounds_diagram.py

Replaces the unreadable side-by-side 840px bounds SVG in week1-lecture3.html
with two stacked, responsive, large-format SVGs designed for mobile legibility.
"""

import re
import sys
import subprocess
from pathlib import Path

STACKED_BOUNDS_HTML = """            <!-- 2-PANEL RESPONSIVE VISUALIZATION FOR BOUNDEDNESS -->
            <div style="background: #f8fafc; border: 1px solid var(--border); border-radius: 8px; padding: 1.5rem; margin: 1.75rem 0; text-align: center;">
                <p style="font-size: 1.05rem; font-weight: 700; color: #1e293b; margin-top: 0; margin-bottom: 0.35rem;">
                    VISUALIZING BOUNDS: Shaded Corridors vs. Unbounded Escapes
                </p>
                <p style="font-size: 0.92rem; color: #64748b; margin-top: 0; margin-bottom: 1.5rem; max-width: 780px; display: inline-block; line-height: 1.6;">
                    A sequence is bounded if all infinitely many terms live trapped inside a horizontal corridor between ceiling $M$ and floor $m$. If terms eventually punch through every horizontal ceiling, the sequence is unbounded.
                </p>

                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.5rem; text-align: left;">
                    <!-- PANEL 1: BOUNDED CORRIDOR -->
                    <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 6px; padding: 1.25rem;">
                        <span style="font-size: 0.95rem; font-weight: 700; color: #047857; display: block; margin-bottom: 0.2rem;">
                            1. Bounded Sequence: m &le; aₙ &le; M
                        </span>
                        <span style="font-size: 0.85rem; color: #64748b; display: block; margin-bottom: 1rem;">
                            Trapped forever inside a horizontal corridor
                        </span>
                        <svg viewBox="0 0 420 240" style="width: 100%; height: auto; display: block; overflow: visible;">
                            <!-- Shaded Corridor between y=70 (M) and y=165 (m) -->
                            <rect x="75" y="70" width="315" height="95" fill="#ecfdf5" rx="4" opacity="0.9" />

                            <!-- Axes -->
                            <line x1="70" y1="205" x2="395" y2="205" stroke="#0f172a" stroke-width="2" />
                            <line x1="75" y1="210" x2="75" y2="45" stroke="#0f172a" stroke-width="2" />
                            <text x="400" y="210" font-size="14" font-weight="bold" fill="#0f172a">n</text>
                            <text x="75" y="35" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">aₙ</text>

                            <!-- Ceiling M line -->
                            <line x1="75" y1="70" x2="390" y2="70" stroke="#059669" stroke-width="2" stroke-dasharray="5,4" />
                            <text x="68" y="75" font-size="13" font-weight="bold" fill="#047857" text-anchor="end">Ceiling M</text>

                            <!-- Floor m line -->
                            <line x1="75" y1="165" x2="390" y2="165" stroke="#059669" stroke-width="2" stroke-dasharray="5,4" />
                            <text x="68" y="170" font-size="13" font-weight="bold" fill="#047857" text-anchor="end">Floor m</text>

                            <!-- Trapped Points -->
                            <circle cx="110" cy="145" r="5.5" fill="#059669" />
                            <circle cx="150" cy="85" r="5.5" fill="#059669" />
                            <circle cx="190" cy="135" r="5.5" fill="#059669" />
                            <circle cx="230" cy="100" r="5.5" fill="#059669" />
                            <circle cx="270" cy="130" r="5.5" fill="#059669" />
                            <circle cx="310" cy="110" r="5.5" fill="#059669" />
                            <circle cx="350" cy="120" r="5.5" fill="#059669" />

                            <text x="235" y="118" font-size="12" font-weight="bold" fill="#065f46" text-anchor="middle">|aₙ| &le; K (Trapped inside corridor)</text>
                        </svg>
                    </div>

                    <!-- PANEL 2: UNBOUNDED ESCAPE -->
                    <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 6px; padding: 1.25rem;">
                        <span style="font-size: 0.95rem; font-weight: 700; color: #b91c1c; display: block; margin-bottom: 0.2rem;">
                            2. Unbounded Sequence (Escape)
                        </span>
                        <span style="font-size: 0.85rem; color: #64748b; display: block; margin-bottom: 1rem;">
                            Punches through any proposed ceiling M
                        </span>
                        <svg viewBox="0 0 420 240" style="width: 100%; height: auto; display: block; overflow: visible;">
                            <!-- Axes -->
                            <line x1="70" y1="205" x2="395" y2="205" stroke="#0f172a" stroke-width="2" />
                            <line x1="75" y1="210" x2="75" y2="45" stroke="#0f172a" stroke-width="2" />
                            <text x="400" y="210" font-size="14" font-weight="bold" fill="#0f172a">n</text>
                            <text x="75" y="35" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">aₙ</text>

                            <!-- Proposed Ceiling M -->
                            <line x1="75" y1="125" x2="390" y2="125" stroke="#dc2626" stroke-width="2" stroke-dasharray="5,4" />
                            <text x="68" y="130" font-size="13" font-weight="bold" fill="#b91c1c" text-anchor="end">Ceiling M</text>

                            <!-- Escaping Points -->
                            <circle cx="105" cy="190" r="5.5" fill="#dc2626" />
                            <circle cx="145" cy="170" r="5.5" fill="#dc2626" />
                            <circle cx="195" cy="145" r="5.5" fill="#dc2626" />
                            <circle cx="245" cy="120" r="5.5" fill="#dc2626" />
                            <circle cx="295" cy="85" r="6.5" fill="#dc2626" stroke="#991b1b" stroke-width="2" />
                            <circle cx="345" cy="45" r="6.5" fill="#dc2626" stroke="#991b1b" stroke-width="2" />

                            <!-- Break indicator -->
                            <line x1="295" y1="115" x2="295" y2="95" stroke="#dc2626" stroke-width="1.8" />
                            <text x="305" y="105" font-size="11.5" font-weight="bold" fill="#b91c1c">Breaks ceiling!</text>
                        </svg>
                    </div>
                </div>
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

    # Locate the old 2-panel bounds SVG container
    pattern = re.compile(
        r'<!-- 2-PANEL VISUALIZATION FOR BOUNDEDNESS.*?</div>\s*</div>',
        re.DOTALL | re.IGNORECASE
    )

    if not pattern.search(content):
        # Fallback search by title
        pattern = re.compile(
            r'<div[^>]*>\s*<p[^>]*>\s*VISUALIZING BOUNDS:.*?</svg>\s*</div>',
            re.DOTALL | re.IGNORECASE
        )

    if not pattern.search(content):
        print("Error: Could not locate bounds visualization block in week1-lecture3.html", file=sys.stderr)
        sys.exit(1)

    updated_content = pattern.sub(STACKED_BOUNDS_HTML.strip(), content, count=1)
    target.write_text(updated_content, encoding="utf-8")
    print(f"Successfully replaced bounds diagram in {target.name}")

    py_files = [str(p) for p in Path(".").glob("*.py")]
    stage_targets = list(set([str(target)] + py_files))

    execute_git(["git", "add"] + stage_targets)
    diff_status = subprocess.run(["git", "diff", "--cached", "--quiet"])
    if diff_status.returncode != 0:
        commit_subject = "Enlarge and make responsive the bounds diagrams in Lecture 3"
        commit_body = (
            "Split the 840px side-by-side bounds SVG in week1-lecture3.html into\n"
            "two stacked, responsive cards with upgraded font sizes (13-15px)\n"
            "and larger markers for clear readability on mobile viewports."
        )
        execute_git(["git", "commit", "-m", f"{commit_subject}\n\n{commit_body}"])
        execute_git(["git", "push"])
        print("Successfully committed and pushed diagram scaling update.")
    else:
        print("No staged changes detected to commit.")

if __name__ == "__main__":
    main()
