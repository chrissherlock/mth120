#!/usr/bin/env python3
"""
update.py

Injects historical biography sidebars for Hippasus, Eudoxus, Weierstrass,
and Dedekind into week1-lecture2.html, then stages both the updated HTML
and update.py itself before committing and pushing upstream.
"""

from pathlib import Path
import subprocess
import sys

TARGET_HTML = Path("week1-lecture2.html")
SCRIPT_FILE = Path(__file__).resolve()

HIPPASUS_BOX = """            <!-- HISTORICAL CONTEXT: HIPPASUS -->
            <div class="biography-box" style="margin-top: 2rem;">
                <h4>🏛️ The Scandal of Incommensurability: Hippasus of Metapontum</h4>
                <div style="display: flex; gap: 1.5rem; align-items: flex-start; flex-wrap: wrap; margin-top: 0.75rem;">
                    <div style="flex: 0 0 135px; max-width: 135px;">
                        <img src="images/hippasus.jpg" alt="Hippasus of Metapontum" style="width: 100%; height: auto; border-radius: 6px; border: 1px solid var(--border); box-shadow: 0 2px 4px rgba(0,0,0,0.06); display: block;">
                        <span style="display: block; font-size: 0.8rem; color: #64748b; text-align: center; margin-top: 0.4rem; line-height: 1.3;">Hippasus of Metapontum<br>(c. 5th Century BCE)</span>
                    </div>
                    <div style="flex: 1; min-width: 260px;">
                        <p style="margin-top: 0; color: #334155; line-height: 1.65; font-size: 0.96rem;">
                            <strong>Hippasus of Metapontum</strong> was an early Greek philosopher and member of the Pythagorean brotherhood. The Pythagoreans lived by the sacred creed <em>"all is number"</em>, believing that every geometric magnitude in the cosmos could be expressed as a ratio of integers.
                        </p>
                        <p style="color: #334155; line-height: 1.65; font-size: 0.96rem; margin-bottom: 0.5rem;">
                            <strong>Shattering the World of Fractions:</strong> While investigating a unit square with side lengths of $1$, Hippasus evaluated the hypotenuse $\sqrt{1^2 + 1^2} = \sqrt{2}$. Using a geometric parity contradiction, he discovered the diagonal is <strong>incommensurable</strong> with the sides: no common sub-unit exists that divides evenly into both.
                        </p>
                        <p style="color: #334155; line-height: 1.65; font-size: 0.96rem; margin-bottom: 0;">
                            By proving that $\sqrt{2} \notin \mathbb{Q}$, Hippasus revealed that rational numbers leave pinprick holes along the number line. According to mathematical lore, this rupture was so destabilizing to Pythagorean doctrine that Hippasus was taken out to sea and cast overboard for heresy.
                        </p>
                    </div>
                </div>
            </div>
"""

EUDOXUS_BOX = """            <!-- HISTORICAL CONTEXT: EUDOXUS -->
            <div class="biography-box" style="margin-top: 2rem;">
                <h4>🏛️ Banishment of the Infinitesimal: Eudoxus of Cnidus</h4>
                <div style="display: flex; gap: 1.5rem; align-items: flex-start; flex-wrap: wrap; margin-top: 0.75rem;">
                    <div style="flex: 0 0 135px; max-width: 135px;">
                        <img src="images/eudoxus.jpg" alt="Eudoxus of Cnidus" style="width: 100%; height: auto; border-radius: 6px; border: 1px solid var(--border); box-shadow: 0 2px 4px rgba(0,0,0,0.06); display: block;">
                        <span style="display: block; font-size: 0.8rem; color: #64748b; text-align: center; margin-top: 0.4rem; line-height: 1.3;">Eudoxus of Cnidus<br>(c. 408–355 BCE)</span>
                    </div>
                    <div style="flex: 1; min-width: 260px;">
                        <p style="margin-top: 0; color: #334155; line-height: 1.65; font-size: 0.96rem;">
                            <strong>Eudoxus of Cnidus</strong> was an ancient Greek astronomer and mathematician, considered antiquity's greatest geometer alongside Archimedes. Following the crisis of incommensurability, Greek mathematics stalled because proofs relied on fractional proportions that failed for irrational lengths.
                        </p>
                        <p style="color: #334155; line-height: 1.65; font-size: 0.96rem; margin-bottom: 0.5rem;">
                            <strong>The Theory of Proportions:</strong> Preserved in Book V of Euclid's <em>Elements</em>, Eudoxus created a rigorous definition of proportion that applied equally to rational and incommensurable magnitudes. This established the foundation for the <strong>Archimedean Property</strong>: any two positive quantities can exceed one another if either is added repeatedly.
                        </p>
                        <p style="color: #334155; line-height: 1.65; font-size: 0.96rem; margin-bottom: 0;">
                            In real analysis, this guarantees the real line contains no non-zero "infinitely small" ghosts. No matter how small an interval $\epsilon > 0$ is chosen, stepping by size $\epsilon$ will eventually outrun any finite number, bridging discrete counting rungs to continuous geometry.
                        </p>
                    </div>
                </div>
            </div>
"""

