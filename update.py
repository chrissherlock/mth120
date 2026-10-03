#!/usr/bin/env python3
import os
import subprocess

def add_worked_examples():
    # --- UPDATE WEEK 1 ---
    w1_path = 'week1.html'
    if os.path.exists(w1_path):
        with open(w1_path, 'r', encoding='utf-8') as f:
            w1_content = f.read()

        w1_example = r'''
            <div class="aside-box" style="margin-top: 1.5rem;">
                <h4>🎯 Worked Example: Telescoping Sums &amp; Index Shifting</h4>
                <p>Evaluate the sum $\sum_{k=1}^{n} \left(\frac{1}{k} - \frac{1}{k+1}\right)$ by writing out terms and identifying cancellations:</p>
                <ol style="margin: 0.5rem 0 0.5rem 1.25rem; padding: 0;">
                    <li style="margin-bottom: 0.4rem;"><strong>Step 1: Write out the first few terms.</strong>
                        $$\left(1 - \frac{1}{2}\right) + \left(\frac{1}{2} - \frac{1}{3}\right) + \left(\frac{1}{3} - \frac{1}{4}\right) + \dots + \left(\frac{1}{n} - \frac{1}{n+1}\right)$$
                    </li>
                    <li style="margin-bottom: 0.4rem;"><strong>Step 2: Observe interior cancellations.</strong> Notice how $-\frac{1}{2}$ cancels with $+\frac{1}{2}$, $-\frac{1}{3}$ cancels with $+\frac{1}{3}$, and so on.</li>
                    <li><strong>Step 3: Evaluate the finite sum.</strong> Only the very first term and the very last term survive:
                        $$\sum_{k=1}^{n} \left(\frac{1}{k} - \frac{1}{k+1}\right) = 1 - \frac{1}{n+1} = \frac{n}{n+1}$$
                    </li>
                </ol>
            </div>'''

        if 'Telescoping Sums' not in w1_content and 'Summation Mechanics' in w1_content:
            # Insert right after Summation Mechanics section
            w1_content = w1_content.replace('</div>\n\n            <!-- SECTION', w1_content + '\n\n' + w1_example + '\n\n            <!-- SECTION', 1) if '<!-- SECTION' in w1_content else w1_content + w1_example
            with open(w1_path, 'w', encoding='utf-8') as f:
                f.write(w1_content)
            print("Successfully added worked example to week1.html.")

    # --- UPDATE WEEK 2 ---
    w2_path = 'week2.html'
    if os.path.exists(w2_path):
        with open(w2_path, 'r', encoding='utf-8') as f:
            w2_content = f.read()

        w2_examples = r'''
            <div class="aside-box" style="margin-top: 1.5rem;">
                <h4>🎯 Worked Example 1: The $\epsilon\text{-}N$ Scratchpad Method</h4>
                <p>Prove formally that $\lim_{n\to\infty} \frac{2n+1}{n} = 2$:</p>
                <ol style="margin: 0.5rem 0 0.5rem 1.25rem; padding: 0;">
                    <li style="margin-bottom: 0.4rem;"><strong>Step 1: The Scratchpad Analysis.</strong> Start with $|a_n - L| < \epsilon$:
                        $$\left|\frac{2n+1}{n} - 2\right| = \left|2 + \frac{1}{n} - 2\right| = \left|\frac{1}{n}\right| = \frac{1}{n} < \epsilon$$
                    </li>
                    <li style="margin-bottom: 0.4rem;"><strong>Step 2: Solving for $n$.</strong> Rearranging gives $n > \frac{1}{\epsilon}$.</li>
                    <li style="margin-bottom: 0.4rem;"><strong>Step 3: Choosing $N$.</strong> Choose an integer $N \ge \frac{1}{\epsilon}$ (formally $N = \lceil 1/\epsilon \rceil$).</li>
                    <li><strong>Step 4: Formal Proof Write-Up.</strong> Given $\epsilon > 0$, let $N = \lceil 1/\epsilon \rceil$. For any $n > N$, we have $n > \frac{1}{\epsilon}$, which implies $\frac{1}{n} < \epsilon$, proving $\left|\frac{2n+1}{n} - 2\right| < \epsilon$. Q.E.D.</li>
                </ol>
            </div>

            <div class="aside-box" style="margin-top: 1.5rem;">
                <h4>🎯 Worked Example 2: Applying Algebraic Limit Laws</h4>
                <p>Evaluate $\lim_{n\to\infty} \frac{3n^2 - 1}{2n^2 + 5}$ using the Limit Laws:</p>
                <ol style="margin: 0.5rem 0 0.5rem 1.25rem; padding: 0;">
                    <li style="margin-bottom: 0.4rem;"><strong>Step 1: Divide by highest power.</strong> Divide both numerator and denominator by $n^2$:
                        $$\lim_{n\to\infty} \frac{3 - \frac{1}{n^2}}{2 + \frac{5}{n^2}}$$
                    </li>
                    <li style="margin-bottom: 0.4rem;"><strong>Step 2: Apply Quotient &amp; Sum Laws.</strong> Because $\lim \frac{1}{n^2} = 0$, we apply the arithmetic laws:
                        $$\frac{\lim(3) - \lim\left(\frac{1}{n^2}\right)}{\lim(2) + \lim\left(\frac{5}{n^2}\right)}$$
                    </li>
                    <li><strong>Step 3: Final Calculation.</strong> Substituting standard limits gives:
                        $$\frac{3 - 0}{2 + 0} = \frac{3}{2}$$
                    </li>
                </ol>
            </div>'''

        if 'Worked Example 1: The $\epsilon\text{-}N$ Scratchpad Method' not in w2_content:
            # Insert right before Section 2 header
            if '<h2 id="section-theorems">2. Limit Theorems' in w2_content:
                w2_content = w2_content.replace('<h2 id="section-theorems">2. Limit Theorems', w2_examples + '\n\n            <h2 id="section-theorems">2. Limit Theorems')
                with open(w2_path, 'w', encoding='utf-8') as f:
                    f.write(w2_content)
                print("Successfully added worked examples to week2.html.")

def execute_git_sync():
    commit_message = (
        "Add comprehensive worked examples to week1.html and week2.html\n\n"
        "Inserted telescoping sums for week1.html, and epsilon-N scratchpad proofs\n"
        "and rational limit law evaluations for week2.html."
    )
    commands = [
        ['git', 'add', 'week1.html', 'week2.html', 'update.py'],
        ['git', 'commit', '-m', commit_message],
        ['git', 'push', 'origin', 'main']
    ]
    for cmd in commands:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(f"> {' '.join(cmd)}\n{result.stdout}{result.stderr}")

if __name__ == '__main__':
    add_worked_examples()
    execute_git_sync()
