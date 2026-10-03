#!/usr/bin/env python3
import os
import subprocess

def expand_limits_and_supremum():
    filepath = 'week2.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The expanded Section 3 content block
    new_section_3 = r'''            <!-- SECTION 3 -->
            <h2 id="section-supremum">3. Limits and Supremum (Monotone Convergence)</h2>
            <p>While the formal $\epsilon\text{-}N$ definition lets us <em>verify</em> a limit when we already know it, how do we prove a limit exists for a sequence defined recursively or implicitly where the exact value is unknown? The answer lies in the profound link between sequence order and the <strong>Completeness Axiom</strong> of the real numbers.</p>

            <div class="definition-box">
                <p><strong>Definition: Monotonicity</strong></p>
                <ul style="margin: 0.5rem 0 0.5rem 1.25rem; padding: 0;">
                    <li style="margin-bottom: 0.3rem;">A sequence $(a_n)$ is <strong>non-decreasing</strong> (increasing) if $a_n \le a_{n+1}$ for all $n \ge 1$.</li>
                    <li style="margin-bottom: 0.3rem;">A sequence $(a_n)$ is <strong>non-increasing</strong> (decreasing) if $a_n \ge a_{n+1}$ for all $n \ge 1$.</li>
                    <li>A sequence is <strong>monotonic</strong> if it is either non-decreasing or non-increasing.</li>
                </ul>
            </div>

            <div class="infobox" style="margin-top: 1.5rem;">
                <h4>📈 Theorem 2: The Monotone Convergence Theorem (MCT)</h4>
                <div class="infobox-intro">
                    One of the foundational pillars of real analysis: Every bounded monotonic sequence converges.
                </div>
                <div style="display: flex; flex-direction: column; gap: 0.75rem; font-size: 0.95rem;">
                    <div style="padding-bottom: 0.5rem; border-bottom: 1px solid #e2e8f0;">
                        <strong>1. Non-Decreasing Case:</strong> If $(a_n)$ is non-decreasing and <em>bounded above</em> (i.e., $a_n \le M$ for some real number $M$), then $(a_n)$ converges, and:
                        <p style="text-align: center; margin: 0.5rem 0;">$$\lim_{n\to\infty} a_n = \sup \{a_n : n \in \mathbb{N}\}$$</p>
                    </div>
                    <div>
                        <strong>2. Non-Increasing Case:</strong> If $(a_n)$ is non-increasing and <em>bounded below</em> (i.e., $a_n \ge m$ for some real number $m$), then $(a_n)$ converges, and:
                        <p style="text-align: center; margin: 0.5rem 0;">$$\lim_{n\to\infty} a_n = \inf \{a_n : n \in \mathbb{N}\}$$</p>
                    </div>
                </div>
            </div>

            <div class="aside-box" style="margin-top: 1.5rem;">
                <h4>💡 Why Does This Matter? (The Completeness of $\mathbb{R}$)</h4>
                <p>The Monotone Convergence Theorem is not true in the rational numbers ($\mathbb{Q}$). For example, consider the sequence of rational decimal approximations for $\sqrt{2}$ ($1, 1.4, 1.41, 1.414, \dots$). This sequence is non-decreasing and bounded above by $2$, but it <strong>does not converge within $\mathbb{Q}$</strong> because its limit ($\sqrt{2}$) is irrational. The MCT relies entirely on the fact that $\mathbb{R}$ has no "gaps" (satisfying the Least Upper Bound Property).</p>
            </div>

            <div class="aside-box" style="margin-top: 1.5rem;">
                <h4>🎯 Example: Evaluating a Bounded Monotone Limit</h4>
                <p>Consider the sequence $a_n = 1 - \frac{1}{n}$ for $n \ge 1$. Let's check its properties:</p>
                <ol style="margin: 0.5rem 0 0.5rem 1.25rem; padding: 0;">
                    <li style="margin-bottom: 0.4rem;"><strong>Monotonicity:</strong> $a_{n+1} - a_n = \left(1 - \frac{1}{n+1}\right) - \left(1 - \frac{1}{n}\right) = \frac{1}{n} - \frac{1}{n+1} > 0$, so the sequence is strictly increasing.</li>
                    <li style="margin-bottom: 0.4rem;"><strong>Boundedness:</strong> Every term satisfies $0 \le a_n < 1$, so it is bounded above by $M = 1$.</li>
                    <li style="margin-bottom: 0.4rem;"><strong>Conclusion:</strong> By the Monotone Convergence Theorem, the limit exists and equals its supremum: $\lim_{n\to\infty} \left(1 - \frac{1}{n}\right) = \sup\left\{1 - \frac{1}{n}\right\} = 1$.</li>
                </ol>
            </div>'''

    # Section 3 anchor to replace
    old_section_3_marker = '<!-- SECTION 3 -->'
    old_section_4_marker = '<!-- SECTION 4 -->'

    if old_section_3_marker in content and old_section_4_marker in content:
        parts = content.split('<!-- SECTION 3 -->')
        header_part = parts[0]
        rest_part = parts[1].split('<!-- SECTION 4 -->')[1]

        updated_content = header_part + new_section_3 + '\n\n            <!-- SECTION 4 -->' + rest_part
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print("Successfully expanded Section 3 in week2.html.")
    else:
        print("Section 3/4 anchors not found in week2.html.")

def execute_git_sync():
    commit_message = (
        "Expand and update Section 3: Limits and Supremum in week2.html\n\n"
        "Added the Monotone Convergence Theorem, formal supremum definitions, and\n"
        "real number completeness insights to week2.html."
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
    expand_limits_and_supremum()
    execute_git_sync()
