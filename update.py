#!/usr/bin/env python3
r"""
update.py

Inserts comprehensive historical profile boxes for Brook Taylor (Section 6)
and Carl Friedrich Gauss (Section 7) into week1-lecture3.html.
Uses structured sections (Background, Key Contributions, Vignette) and
standard rectangular portrait formatting.
"""

from pathlib import Path
import subprocess
import sys

TARGET_HTML = Path("week1-lecture3.html")
SCRIPT_FILE = Path(__file__).resolve()

def execute_git(args: list[str]) -> subprocess.CompletedProcess:
    res = subprocess.run(args, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Git execution error: {' '.join(args)}", file=sys.stderr)
        print(res.stderr.strip(), file=sys.stderr)
        sys.exit(res.returncode)
    return res

def main() -> None:
    if not TARGET_HTML.exists():
        print(f"Error: {TARGET_HTML} not found in workspace.", file=sys.stderr)
        sys.exit(1)

    content = TARGET_HTML.read_text(encoding="utf-8")
    original = content

    # 1. Brook Taylor Card (Section 6)
    taylor_box = r"""
            <!-- HISTORICAL PROFILE: BROOK TAYLOR -->
            <div class="infobox" style="background: #f8fafc; border: 1px solid var(--border); border-left: 5px solid #0284c7; border-radius: 6px; padding: 1.5rem; margin: 1.75rem 0;">
                <div style="display: flex; flex-direction: row; gap: 1.5rem; align-items: flex-start; flex-wrap: wrap;">
                    <div style="flex: 0 0 130px; text-align: center;">
                        <img src="images/taylor.jpg" alt="Brook Taylor portrait" style="width: 130px; height: auto; border-radius: 6px; border: 1px solid var(--border); box-shadow: 0 2px 4px rgba(0,0,0,0.05); display: block; margin-bottom: 0.5rem;">
                        <span style="font-weight: 700; font-size: 0.85rem; color: #0f172a; display: block;">Brook Taylor</span>
                        <span style="font-size: 0.75rem; color: #64748b;">(1685–1731)</span>
                    </div>
                    <div style="flex: 1; min-width: 260px;">
                        <h4 style="margin-top: 0; margin-bottom: 0.5rem; color: #0284c7; font-size: 1.05rem;">
                            Historical Profile: The Pioneer of Finite Differences
                        </h4>
                        <p style="font-size: 0.92rem; line-height: 1.65; color: #334155; margin-bottom: 0.75rem;">
                            <strong>Background:</strong> An English mathematician and Secretary of the Royal Society, Brook Taylor worked in the turbulent aftermath of the Newton-Leibniz calculus dispute. Rather than treating calculus solely as smooth tangents and infinitesimals, Taylor approached change through discrete increments.
                        </p>
                        <p style="font-size: 0.92rem; line-height: 1.65; color: #334155; margin-bottom: 0.75rem;">
                            <strong>Key Contributions:</strong>
                        </p>
                        <ul style="font-size: 0.9rem; line-height: 1.6; color: #334155; margin: 0 0 0.75rem 1.25rem; padding: 0;">
                            <li>Published <em>Methodus Incrementorum Directa et Inversa</em> (1715), formally inaugurating the <strong>calculus of finite differences</strong>.</li>
                            <li>Formulated Taylor's Theorem as the natural limiting case when discrete step sizes <span class="nobr">$\Delta x$</span> approach zero.</li>
                            <li>Pioneered the mathematical study of vibrating strings and linear perspective in projective geometry.</li>
                        </ul>
                        <div style="background: #ffffff; border: 1px solid var(--border); border-radius: 6px; padding: 0.75rem 1rem;">
                            <strong style="color: #0f172a; font-size: 0.88rem;">Vignette — Discrete Foundations First:</strong>
                            <p style="margin: 0.25rem 0 0 0; font-size: 0.88rem; line-height: 1.55; color: #475569;">
                                While calculus textbooks today treat Taylor series as high-level continuous machinery, Taylor arrived at them by subtracting discrete numbers in sequence tables. He viewed the continuous derivative not as a mysterious standalone object, but as the shadow cast by sequential steps when the gaps become imperceptible.
                            </p>
                        </div>
                    </div>
                </div>
            </div>
"""

    # 2. Carl Friedrich Gauss Card (Section 7)
    gauss_box = r"""
            <!-- HISTORICAL PROFILE: CARL FRIEDRICH GAUSS -->
            <div class="infobox" style="background: #f8fafc; border: 1px solid var(--border); border-left: 5px solid #10b981; border-radius: 6px; padding: 1.5rem; margin: 1.75rem 0;">
                <div style="display: flex; flex-direction: row; gap: 1.5rem; align-items: flex-start; flex-wrap: wrap;">
                    <div style="flex: 0 0 130px; text-align: center;">
                        <img src="images/gauss.jpg" alt="Carl Friedrich Gauss portrait" style="width: 130px; height: auto; border-radius: 6px; border: 1px solid var(--border); box-shadow: 0 2px 4px rgba(0,0,0,0.05); display: block; margin-bottom: 0.5rem;">
                        <span style="font-weight: 700; font-size: 0.85rem; color: #0f172a; display: block;">Carl Friedrich Gauss</span>
                        <span style="font-size: 0.75rem; color: #64748b;">(1777–1855)</span>
                    </div>
                    <div style="flex: 1; min-width: 260px;">
                        <h4 style="margin-top: 0; margin-bottom: 0.5rem; color: #047857; font-size: 1.05rem;">
                            Historical Profile: The Prince of Mathematicians
                        </h4>
                        <p style="font-size: 0.92rem; line-height: 1.65; color: #334155; margin-bottom: 0.75rem;">
                            <strong>Background:</strong> Widely regarded as the <em>Princeps mathematicorum</em>, Gauss was a German child prodigy who revolutionized number theory, differential geometry, geodesy, and astronomy. He served for decades as director of the Göttingen Observatory.
                        </p>
                        <p style="font-size: 0.92rem; line-height: 1.65; color: #334155; margin-bottom: 0.75rem;">
                            <strong>Key Contributions:</strong>
                        </p>
                        <ul style="font-size: 0.9rem; line-height: 1.6; color: #334155; margin: 0 0 0.75rem 1.25rem; padding: 0;">
                            <li>Published <em>Disquisitiones Arithmeticae</em> (1801) at age 21, establishing modern number theory and modular congruence notation.</li>
                            <li>Proved the Fundamental Theorem of Algebra and the construction of the regular 17-gon using only ruler and compass.</li>
                            <li>Formalized the Gaussian normal distribution and the method of least squares in planetary orbit determination.</li>
                        </ul>
                        <div style="background: #ffffff; border: 1px solid var(--border); border-radius: 6px; padding: 0.75rem 1rem;">
                            <strong style="color: #0f172a; font-size: 0.88rem;">Vignette — The 1 to 100 Classroom Sum:</strong>
                            <p style="margin: 0.25rem 0 0 0; font-size: 0.88rem; line-height: 1.55; color: #475569;">
                                In 1786, his Brunswick schoolmaster J.G. Büttner assigned the unruly class the chore of summing all integers from 1 to 100. While his classmates ground through tedious column addition, the nine-year-old Gauss laid his slate on the teacher's desk within seconds with the exact total: <span class="nobr"><strong>5050</strong>.</span> He recognized that pairing symmetrically from opposite ends (<span class="nobr">$1 + 100 = 101$,</span> <span class="nobr">$2 + 99 = 101$</span>) yields 50 identical pairs of 101.
                            </p>
                        </div>
                    </div>
                </div>
            </div>
"""

    # Replace or insert Taylor box in Section 6
    if "images/taylor.jpg" not in content:
        target_s6 = '<h2 id="derived-sequences">'
        idx_s6 = content.find(target_s6)
        if idx_s6 != -1:
            end_s6 = content.find("</h2>", idx_s6)
            if end_s6 != -1:
                pos_s6 = end_s6 + len("</h2>")
                content = content[:pos_s6] + taylor_box + content[pos_s6:]

    # Replace or insert Gauss box in Section 7
    if "images/gauss.jpg" not in content:
        target_s7 = '<h2 id="discrete-integration">'
        idx_s7 = content.find(target_s7)
        if idx_s7 != -1:
            end_s7 = content.find("</h2>", idx_s7)
            if end_s7 != -1:
                pos_s7 = end_s7 + len("</h2>")
                content = content[:pos_s7] + gauss_box + content[pos_s7:]

    if content != original:
        TARGET_HTML.write_text(content, encoding="utf-8")
        print(f"Updated historical profile cards in {TARGET_HTML.name}.")

    execute_git(["git", "add", str(TARGET_HTML), str(SCRIPT_FILE)])

    diff_check = subprocess.run(["git", "diff", "--cached", "--quiet"])
    if diff_check.returncode == 0:
        print("No staged changes detected. Working tree clean.")
        return

    commit_subject = "Add structured historical profile boxes for Taylor and Gauss"
    commit_body = (
        "Add rectangular portrait cards for Brook Taylor in Section 6 and\n"
        "Carl Friedrich Gauss in Section 7 of week1-lecture3.html.\n"
        "Structure biographical content into background, key contributions,\n"
        "and vignettes to match existing lecture profile formatting."
    )
    full_message = f"{commit_subject}\n\n{commit_body}"

    execute_git(["git", "commit", "-m", full_message])
    print("Committed successfully.")

    print("Pushing upstream...")
    execute_git(["git", "push"])
    print("Push complete.")

if __name__ == "__main__":
    main()
