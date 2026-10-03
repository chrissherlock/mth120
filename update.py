#!/usr/bin/env python3
import os
import subprocess

def box_derived_sequence_example():
    filepath = 'week1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    old_example_block = r'''            <h3>Worked Example: Squares and Differences</h3>
            <p>Consider the sequence of squares $(a_n) = (1, 4, 9, 16, 25, \dots)$, where $a_n = n^2$. Let's calculate its derived sequence step by step:</p>
            <ul>
                <li>$a_1' = a_2 - a_1 = 4 - 1 = 3$</li>
                <li>$a_2' = a_3 - a_2 = 9 - 4 = 5$</li>
                <li>$a_3' = a_4 - a_3 = 16 - 9 = 7$</li>
                <li>$a_4' = a_5 - a_4 = 25 - 16 = 9$</li>
            </ul>
            <p>The resulting derived sequence is $(3, 5, 7, 9, \dots)$, which follows the explicit formula $a_n' = 2n + 1$.</p>'''

    new_example_block = r'''            <div class="worked-example-box">
                <h4>🎯 Worked Example: Squares and Differences</h4>
                <p>Consider the sequence of squares $(a_n) = (1, 4, 9, 16, 25, \dots)$, where $a_n = n^2$. Let's calculate its derived sequence step by step:</p>
                <ul style="margin: 0.5rem 0 0.5rem 1.25rem; padding: 0;">
                    <li style="margin-bottom: 0.3rem;">$a_1' = a_2 - a_1 = 4 - 1 = 3$</li>
                    <li style="margin-bottom: 0.3rem;">$a_2' = a_3 - a_2 = 9 - 4 = 5$</li>
                    <li style="margin-bottom: 0.3rem;">$a_3' = a_4 - a_3 = 16 - 9 = 7$</li>
                    <li style="margin-bottom: 0.3rem;">$a_4' = a_5 - a_4 = 25 - 16 = 9$</li>
                </ul>
                <p style="margin-top: 0.5rem; margin-bottom: 0;">The resulting derived sequence is $(3, 5, 7, 9, \dots)$, which follows the explicit formula $a_n' = 2n + 1$.</p>
            </div>'''

    if old_example_block in content:
        content = content.replace(old_example_block, new_example_block)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully wrapped Derived Sequences worked example in week1.html.")
    else:
        print("Old example block not found.")

def execute_git_sync():
    commit_message = (
        "Wrap Derived Sequences worked example in emerald box in week1.html\n\n"
        "Converted the Squares and Differences worked example in Section 5 of week1.html\n"
        "to use the .worked-example-box emerald container."
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
    box_derived_sequence_example()
    execute_git_sync()
