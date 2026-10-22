#!/usr/bin/env python3
"""Fix broken LaTeX rendering in Bernoulli's biography text, then commit and push."""

import subprocess
import sys

COMMIT_MESSAGE = """Fix: Correct LaTeX formatting in Bernoulli biography text

Update week2-lecture5.html to fix broken math rendering in Jacob
Bernoulli's biographical text box by properly wrapping expressions
in KaTeX delimiters and fixing spacing.
"""

OLD_BIOGRAPHY_BLOCK = r"""                    <!-- Bernoulli -->
                    <div style="display: flex; flex-direction: column; gap: 1rem;">
                        <img src="images/bernoulli.jpg" alt="Jacob Bernoulli" style="width: 100%; height: 180px; object-fit: cover; border-radius: 6px; border: 1px solid #ddd6fe; background: #ffffff; box-shadow: 0 2px 4px rgba(0,0,0,0.04);">
                        <div>
                            <strong style="color: #3730a3; display: block; font-size: 1.1rem; margin-bottom: 0.35rem;">Jacob Bernoulli (1655–1705)</strong>
                            <p style="margin: 0; font-size: 0.93rem; line-height: 1.65; color: #1e293b;">
                                In 1683, Swiss mathematician Jacob Bernoulli stumbled upon the constant while studying a question concerning compound interest. He imagined a bank account paying 100% interest per year. If compounded annually, you double your money ($2.00).If compoundedsemiannually, youget(1 + \frac{1}{2})^2 = \$2.25. Bernoulli realized that even if compounded continuously (infinitely fast), the total return doesn't shoot off to infinity—it hits a strict, unyielding financial and mathematical ceiling: approximately $2.71828$. Though he couldn't evaluate it explicitly, he set the stage for its discovery.
                            </p>
                        </div>
                    </div>"""

NEW_BIOGRAPHY_BLOCK = r"""                    <!-- Bernoulli -->
                    <div style="display: flex; flex-direction: column; gap: 1rem;">
                        <img src="images/bernoulli.jpg" alt="Jacob Bernoulli" style="width: 100%; height: 180px; object-fit: cover; border-radius: 6px; border: 1px solid #ddd6fe; background: #ffffff; box-shadow: 0 2px 4px rgba(0,0,0,0.04);">
                        <div>
                            <strong style="color: #3730a3; display: block; font-size: 1.1rem; margin-bottom: 0.35rem;">Jacob Bernoulli (1655–1705)</strong>
                            <p style="margin: 0; font-size: 0.93rem; line-height: 1.65; color: #1e293b;">
                                In 1683, Swiss mathematician Jacob Bernoulli stumbled upon the constant while studying a question concerning compound interest. He imagined a bank account paying 100% interest per year. If compounded annually, you double your money ($\$2.00$). If compounded semiannually, you get $\left(1 + \frac{1}{2}\right)^2 = \$2.25$. Bernoulli realized that even if compounded continuously (infinitely fast), the total return doesn't shoot off to infinity—it hits a strict, unyielding financial and mathematical ceiling: approximately $2.71828$. Though he couldn't evaluate it explicitly, he set the stage for its discovery.
                            </p>
                        </div>
                    </div>"""

def run_git_command(cmd, **kwargs):
    try:
        result = subprocess.run(cmd, check=True, text=True, capture_output=True, **kwargs)
        print(f"[OK] {' '.join(cmd)}")
        return result
    except subprocess.CalledProcessError as e:
        print(f"\n[ERROR] Command failed: {' '.join(cmd)}", file=sys.stderr)
        print(f"Details:\n{e.stderr or e.stdout}", file=sys.stderr)
        sys.exit(1)

def apply_patch():
    target_file = "week2-lecture5.html"

    try:
        with open(target_file, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: {target_file} not found.")
        sys.exit(1)

    if OLD_BIOGRAPHY_BLOCK in content:
        content = content.replace(OLD_BIOGRAPHY_BLOCK, NEW_BIOGRAPHY_BLOCK)
        print("Successfully corrected Bernoulli's biography text.")
    else:
        print("Warning: Could not find exact Bernoulli text block to replace. Check if it was modified.", file=sys.stderr)
        sys.exit(1)

    with open(target_file, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"\nSaved changes to {target_file}.")

    print(f"Staging {target_file}...")
    run_git_command(['git', 'add', target_file])

    print("Committing changes...")
    run_git_command(['git', 'commit', '-F', '-'], input=COMMIT_MESSAGE)

    print("Pushing to remote repository...")
    run_git_command(['git', 'push'])

    print("\n✅ Fix applied, committed, and pushed!")

if __name__ == "__main__":
    apply_patch()
