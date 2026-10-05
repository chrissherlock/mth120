#!/usr/bin/env python3
"""
update.py

Injects historical biography boxes for Hippasus, Eudoxus, Weierstrass,
and Dedekind into week1-lecture2.html matching the week1-lecture1 format,
corrects image paths, uses raw strings to prevent KaTeX escape warnings,
and stages both the HTML and this script before committing and pushing.
"""

from pathlib import Path
import subprocess
import sys

TARGET_HTML = Path("week1-lecture2.html")
SCRIPT_FILE = Path(__file__).resolve()

HIPPASUS_BOX = r"""            <!-- HISTORICAL CONTEXT: HIPPASUS -->
            <div class="biography-box" style="margin-top: 2rem;">
                <h4>🏛️ The Scandal of Incommensurability: Hippasus of Metapontum</h4>
                <div style="display: flex; gap: 1.5rem; align-items: flex-start; flex-wrap: wrap; margin-top: 0.75rem;">
                    <div style="flex: 0 0 135px; max-width: 135px;">
                        <img src="images/hippasus.png" alt="Hippasus of Metapontum" style="width: 100%; height: auto; border-radius: 6px; border: 1px solid var(--border); box-shadow: 0 2px 4px rgba(0,0,0,0.06); display: block;">
                        <span style="display: block; font-size: 0.8rem; color: #64748b; text-align: center; margin-top: 0.4rem; line-height: 1.3;">Hippasus of Metapontum<br>(c. 5th Century BCE)</span>
                    </div>
                    <div style="flex: 1; min-width: 260px;">
                        <p style="margin-top: 0; color: #334155; line-height: 1.65; font-size: 0.96rem;">
                            <strong><a href="https://en.wikipedia.org/wiki/Hippasus" target="_blank" rel="noopener noreferrer" style="color: #4f46e5; text-decoration: underline;">Hippasus of Metapontum</a></strong> was an early Greek philosopher and member of the Pythagorean brotherhood. The Pythagoreans held a mystical doctrine that <em>"all is number"</em>, believing that every geometric magnitude in the cosmos could be expressed as an exact ratio of integers.
                        </p>
                        <p style="color: #334155; line-height: 1.65; font-size: 0.96rem; margin-bottom: 0.5rem;">
                            <strong>Shattering the World of Fractions:</strong> While examining the simplest geometric figure imaginable—a unit square with side lengths of $1$—Hippasus evaluated the diagonal hypotenuse $\sqrt{1^2 + 1^2} = \sqrt{2}$. Using an early geometric version of the parity contradiction shown above, he proved the diagonal is <strong>incommensurable</strong> with the sides: no common sub-unit exists that divides evenly into both.
                        </p>
                        <p style="color: #334155; line-height: 1.65; font-size: 0.96rem; margin-bottom: 0;">
                            By proving that $\sqrt{2} \notin \mathbb{Q}$, Hippasus revealed that the rational numbers leave gaping, invisible pinprick holes along the number line. According to mathematical lore, the discovery so severely undermined Pythagorean cosmology that Hippasus was taken out to sea and thrown overboard for heresy.
                        </p>
                    </div>
                </div>
            </div>"""

EUDOXUS_BOX = r"""            <!-- HISTORICAL CONTEXT: EUDOXUS -->
            <div class="biography-box" style="margin-top: 2rem;">
                <h4>🏛️️ Banishment of the Infinitesimal: Eudoxus of Cnidus</h4>
                <div style="display: flex; gap: 1.5rem; align-items: flex-start; flex-wrap: wrap; margin-top: 0.75rem;">
                    <div style="flex: 0 0 135px; max-width: 135px;">
                        <img src="images/eudoxus.jpg" alt="Eudoxus of Cnidus" style="width: 100%; height: auto; border-radius: 6px; border: 1px solid var(--border); box-shadow: 0 2px 4px rgba(0,0,0,0.06); display: block;">
                        <span style="display: block; font-size: 0.8rem; color: #64748b; text-align: center; margin-top: 0.4rem; line-height: 1.3;">Eudoxus of Cnidus<br>(c. 408–355 BCE)</span>
                    </div>
                    <div style="flex: 1; min-width: 260px;">
                        <p style="margin-top: 0; color: #334155; line-height: 1.65; font-size: 0.96rem;">
                            <strong><a href="https://en.wikipedia.org/wiki/Eudoxus_of_Cnidus" target="_blank" rel="noopener noreferrer" style="color: #4f46e5; text-decoration: underline;">Eudoxus of Cnidus</a></strong> was an ancient Greek astronomer, scholar, and mathematician, widely considered antiquity's greatest geometer alongside Archimedes. Following the crisis of incommensurability sparked by Hippasus, Greek geometry was paralyzed because existing proofs relied on integer ratios that failed for irrational lengths.
                        </p>
                        <p style="color: #334155; line-height: 1.65; font-size: 0.96rem; margin-bottom: 0.5rem;">
                            <strong>The Theory of Proportions:</strong> Preserved in Book V of Euclid's <em><a href="https://en.wikipedia.org/wiki/Euclid%27s_Elements" target="_blank" rel="noopener noreferrer" style="color: #4f46e5; font-style: italic; text-decoration: underline;">Elements</a></em>, Eudoxus formulated a rigorous definition of proportion that applied equally to rational and incommensurable magnitudes. Crucially, he established what we now know as the <strong>Archimedean Property</strong>: any two positive quantities can exceed one another if either is added to itself a sufficient number of times.
                        </p>
                        <p style="color: #334155; line-height: 1.65; font-size: 0.96rem; margin-bottom: 0;">
                            In modern analysis, this guarantees that the real line contains no non-zero "infinitely small" ghosts. No matter how small an interval $\epsilon > 0$ is chosen, taking enough discrete steps of size $\epsilon$ will inevitably outrun any finite number, establishing an essential bridge between discrete counting and continuous space.
                        </p>
                    </div>
                </div>
            </div>"""

