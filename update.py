#!/usr/bin/env python3
r"""
update.py

Inserts historical portrait callout boxes for Brook Taylor (Section 6) and
Carl Friedrich Gauss (Section 7) into week1-lecture3.html, integrating
images/taylor.jpg and images/gauss.jpg.

Stages week1-lecture3.html and update.py, commits, and pushes upstream.
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

    # 1. Taylor Injection into Section 6
    taylor_box = r"""
            <!-- HISTORICAL PROFILE: BROOK TAYLOR -->
            <div style="background: #f8fafc; border: 1px solid var(--border); border-left: 5px solid #0284c7; border-radius: 6px; padding: 1.25rem 1.5rem; margin: 1.5rem 0; display: flex; flex-wrap: wrap; gap: 1.25rem; align-items: center;">
                <div style="flex: 0 0 110px; text-align: center;">
                    <img src="images/taylor.jpg" alt="Brook Taylor" style="width: 100px; height: 100px; object-fit: cover; border-radius: 50%; border: 2px solid var(--border); display: block; margin: 0 auto 0.4rem auto;">
                    <span style="font-size: 0.78rem; font-weight: 700; color: #0284c7;">Brook Taylor</span>
                    <span style="font-size: 0.72rem; color: #64748b; display: block;">(1685–1731)</span>
                </div>
                <div style="flex: 1; min-width: 240px;">
                    <h4 style="margin: 0 0 0.5rem 0; color: #0f172a; font-size: 1rem;">Historical Insight: The Calculus of Finite Differences</h4>
                    <p style="margin: 0; font-size: 0.93rem; line-height: 1.65; color: #334155;">
                        While Brook Taylor is famously remembered today for continuous polynomial expansions, his seminal 1715 work <em>Methodus Incrementorum Directa et Inversa</em> was entirely focused on finite differences and discrete sequences. Taylor treated the difference operator <span class="nobr">$\Delta a_n = a_{n+1} - a_n$</span> as the primary foundation of mathematics, viewing continuous calculus as merely a smooth limiting case of discrete step-by-step arithmetic.
                    </p>
                </div>
            </div>
"""

    if "images/taylor.jpg" not in content:
        target_s6 = '<h2 id="derived-sequences">'
        idx_s6 = content.find(target_s6)
        if idx_s6 != -1:
            end_s6 = content.find("</h2>", idx_s6)
            if end_s6 != -1:
                insertion_pos = end_s6 + len("</h2>")
                content = content[:insertion_pos] + taylor_box + content[insertion_pos:]

    # 2. Gauss Injection into Section 7
    gauss_box = r"""
            <!-- HISTORICAL PROFILE: CARL FRIEDRICH GAUSS -->
            <div style="background: #f8fafc; border: 1px solid var(--border); border-left: 5px solid #10b981; border-radius: 6px; padding: 1.25rem 1.5rem; margin: 1.5rem 0; display: flex; flex-wrap: wrap; gap: 1.25rem; align-items: center;">
                <div style="flex: 0 0 110px; text-align: center;">
                    <img src="images/gauss.jpg" alt="Carl Friedrich Gauss" style="width: 100px; height: 100px; object-fit: cover; border-radius: 50%; border: 2px solid var(--border); display: block; margin: 0 auto 0.4rem auto;">
                    <span style="font-size: 0.78rem; font-weight: 700; color: #047857;">Carl Friedrich Gauss</span>
                    <span style="font-size: 0.72rem; color: #64748b; display: block;">(1777–1855)</span>
                </div>
                <div style="flex: 1; min-width: 240px;">
                    <h4 style="margin: 0 0 0.5rem 0; color: #0f172a; font-size: 1rem;">Historical Insight: The Prince of Mathematicians at School</h4>
                    <p style="margin: 0; font-size: 0.93rem; line-height: 1.65; color: #334155;">
                        As the legend goes, when young Gauss was roughly nine years old, his schoolteacher tried to keep the class busy by asking them to sum all integers from 1 to 100. To the teacher's astonishment, Gauss wrote the correct answer down almost instantly by pairing opposite ends (<span class="nobr">$1 + 100$,</span> <span class="nobr">$2 + 99$,</span> etc.). Our telescoping proof reveals the underlying calculus mechanism: summing integers is simply the discrete anti-difference of quadratic polynomials!
                    </p>
                </div>
            </div>
"""

    if "images/gauss.jpg" not in content:
        target_s7 = '<h2 id="discrete-integration">'
        idx_s7 = content.find(target_s7)
        if idx_s7 != -1:
            end_s7 = content.find("</h2>", idx_s7)
            if end_s7 != -1:
                insertion_pos = end_s7 + len("</h2>")
                content = content[:insertion_pos] + gauss_box + content[insertion_pos:]

    if content != original:
        TARGET_HTML.write_text(content, encoding="utf-8")
        print(f"Successfully embedded Taylor and Gauss profiles into {TARGET_HTML.name}.")

    execute_git(["git", "add", str(TARGET_HTML), str(SCRIPT_FILE)])

    diff_check = subprocess.run(["git", "diff", "--cached", "--quiet"])
    if diff_check.returncode == 0:
        print("No staged changes detected. Working tree clean.")
        return

    commit_subject = "Add historical profile callout boxes for Taylor and Gauss"
    commit_body = (
        "Embed Brook Taylor profile and portrait in Section 6 to highlight\n"
        "finite differences, and add Carl Friedrich Gauss profile and portrait\n"
        "in Section 7 to connect the legendary 100-integer summation anecdote\n"
        "with underlying telescoping mechanics.\n"
        "Stage and commit updated week1-lecture3.html alongside update.py."
    )
    full_message = f"{commit_subject}\n\n{commit_body}"

    execute_git(["git", "commit", "-m", full_message])
    print("Committed successfully.")

    print("Pushing to remote repository...")
    execute_git(["git", "push"])
    print("Push complete.")

if __name__ == "__main__":
    main()
