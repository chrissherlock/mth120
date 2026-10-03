#!/usr/bin/env python3
import os
import subprocess

def expand_recursive_section_in_html():
    filepath = 'week2.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Old concise recursive subsection block to replace
    old_recursion_block = r'''            <h3 style="margin-top: 2rem;">Evaluating Recursively Defined Sequences</h3>
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

    # Fully expanded replacement block with deep conceptual explanations
    new_recursion_block = r'''            <h3 style="margin-top: 2rem;">Evaluating Recursively Defined Sequences</h3>
            <p>When a sequence is given by a recurrence relation (e.g., $x_{n+1} = f(x_n)$) rather than an explicit formula, we cannot calculate its limit directly at first glance. But <em>why</em> can't we just take the limit algebraically right away? Understanding this reveals why a rigorous strategy is essential.</p>

            <div class="aside-box" style="margin-top: 1.5rem;">
                <h4>⚠️ The Core Dilemma: Explicit vs. Recurrence &amp; The Trap of Blind Algebra</h4>
                <ul style="margin: 0.5rem 0 0.5rem 1.25rem; padding: 0;">
                    <li style="margin-bottom: 0.5rem;"><strong>Explicit Formulas ($x_n = f(n)$):</strong> You have a direct formula where $n$ is isolated. You can take $\lim_{n\to\infty}$ instantly because you see the long-term behavior directly.</li>
                    <li style="margin-bottom: 0.5rem;"><strong>Recurrence Relations ($x_{n+1} = f(x_n)$):</strong> You are climbing a ladder one rung at a time. Each term depends entirely on the previous one, so $n$ does not appear as an independent variable.</li>
                    <li><strong>The Logical Trap:</strong> If you try to take a shortcut by blindly assuming a limit $L$ exists and writing $L = f(L)$ (e.g., $L = \sqrt{2 + L}$), you are <strong>putting the cart before the horse</strong>. If a sequence diverges (like $x_{n+1} = x_n + 1$), a limit does not exist, and treating $L$ as a normal algebra variable leads to nonsense ($0 = 1$). Algebraic substitution <em>assumes</em> existence before proving it.</li>
                </ul>
            </div>

            <p>To make our algebraic calculation legally sound, we must split the problem into two distinct phases: <strong>proving the limit exists</strong> using the Monotone Convergence Theorem first, and <strong>calculating what it is</strong> second.</p>

            <div class="infobox">
                <h4>🛠️ The 4-Step Strategy for Recursive Sequences</h4>
                <ol style="margin: 0.5rem 0 0.5rem 1.25rem; padding: 0;">
                    <li style="margin-bottom: 0.5rem;"><strong>Step 1: Prove Boundedness.</strong> Use mathematical induction to show that all terms remain bounded above or below by a constant $M$. (This ensures the sequence doesn't run off to infinity).</li>
                    <li style="margin-bottom: 0.5rem;"><strong>Step 2: Prove Monotonicity.</strong> Show that $x_{n+1} \ge x_n$ (increasing) or $x_{n+1} \le x_n$ (decreasing). (This ensures the sequence moves in a single direction without chaotic oscillation).</li>
                    <li style="margin-bottom: 0.5rem;"><strong>Step 3: Invoke the MCT.</strong> Because the sequence is bounded and monotonic, the Monotone Convergence Theorem steps in as an absolute legal guarantee that $\lim_{n\to\infty} x_n = L$ exists.</li>
                    <li><strong>Step 4: Solve Algebraically.</strong> Now—and <em>only</em> now that existence is guaranteed—take the limit on both sides of the recurrence relation ($L = f(L)$) and solve for $L$.</li>
                </ol>
            </div>

            <div class="aside-box" style="margin-top: 1.5rem;">
                <h4>🎯 Worked Example: The Nested Radical Sequence</h4>
                <p>Consider the recursively defined sequence given by $x_1 = \sqrt{2}$ and $x_{n+1} = \sqrt{2 + x_n}$ for $n \ge 1$. Let's evaluate its limit using our 4-step strategy:</p>
                <ol style="margin: 0.5rem 0 0.5rem 1.25rem; padding: 0;">
                    <li style="margin-bottom: 0.4rem;"><strong>Step 1 (Boundedness):</strong> We show by induction that $x_n < 2$ for all $n$. Base case ($n=1$): $x_1 = \sqrt{2} < 2$ (true). Assuming $x_k < 2$, then $x_{k+1} = \sqrt{2 + x_k} < \sqrt{2 + 2} = 2$. Thus, bounded above by $2$.</li>
                    <li style="margin-bottom: 0.4rem;"><strong>Step 2 (Monotonicity):</strong> We show $x_{n+1} > x_n$. Base case: $x_2 = \sqrt{2 + \sqrt{2}} > \sqrt{2} = x_1$. By induction, if $x_k > x_{k-1}$, then $\sqrt{2 + x_k} > \sqrt{2 + x_{k-1}}$, so the sequence is strictly increasing.</li>
                    <li style="margin-bottom: 0.4rem;"><strong>Step 3 (Existence):</strong> By the Monotone Convergence Theorem, $\lim_{n\to\infty} x_n = L$ exists.</li>
                    <li><strong>Step 4 (Algebraic Evaluation):</strong> Taking the limit on both sides of $x_{n+1} = \sqrt{2 + x_n}$:
                        <p style="text-align: center; margin: 0.5rem 0;">$$L = \sqrt{2 + L} \implies L^2 = 2 + L \implies L^2 - L - 2 = 0$$</p>
                        Factoring yields $(L - 2)(L + 1) = 0$. Since all terms $x_n > 0$, the limit must be positive, giving <strong>$L = 2$</strong>.
                    </li>
                </ol>
            </div>'''

    if old_recursion_block in content:
        content = content.replace(old_recursion_block, new_recursion_block)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully updated recursive sequences section in week2.html.")
    else:
        print("Old recursion block not found exactly; performing fallback anchor replacement.")
        # Fallback anchor replacement if needed
        if 'Evaluating Recursively Defined Sequences' in content:
            parts = content.split('Evaluating Recursively Defined Sequences')
            # Find next section or end
            rest = parts[1].split('<!-- SECTION 4 -->')[1]
            updated_content = parts[0] + 'Evaluating Recursively Defined Sequences' + new_recursion_block.split('Evaluating Recursively Defined Sequences')[1] + '\n\n            <!-- SECTION 4 -->' + rest
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print("Successfully updated via fallback anchor.")

def execute_git_sync():
    commit_message = (
        "Fully expand recursive sequence explanation in week2.html\n\n"
        "Added comprehensive conceptual breakdown contrasting explicit vs recurrence\n"
        "formulas, explaining the logical trap of blind algebra, and detailing\n"
        "the two-phase guarantee in week2.html."
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
    expand_recursive_section_in_html()
    execute_git_sync()
