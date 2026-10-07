#!/usr/bin/env python3
r"""
add_prototypes_diagrams.py

Embeds a dedicated, responsive SVG diagram directly underneath each of the
four fundamental prototype sequences in Section 2 of week1-lecture3.html.
Uses string slice insertion to avoid regex template escape parsing.
"""

import sys
import subprocess
from pathlib import Path

SECTION_2_BLOCK = """            <!-- SECTION 2 -->
            <h2 id="catalogue-sequences">2. A Gallery of Fundamental Sequences</h2>
            <div style="margin-bottom: 1.5rem;">
                <h3 style="margin-top: 0; color: #0f172a; font-size: 1.15rem;">How Do We Specify What Goes Inside Each Locker?</h3>
                <p style="font-size: 1.02rem; line-height: 1.75; color: #334155; margin-bottom: 1rem;">
                    When constructing a sequence, there are two primary ways to describe the contents of every locker along the infinite corridor:
                </p>
                <ul style="font-size: 0.98rem; line-height: 1.75; color: #334155; padding-left: 1.25rem; margin-bottom: 1rem;">
                    <li style="margin-bottom: 0.5rem;">
                        <strong>An Explicit Formula (Direct Calculation):</strong> A direct algebraic equation that lets you calculate the value inside locker $n$ immediately. For example, if <span class="nobr">$a_n = n^2$,</span> finding the contents of the $100\\text{th}$ locker requires no intermediate work: <span class="nobr">$a_{100} = 100^2 = 10{,}000$.</span>
                    </li>
                    <li>
                        <strong>A Descriptive or Structural Rule (Pattern-Based):</strong> A well-defined rule that uniquely determines what number belongs at step $n$, even if there is no high-school algebraic formula to jump there directly. For instance, "let <span class="nobr">$p_n$</span> be the $n\\text{th}$ prime number" is completely rigorous because every natural index $n$ pairs with a single, unambiguous prime.
                    </li>
                </ul>
                <p style="font-size: 1.02rem; line-height: 1.75; color: #334155; margin-bottom: 1.5rem;">
                    Below are four foundational prototypes encountered throughout real analysis, each paired with its discrete graphical profile:
                </p>
            </div>

            <!-- PROTOTYPES WITH INLINE DIAGRAMS -->
            <div style="display: flex; flex-direction: column; gap: 2rem; margin: 1.5rem 0 2.5rem 0;">
                <!-- 1. PERFECT SQUARES -->
                <div style="background: #ffffff; border: 1px solid var(--border); border-left: 5px solid #0284c7; border-radius: 8px; padding: 1.5rem; box-shadow: 0 2px 4px rgba(0,0,0,0.03);">
                    <h4 style="margin-top: 0; margin-bottom: 0.5rem; color: #0284c7; font-size: 1.15rem;">
                        1. The Sequence of Perfect Squares: <span class="nobr">$a_n = n^2$</span> <span style="font-size: 0.9rem; font-weight: normal; color: #64748b;">(for $n \\ge 0$)</span>
                    </h4>
                    <p style="font-size: 0.96rem; line-height: 1.65; color: #334155; margin-bottom: 0.4rem;">
                        <strong>Explicit terms:</strong> <span class="nobr">$a_0 = 0,$</span> <span class="nobr">$a_1 = 1,$</span> <span class="nobr">$a_2 = 4,$</span> <span class="nobr">$a_3 = 9,$</span> <span class="nobr">$a_4 = 16,$</span> $\\dots$
                    </p>
                    <p style="font-size: 0.96rem; line-height: 1.65; color: #334155; margin-bottom: 1.25rem;">
                        <strong>Behavior:</strong> Accelerates strictly upward without bound as <span class="nobr">$n \\to \\infty$</span> (diverges to $\\infty$).
                    </p>
                    <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 6px; padding: 1.25rem; text-align: center;">
                        <svg viewBox="0 0 420 220" style="width: 100%; max-width: 480px; height: auto; display: inline-block; overflow: visible;">
                            <line x1="45" y1="180" x2="395" y2="180" stroke="#0f172a" stroke-width="2" />
                            <line x1="55" y1="185" x2="55" y2="35" stroke="#0f172a" stroke-width="2" />
                            <text x="400" y="184" font-size="14" font-weight="bold" fill="#0f172a">n</text>
                            <text x="55" y="24" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">aₙ</text>

                            <!-- Point 0 -->
                            <circle cx="55" cy="180" r="5.5" fill="#0284c7" />
                            <text x="55" y="198" font-size="12" fill="#475569" text-anchor="middle">0</text>
                            <text x="45" y="184" font-size="11" font-weight="bold" fill="#0284c7" text-anchor="end">0</text>

                            <!-- Point 1 -->
                            <line x1="125" y1="180" x2="125" y2="171" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="125" cy="171" r="5.5" fill="#0284c7" />
                            <text x="125" y="198" font-size="12" fill="#475569" text-anchor="middle">1</text>
                            <text x="125" y="163" font-size="11" font-weight="bold" fill="#0284c7" text-anchor="middle">1</text>

                            <!-- Point 2 -->
                            <line x1="195" y1="180" x2="195" y2="145" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="195" cy="145" r="5.5" fill="#0284c7" />
                            <text x="195" y="198" font-size="12" fill="#475569" text-anchor="middle">2</text>
                            <text x="195" y="137" font-size="11" font-weight="bold" fill="#0284c7" text-anchor="middle">4</text>

                            <!-- Point 3 -->
                            <line x1="265" y1="180" x2="265" y2="101" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="265" cy="101" r="5.5" fill="#0284c7" />
                            <text x="265" y="198" font-size="12" fill="#475569" text-anchor="middle">3</text>
                            <text x="265" y="93" font-size="11" font-weight="bold" fill="#0284c7" text-anchor="middle">9</text>

                            <!-- Point 4 -->
                            <line x1="335" y1="180" x2="335" y2="40" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="335" cy="40" r="5.5" fill="#0284c7" />
                            <text x="335" y="198" font-size="12" fill="#475569" text-anchor="middle">4</text>
                            <text x="335" y="32" font-size="11" font-weight="bold" fill="#0284c7" text-anchor="middle">16</text>

                            <path d="M 55 180 Q 200 160 335 40" fill="none" stroke="#0284c7" stroke-width="2" stroke-dasharray="4,4" opacity="0.4" />
                        </svg>
                    </div>
                </div>

                <!-- 2. HARMONIC SEQUENCE -->
                <div style="background: #ffffff; border: 1px solid var(--border); border-left: 5px solid #059669; border-radius: 8px; padding: 1.5rem; box-shadow: 0 2px 4px rgba(0,0,0,0.03);">
                    <h4 style="margin-top: 0; margin-bottom: 0.5rem; color: #059669; font-size: 1.15rem;">
                        2. The Harmonic Sequence: <span class="nobr">$a_n = \\frac{1}{n}$</span> <span style="font-size: 0.9rem; font-weight: normal; color: #64748b;">(for $n \\ge 1$)</span>
                    </h4>
                    <p style="font-size: 0.96rem; line-height: 1.65; color: #334155; margin-bottom: 0.4rem;">
                        <strong>Explicit terms:</strong> <span class="nobr">$a_1 = 1,$</span> <span class="nobr">$a_2 = \\frac{1}{2},$</span> <span class="nobr">$a_3 = \\frac{1}{3},$</span> <span class="nobr">$a_4 = \\frac{1}{4},$</span> <span class="nobr">$a_5 = \\frac{1}{5},$</span> $\\dots$
                    </p>
                    <p style="font-size: 0.96rem; line-height: 1.65; color: #334155; margin-bottom: 1.25rem;">
                        <strong>Behavior:</strong> Strictly decreasing, bounded below by $0$, and converges asymptotically toward $0$.
                    </p>
                    <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 6px; padding: 1.25rem; text-align: center;">
                        <svg viewBox="0 0 420 220" style="width: 100%; max-width: 480px; height: auto; display: inline-block; overflow: visible;">
                            <line x1="45" y1="180" x2="395" y2="180" stroke="#0f172a" stroke-width="2" />
                            <line x1="55" y1="185" x2="55" y2="35" stroke="#0f172a" stroke-width="2" />
                            <text x="400" y="184" font-size="14" font-weight="bold" fill="#0f172a">n</text>
                            <text x="55" y="24" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">aₙ</text>

                            <!-- Point 1 -->
                            <line x1="100" y1="180" x2="100" y2="50" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="100" cy="50" r="5.5" fill="#059669" />
                            <text x="100" y="198" font-size="12" fill="#475569" text-anchor="middle">1</text>
                            <text x="100" y="42" font-size="12" font-weight="bold" fill="#059669" text-anchor="middle">1</text>

                            <!-- Point 2 -->
                            <line x1="165" y1="180" x2="165" y2="115" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="165" cy="115" r="5.5" fill="#059669" />
                            <text x="165" y="198" font-size="12" fill="#475569" text-anchor="middle">2</text>
                            <text x="165" y="107" font-size="12" font-weight="bold" fill="#059669" text-anchor="middle">½</text>

                            <!-- Point 3 -->
                            <line x1="230" y1="180" x2="230" y2="137" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="230" cy="137" r="5.5" fill="#059669" />
                            <text x="230" y="198" font-size="12" fill="#475569" text-anchor="middle">3</text>
                            <text x="230" y="129" font-size="12" font-weight="bold" fill="#059669" text-anchor="middle">⅓</text>

                            <!-- Point 4 -->
                            <line x1="295" y1="180" x2="295" y2="148" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="295" cy="148" r="5.5" fill="#059669" />
                            <text x="295" y="198" font-size="12" fill="#475569" text-anchor="middle">4</text>
                            <text x="295" y="140" font-size="12" font-weight="bold" fill="#059669" text-anchor="middle">¼</text>

                            <!-- Point 5 -->
                            <line x1="360" y1="180" x2="360" y2="154" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="360" cy="154" r="5.5" fill="#059669" />
                            <text x="360" y="198" font-size="12" fill="#475569" text-anchor="middle">5</text>
                            <text x="360" y="146" font-size="12" font-weight="bold" fill="#059669" text-anchor="middle">⅕</text>

                            <!-- Limit line -->
                            <line x1="55" y1="180" x2="395" y2="180" stroke="#10b981" stroke-width="2" stroke-dasharray="5,4" />
                            <text x="390" y="172" font-size="11" font-weight="bold" fill="#047857" text-anchor="end">Limit = 0</text>
                        </svg>
                    </div>
                </div>

                <!-- 3. ALTERNATING SEQUENCE -->
                <div style="background: #ffffff; border: 1px solid var(--border); border-left: 5px solid #d97706; border-radius: 8px; padding: 1.5rem; box-shadow: 0 2px 4px rgba(0,0,0,0.03);">
                    <h4 style="margin-top: 0; margin-bottom: 0.5rem; color: #d97706; font-size: 1.15rem;">
                        3. The Alternating Sequence: <span class="nobr">$a_n = (-1)^n$</span> <span style="font-size: 0.9rem; font-weight: normal; color: #64748b;">(for $n \\ge 0$)</span>
                    </h4>
                    <p style="font-size: 0.96rem; line-height: 1.65; color: #334155; margin-bottom: 0.4rem;">
                        <strong>Explicit terms:</strong> <span class="nobr">$a_0 = 1,$</span> <span class="nobr">$a_1 = -1,$</span> <span class="nobr">$a_2 = 1,$</span> <span class="nobr">$a_3 = -1,$</span> <span class="nobr">$a_4 = 1,$</span> $\\dots$
                    </p>
                    <p style="font-size: 0.96rem; line-height: 1.65; color: #334155; margin-bottom: 1.25rem;">
                        <strong>Behavior:</strong> Non-monotonic oscillation trapped between $-1$ and $+1$; never settles to a single limit.
                    </p>
                    <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 6px; padding: 1.25rem; text-align: center;">
                        <svg viewBox="0 0 420 220" style="width: 100%; max-width: 480px; height: auto; display: inline-block; overflow: visible;">
                            <line x1="45" y1="115" x2="395" y2="115" stroke="#0f172a" stroke-width="2" />
                            <line x1="55" y1="185" x2="55" y2="35" stroke="#0f172a" stroke-width="2" />
                            <text x="400" y="119" font-size="14" font-weight="bold" fill="#0f172a">n</text>
                            <text x="55" y="24" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">aₙ</text>

                            <line x1="55" y1="65" x2="390" y2="65" stroke="#fde68a" stroke-width="1.8" stroke-dasharray="4,4" />
                            <text x="48" y="69" font-size="12" font-weight="bold" fill="#b45309" text-anchor="end">+1</text>
                            <line x1="55" y1="165" x2="390" y2="165" stroke="#fde68a" stroke-width="1.8" stroke-dasharray="4,4" />
                            <text x="48" y="169" font-size="12" font-weight="bold" fill="#b45309" text-anchor="end">-1</text>

                            <!-- n=0 -->
                            <line x1="90" y1="115" x2="90" y2="65" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="90" cy="65" r="5.5" fill="#d97706" />
                            <text x="90" y="132" font-size="12" fill="#475569" text-anchor="middle">0</text>

                            <!-- n=1 -->
                            <line x1="150" y1="115" x2="150" y2="165" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="150" cy="165" r="5.5" fill="#d97706" />
                            <text x="150" y="105" font-size="12" fill="#475569" text-anchor="middle">1</text>

                            <!-- n=2 -->
                            <line x1="210" y1="115" x2="210" y2="65" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="210" cy="65" r="5.5" fill="#d97706" />
                            <text x="210" y="132" font-size="12" fill="#475569" text-anchor="middle">2</text>

                            <!-- n=3 -->
                            <line x1="270" y1="115" x2="270" y2="165" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="270" cy="165" r="5.5" fill="#d97706" />
                            <text x="270" y="105" font-size="12" fill="#475569" text-anchor="middle">3</text>

                            <!-- n=4 -->
                            <line x1="330" y1="115" x2="330" y2="65" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="330" cy="65" r="5.5" fill="#d97706" />
                            <text x="330" y="132" font-size="12" fill="#475569" text-anchor="middle">4</text>

                            <path d="M 90 65 L 150 165 L 210 65 L 270 165 L 330 65" fill="none" stroke="#d97706" stroke-width="2" stroke-dasharray="3,3" opacity="0.4" />
                        </svg>
                    </div>
                </div>

                <!-- 4. PRIME SEQUENCE -->
                <div style="background: #ffffff; border: 1px solid var(--border); border-left: 5px solid #6366f1; border-radius: 8px; padding: 1.5rem; box-shadow: 0 2px 4px rgba(0,0,0,0.03);">
                    <h4 style="margin-top: 0; margin-bottom: 0.5rem; color: #4338ca; font-size: 1.15rem;">
                        4. The Prime Sequence: <span class="nobr">$p_n$</span> <span style="font-size: 0.9rem; font-weight: normal; color: #64748b;">(for $n \\ge 1$)</span>
                    </h4>
                    <p style="font-size: 0.96rem; line-height: 1.65; color: #334155; margin-bottom: 0.4rem;">
                        <strong>Explicit terms:</strong> <span class="nobr">$p_1 = 2,$</span> <span class="nobr">$p_2 = 3,$</span> <span class="nobr">$p_3 = 5,$</span> <span class="nobr">$p_4 = 7,$</span> <span class="nobr">$p_5 = 11,$</span> $\\dots$
                    </p>
                    <p style="font-size: 0.96rem; line-height: 1.65; color: #334155; margin-bottom: 1.25rem;">
                        <strong>Behavior:</strong> Strictly increasing without bound (<span class="nobr">$p_n \\to \\infty$</span>), governed by intrinsic primality rather than a simple algebraic formula.
                    </p>
                    <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 6px; padding: 1.25rem; text-align: center;">
                        <svg viewBox="0 0 420 220" style="width: 100%; max-width: 480px; height: auto; display: inline-block; overflow: visible;">
                            <line x1="45" y1="180" x2="395" y2="180" stroke="#0f172a" stroke-width="2" />
                            <line x1="55" y1="185" x2="55" y2="35" stroke="#0f172a" stroke-width="2" />
                            <text x="400" y="184" font-size="14" font-weight="bold" fill="#0f172a">n</text>
                            <text x="55" y="24" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">pₙ</text>

                            <!-- p1 = 2 -->
                            <line x1="100" y1="180" x2="100" y2="155" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="100" cy="155" r="5.5" fill="#6366f1" />
                            <text x="100" y="198" font-size="12" fill="#475569" text-anchor="middle">1</text>
                            <text x="100" y="146" font-size="12" font-weight="bold" fill="#4338ca" text-anchor="middle">2</text>

                            <!-- p2 = 3 -->
                            <line x1="165" y1="180" x2="165" y2="142" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="165" cy="142" r="5.5" fill="#6366f1" />
                            <text x="165" y="198" font-size="12" fill="#475569" text-anchor="middle">2</text>
                            <text x="165" y="133" font-size="12" font-weight="bold" fill="#4338ca" text-anchor="middle">3</text>

                            <!-- p3 = 5 -->
                            <line x1="230" y1="180" x2="230" y2="117" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="230" cy="117" r="5.5" fill="#6366f1" />
                            <text x="230" y="198" font-size="12" fill="#475569" text-anchor="middle">3</text>
                            <text x="230" y="108" font-size="12" font-weight="bold" fill="#4338ca" text-anchor="middle">5</text>

                            <!-- p4 = 7 -->
                            <line x1="295" y1="180" x2="295" y2="92" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="295" cy="92" r="5.5" fill="#6366f1" />
                            <text x="295" y="198" font-size="12" fill="#475569" text-anchor="middle">4</text>
                            <text x="295" y="83" font-size="12" font-weight="bold" fill="#4338ca" text-anchor="middle">7</text>

                            <!-- p5 = 11 -->
                            <line x1="360" y1="180" x2="360" y2="42" stroke="#94a3b8" stroke-dasharray="3,3" />
                            <circle cx="360" cy="42" r="5.5" fill="#6366f1" />
                            <text x="360" y="198" font-size="12" fill="#475569" text-anchor="middle">5</text>
                            <text x="360" y="33" font-size="12" font-weight="bold" fill="#4338ca" text-anchor="middle">11</text>

                            <path d="M 100 155 L 165 142 L 230 117 L 295 92 L 360 42" fill="none" stroke="#6366f1" stroke-width="2" stroke-dasharray="4,4" opacity="0.4" />
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

    start_token = '<h2 id="catalogue-sequences">'
    end_token = '<h2 id="arithmetic-geometric">'

    start_idx = content.find(start_token)
    end_idx = content.find(end_token)

    if start_idx == -1 or end_idx == -1 or start_idx >= end_idx:
        print("Error: Could not locate Section 2 and Section 3 boundary markers.", file=sys.stderr)
        sys.exit(1)

    # Walk backwards from start_idx to catch any preceding section comment
    comment_token = "<!-- SECTION 2 -->"
    preceding_comment = content.rfind(comment_token, 0, start_idx)
    if preceding_comment != -1 and (start_idx - preceding_comment) < 120:
        start_idx = preceding_comment

    # Walk backwards from end_idx to catch preceding comment for section 3
    sec3_comment = "<!-- SECTION 3 -->"
    preceding_sec3_comment = content.rfind(sec3_comment, start_idx, end_idx)
    if preceding_sec3_comment != -1:
        end_idx = preceding_sec3_comment

    updated_content = content[:start_idx] + SECTION_2_BLOCK.strip() + "\n\n            " + content[end_idx:]
    target.write_text(updated_content, encoding="utf-8")
    print(f"Successfully injected prototype diagrams into {target.name}")

    py_files = [str(p) for p in Path(".").glob("*.py")]
    stage_targets = list(set([str(target)] + py_files))

    execute_git(["git", "add"] + stage_targets)
    diff_status = subprocess.run(["git", "diff", "--cached", "--quiet"])
    if diff_status.returncode != 0:
        commit_subject = "Add responsive diagrams under each prototype sequence"
        commit_body = (
            "Embed dedicated, high-contrast SVG coordinate plots directly beneath\n"
            "each of the four fundamental sequence prototypes in Section 2 of\n"
            "week1-lecture3.html, eliminating regex template parsing errors."
        )
        execute_git(["git", "commit", "-m", f"{commit_subject}\n\n{commit_body}"])
        execute_git(["git", "push"])
        print("Successfully committed and pushed prototype diagram updates.")
    else:
        print("No staged changes detected to commit.")

if __name__ == "__main__":
    main()
