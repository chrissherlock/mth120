#!/usr/bin/env python3
import os
import subprocess

def fix_notation_spacing():
    filepath = 'week1-lecture1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    target_entry = r'<div class="notation-item"><span class="notation-sym">$f(X)$ or $\text{ran}(f)$</span>'

    fixed_entry = (
        r'<div class="notation-item">'
        r'<span class="notation-sym" style="gap: 0.35rem;">$f(X)$ '
        r'<span style="margin: 0 0.35rem; font-weight: 500; font-size: 0.9rem; color: #64748b;">or</span> '
        r'$\text{ran}(f)$</span>'
    )

    if target_entry in content:
        content = content.replace(target_entry, fixed_entry, 1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully corrected spacing around 'or' in week1-lecture1.html.")
    else:
        print("Target entry not found. It may have already been updated.")

def execute_git_sync():
    commit_message = (
        "Fix inline spacing around 'or' in function range notation\n\n"
        "Add explicit margin and flex gap around the conjunction 'or' in the\n"
        "function notation infobox in week1-lecture1.html. This prevents CSS\n"
        "flexbox from collapsing the anonymous text node whitespace between\n"
        "adjacent KaTeX span elements."
    )
    commands = [
        ['git', 'add', 'week1-lecture1.html', 'update.py'],
        ['git', 'commit', '-m', commit_message],
        ['git', 'push', 'origin', 'main']
    ]
    for cmd in commands:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(f"> {' '.join(cmd)}\n{result.stdout}{result.stderr}")

if __name__ == '__main__':
    fix_notation_spacing()
    execute_git_sync()
