#!/usr/bin/env python3
import os
import subprocess

def reposition_mct_example():
    filepath = 'week2.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    mct_example = r'''            <div class="aside-box" style="margin-top: 1.5rem;">
                <h4>🎯 Worked Example: Applying the Monotone Convergence Theorem</h4>
                <p>Consider the sequence defined recursively by $x_1 = 1$ and $x_{n+1} = \frac{1}{3}x_n + 1$ for $n \ge 1$. Let's prove its convergence using the Monotone Convergence Theorem:</p>
                <ol style="margin: 0.5rem 0 0.5rem 1.25rem; padding: 0;">
                    <li style="margin-bottom: 0.5rem;"><strong>Step 1: Prove Boundedness Above.</strong>
                        We show by induction that $x_n < \frac{3}{2}$ for all $n$.<br>
                        <em>Base Case ($n=1$):</em> $x_1 = 1 < \frac{3}{2}$ (true).<br>
                        <em>Inductive Step:</em> Assume $x_k < \frac{3}{2}$. Then:
                        $$x_{k+1} = \frac{1}{3}x_k + 1 < \frac{1}{3}\left(\frac{3}{2}\right) + 1 = \frac{1}{2} + 1 = \frac{3}{2}$$
                        Thus, the sequence is bounded above by $M = \frac{3}{2}$.
                    </li>
                    <li style="margin-bottom: 0.5rem;"><strong>Step 2: Prove Monotonicity (Increasing).</strong>
                        We show that $x_{n+1} \ge x_n$. Let's examine $x_{n+1} - x_n$:
                        $$x_{n+1} - x_n = \left(\frac{1}{3}x_n + 1\right) - x_n = 1 - \frac{2}{3}x_n = \frac{2}{3}\left(\frac{3}{2} - x_n\right)$$
                        Since we proved in Step 1 that $x_n < \frac{3}{2}$, the term $\left(\frac{3}{2} - x_n\right)$ is always positive. Therefore, $x_{n+1} - x_n > 0$, confirming the sequence is strictly increasing.
                    </li>
                    <li style="margin-bottom: 0.5rem;"><strong>Step 3: Invoke the MCT.</strong>
                        Because $(x_n)$ is non-decreasing (increasing) and bounded above, the <strong>Monotone Convergence Theorem</strong> guarantees that $\lim_{n\to\infty} x_n = L$ exists as a finite real number.
                    </li>
                    <li><strong>Step 4: Evaluate the Limit Algebraically.</strong>
                        Now that existence is guaranteed, we take the limit on both sides of $x_{n+1} = \frac{1}{3}x_n + 1$:
                        $$L = \frac{1}{3}L + 1 \implies \frac{2}{3}L = 1 \implies L = \frac{3}{2}$$
                        Thus, the exact limit is <strong>$L = \frac{3}{2}$</strong> (which matches our least upper bound / supremum).
                    </li>
                </ol>
            </div>'''

    # Cleanly remove the block from wherever it currently is
    content = content.replace(mct_example, '')

    # Target anchor: right after the first example "Example: Evaluating a Bounded Monotone Limit"
    target = r'''            <div class="aside-box" style="margin-top: 1.5rem;">
                <h4>🎯 Example: Evaluating a Bounded Monotone Limit</h4>
                <p>Consider the sequence $a_n = 1 - \frac{1}{n}$ for $n \ge 1$. Let's check its properties:</p>
                <ol style="margin: 0.5rem 0 0.5rem 1.25rem; padding: 0;">
                    <li style="margin-bottom: 0.4rem;"><strong>Monotonicity:</strong> $a_{n+1} - a_n = \left(1 - \frac{1}{n+1}\right) - \left(1 - \frac{1}{n}\right) = \frac{1}{n} - \frac{1}{n+1} > 0$, so the sequence is strictly increasing.</li>
                    <li style="margin-bottom: 0.4rem;"><strong>Boundedness:</strong> Every term satisfies $0 \le a_n < 1$, so it is bounded above by $M = 1$.</li>
                    <li style="margin-bottom: 0.4rem;"><strong>Conclusion:</strong> By the Monotone Convergence Theorem, the limit exists and equals its supremum: $\lim_{n\to\infty} \left(1 - \frac{1}{n}\right) = \sup\left\{1 - \frac{1}{n}\right\} = 1$.</li>
                </ol>
            </div>'''

    replacement = target + '\n\n' + mct_example

    if target in content:
        content = content.replace(target, replacement, 1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully repositioned MCT worked example in week2.html.")
    else:
        print("Target example block not found.")

def execute_git_sync():
    commit_message = (
        "Reposition Monotone Convergence Theorem worked example in week2.html\n\n"
        "Moved the MCT worked example block to sit directly beneath the bounded\n"
        "monotone limit example in Section 3 of week2.html."
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
    reposition_mct_example()
    execute_git_sync()
