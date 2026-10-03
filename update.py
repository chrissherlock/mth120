#!/usr/bin/env python3
import os
import subprocess

def expand_limit_theorems_section():
    filepath = 'week2.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The expanded Section 2 content block
    new_section_2 = r'''            <!-- SECTION 2 -->
            <h2 id="section-theorems">2. Limit Theorems &amp; Arithmetic</h2>
            <p>Computing limits directly from the formal $\epsilon\text{-}N$ definition for every new sequence can quickly become cumbersome. Instead, mathematicians build a toolkit of <strong>Limit Theorems</strong>—fundamental arithmetic rules and bounding principles that let us combine known limits to evaluate complex new ones instantly.</p>

            <div class="infobox">
                <h4>📐 Algebraic Limit Laws (Theorem 1)</h4>
                <div class="infobox-intro">
                    Suppose $(a_n)$ and $(b_n)$ are convergent sequences such that $\lim_{n\to\infty} a_n = K$ and $\lim_{n\to\infty} b_n = L$, and let $c \in \mathbb{R}$ be a constant. Then:
                </div>
                <div style="display: flex; flex-direction: column; gap: 0.75s; font-size: 0.95rem;">
                    <div style="display: grid; grid-template-columns: 200px 1fr; gap: 1rem; border-bottom: 1px solid #e2e8f0; padding-bottom: 0.5rem;">
                        <strong>1. Constant Rule:</strong> <span>If $a_n = c$ for all $n$, then $\lim_{n\to\infty} c = c$.</span>
                    </div>
                    <div style="display: grid; grid-template-columns: 200px 1fr; gap: 1rem; border-bottom: 1px solid #e2e8f0; padding-bottom: 0.5rem;">
                        <strong>2. Scalar Multiple:</strong> <span>$\lim_{n\to\infty} (c \cdot a_n) = c \cdot K$</span>
                    </div>
                    <div style="display: grid; grid-template-columns: 200px 1fr; gap: 1rem; border-bottom: 1px solid #e2e8f0; padding-bottom: 0.5rem;">
                        <strong>3. Sum / Difference:</strong> <span>$\lim_{n\to\infty} (a_n \pm b_n) = K \pm L$</span>
                    </div>
                    <div style="display: grid; grid-template-columns: 200px 1fr; gap: 1rem; border-bottom: 1px solid #e2e8f0; padding-bottom: 0.5rem;">
                        <strong>4. Product Rule:</strong> <span>$\lim_{n\to\infty} (a_n \cdot b_n) = K \cdot L$</span>
                    </div>
                    <div style="display: grid; grid-template-columns: 200px 1fr; gap: 1rem; border-bottom: 1px solid #e2e8f0; padding-bottom: 0.5rem;">
                        <strong>5. Quotient Rule:</strong> <span>$\lim_{n\to\infty} \left(\frac{a_n}{b_n}\right) = \frac{K}{L}$, provided that $L \neq 0$ and $b_n \neq 0$ for all $n$.</span>
                    </div>
                    <div style="display: grid; grid-template-columns: 200px 1fr; gap: 1rem;">
                        <strong>6. Power Rule:</strong> <span>$\lim_{n\to\infty} (a_n)^p = K^p$ (for real powers where terms remain defined).</span>
                    </div>
                </div>
            </div>

            <div class="aside-box" style="margin-top: 1.5rem;">
                <h4>💡 Intuition: Why Arithmetic Laws Work</h4>
                <p>These laws reflect a powerful principle: <strong>limits respect basic arithmetic operations</strong>. If sequence $A$ is zooming in on $K$ and sequence $B$ is zooming in on $L$, their sum, product, or ratio must naturally zoom in on $K+L$, $K \cdot L$, or $K/L$. The only exception is division by zero, which destroys the neighborhood structure around $L$.</p>
            </div>

            <h3 style="margin-top: 2rem;">The Squeeze Theorem (Sandwich Theorem)</h3>
            <p>Sometimes a sequence is too complex or oscillatory to evaluate directly, but it can be trapped between two simpler sequences that share the exact same limit. This is formalized by the <strong>Squeeze Theorem</strong>:</p>

            <div class="definition-box">
                <p>Let $(a_n)$, $(b_n)$, and $(c_n)$ be sequences such that $a_n \le b_n \le c_n$ for all $n \ge N_0$. If</p>
                <p style="text-align: center; margin: 0.75rem 0;">$$\lim_{n\to\infty} a_n = L \quad \text{and} \quad \lim_{n\to\infty} c_n = L$$</p>
                <p>then the middle sequence $(b_n)$ is forced to converge to the same limit:</p>
                <p style="text-align: center; margin-top: 0.75rem;">$$\lim_{n\to\infty} b_n = L$$</p>
            </div>

            <div class="aside-box" style="margin-top: 1.5rem;">
                <h4>🎯 Classic Example: Applying the Squeeze Theorem</h4>
                <p>Consider evaluating $\lim_{n\to\infty} \frac{\sin(n)}{n}$. Because sine oscillates between $-1$ and $1$, we know:</p>
                <p style="text-align: center; margin: 0.75rem 0;">$$-\frac{1}{n} \le \frac{\sin(n)}{n} \le \frac{1}{n}$$</p>
                <p>Since $\lim_{n\to\infty} \left(-\frac{1}{n}\right) = 0$ and $\lim_{n\to\infty} \left(\frac{1}{n}\right) = 0$, the Squeeze Theorem forces our middle sequence to also converge:</p>
                <p style="text-align: center; margin-top: 0.75rem;">$$\lim_{n\to\infty} \frac{\sin(n)}{n} = 0$$</p>
            </div>'''

    # Anchor to replace old Section 2 content
    old_section_2_start = '<!-- SECTION 2 -->'
    old_section_3_start = '<!-- SECTION 3 -->'

    if old_section_2_start in content and old_section_3_start in content:
        # Extract everything between section 2 and section 3 headers to replace it
        parts = content.split('<!-- SECTION 2 -->')
        header_part = parts[0]
        rest_part = parts[1].split('<!-- SECTION 3 -->')[1]

        updated_content = header_part + new_section_2 + '\n\n            <!-- SECTION 3 -->' + rest_part
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print("Successfully expanded Section 2 in week2.html.")
    else:
        print("Section anchors not found in week2.html.")

def execute_git_sync():
    commit_message = (
        "Expand and update Section 2: Limit Theorems & Arithmetic in week2.html\n\n"
        "Added comprehensive algebraic limit laws, formal statements, proofs/intuition\n"
        "for the Squeeze Theorem, and structured infoboxes for week2.html."
    )
    commands = [
        ['git', 'add', 'week2.html', 'update.py'],
        ['git', 'commit', '-m', commit_message],
        ['git', 'push', 'origin', 'main']
    ]
    for cmd in commands:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(f"> {' '.join(cmd)}\n{result.stdout}{result.stderr}")

if __name__ == '__main__':
    expand_limit_theorems_section()
    execute_git_sync()
