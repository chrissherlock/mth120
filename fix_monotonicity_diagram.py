#!/usr/bin/env python3
r"""
fix_monotonicity_diagram.py

Replaces the unreadable 4-panel 840px Monotonicity SVG in week1-lecture3.html
with four responsive, individually scaled cards designed for mobile legibility.
"""

import re
import sys
import subprocess
from pathlib import Path

RESPONSIVE_MONOTONICITY_HTML = """            <!-- 4-PANEL RESPONSIVE VISUALIZATION FOR MONOTONICITY -->
            <div style="background: #f8fafc; border: 1px solid var(--border); border-radius: 8px; padding: 1.5rem; margin: 1.75rem 0; text-align: center;">
                <p style="font-size: 1.05rem; font-weight: 700; color: #1e293b; margin-top: 0; margin-bottom: 0.35rem;">
                    VISUALIZING MONOTONICITY: Directional Profiles in the Discrete Plane
                </p>
                <p style="font-size: 0.92rem; color: #64748b; margin-top: 0; margin-bottom: 1.5rem; max-width: 780px; display: inline-block; line-height: 1.6;">
                    Monotonicity means committing to a direction along the real line and never reversing course. Notice that weak monotonicity permits flat horizontal rests, but strictly forbids a step backward.
                </p>

                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.25rem; text-align: left;">
                    <!-- PANEL 1: STRICTLY INCREASING -->
                    <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 6px; padding: 1.25rem;">
                        <span style="font-size: 0.95rem; font-weight: 700; color: #0284c7; display: block; margin-bottom: 0.2rem;">
                            1. Strictly Increasing: aₙ₊₁ > aₙ
                        </span>
                        <span style="font-size: 0.85rem; color: #64748b; display: block; margin-bottom: 0.75rem;">
                            Climbs at every single step (never pauses or dips)
                        </span>
                        <svg viewBox="0 0 380 220" style="width: 100%; height: auto; display: block; overflow: visible;">
                            <line x1="45" y1="180" x2="355" y2="180" stroke="#0f172a" stroke-width="2" />
                            <line x1="50" y1="185" x2="50" y2="35" stroke="#0f172a" stroke-width="2" />
                            <text x="360" y="185" font-size="14" font-weight="bold" fill="#0f172a">n</text>
                            <text x="50" y="25" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">aₙ</text>

                            <!-- Points & Ticks -->
                            <line x1="80" y1="180" x2="80" y2="155" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="80" cy="155" r="5.5" fill="#0284c7" />
                            <text x="80" y="198" font-size="12" fill="#475569" text-anchor="middle">0</text>

                            <line x1="140" y1="180" x2="140" y2="130" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="140" cy="130" r="5.5" fill="#0284c7" />
                            <text x="140" y="198" font-size="12" fill="#475569" text-anchor="middle">1</text>

                            <line x1="200" y1="180" x2="200" y2="105" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="200" cy="105" r="5.5" fill="#0284c7" />
                            <text x="200" y="198" font-size="12" fill="#475569" text-anchor="middle">2</text>

                            <line x1="260" y1="180" x2="260" y2="78" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="260" cy="78" r="5.5" fill="#0284c7" />
                            <text x="260" y="198" font-size="12" fill="#475569" text-anchor="middle">3</text>

                            <line x1="320" y1="180" x2="320" y2="52" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="320" cy="52" r="5.5" fill="#0284c7" />
                            <text x="320" y="198" font-size="12" fill="#475569" text-anchor="middle">4</text>

                            <path d="M 80 155 L 140 130 L 200 105 L 260 78 L 320 52" fill="none" stroke="#0284c7" stroke-width="2" stroke-dasharray="4,4" opacity="0.5" />
                        </svg>
                    </div>

                    <!-- PANEL 2: WEAKLY INCREASING -->
                    <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 6px; padding: 1.25rem;">
                        <span style="font-size: 0.95rem; font-weight: 700; color: #059669; display: block; margin-bottom: 0.2rem;">
                            2. Increasing (Weak): aₙ₊₁ &ge; aₙ
                        </span>
                        <span style="font-size: 0.85rem; color: #64748b; display: block; margin-bottom: 0.75rem;">
                            Never steps backward, flat plateaus permitted
                        </span>
                        <svg viewBox="0 0 380 220" style="width: 100%; height: auto; display: block; overflow: visible;">
                            <line x1="45" y1="180" x2="355" y2="180" stroke="#0f172a" stroke-width="2" />
                            <line x1="50" y1="185" x2="50" y2="35" stroke="#0f172a" stroke-width="2" />
                            <text x="360" y="185" font-size="14" font-weight="bold" fill="#0f172a">n</text>
                            <text x="50" y="25" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">aₙ</text>

                            <line x1="80" y1="180" x2="80" y2="150" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="80" cy="150" r="5.5" fill="#059669" />
                            <text x="80" y="198" font-size="12" fill="#475569" text-anchor="middle">0</text>

                            <!-- Plateau at n=1 and n=2 -->
                            <line x1="140" y1="180" x2="140" y2="115" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="140" cy="115" r="5.5" fill="#059669" />
                            <text x="140" y="198" font-size="12" fill="#475569" text-anchor="middle">1</text>

                            <line x1="200" y1="180" x2="200" y2="115" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="200" cy="115" r="5.5" fill="#059669" />
                            <text x="200" y="198" font-size="12" fill="#475569" text-anchor="middle">2</text>

                            <line x1="140" y1="115" x2="200" y2="115" stroke="#10b981" stroke-width="3" />
                            <text x="170" y="103" font-size="11.5" font-weight="bold" fill="#047857" text-anchor="middle">Plateau: a₁ = a₂</text>

                            <line x1="260" y1="180" x2="260" y2="80" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="260" cy="80" r="5.5" fill="#059669" />
                            <text x="260" y="198" font-size="12" fill="#475569" text-anchor="middle">3</text>

                            <line x1="320" y1="180" x2="320" y2="52" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="320" cy="52" r="5.5" fill="#059669" />
                            <text x="320" y="198" font-size="12" fill="#475569" text-anchor="middle">4</text>

                            <path d="M 80 150 L 140 115 L 200 115 L 260 80 L 320 52" fill="none" stroke="#059669" stroke-width="2" stroke-dasharray="4,4" opacity="0.5" />
                        </svg>
                    </div>

                    <!-- PANEL 3: STRICTLY DECREASING -->
                    <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 6px; padding: 1.25rem;">
                        <span style="font-size: 0.95rem; font-weight: 700; color: #d97706; display: block; margin-bottom: 0.2rem;">
                            3. Strictly Decreasing: aₙ₊₁ &lt; aₙ
                        </span>
                        <span style="font-size: 0.85rem; color: #64748b; display: block; margin-bottom: 0.75rem;">
                            Cascades downward at each step (always drops)
                        </span>
                        <svg viewBox="0 0 380 220" style="width: 100%; height: auto; display: block; overflow: visible;">
                            <line x1="45" y1="180" x2="355" y2="180" stroke="#0f172a" stroke-width="2" />
                            <line x1="50" y1="185" x2="50" y2="35" stroke="#0f172a" stroke-width="2" />
                            <text x="360" y="185" font-size="14" font-weight="bold" fill="#0f172a">n</text>
                            <text x="50" y="25" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">aₙ</text>

                            <line x1="80" y1="180" x2="80" y2="55" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="80" cy="55" r="5.5" fill="#d97706" />
                            <text x="80" y="198" font-size="12" fill="#475569" text-anchor="middle">0</text>

                            <line x1="140" y1="180" x2="140" y2="85" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="140" cy="85" r="5.5" fill="#d97706" />
                            <text x="140" y="198" font-size="12" fill="#475569" text-anchor="middle">1</text>

                            <line x1="200" y1="180" x2="200" y2="115" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="200" cy="115" r="5.5" fill="#d97706" />
                            <text x="200" y="198" font-size="12" fill="#475569" text-anchor="middle">2</text>

                            <line x1="260" y1="180" x2="260" y2="140" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="260" cy="140" r="5.5" fill="#d97706" />
                            <text x="260" y="198" font-size="12" fill="#475569" text-anchor="middle">3</text>

                            <line x1="320" y1="180" x2="320" y2="160" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="320" cy="160" r="5.5" fill="#d97706" />
                            <text x="320" y="198" font-size="12" fill="#475569" text-anchor="middle">4</text>

                            <path d="M 80 55 L 140 85 L 200 115 L 260 140 L 320 160" fill="none" stroke="#d97706" stroke-width="2" stroke-dasharray="4,4" opacity="0.5" />
                        </svg>
                    </div>

                    <!-- PANEL 4: NON-MONOTONIC -->
                    <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 6px; padding: 1.25rem;">
                        <span style="font-size: 0.95rem; font-weight: 700; color: #dc2626; display: block; margin-bottom: 0.2rem;">
                            4. Non-Monotonic: Direction Changes
                        </span>
                        <span style="font-size: 0.85rem; color: #64748b; display: block; margin-bottom: 0.75rem;">
                            Zigzags up and down (fails single direction test)
                        </span>
                        <svg viewBox="0 0 380 220" style="width: 100%; height: auto; display: block; overflow: visible;">
                            <line x1="45" y1="180" x2="355" y2="180" stroke="#0f172a" stroke-width="2" />
                            <line x1="50" y1="185" x2="50" y2="35" stroke="#0f172a" stroke-width="2" />
                            <text x="360" y="185" font-size="14" font-weight="bold" fill="#0f172a">n</text>
                            <text x="50" y="25" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">aₙ</text>

                            <line x1="80" y1="180" x2="80" y2="140" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="80" cy="140" r="5.5" fill="#ef4444" />
                            <text x="80" y="198" font-size="12" fill="#475569" text-anchor="middle">0</text>

                            <line x1="140" y1="180" x2="140" y2="70" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="140" cy="70" r="5.5" fill="#ef4444" />
                            <text x="140" y="198" font-size="12" fill="#475569" text-anchor="middle">1</text>

                            <line x1="200" y1="180" x2="200" y2="155" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="200" cy="155" r="5.5" fill="#ef4444" />
                            <text x="200" y="198" font-size="12" fill="#475569" text-anchor="middle">2</text>

                            <line x1="260" y1="180" x2="260" y2="85" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="260" cy="85" r="5.5" fill="#ef4444" />
                            <text x="260" y="198" font-size="12" fill="#475569" text-anchor="middle">3</text>

                            <line x1="320" y1="180" x2="320" y2="135" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="320" cy="135" r="5.5" fill="#ef4444" />
                            <text x="320" y="198" font-size="12" fill="#475569" text-anchor="middle">4</text>

                            <path d="M 80 140 L 140 70 L 200 155 L 260 85 L 320 135" fill="none" stroke="#ef4444" stroke-width="2" stroke-dasharray="4,4" opacity="0.6" />
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

    # Locate the old 4-panel monotonicity SVG container
    pattern = re.compile(
        r'<!--\s*2x2 VISUAL GRID FOR MONOTONICITY\s*-->.*?</div>\s*</div>',
        re.DOTALL | re.IGNORECASE
    )

    if not pattern.search(content):
        # Fallback search by title text
        pattern = re.compile(
            r'<div[^>]*>\s*<p[^>]*>\s*VISUALIZING MONOTONICITY:.*?</svg>\s*</div>',
            re.DOTALL | re.IGNORECASE
        )

    if not pattern.search(content):
        print("Error: Could not locate Monotonicity visualization block in week1-lecture3.html", file=sys.stderr)
        sys.exit(1)

    updated_content = pattern.sub(RESPONSIVE_MONOTONICITY_HTML.strip(), content, count=1)
    target.write_text(updated_content, encoding="utf-8")
    print(f"Successfully replaced Monotonicity diagram in {target.name}")

    py_files = [str(p) for p in Path(".").glob("*.py")]
    stage_targets = list(set([str(target)] + py_files))

    execute_git(["git", "add"] + stage_targets)
    diff_status = subprocess.run(["git", "diff", "--cached", "--quiet"])
    if diff_status.returncode != 0:
        commit_subject = "Enlarge and make responsive Monotonicity diagrams in Lecture 3"
        commit_body = (
            "Split the 4-panel 840px Monotonicity SVG in week1-lecture3.html into\n"
            "four responsive, auto-fitting cards with upgraded font sizes (12-14px)\n"
            "and larger markers for mobile readability."
        )
        execute_git(["git", "commit", "-m", f"{commit_subject}\n\n{commit_body}"])
        execute_git(["git", "push"])
        print("Successfully committed and pushed Monotonicity diagram update.")
    else:
        print("No staged changes detected to commit.")

if __name__ == "__main__":
    main()
