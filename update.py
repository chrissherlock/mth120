#!/usr/bin/env python3
import os
import subprocess

def fix_latex_corruption():
    filepath = 'week2.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Repair corrupted sequences where \f became form feed (\x0c) or \t became tab
    # We replace any occurrences of corrupted tokens with correct LaTeX strings
    content = content.replace('rac', r'\frac')
    content = content.replace('\x0crac', r'\frac')
    content = content.replace('\tostart', r'\to')

    # Also fix any literal tab/form-feed issues in lim expressions
    content = content.replace('lim_{n\to\\infty}', r'\lim_{n\to\infty}')
    content = content.replace('lim_{n\t', r'\lim_{n\to')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully repaired LaTeX escape corruption in week2.html.")

def execute_git_sync():
    commit_message = (
        "Fix broken LaTeX escape sequences (\\frac and \\to) in Squeeze Theorem section\n\n"
        "Replaced corrupted literal escape characters (such as form feeds and tabs)\n"
        "with properly escaped LaTeX macros (\\frac and \\to) in week2.html."
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
    fix_latex_corruption()
    execute_git_sync()
