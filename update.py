#!/usr/bin/env python3
import os
import subprocess

def add_squeeze_theorem_example():
    filepath = 'week2.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_example = r'''            <div class="worked-example-box" style="margin-bottom: 2.5rem;">
                <h4>🎯 Worked Example: The Expanding Sum (Squeeze Theorem)</h4>
                <p>Evaluate the limit of the sequence $x_n = \frac{1}{n^2+1} + \frac{1}{n^2+2} + \dots + \frac{1}{n^2+n}$.</p>
                <p style="font-size: 0.95rem; color: #475569; font-style: italic;">Note: We cannot use the standard Sum Limit Law here because the number of terms we are adding grows to infinity as $n$ increases. The law only applies to a fixed, finite number of terms. We must trap the entire sum.</p>
                <ol style="margin: 0.5rem 0 0.5rem 1.25rem; padding: 0;">
                    <li style="margin-bottom: 0.6rem;"><strong>Step 1: Construct a Lower Bound.</strong><br>
                        The sum has exactly $n$ fractions. The smallest fraction in the sum is the very last one (because it has the largest denominator: $n^2+n$). If we replace every single term in our sum with this smallest term, we get a sum that is strictly smaller:
                        $$a_n = \underbrace{\frac{1}{n^2+n} + \dots + \frac{1}{n^2+n}}_{n \text{ times}} = n \left( \frac{1}{n^2+n} \right) = \frac{n}{n(n+1)} = \frac{1}{n+1}$$
                    </li>
                    <li style="margin-bottom: 0.6rem;"><strong>Step 2: Construct an Upper Bound.</strong><br>
                        Similarly, the largest fraction is the first one (smallest denominator: $n^2+1$). If we replace every term with this largest term, we create a sum that is strictly larger:
                        $$c_n = \underbrace{\frac{1}{n^2+1} + \dots + \frac{1}{n^2+1}}_{n \text{ times}} = n \left( \frac{1}{n^2+1} \right) = \frac{n}{n^2+1}$$
                    </li>
                    <li style="margin-bottom: 0.6rem;"><strong>Step 3: Establish the Squeeze.</strong><br>
                        We have successfully trapped our expanding sum sequence:
                        $$\frac{1}{n+1} \le x_n \le \frac{n}{n^2+1}$$
                    </li>
                    <li><strong>Step 4: Take Limits of the Outer Bounds.</strong><br>
                        Now, evaluate the limits of our new, simplified bounds:
                        $$\lim_{n\to\infty} a_n = \lim_{n\to\infty} \frac{1}{n+1} = 0$$
                        $$\lim_{n\to\infty} c_n = \lim_{n\to\infty} \frac{n}{n^2+1} = \lim_{n\to\infty} \frac{1/n}{1 + 1/n^2} = \frac{0}{1+0} = 0$$
                        Because both the ceiling and the floor collapse to $0$, the Squeeze Theorem forces the trapped sequence to share the exact same limit. Thus, $\lim_{n\to\infty} x_n = 0$.
                    </li>
                </ol>
            </div>

            <!-- SECTION 3 -->'''

    target = '<!-- SECTION 3 -->'

    if target in content and 'Worked Example: The Expanding Sum' not in content:
        content = content.replace(target, new_example, 1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully injected the Squeeze Theorem worked example into week2.html.")
    elif 'Worked Example: The Expanding Sum' in content:
        print("The worked example is already present in week2.html.")
    else:
        print("Target anchor '<!-- SECTION 3 -->' not found in week2.html.")

def execute_git_sync():
    commit_message = (
        "Add Squeeze Theorem worked example for expanding sums\n\n"
        "Inserted a step-by-step worked example into week2.html demonstrating \n"
        "how to use the Squeeze Theorem on a sequence with a growing number of \n"
        "fractional terms where standard algebraic limit laws fail."
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
    add_squeeze_theorem_example()
    execute_git_sync()
