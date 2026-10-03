#!/usr/bin/env python3
import os
import subprocess

def add_sequences_intuition_box():
    filepath = 'week1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    intuition_section = r'''
            <div class="aside-box" style="margin-top: 1.75rem;">
                <h4>💡 Intuitive Guide: Making Sense of Derived Sequences and Partial Sums</h4>
                <p>These two concepts can feel tricky because they require a shift in perspective. Instead of just looking at where a sequence sits at a given moment, <strong>derived sequences</strong> look at how fast it is <em>changing</em>, while <strong>partial sums</strong> look at how much it has <em>accumulated</em>.</p>

                <h5 style="color: #92400e; margin: 1rem 0 0.4rem 0;">1. Derived Sequences: The Speedometer</h5>
                <p>When you look at a regular sequence like $(a_n) = (1, 4, 9, 16, 25)$, you see its positions at each step ($1^2, 2^2, 3^2$, etc.). A derived sequence ($a_n' = a_{n+1} - a_n$) asks: <strong>"How much did the sequence jump from one step to the next?"</strong></p>
                <ul>
                    <li><strong>The Analogy:</strong> Think of the original sequence as an odometer (total distance traveled), and the derived sequence as the speedometer (how fast you are moving right now).</li>
                    <li><strong>Example ($a_n = n^2$):</strong> The terms are $1, 4, 9, 16$. The gaps are $4-1=3$, then $9-4=5$, then $16-9=7$. The derived sequence is $(3, 5, 7, \dots)$. If the derived sequence is always positive ($a_n' > 0$), the original sequence is always climbing.</li>
                </ul>

                <h5 style="color: #92400e; margin: 1rem 0 0.4rem 0;">2. Partial Sums: The Running Tally</h5>
                <p>If derived sequences are about <em>stepping forward</em>, <strong>partial sums</strong> ($s_n = \sum_{\nu=0}^n b_\nu$) keep a <strong>running total</strong>.</p>
                <ul>
                    <li><strong>The Analogy:</strong> Imagine collecting coins in each video game level. Level 0 gives 2 coins, Level 1 gives 3, Level 2 gives 5. Your partial sum is your total score up to that exact moment.</li>
                    <li><strong>Process:</strong> Add terms cumulatively. Given terms $(2, 3, 5, 1)$, the partial sums are $s_0 = 2$, $s_1 = 2+3 = 5$, $s_2 = 2+3+5 = 10$, resulting in $(2, 5, 10, 11)$. In calculus, this is how we build infinite series.</li>
                </ul>
            </div>

            <h3>Derived Sequences and Partial Sums</h3>'''

    target_anchor = '<h3>Derived Sequences and Partial Sums</h3>'

    if target_anchor in content and 'Intuitive Guide: Making Sense of Derived Sequences' not in content:
        content = content.replace(target_anchor, intuition_section, 1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully added sequence intuition guide to week1.html.")
    else:
        print("Target anchor not found or guide already present.")

def execute_git_sync():
    commit_message = (
        "Add intuitive beginner guide for derived sequences and partial sums\n\n"
        "Inserted an accessible explanation featuring the odometer/speedometer\n"
        "analogy and running-tally coin game directly into week1.html."
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
    add_sequences_intuition_box()
    execute_git_sync()
