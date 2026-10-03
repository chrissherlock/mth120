#!/usr/bin/env python3
import os
import subprocess

def add_sums_section():
    filepath = 'week1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Table of Contents
    old_toc = """                <ul class="toc-grid">
                    <li><a href="#section-sets">1. Sets and Functions</a></li>
                    <li><a href="#section-numbers">2. Number Systems and Completeness</a></li>
                    <li><a href="#section-sequences">3. Sequences and Derived Sequences</a></li>
                </ul>"""

    new_toc = """                <ul class="toc-grid">
                    <li><a href="#section-sets">1. Sets and Functions</a></li>
                    <li><a href="#section-numbers">2. Number Systems and Completeness</a></li>
                    <li><a href="#section-sequences">3. Sequences and Derived Sequences</a></li>
                    <li><a href="#section-sums">4. Sums and Partial Sums</a></li>
                </ul>"""

    if old_toc in content:
        content = content.replace(old_toc, new_toc)

    # 2. Insert Section 4 before closing div of module-content or body
    section_4_html = r"""
            <h2 id="section-sums">4. Sums and Partial Sums</h2>
            <div class="infobox">
                <h4>📖 Notation Reference: Summation Mechanics</h4>
                <div class="infobox-intro">
                    <strong>Meet the sigma machine:</strong> The Greek letter sigma ($\sum$) is simply shorthand for adding up a string of numbers without having to write out endless plus signs.
                </div>
                <div class="notation-grid">
                    <div class="notation-item"><span class="notation-sym">$\sum$</span><span class="notation-desc">Sigma operator: shorthand instruction to add numbers together</span></div>
                    <div class="notation-item"><span class="notation-sym">$\nu = 0$ or $1$</span><span class="notation-desc">Lower limit: the starting index value</span></div>
                    <div class="notation-item"><span class="notation-sym">$n$</span><span class="notation-desc">Upper limit: the final index value where the sum stops</span></div>
                    <div class="notation-item"><span class="notation-sym">$b_\nu$</span><span class="notation-desc">General term being added at each step</span></div>
                    <div class="notation-item"><span class="notation-sym">$s_n$</span><span class="notation-desc">Partial sum: the running total up to index $n$</span></div>
                </div>
            </div>

            <p>When studying sequences, we often want to know what happens when we add their terms together. Writing out $b_0 + b_1 + b_2 + \dots + b_n$ gets messy very quickly, so we use <strong>summation notation</strong>:</p>

            <div class="definition-box">
                <p>$$\sum_{\nu=0}^{n} b_\nu = b_0 + b_1 + b_2 + \dots + b_n$$</p>
            </div>

            <h3>Anatomy of a Summation</h3>
            <p>Think of $\sum$ as a loop in computer programming or an assembly line:</p>
            <ul>
                <li><strong>The Index ($\nu$):</strong> The counter variable (sometimes written as $i$ or $k$) that ticks upward by whole numbers.</li>
                <li><strong>The Starting Point (Lower Limit):</strong> Where the counter begins (e.g., $\nu = 0$ or $\nu = 1$).</li>
                <li><strong>The Stopping Point (Upper Limit):</strong> The final number $n$ where the counting finishes.</li>
                <li><strong>The Formula ($b_\v$):</strong> The rule evaluated at each step of the counter.</li>
            </ul>

            <h3>Partial Sums: The Running Total</h3>
            <p>As we saw with our coin-collection analogy, a <strong>partial sum</strong> ($s_n$) is simply a running total of a sequence up to step $n$:</p>

            <div class="definition-box">
                <p>$$s_n = \sum_{\nu=0}^{n} b_\nu$$</p>
            </div>

            <p>Instead of just looking at individual terms, partial sums allow us to watch how an accumulation grows. Two famous summation formulas appear frequently in your coursework:</p>

            <ul class="example-list">
                <li><strong>Sum of the First $n$ Integers (Triangular Numbers):</strong><br>
                $$\sum_{\nu=1}^{n} \nu = 1 + 2 + 3 + \dots + n = \frac{n(n+1)}{2}$$</li>
                <li><strong>Geometric Series Partial Sum:</strong><br>
                $$\sum_{\nu=0}^{n-1} q^\nu = 1 + q + q^2 + \dots + q^{n-1} = \frac{1 - q^n}{1 - q} \quad (\text{for } q \neq 1)$$</li>
            </ul>
</div>"""

    # Replace before the end of module-content
    if '<div class="module-content">' in content and section_4_html not in content:
        # Insert before the last closing div inside module-content or at the end of module-content
        # Let's find the closing tag of the last div or just before </body>
        content = content.replace('</body>', section_4_html + '\n</body>')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully added Section 4: Sums and Partial Sums to week1.html.")
    else:
        print("Module content container or section already present.")

def execute_git_sync():
    commit_message = (
        "Create dedicated standalone section for Sums and Partial Sums\n\n"
        "Added a new Section 4 in week1.html breaking down sigma notation,\n"
        "summation anatomy, partial sums, and standard formulas."
    )
    commands = [
        ['git', 'add', 'week1.html', 'update.py'],
        ['git', 'commit', '-m', commit_message],
        ['git', 'push', 'origin', 'main']
    ]
    for cmd in commands:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(f"> {' '.join(cmd)}\n{result.stdout}{result.stderr}")

if __name__ == '__main__':
    add_sums_section()
    execute_git_sync()