WEIERSTRASS_BOX = r"""            <!-- HISTORICAL CONTEXT: WEIERSTRASS -->
            <div class="biography-box" style="margin-top: 2rem;">
                <h4>🏛️ The Architect of Rigor: Karl Weierstrass</h4>
                <div style="display: flex; gap: 1.5rem; align-items: flex-start; flex-wrap: wrap; margin-top: 0.75rem;">
                    <div style="flex: 0 0 135px; max-width: 135px;">
                        <img src="images/weierstrass.png" alt="Karl Weierstrass" style="width: 100%; height: auto; border-radius: 6px; border: 1px solid var(--border); box-shadow: 0 2px 4px rgba(0,0,0,0.06); display: block;">
                        <span style="display: block; font-size: 0.8rem; color: #64748b; text-align: center; margin-top: 0.4rem; line-height: 1.3;">Karl Weierstrass<br>(1815–1897)</span>
                    </div>
                    <div style="flex: 1; min-width: 260px;">
                        <p style="margin-top: 0; color: #334155; line-height: 1.65; font-size: 0.96rem;">
                            <strong><a href="https://en.wikipedia.org/wiki/Karl_Weierstrass" target="_blank" rel="noopener noreferrer" style="color: #4f46e5; text-decoration: underline;">Karl Weierstrass</a></strong> was a German mathematician universally regarded as the "father of modern analysis." For the first two centuries following Newton and Leibniz, calculus relied heavily on physical intuition, moving particles, and geometric graphs—descriptions that frequently collapsed when dealing with pathological curves.
                        </p>
                        <p style="color: #334155; line-height: 1.65; font-size: 0.96rem; margin-bottom: 0.5rem;">
                            <strong>Absolute Value as a Metric:</strong> Weierstrass realized that rigorous analysis required eliminating vague kinematic phrases like <em>"approaches"</em> or <em>"gets infinitely close."</em> He replaced them with static, algebraic inequalities centered entirely on the <strong>absolute value function</strong> $|x - y|$.
                        </p>
                        <p style="color: #334155; line-height: 1.65; font-size: 0.96rem; margin-bottom: 0;">
                            By defining closeness through exact distance bounds ($|f(x) - L| < \epsilon$ whenever $|x - c| < \delta$), Weierstrass transformed the absolute value from a mere sign-stripping operation into the primary measuring tape of pure mathematics. Properties like the <strong>Triangle Inequality</strong> became the workhorses that prove whether sequences converge and functions stay continuous.
                        </p>
                    </div>
                </div>
            </div>"""

DEDEKIND_BOX = r"""            <!-- HISTORICAL CONTEXT: DEDEKIND -->
            <div class="biography-box" style="margin-top: 2rem;">
                <h4>🏛️ Slicing the Continuum: Richard Dedekind</h4>
                <div style="display: flex; gap: 1.5rem; align-items: flex-start; flex-wrap: wrap; margin-top: 0.75rem;">
                    <div style="flex: 0 0 135px; max-width: 135px;">
                        <img src="images/dedekind.jpg" alt="Richard Dedekind" style="width: 100%; height: auto; border-radius: 6px; border: 1px solid var(--border); box-shadow: 0 2px 4px rgba(0,0,0,0.06); display: block;">
                        <span style="display: block; font-size: 0.8rem; color: #64748b; text-align: center; margin-top: 0.4rem; line-height: 1.3;">Richard Dedekind<br>(1831–1916)</span>
                    </div>
                    <div style="flex: 1; min-width: 260px;">
                        <p style="margin-top: 0; color: #334155; line-height: 1.65; font-size: 0.96rem;">
                            <strong><a href="https://en.wikipedia.org/wiki/Richard_Dedekind" target="_blank" rel="noopener noreferrer" style="color: #4f46e5; text-decoration: underline;">Richard Dedekind</a></strong> was a German mathematician who made foundational contributions to abstract algebra and number theory. In 1858, while preparing lecture notes for an introductory calculus class at the Polytechnic in Zürich, he was deeply troubled to discover that while textbooks spoke constantly of the "continuous real line," mathematics possessed no rigorous definition of what continuity actually meant.
                        </p>
                        <p style="color: #334155; line-height: 1.65; font-size: 0.96rem; margin-bottom: 0.5rem;">
                            <strong>Dedekind Cuts:</strong> In his landmark 1872 treatise <em><a href="https://en.wikipedia.org/wiki/Dedekind_cut" target="_blank" rel="noopener noreferrer" style="color: #4f46e5; font-style: italic; text-decoration: underline;">Stetigkeit und irrationale Zahlen</a></em> (Continuity and Irrational Numbers), Dedekind asked: <em>What is the fundamental property of a line that has no gaps?</em> His insight was that any knife cut dividing the real numbers into left and right halves must pass through an exact boundary point.
                        </p>
                        <p style="color: #334155; line-height: 1.65; font-size: 0.96rem; margin-bottom: 0;">
                            When slicing the rational numbers $\mathbb{Q}$ at $\sqrt{2}$, however, the knife passes through nothing: the left set has no maximum, and the right set has no minimum. Dedekind showed that by defining irrational numbers as the <em>cuts themselves</em>, we fill every microscopic pinprick hole in $\mathbb{Q}$, guaranteeing that every bounded set has a supremum and completing the continuum $\mathbb{R}$.
                        </p>
                    </div>
                </div>
            </div>"""

