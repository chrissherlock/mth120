#!/usr/bin/env python3
r"""
update_prototype_descriptions.py

Rewrites the behavior descriptions in Section 2 of week1-lecture3.html
into friendly 'Plain English' intuitions paired with clear 'Analyst's Word'
explanations for undergraduate beginners.
"""

import sys
import subprocess
from pathlib import Path

SECTION_2_REFINED = """            <!-- PROTOTYPES WITH INLINE DIAGRAMS -->
            <div style="display: flex; flex-direction: column; gap: 2rem; margin: 1.5rem 0 2.5rem 0;">
                <!-- 1. PERFECT SQUARES -->
                <div style="background: #ffffff; border: 1px solid var(--border); border-left: 5px solid #0284c7; border-radius: 8px; padding: 1.5rem; box-shadow: 0 2px 4px rgba(0,0,0,0.03);">
                    <h4 style="margin-top: 0; margin-bottom: 0.5rem; color: #0284c7; font-size: 1.15rem;">
                        1. The Sequence of Perfect Squares: <span class="nobr">$a_n = n^2$</span> <span style="font-size: 0.9rem; font-weight: normal; color: #64748b;">(for $n \\ge 0$)</span>
                    </h4>
                    <p style="font-size: 0.96rem; line-height: 1.65; color: #334155; margin-bottom: 0.5rem;">
                        <strong>Explicit terms:</strong> <span class="nobr">$a_0 = 0,$</span> <span class="nobr">$a_1 = 1,$</span> <span class="nobr">$a_2 = 4,$</span> <span class="nobr">$a_3 = 9,$</span> <span class="nobr">$a_4 = 16,$</span> $\\dots$
                    </p>
                    <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 0.85rem 1rem; margin-bottom: 1.25rem; font-size: 0.92rem; line-height: 1.6;">
                        <div style="margin-bottom: 0.35rem;">
                            <strong style="color: #0f172a;">🏃 What your eyes see:</strong>
                            <span style="color: #334155;"> The numbers blast upward like a rocket. The jump from one locker to the next gets bigger with every single step ($+1, +3, +5, +7, \\dots$). There is no ceiling in sight.</span>
                        </div>
                        <div>
                            <strong style="color: #0284c7;">🎓 The Analyst's Word:</strong>
                            <span style="color: #475569;"> We say this sequence <em>diverges to infinity</em> ($a_n \\to \\infty$). "Diverging" simply means it never settles down to a single steady destination point.</span>
                        </div>
                    </div>
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
                    <p style="font-size: 0.96rem; line-height: 1.65; color: #334155; margin-bottom: 0.5rem;">
                        <strong>Explicit terms:</strong> <span class="nobr">$a_1 = 1,$</span> <span class="nobr">$a_2 = \\frac{1}{2},$</span> <span class="nobr">$a_3 = \\frac{1}{3},$</span> <span class="nobr">$a_4 = \\frac{1}{4},$</span> <span class="nobr">$a_5 = \\frac{1}{5},$</span> $\\dots$
                    </p>
                    <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 0.85rem 1rem; margin-bottom: 1.25rem; font-size: 0.92rem; line-height: 1.6;">
                        <div style="margin-bottom: 0.35rem;">
                            <strong style="color: #0f172a;">🏃 What your eyes see:</strong>
                            <span style="color: #334155;"> The numbers get sliced thinner and thinner ($1, 0.5, 0.33, 0.25, \\dots$), sinking toward $0$. But dividing $1$ by a positive number can never produce zero or a negative!</span>
                        </div>
                        <div>
                            <strong style="color: #059669;">🎓 The Analyst's Word:</strong>
                            <span style="color: #475569;"> We say this sequence <em>converges to zero</em> ($a_n \\to 0$). "Converging" means zooming into an exact destination. Zero acts like a magnet that the terms crowd around forever.</span>
                        </div>
                    </div>
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
                            <text x="390" y="172" font-size="11" font-weight="bold" fill="#047857" text-anchor="end">Target = 0</text>
                        </svg>
                    </div>
                </div>

                <!-- 3. ALTERNATING SEQUENCE -->
                <div style="background: #ffffff; border: 1px solid var(--border); border-left: 5px solid #d97706; border-radius: 8px; padding: 1.5rem; box-shadow: 0 2px 4px rgba(0,0,0,0.03);">
                    <h4 style="margin-top: 0; margin-bottom: 0.5rem; color: #d97706; font-size: 1.15rem;">
                        3. The Alternating Sequence: <span class="nobr">$a_n = (-1)^n$</span> <span style="font-size: 0.9rem; font-weight: normal; color: #64748b;">(for $n \\ge 0$)</span>
                    </h4>
                    <p style="font-size: 0.96rem; line-height: 1.65; color: #334155; margin-bottom: 0.5rem;">
                        <strong>Explicit terms:</strong> <span class="nobr">$a_0 = 1,$</span> <span class="nobr">$a_1 = -1,$</span> <span class="nobr">$a_2 = 1,$</span> <span class="nobr">$a_3 = -1,$</span> <span class="nobr">$a_4 = 1,$</span> $\\dots$
                    </p>
                    <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 0.85rem 1rem; margin-bottom: 1.25rem; font-size: 0.92rem; line-height: 1.6;">
                        <div style="margin-bottom: 0.35rem;">
                            <strong style="color: #0f172a;">🏃 What your eyes see:</strong>
                            <span style="color: #334155;"> Like a light switch being flipped with every step ($+1, -1, +1, -1, \\dots$). It stays trapped in place, never growing large, but never coming to rest.</span>
                        </div>
                        <div>
                            <strong style="color: #d97706;">🎓 The Analyst's Word:</strong>
                            <span style="color: #475569;"> We say this sequence <em>diverges by oscillation</em>. Even though it is fenced into a tiny box between $-1$ and $+1$, it fails to settle on a single final destination.</span>
                        </div>
                    </div>
                    <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 6px; padding: 1.25rem; text-align: center;">
                        <svg viewBox="0 0 420 220" style="width: 100%; max-width: 480px; height: auto; display: inline-block; overflow: visible;">
                            <line x1="45" y1="115" x2="395" y2="115" stroke="#0f172a" stroke-width="2" />
                            <line x1="55" y1="185" x2="55" y2="35" stroke="#0f172a" stroke-width="2" />
                            <text x="400" y="119" font-size="14" font-weight="bold" fill="#0f172a">n</text>
                            <text x="55" y="24" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">aₙ</text>

                            <!-- Guide rails -->
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
                    <p style="font-size: 0.96rem; line-height: 1.65; color: #334155; margin-bottom: 0.5rem;">
                        <strong>Explicit terms:</strong> <span class="nobr">$p_1 = 2,$</span> <span class="nobr">$p_2 = 3,$</span> <span class="nobr">$p_3 = 5,$</span> <span class="nobr">$p_4 = 7,$</span> <span class="nobr">$p_5 = 11,$</span> $\\dots$
                    </p>
                    <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 0.85rem 1rem; margin-bottom: 1.25rem; font-size: 0.92rem; line-height: 1.6;">
                        <div style="margin-bottom: 0.35rem;">
                            <strong style="color: #0f172a;">🏃 What your eyes see:</strong>
                            <span style="color: #334155;"> The numbers climb upward forever, but the step size is erratic. Sometimes primes sit right next to each other ($2, 3$), while other times you must hike through long stretches of non-primes to find the next one.</span>
                        </div>
                        <div>
                            <strong style="color: #4338ca;">🎓 The Analyst's Word:</strong>
                            <span style="color: #475569;"> This sequence is <em>strictly increasing and unbounded</em> ($p_{n+1} > p_n$), but has <em>no simple closed algebraic formula</em>. It demonstrates that a sequence doesn't need an elementary equation to be completely well-defined.</span>
                        </div>
                    </div>
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

    start_token = '<div style="display: flex; flex-direction: column; gap: 2rem; margin: 1.5rem 0 2.5rem 0;">'
    end_token = '<h2 id="arithmetic-geometric">'

    start_idx = content.find(start_token)
    end_idx = content.find(end_token)

    if start_idx == -1 or end_idx == -1:
        # Fallback if previous replacement hadn't occurred
        start_token = '<h4 style="color: #0f172a; font-size: 1.1rem; margin-bottom: 0.75rem;">Prototypes of Fundamental Sequences</h4>'
        start_idx = content.find(start_token)
        if start_idx != -1:
            div_start = content.rfind('<div', 0, start_idx)
            if div_start != -1:
                start_idx = div_start

    if start_idx == -1 or end_idx == -1 or start_idx >= end_idx:
        print("Error: Could not locate boundary markers in week1-lecture3.html", file=sys.stderr)
        sys.exit(1)

    # Search for comment token before section 3 to preserve structure
    comment_token = '<!-- SECTION 3 -->'
    comment_idx = content.rfind(comment_token, start_idx, end_idx)
    target_end_idx = comment_idx if comment_idx != -1 else end_idx

    updated_content = content[:start_idx] + SECTION_2_REFINED.strip() + "\n\n            " + content[target_end_idx:]
    target.write_text(updated_content, encoding="utf-8")
    print(f"Successfully refined prototype behavior descriptions in {target.name}")

    py_files = [str(p) for p in Path(".").glob("*.py")]
    stage_targets = list(set([str(target)] + py_files))

    execute_git(["git", "add"] + stage_targets)
    diff_status = subprocess.run(["git", "diff", "--cached", "--quiet"])
    if diff_status.returncode != 0:
        commit_subject = "Refactor sequence prototype descriptions for beginners"
        commit_body = (
            "Split behavior descriptions in Section 2 of week1-lecture3.html\n"
            "into intuitive 'Plain English' visual pictures and demystifying\n"
            "'Analyst's Word' glossaries for undergraduate beginners."
        )
        execute_git(["git", "commit", "-m", f"{commit_subject}\n\n{commit_body}"])
        execute_git(["git", "push"])
        print("Successfully committed and pushed description updates.")
    else:
        print("No staged changes detected to commit.")

if __name__ == "__main__":
    main()
