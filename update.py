#!/usr/bin/env python3
import os
import subprocess

def add_summation_to_notation_grid():
    filepath = 'week1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    old_grid = """                    <div class="notation-item"><span class="notation-sym">$(a_n)$</span><span class="notation-desc">Sequence $(a_0, a_1, a_2, \dots)$</span></div>
                    <div class="notation-item"><span class="notation-sym">$a_n'$</span><span class="notation-desc">Derived sequence $a_{n+1} - a_n$</span></div>
                    <div class="notation-item"><span class="notation-sym">$s_n$</span><span class="notation-desc">Partial sum $\sum_{\nu=0}^n b_\nu$</span></div>
                    <div class="notation-item"><span class="notation-sym">$an + b$</span><span class="notation-desc">Arithmetic progression</span></div>
                    <div class="notation-item"><span class="notation-sym">$aq^n$</span><span class="notation-desc">Geometric progression</span></div>"""

    new_grid = """                    <div class="notation-item"><span class="notation-sym">$(a_n)$</span><span class="notation-desc">Sequence $(a_0, a_1, a_2, \dots)$</span></div>
                    <div class="notation-item"><span class="notation-sym">$a_n'$</span><span class="notation-desc">Derived sequence $a_{n+1} - a_n$</span></div>
                    <div class="notation-item"><span class="notation-sym">$\sum_{\nu=0}^n$</span><span class="notation-desc">Summation operator: adding indexed terms cumulatively</span></div>
                    <div class="notation-item"><span class="notation-sym">$s_n$</span><span class="notation-desc">Partial sum $\sum_{\nu=0}^n b_\nu$</span></div>
                    <div class="notation-item"><span class="notation-sym">$an + b$</span><span class="notation-desc">Arithmetic progression</span></div>
                    <div class="notation-item"><span class="notation-sym">$aq^n$</span><span class="notation-desc">Geometric progression</span></div>"""

    if old_grid in content:
        content = content.replace(old_grid, new_grid)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully added summation operator to sequence mechanics notation box.")
    else:
        print("Target notation grid block not found.")

def execute_git_sync():
    commit_message = (
        "Add summation operator to Sequence Mechanics notation reference\n\n"
        "Included the sigma summation notation (sum from i to n) inside the\n"
        "infobox reference grid in week1.html."
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
    add_summation_to_notation_grid()
    execute_git_sync()
