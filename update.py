#!/usr/bin/env python3
import os
import subprocess

def update_recursion_subsection():
    filepath = 'week2.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The new subsection to insert into Section 3
    recursion_markup = r'''            <h3 style="margin-top: 2rem;">Evaluating Recursively Defined Sequences</h3>
            <p>When a sequence is given by a recurrence relation (e.g., $x_{n+1} = f(x_n)$) rather than an explicit formula, we cannot calculate its limit directly at first glance. Instead, we use a powerful <strong>4-step strategy</strong> combining induction and the Monotone Convergence Theorem:</p>

            <div class="infobox">
                <h4>🛠️ The 4-Step Strategy for Recursive Sequences</h4>
                <ol style="margin: 0.5rem 0 0.5rem 1.25rem; padding: 0;">
                    <li style="margin-bottom: 0.5rem;"><strong>Step 1: Prove Boundedness.</strong> Use mathematical induction to show that all terms remain bounded above or below by a constant $M$.</li>
                    <li style="margin-bottom: 0.5rem;"><strong>Step 2: Prove Monotonicity.</strong> Show that $x_{n+1} \ge x_n$ (increasing) or $x_{n+1} \le x_n$ (decreasing), often via induction or direct algebraic comparison.</li>
                    <li style="margin-bottom: 0.5rem;"><strong>Step 3: Invoke the MCT.</strong> Since the sequence is monotonic and bounded, conclude that $\lim_{n\to\infty} x_n = L$ exists.</li>
                    <li><div><strong>Step 4: Solve Algebraically.</strong> Take the limit $\lim_{n\to\infty}$ on both sides of the recurrence relation (substituting $L$ for both $x_{n+1}$ and $x_n$) and solve for $L$.</div></li>
                </ol>
            </div>

            <div class="aside-box" style="margin-top: 1.5rem;">
                <h4>🎯 Worked Example: The Nested Radical Sequence</h4>
                <p>Consider the recursively defined sequence given by $x_1 = \sqrt{2}$ and $x_{n+1} = \sqrt{2 + x_n}$ for $n \ge 1$. Let's evaluate its limit:</p>
                <ol style="margin: 0.5rem 0 0.5rem 1.25rem; padding: 0;">
                    <li style="margin-bottom: 0.4rem;"><strong>Boundedness:</strong> We show by induction that $x_n < 2$ for all $n$. Base case ($n=1$): $x_1 = \sqrt{2} < 2$ (true). Assuming $x_k < 2$, then $x_{k+1} = \sqrt{2 + x_k} < \sqrt{2 + 2} = 2$. Thus, the sequence is bounded above by $2$.</li>
                    <li style="margin-bottom: 0.4rem;"><strong>Monotonicity:</strong> We show $x_{n+1} > x_n$. Base case: $x_2 = \sqrt{2 + \sqrt{2}} > \sqrt{2} = x_1$. By induction, if $x_k > x_{k-1}$, then $\sqrt{2 + x_k} > \sqrt{2 + x_{k-1}}$, so $x_{n+1}$ is strictly increasing.</li>
                    <li style="margin-bottom: 0.4rem;"><strong>Existence:</strong> By the Monotone Convergence Theorem, $\lim_{n\to\infty} x_n = L$ exists.</li>
                    <li><strong>Algebraic Evaluation:</strong> Taking the limit on both sides of $x_{n+1} = \sqrt{2 + x_n}$:
                        <p style="text-align: center; margin: 0.5rem 0;">$$L = \sqrt{2 + L} \implies L^2 = 2 + L \implies L^2 - L - 2 = 0$$</p>
                        Factoring yields $(L - 2)(L + 1) = 0$. Since all terms $x_n > 0$, the limit must be positive, giving <strong>$L = 2$</strong>.
                    </li>
                </ol>
            </div>'''

    # Anchor target in Section 3 just before Section 4
    anchor_target = '<!-- SECTION 4 -->'

    if anchor_target in content and 'Evaluating Recursively Defined Sequences' not in content:
        content = content.replace(anchor_target, recursion_markup + '\n\n            <!-- SECTION 4 -->')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully added recursive sequences subsection to week2.html.")
    else:
        print("Anchor target not found or subsection already present.")

def execute_git_sync():
    commit_message = (
        "Add recursively defined sequences subsection to Section 3 in week2.html\n\n"
        "Added a comprehensive 4-step strategy and worked example for analyzing\n"
        "recursive sequences using induction, monotonicity, the Monotone\n"
        "Convergence Theorem, and algebraic limit evaluation."
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
    update_recursion_subsection()
    execute_git_sync()