WEIERSTRASS_BOX = """            <!-- HISTORICAL CONTEXT: WEIERSTRASS -->
            <div class="biography-box" style="margin-top: 2rem;">
                <h4>🏛️ The Architect of Rigor: Karl Weierstrass</h4>
                <div style="display: flex; gap: 1.5rem; align-items: flex-start; flex-wrap: wrap; margin-top: 0.75rem;">
                    <div style="flex: 0 0 135px; max-width: 135px;">
                        <img src="images/weierstrass.png" alt="Karl Weierstrass" style="width: 100%; height: auto; border-radius: 6px; border: 1px solid var(--border); box-shadow: 0 2px 4px rgba(0,0,0,0.06); display: block;">
                        <span style="display: block; font-size: 0.8rem; color: #64748b; text-align: center; margin-top: 0.4rem; line-height: 1.3;">Karl Weierstrass<br>(1815–1897)</span>
                    </div>
                    <div style="flex: 1; min-width: 260px;">
                        <p style="margin-top: 0; color: #334155; line-height: 1.65; font-size: 0.96rem;">
                            <strong>Karl Weierstrass</strong> was a German mathematician regarded as the "father of modern analysis." For two centuries after Newton and Leibniz, calculus relied on physical intuition, moving particles, and geometric curves—analogies that collapsed when analyzing pathological curves.
                        </p>
                        <p style="color: #334155; line-height: 1.65; font-size: 0.96rem; margin-bottom: 0.5rem;">
                            <strong>Absolute Value as a Metric:</strong> Weierstrass replaced vague phrases like <em>"approaches"</em> or <em>"tends toward"</em> with static, algebraic inequalities centered entirely on the <strong>absolute value function</strong> $|x - y|$.
                        </p>
                        <p style="color: #334155; line-height: 1.65; font-size: 0.96rem; margin-bottom: 0;">
                            By formalizing closeness through exact bounds ($|f(x) - L| < \epsilon$ whenever $|x - c| < \delta$), Weierstrass made absolute value the universal measuring tape of analysis. Properties like the <strong>Triangle Inequality</strong> became the engine proving convergence and continuity.
                        </p>
                    </div>
                </div>
            </div>
"""

