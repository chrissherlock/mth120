#!/usr/bin/env python3
import os
import subprocess

def update_derived_sequences_section():
    filepath = 'week1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    old_section_5 = r"""            <!-- SECTION 5 -->
            <h2 id="section-derived">5. Derived Sequences</h2>
            <div class="infobox">
                <h4>📖 Notation Reference: Derived Sequences</h4>
                <div class="infobox-intro">
                    <strong>The Speedometer Analogy:</strong> While a regular sequence tells you your position (like a car odometer), a derived sequence tells you how fast you are jumping from step to step (like a speedometer).
                </div>
                <div class="notation-grid">
                    <div class="notation-item"><span class="notation-sym">$a_n'$</span><span class="notation-desc">Derived sequence: consecutive differences $a_{n+1} - a_n$</span></div>
                </div>
            </div>

            <p>The <strong>derived sequence</strong> of $(a_n)$ is defined by consecutive differences $a_n' = a_{n+1} - a_n$. A sequence is constant, increasing, or decreasing if and only if its derived sequence is identically zero, non-negative, or non-positive.</p>

            <div class="aside-box">
                <h4>💡 Intuitive Guide: Making Sense of Derived Sequences and Partial Sums</h4>
                <p><strong>Derived sequences</strong> look at how fast a sequence is <em>changing</em> (the speedometer), while <strong>partial sums</strong> look at how much it has <em>accumulated</em> (the running total).</p>
            </div>"""

    new_section_5 = r"""            <!-- SECTION 5 -->
            <h2 id="section-derived">5. Derived Sequences</h2>
            <div class="infobox">
                <h4>📖 Notation Reference: Derived Sequences</h4>
                <div class="infobox-intro">
                    <strong>The Speedometer Analogy:</strong> While a regular sequence tells you your position (like a car odometer), a derived sequence tells you how fast you are jumping from step to step (like a speedometer).
                </div>
                <div class="notation-grid">
                    <div class="notation-item"><span class="notation-sym">$a_n'$</span><span class="notation-desc">Derived sequence: consecutive differences $a_{n+1} - a_n$</span></div>
                </div>
            </div>

            <p>When you look at a regular sequence, you see its position at each step. A <strong>derived sequence</strong> ($a_n' = a_{n+1} - a_n$) answers a single question: <strong>"How much did the sequence jump from one step to the next?"</strong></p>

            <div class="definition-box">
                <p>$$a_n' = a_{n+1} - a_n$$</p>
            </div>

            <h3>Worked Example: Squares and Differences</h3>
            <p>Consider the sequence of squares $(a_n) = (1, 4, 9, 16, 25, \dots)$, where $a_n = n^2$. Let's calculate its derived sequence step by step:</p>
            <ul>
                <li>$a_1' = a_2 - a_1 = 4 - 1 = 3$</li>
                <li>$a_2' = a_3 - a_2 = 9 - 4 = 5$</li>
                <li>$a_3' = a_4 - a_3 = 16 - 9 = 7$</li>
                <li>$a_4' = a_5 - a_4 = 25 - 16 = 9$</li>
            </ul>
            <p>The resulting derived sequence is $(3, 5, 7, 9, \dots)$, which follows the explicit formula $a_n' = 2n + 1$.</p>

            <h3>Connecting Derived Sequences to Behavior</h3>
            <p>Derived sequences give us an instant test for monotonicity:</p>
            <ul>
                <li><strong>Increasing:</strong> If $a_n' \ge 0$ for all $n$, the sequence never steps backward, so it is monotonically increasing.</li>
                <li><strong>Decreasing:</strong> If $a_n' \le 0$ for all $n$, the sequence is monotonically decreasing.</li>
                <li><strong>Constant:</strong> If $a_n' = 0$ for all $n$, every term is identical.</li>
            </ul>"""

    if old_section_5 in content:
        content = content.replace(old_section_5, new_section_5)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully updated Section 5 in week1.html.")
    else:
        print("Warning: old Section 5 block not found for replacement.")

def execute_git_sync():
    commit_message = (
        "Expand Section 5 with worked example and behavioral tests\n\n"
        "Added a step-by-step walkthrough of squared terms and their derived\n"
        "differences to make derived sequences easier to understand."
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
    update_derived_sequences_section()
    execute_git_sync()
