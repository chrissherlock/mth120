#!/usr/bin/env python3
import os
import subprocess

def reorder_sums_section():
    filepath = 'week1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Clean up any previously misplaced Section 4 at the very end
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
                <li><strong>The Formula ($b_\nu$):</strong> The rule evaluated at each step of the counter.</li>
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
            </ul>"""

    # Remove any existing Section 4 block if it was appended at the bottom
    if section_4_html in content:
        content = content.replace(section_4_html, '')

    # Update TOC to include Section 4 before derived sequences
    old_toc = """                <ul class="toc-grid">
                    <li><a href="#section-sets">1. Sets and Functions</a></li>
                    <li><a href="#section-numbers">2. Number Systems and Completeness</a></li>
                    <li><a href="#section-sequences">3. Sequences, Derived Sequences, and Partial Sums</a></li>
                </ul>"""

    new_toc = """                <ul class="toc-grid">
                    <li><a href="#section-sets">1. Sets and Functions</a></li>
                    <li><a href="#section-numbers">2. Number Systems and Completeness</a></li>
                    <li><a href="#section-sequences">3. Sequences</a></li>
                    <li><a href="#section-sums">4. Sums and Partial Sums</a></li>
                </ul>"""

    if old_toc in content:
        content = content.replace(old_toc, new_toc)

    # Insert Section 4 right before Section 3's derived sequences discussion
    target_anchor = '<h3>Derived Sequences and Partial Sums</h3>'

    if target_anchor in content and section_4_html not in content:
        content = content.replace(target_anchor, section_4_html + '\n\n            <h2 id="section-derived">5. Derived Sequences</h2>\n            <h3>Derived Sequences and Partial Sums</h3>')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully reordered Sums and Partial Sums above Derived Sequences.")
    else:
        print("Target anchor not found.")

def execute_git_sync():
    commit_message = (
        "Reorder sections to place Sums and Partial Sums above Derived Sequences\n\n"
        "Moved Section 4 (Sums and Partial Sums) to appear right before derived\n"
        "sequences in week1.html for a more logical learning progression."
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
    reorder_sums_section()
    execute_git_sync()
