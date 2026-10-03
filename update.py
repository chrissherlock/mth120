#!/usr/bin/env python3
import os
import re
import subprocess

def inject_summation_notation():
    filepath = 'week1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Target the Sequence Mechanics notation box specifically
    target_box_pattern = r'(<h4>📖 Notation Reference: Sequence Mechanics</h4>[\s\S]*?<div class="notation-grid">)([\s\S]*?)(</div>)'

    def replacement_fn(match):
        header_and_grid = match.group(1)
        grid_items = match.group(2)
        closing_div = match.group(3)

        summation_item = '                    <div class="notation-item"><span class="notation-sym">$\\sum_{\\nu=0}^n$</span><span class="notation-desc">Summation operator: adding indexed terms cumulatively</span></div>\n'

        if '$\\sum_{\\nu=0}^n$' not in grid_items:
            # Insert right after the opening grid tag or after the first item
            return header_and_grid + summation_item + grid_items + closing_div
        return match.group(0)

    new_content, count = re.subn(target_box_pattern, replacement_fn, content)

    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Successfully injected summation operator into Sequence Mechanics infobox.")
    else:
        print("Warning: Sequence Mechanics infobox pattern not found.")

def execute_git_sync():
    commit_message = (
        "Robustly inject summation operator into Sequence Mechanics notation grid\n\n"
        "Used a regex-based substitution in update.py to reliably add the sigma\n"
        "summation item into the infobox reference grid in week1.html."
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
    inject_summation_notation()
    execute_git_sync()
