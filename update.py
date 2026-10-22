#!/usr/bin/env python3
"""Add a historical infobox for Bernoulli and Euler, then commit and push."""

import subprocess
import sys

COMMIT_MESSAGE = """Content: Add biography infobox for Bernoulli and Euler

Update week2-lecture5.html to include a two-column biography infobox
featuring Jacob Bernoulli and Leonhard Euler directly beneath the
historical narrative in Section 2. Uses the existing .biography-box
CSS class for styling and a responsive grid layout to display the
provided image assets alongside their historical contributions to
the constant 'e'.
"""

OLD_TARGET = r"""                <p style="color: #334155; line-height: 1.75; font-size: 1.05rem; margin-bottom: 0;">
                    Euler didn't just find a number; he proved that $e$ represents the fundamental rate of growth for all natural continuous processes. By proving that it can be defined as the infinite limit of $\left(1 + \frac{1}{n}\right)^n$, Euler hardwired $e$ into the very foundations of calculus, physics, and probability. Today, we are going to reconstruct his exact proof to show that this sequence safely converges.
                </p>
            </div>

            <div style="margin: 2.5rem 0; padding: 2rem; background: #ffffff; border: 1px solid #cbd5e1; border-radius: 8px;">"""

NEW_TARGET = r"""                <p style="color: #334155; line-height: 1.75; font-size: 1.05rem; margin-bottom: 0;">
                    Euler didn't just find a number; he proved that $e$ represents the fundamental rate of growth for all natural continuous processes. By proving that it can be defined as the infinite limit of $\left(1 + \frac{1}{n}\right)^n$, Euler hardwired $e$ into the very foundations of calculus, physics, and probability. Today, we are going to reconstruct his exact proof to show that this sequence safely converges.
                </p>
            </div>

            <div class="biography-box" style="margin-top: 1.5rem; margin-bottom: 3rem;">
                <h4>🏛️ The Architects of $e$</h4>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.75rem; margin-top: 1.25rem;">
                    <!-- Bernoulli -->
                    <div style="display: flex; gap: 1.25rem; align-items: flex-start;">
                        <img src="image/bernoulli.jpg" alt="Jacob Bernoulli" style="width: 75px; height: 75px; border-radius: 50%; object-fit: cover; border: 2px solid #ddd6fe; flex-shrink: 0; background: #ffffff;">
                        <div>
                            <strong style="color: #3730a3; display: block; font-size: 1.05rem;">Jacob Bernoulli (1655–1705)</strong>
                            <p style="margin: 0.25rem 0 0 0; font-size: 0.9rem; line-height: 1.6; color: #1e293b;">
                                Discovered the constant in 1683 while calculating continuous compound interest. He realized that as compounding intervals approach infinity, the return hits a strict mathematical ceiling—the very first approximation of $e$.
                            </p>
                        </div>
                    </div>
                    <!-- Euler -->
                    <div style="display: flex; gap: 1.25rem; align-items: flex-start;">
                        <img src="image/euler.jpg" alt="Leonhard Euler" style="width: 75px; height: 75px; border-radius: 50%; object-fit: cover; border: 2px solid #ddd6fe; flex-shrink: 0; background: #ffffff;">
                        <div>
                            <strong style="color: #3730a3; display: block; font-size: 1.05rem;">Leonhard Euler (1707–1783)</strong>
                            <p style="margin: 0.25rem 0 0 0; font-size: 0.9rem; line-height: 1.6; color: #1e293b;">
                                Standardized the symbol $e$ in 1727. He seamlessly integrated the constant into the core of mathematics, proving its irrationality and formulating the famous Euler's Identity ($e^{i\pi} + 1 = 0$).
                            </p>
                        </div>
                    </div>
                </div>
            </div>

            <div style="margin: 2.5rem 0; padding: 2rem; background: #ffffff; border: 1px solid #cbd5e1; border-radius: 8px;">"""

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

    if OLD_TARGET in content:
        content = content.replace(OLD_TARGET, NEW_TARGET)
        print(f"Successfully injected the Bernoulli & Euler infobox.")
    else:
        print(f"Warning: Could not find target injection site. Check if the file was modified.", file=sys.stderr)
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

    print("\n✅ Infobox added, committed, and pushed!")

if __name__ == "__main__":
    apply_patch()