DEDEKIND_BOX = """            <!-- HISTORICAL CONTEXT: DEDEKIND -->
            <div class="biography-box" style="margin-top: 2rem;">
                <h4>🏛️ Slicing the Continuum: Richard Dedekind</h4>
                <div style="display: flex; gap: 1.5rem; align-items: flex-start; flex-wrap: wrap; margin-top: 0.75rem;">
                    <div style="flex: 0 0 135px; max-width: 135px;">
                        <img src="images/dedekind.jpg" alt="Richard Dedekind" style="width: 100%; height: auto; border-radius: 6px; border: 1px solid var(--border); box-shadow: 0 2px 4px rgba(0,0,0,0.06); display: block;">
                        <span style="display: block; font-size: 0.8rem; color: #64748b; text-align: center; margin-top: 0.4rem; line-height: 1.3;">Richard Dedekind<br>(1831–1916)</span>
                    </div>
                    <div style="flex: 1; min-width: 260px;">
                        <p style="margin-top: 0; color: #334155; line-height: 1.65; font-size: 0.96rem;">
                            <strong>Richard Dedekind</strong> made foundational contributions to abstract algebra and analysis. In 1858, while preparing calculus lectures in Zürich, he realized that while educators spoke constantly of the "continuous real line," analysis had no definition of what made it continuous.
                        </p>
                        <p style="color: #334155; line-height: 1.65; font-size: 0.96rem; margin-bottom: 0.5rem;">
                            <strong>Dedekind Cuts:</strong> In his 1872 work <em>Stetigkeit und irrationale Zahlen</em>, Dedekind formulated the essential property of an unbroken line: any partition of numbers into left and right halves must pass through an exact boundary point.
                        </p>
                        <p style="color: #334155; line-height: 1.65; font-size: 0.96rem; margin-bottom: 0;">
                            When slicing rationals $\mathbb{Q}$ at $\sqrt{2}$, the cut passes through empty air: the lower set has no maximum and the upper set has no minimum. Dedekind defined irrational numbers as the <em>cuts themselves</em>, filling every microscopic pinprick hole and completing $\mathbb{R}$.
                        </p>
                    </div>
                </div>
            </div>
"""

def execute_git(args: list[str]) -> subprocess.CompletedProcess:
    result = subprocess.run(args, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Git command failed: {' '.join(args)}", file=sys.stderr)
        print(result.stderr.strip(), file=sys.stderr)
        sys.exit(result.returncode)
    return result

def main() -> None:
    if not TARGET_HTML.exists():
        print(f"Error: {TARGET_HTML} does not exist.", file=sys.stderr)
        sys.exit(1)

    content = TARGET_HTML.read_text(encoding="utf-8")
    original = content

    # 1. Section 2: Insert Hippasus above Section 3
    if "Hippasus of Metapontum" not in content and '<h2 id="field-order">' in content:
        content = content.replace(
            '<h2 id="field-order">',
            f"{HIPPASUS_BOX}\n            <h2 id=\"field-order\">"
        )

    # 2. Section 3: Insert Eudoxus above Section 4
    if "Eudoxus of Cnidus" not in content and '<h2 id="absolute-value">' in content:
        content = content.replace(
            '<h2 id="absolute-value">',
            f"{EUDOXUS_BOX}\n            <h2 id=\"absolute-value\">"
        )

    # 3. Section 4: Insert Weierstrass above Section 5
    if "Karl Weierstrass" not in content and '<h2 id="completeness-bounds">' in content:
        content = content.replace(
            '<h2 id="completeness-bounds">',
            f"{WEIERSTRASS_BOX}\n            <h2 id=\"completeness-bounds\">"
        )

    # 4. Section 5: Insert Dedekind before Footer Navigation
    if "Richard Dedekind" not in content and "<!-- FOOTER NAVIGATION -->" in content:
        content = content.replace(
            "<!-- FOOTER NAVIGATION -->",
            f"{DEDEKIND_BOX}\n            <!-- FOOTER NAVIGATION -->"
        )

    if content != original:
        TARGET_HTML.write_text(content, encoding="utf-8")
        print(f"Successfully patched {TARGET_HTML.name}.")
    else:
        print(f"{TARGET_HTML.name} is already up to date.")

    # Git commit and push workflow: Stage both TARGET_HTML and update.py
    execute_git(["git", "rev-parse", "--is-inside-work-tree"])
    execute_git(["git", "add", str(TARGET_HTML), str(SCRIPT_FILE)])

    diff_check = subprocess.run(["git", "diff", "--cached", "--quiet"])
    if diff_check.returncode == 0:
        print("No staged changes detected. Working tree is clean.")
        return

    commit_subject = "Add Lecture 2 historical biographies and version update.py"
    commit_body = (
        "Add contextual biography boxes for Hippasus, Eudoxus, Weierstrass,\n"
        "and Dedekind to week1-lecture2.html, and stage update.py alongside\n"
        "the modified coursework document."
    )
    full_message = f"{commit_subject}\n\n{commit_body}"

    execute_git(["git", "commit", "-m", full_message])
    print("Committed successfully.")

    print("Pushing to remote repository...")
    execute_git(["git", "push"])
    print("Push complete.")

if __name__ == "__main__":
    main()
