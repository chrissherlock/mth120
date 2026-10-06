#!/usr/bin/env python3
r"""
fix_stepping_table.py

Replaces the clipped 5-column table in week1-lecture3.html with a
responsive design that renders as clean, stacked cards on mobile devices
and preserves the structured table on desktop.
"""

import re
import sys
import subprocess
from pathlib import Path

RESPONSIVE_STEPPING_BLOCK = """            <!-- RESPONSIVE COMPARATIVE STEPPING DISPLAY -->
            <style>
                .stepping-table-container {
                    margin: 1.5rem 0 2rem 0;
                }
                .desktop-stepping-table {
                    width: 100%;
                    border-collapse: collapse;
                    font-size: 0.95rem;
                    text-align: center;
                }
                .mobile-stepping-cards {
                    display: none;
                    flex-direction: column;
                    gap: 0.85rem;
                }
                .stepping-card {
                    background: #ffffff;
                    border: 1px solid var(--border);
                    border-radius: 8px;
                    padding: 1rem 1.15rem;
                    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
                }
                .stepping-card.plateau {
                    background: #f0fdf4;
                    border-color: #bbf7d0;
                }
                .stepping-card-header {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    margin-bottom: 0.6rem;
                    padding-bottom: 0.4rem;
                    border-bottom: 1px solid #e2e8f0;
                }
                .stepping-card-math {
                    display: grid;
                    grid-template-columns: repeat(3, 1fr) auto;
                    align-items: center;
                    gap: 0.5rem;
                    font-size: 0.98rem;
                    font-weight: 600;
                    text-align: center;
                    margin-bottom: 0.5rem;
                }
                @media (max-width: 640px) {
                    .desktop-stepping-table { display: none !important; }
                    .mobile-stepping-cards { display: flex !important; }
                }
            </style>

            <div class="stepping-table-container">
                <!-- DESKTOP TABLE -->
                <div style="overflow-x: auto; -webkit-overflow-scrolling: touch;">
                    <table class="desktop-stepping-table">
                        <thead>
                            <tr style="background: #f1f5f9; border-bottom: 2px solid var(--border);">
                                <th style="padding: 0.65rem 0.75rem; color: #475569; font-weight: 600;">Locker $n$</th>
                                <th style="padding: 0.65rem 0.75rem; color: #0284c7; font-weight: 600;">Climb: $a_n = 2n + 1$</th>
                                <th style="padding: 0.65rem 0.75rem; color: #d97706; font-weight: 600;">Bounce: $b_n = (-1)^n$</th>
                                <th style="padding: 0.65rem 0.75rem; color: #059669; font-weight: 600;">Sum: $c_n = a_n + b_n$</th>
                                <th style="padding: 0.65rem 0.75rem; color: #0f172a; font-weight: 600; text-align: left;">Stepping Motion</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr style="border-bottom: 1px solid #e2e8f0;">
                                <td style="padding: 0.6rem 0.75rem; font-weight: 600; color: #475569;">$n = 0$</td>
                                <td style="padding: 0.6rem 0.75rem; color: #0369a1;">$1$</td>
                                <td style="padding: 0.6rem 0.75rem; color: #b45309;">$+1$</td>
                                <td style="padding: 0.6rem 0.75rem; font-weight: 700; color: #047857;">$2$</td>
                                <td style="padding: 0.6rem 0.75rem; text-align: left; color: #475569;">Baseline starting point</td>
                            </tr>
                            <tr style="border-bottom: 1px solid #e2e8f0; background: #f0fdf4;">
                                <td style="padding: 0.6rem 0.75rem; font-weight: 600; color: #475569;">$n = 1$</td>
                                <td style="padding: 0.6rem 0.75rem; color: #0369a1;">$3$</td>
                                <td style="padding: 0.6rem 0.75rem; color: #b45309;">$-1$</td>
                                <td style="padding: 0.6rem 0.75rem; font-weight: 700; color: #047857;">$2$</td>
                                <td style="padding: 0.6rem 0.75rem; text-align: left; font-weight: 600; color: #166534;">⏸ Flat plateau: $-1$ cancels climb ($c_1 = c_0$)</td>
                            </tr>
                            <tr style="border-bottom: 1px solid #e2e8f0;">
                                <td style="padding: 0.6rem 0.75rem; font-weight: 600; color: #475569;">$n = 2$</td>
                                <td style="padding: 0.6rem 0.75rem; color: #0369a1;">$5$</td>
                                <td style="padding: 0.6rem 0.75rem; color: #b45309;">$+1$</td>
                                <td style="padding: 0.6rem 0.75rem; font-weight: 700; color: #047857;">$6$</td>
                                <td style="padding: 0.6rem 0.75rem; text-align: left; color: #475569;">Steps forward by $+4$</td>
                            </tr>
                            <tr style="border-bottom: 1px solid #e2e8f0; background: #f0fdf4;">
                                <td style="padding: 0.6rem 0.75rem; font-weight: 600; color: #475569;">$n = 3$</td>
                                <td style="padding: 0.6rem 0.75rem; color: #0369a1;">$7$</td>
                                <td style="padding: 0.6rem 0.75rem; color: #b45309;">$-1$</td>
                                <td style="padding: 0.6rem 0.75rem; font-weight: 700; color: #047857;">$6$</td>
                                <td style="padding: 0.6rem 0.75rem; text-align: left; font-weight: 600; color: #166534;">⏸ Flat plateau: $-1$ cancels climb ($c_3 = c_2$)</td>
                            </tr>
                            <tr style="border-bottom: 1px solid #e2e8f0;">
                                <td style="padding: 0.6rem 0.75rem; font-weight: 600; color: #475569;">$n = 4$</td>
                                <td style="padding: 0.6rem 0.75rem; color: #0369a1;">$9$</td>
                                <td style="padding: 0.6rem 0.75rem; color: #b45309;">$+1$</td>
                                <td style="padding: 0.6rem 0.75rem; font-weight: 700; color: #047857;">$10$</td>
                                <td style="padding: 0.6rem 0.75rem; text-align: left; color: #475569;">Steps forward by $+4$</td>
                            </tr>
                            <tr>
                                <td style="padding: 0.6rem 0.75rem; font-weight: 600; color: #475569;">$n = 5$</td>
                                <td style="padding: 0.6rem 0.75rem; color: #0369a1;">$11$</td>
                                <td style="padding: 0.6rem 0.75rem; color: #b45309;">$-1$</td>
                                <td style="padding: 0.6rem 0.75rem; font-weight: 700; color: #047857;">$10$</td>
                                <td style="padding: 0.6rem 0.75rem; text-align: left; font-weight: 600; color: #166534;">⏸ Flat plateau: $-1$ cancels climb ($c_5 = c_4$)</td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <!-- MOBILE STACKED CARDS -->
                <div class="mobile-stepping-cards">
                    <!-- Step 0 -->
                    <div class="stepping-card">
                        <div class="stepping-card-header">
                            <strong style="color: #0f172a;">Locker n = 0</strong>
                            <span style="font-size: 0.75rem; background: #f1f5f9; padding: 0.2rem 0.5rem; border-radius: 4px; color: #475569; font-weight: 600;">Baseline</span>
                        </div>
                        <div class="stepping-card-math">
                            <div><span style="font-size: 0.75rem; color: #0284c7; display: block;">Climb (a₀)</span>1</div>
                            <div style="color: #94a3b8;">+</div>
                            <div><span style="font-size: 0.75rem; color: #d97706; display: block;">Bounce (b₀)</span>+1</div>
                            <div style="border-left: 2px solid #cbd5e1; padding-left: 0.6rem; text-align: left;">
                                <span style="font-size: 0.75rem; color: #059669; display: block;">Sum (c₀)</span>
                                <span style="color: #059669; font-size: 1.1rem;">2</span>
                            </div>
                        </div>
                        <p style="margin: 0; font-size: 0.84rem; color: #64748b;">Starting baseline value</p>
                    </div>

                    <!-- Step 1 -->
                    <div class="stepping-card plateau">
                        <div class="stepping-card-header">
                            <strong style="color: #14532d;">Locker n = 1</strong>
                            <span style="font-size: 0.75rem; background: #dcfce7; color: #166534; padding: 0.2rem 0.5rem; border-radius: 4px; font-weight: 700;">⏸ Flat Plateau</span>
                        </div>
                        <div class="stepping-card-math">
                            <div><span style="font-size: 0.75rem; color: #0284c7; display: block;">Climb (a₁)</span>3</div>
                            <div style="color: #94a3b8;">+</div>
                            <div><span style="font-size: 0.75rem; color: #d97706; display: block;">Bounce (b₁)</span>-1</div>
                            <div style="border-left: 2px solid #86efac; padding-left: 0.6rem; text-align: left;">
                                <span style="font-size: 0.75rem; color: #047857; display: block;">Sum (c₁)</span>
                                <span style="color: #047857; font-size: 1.1rem;">2</span>
                            </div>
                        </div>
                        <p style="margin: 0; font-size: 0.84rem; color: #15803d; font-weight: 500;">-1 cancels the +2 climb &rarr; remains at 2 (c₁ = c₀)</p>
                    </div>

                    <!-- Step 2 -->
                    <div class="stepping-card">
                        <div class="stepping-card-header">
                            <strong style="color: #0f172a;">Locker n = 2</strong>
                            <span style="font-size: 0.75rem; background: #e0f2fe; color: #0369a1; padding: 0.2rem 0.5rem; border-radius: 4px; font-weight: 600;">+4 Leap</span>
                        </div>
                        <div class="stepping-card-math">
                            <div><span style="font-size: 0.75rem; color: #0284c7; display: block;">Climb (a₂)</span>5</div>
                            <div style="color: #94a3b8;">+</div>
                            <div><span style="font-size: 0.75rem; color: #d97706; display: block;">Bounce (b₂)</span>+1</div>
                            <div style="border-left: 2px solid #cbd5e1; padding-left: 0.6rem; text-align: left;">
                                <span style="font-size: 0.75rem; color: #059669; display: block;">Sum (c₂)</span>
                                <span style="color: #059669; font-size: 1.1rem;">6</span>
                            </div>
                        </div>
                        <p style="margin: 0; font-size: 0.84rem; color: #64748b;">Advances forward from 2 to 6</p>
                    </div>

                    <!-- Step 3 -->
                    <div class="stepping-card plateau">
                        <div class="stepping-card-header">
                            <strong style="color: #14532d;">Locker n = 3</strong>
                            <span style="font-size: 0.75rem; background: #dcfce7; color: #166534; padding: 0.2rem 0.5rem; border-radius: 4px; font-weight: 700;">⏸ Flat Plateau</span>
                        </div>
                        <div class="stepping-card-math">
                            <div><span style="font-size: 0.75rem; color: #0284c7; display: block;">Climb (a₃)</span>7</div>
                            <div style="color: #94a3b8;">+</div>
                            <div><span style="font-size: 0.75rem; color: #d97706; display: block;">Bounce (b₃)</span>-1</div>
                            <div style="border-left: 2px solid #86efac; padding-left: 0.6rem; text-align: left;">
                                <span style="font-size: 0.75rem; color: #047857; display: block;">Sum (c₃)</span>
                                <span style="color: #047857; font-size: 1.1rem;">6</span>
                            </div>
                        </div>
                        <p style="margin: 0; font-size: 0.84rem; color: #15803d; font-weight: 500;">-1 cancels the +2 climb &rarr; remains at 6 (c₃ = c₂)</p>
                    </div>

                    <!-- Step 4 -->
                    <div class="stepping-card">
                        <div class="stepping-card-header">
                            <strong style="color: #0f172a;">Locker n = 4</strong>
                            <span style="font-size: 0.75rem; background: #e0f2fe; color: #0369a1; padding: 0.2rem 0.5rem; border-radius: 4px; font-weight: 600;">+4 Leap</span>
                        </div>
                        <div class="stepping-card-math">
                            <div><span style="font-size: 0.75rem; color: #0284c7; display: block;">Climb (a₄)</span>9</div>
                            <div style="color: #94a3b8;">+</div>
                            <div><span style="font-size: 0.75rem; color: #d97706; display: block;">Bounce (b₄)</span>+1</div>
                            <div style="border-left: 2px solid #cbd5e1; padding-left: 0.6rem; text-align: left;">
                                <span style="font-size: 0.75rem; color: #059669; display: block;">Sum (c₄)</span>
                                <span style="color: #059669; font-size: 1.1rem;">10</span>
                            </div>
                        </div>
                        <p style="margin: 0; font-size: 0.84rem; color: #64748b;">Advances forward from 6 to 10</p>
                    </div>

                    <!-- Step 5 -->
                    <div class="stepping-card plateau">
                        <div class="stepping-card-header">
                            <strong style="color: #14532d;">Locker n = 5</strong>
                            <span style="font-size: 0.75rem; background: #dcfce7; color: #166534; padding: 0.2rem 0.5rem; border-radius: 4px; font-weight: 700;">⏸ Flat Plateau</span>
                        </div>
                        <div class="stepping-card-math">
                            <div><span style="font-size: 0.75rem; color: #0284c7; display: block;">Climb (a₅)</span>11</div>
                            <div style="color: #94a3b8;">+</div>
                            <div><span style="font-size: 0.75rem; color: #d97706; display: block;">Bounce (b₅)</span>-1</div>
                            <div style="border-left: 2px solid #86efac; padding-left: 0.6rem; text-align: left;">
                                <span style="font-size: 0.75rem; color: #047857; display: block;">Sum (c₅)</span>
                                <span style="color: #047857; font-size: 1.1rem;">10</span>
                            </div>
                        </div>
                        <p style="margin: 0; font-size: 0.84rem; color: #15803d; font-weight: 500;">-1 cancels the +2 climb &rarr; remains at 10 (c₅ = c₄)</p>
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

    # Locate the old table block
    pattern = re.compile(
        r'<!--\s*BEGINNER-FRIENDLY COMPARATIVE STEPPING TABLE\s*-->.*?</table>\s*</div>',
        re.DOTALL | re.IGNORECASE
    )

    if not pattern.search(content):
        # Fallback search matching table with Locker n headers
        pattern = re.compile(
            r'<div[^>]*overflow-x:\s*auto[^>]*>\s*<table[^>]*>.*?Locker\s*\$n\$.*?</table>\s*</div>',
            re.DOTALL | re.IGNORECASE
        )

    if not pattern.search(content):
        print("Error: Could not locate stepping table block in week1-lecture3.html", file=sys.stderr)
        sys.exit(1)

    updated_content = pattern.sub(RESPONSIVE_STEPPING_BLOCK.strip(), content, count=1)
    target.write_text(updated_content, encoding="utf-8")
    print(f"Successfully replaced stepping table with responsive cards in {target.name}")

    py_files = [str(p) for p in Path(".").glob("*.py")]
    stage_targets = list(set([str(target)] + py_files))

    execute_git(["git", "add"] + stage_targets)
    diff_status = subprocess.run(["git", "diff", "--cached", "--quiet"])
    if diff_status.returncode != 0:
        commit_subject = "Convert sequence combination table to responsive cards"
        commit_body = (
            "Replace the 5-column desktop stepping table in week1-lecture3.html\n"
            "with an adaptive view that transforms into stacked step cards on\n"
            "mobile screens to eliminate cramped horizontal clipping."
        )
        execute_git(["git", "commit", "-m", f"{commit_subject}\n\n{commit_body}"])
        execute_git(["git", "push"])
        print("Successfully committed and pushed table responsiveness update.")
    else:
        print("No staged changes detected to commit.")

if __name__ == "__main__":
    main()