def run_git_command(args: list[str]) -> subprocess.CompletedProcess:
    res = subprocess.run(args, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Git execution error: {' '.join(args)}", file=sys.stderr)
        print(res.stderr.strip(), file=sys.stderr)
        sys.exit(res.returncode)
    return res

def main() -> None:
    if not TARGET_HTML.exists():
        print(f"Error: {TARGET_HTML} does not exist.", file=sys.stderr)
        sys.exit(1)

    content = TARGET_HTML.read_text(encoding="utf-8")
    original = content

    # Clean out any previously injected bio boxes if present to update cleanly
    import re
    content = re.sub(
        r'<!-- HISTORICAL CONTEXT: HIPPASUS -->.*?</div>\s*</div>\s*</div>',
        '',
        content,
        flags=re.DOTALL
    )
    content = re.sub(
        r'<!-- HISTORICAL CONTEXT: EUDOXUS -->.*?</div>\s*</div>\s*</div>',
        '',
        content,
        flags=re.DOTALL
    )
    content = re.sub(
        r'<!-- HISTORICAL CONTEXT: WEIERSTRASS -->.*?</div>\s*</div>\s*</div>',
        '',
        content,
        flags=re.DOTALL
    )
    content = re.sub(
        r'<!-- HISTORICAL CONTEXT: DEDEKIND -->.*?</div>\s*</div>\s*</div>',
        '',
        content,
        flags=re.DOTALL
    )

    # 1. Section 2: Insert Hippasus above Section 3
    if '<h2 id="field-order">' in content:
        content = content.replace(
            '<h2 id="field-order">',
            f"{HIPPASUS_BOX}\n\n            <h2 id=\"field-order\">"
        )

    # 2. Section 3: Insert Eudoxus above Section 4
    if '<h2 id="absolute-value">' in content:
        content = content.replace(
            '<h2 id="absolute-value">',
            f"{EUDOXUS_BOX}\n\n            <h2 id=\"absolute-value\">"
        )

    # 3. Section 4: Insert Weierstrass above Section 5
    if '<h2 id="completeness-bounds">' in content:
        content = content.replace(
            '<h2 id="completeness-bounds">',
            f"{WEIERSTRASS_BOX}\n\n            <h2 id=\"completeness-bounds\">"
        )

    # 4. Section 5: Insert Dedekind before Footer Navigation
    if '<!-- FOOTER NAVIGATION -->' in content:
        content = content.replace(
            '<!-- FOOTER NAVIGATION -->',
            f"{DEDEKIND_BOX}\n\n            <!-- FOOTER NAVIGATION -->"
        )

    if content != original:
        TARGET_HTML.write_text(content, encoding="utf-8")
        print(f"Updated biography boxes in {TARGET_HTML.name}.")
    else:
        print(f"{TARGET_HTML.name} content is unchanged.")

    # Git workflow: stage both week1-lecture2.html and update.py
    run_git_command(["git", "rev-parse", "--is-inside-work-tree"])
    run_git_command(["git", "add", str(TARGET_HTML), str(SCRIPT_FILE)])

    diff_check = subprocess.run(["git", "diff", "--cached", "--quiet"])
    if diff_check.returncode == 0:
        print("No staged changes. Working tree is clean.")
        return

    commit_subject = "Align Lecture 2 bio box format and fix asset paths"
    commit_body = (
        "Standardize biography card styling and Wikipedia reference links\n"
        "to match Lecture 1, correct Hippasus image extension to .png, use\n"
        "raw string literals for KaTeX formulas, and stage update.py."
    )
    full_message = f"{commit_subject}\n\n{commit_body}"

    run_git_command(["git", "commit", "-m", full_message])
    print("Committed successfully.")

    print("Pushing to remote repository...")
    run_git_command(["git", "push"])
    print("Push complete.")

if __name__ == "__main__":
    main()
