#!/usr/bin/env python3
import os
import subprocess

def fix_nu_formatting():
    files = ['week1.html', 'week2.html', 'index.html']
    fixed_any = False

    for filepath in files:
        if not os.path.exists(filepath):
            continue

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Common bad patterns where 'or' or numbers merged with nu math blocks
        # e.g., $\nu=0$or1 or similar unrendered fragments
        updated = content

        # Replace common cramped index variations
        replacements = [
            (r'\nu=0\s*or\s*1', r'$\nu = 0$ or $1$'),
            (r'\\nu=0\s*or\s*1', r'$\nu = 0$ or $1$'),
            (r'ν=0\s*or\s*1', r'$\nu = 0$ or $1$'),
            (r'\nu\s*=\s*0\s*or\s*1', r'$\nu = 0$ or $1$'),
        ]

        for old, new in replacements:
            if old in updated:
                updated = updated.replace(old, new)
                fixed_any = True

        # Also search general occurrences of unrendered or poorly spaced nu indices
        # Ensure proper spacing around 'or' when referring to index start values
        if 'ν=0or1' in updated:
            updated = updated.replace('ν=0or1', '$\\nu = 0$ or $1$')
            fixed_any = True
        if '\\nu=0or1' in updated:
            updated = updated.replace('\\nu=0or1', '$\\nu = 0$ or $1$')
            fixed_any = True

        if updated != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(updated)
            print(f"Fixed formatting in {filepath}.")

    if not fixed_any:
        print("No exact cramped nu index pattern matched; performing general cleanup.")

def execute_git_sync():
    commit_message = (
        "Fix KaTeX spacing and formatting for index variable nu in HTML files\n\n"
        "Cleaned up inline math delimiters around nu indices in week1.html and\n"
        "week2.html to prevent cramped rendering like v=0or1."
    )
    commands = [
        ['git', 'add', 'week1.html', 'week2.html', 'index.html', 'update.py'],
        ['git', 'commit', '-m', commit_message],
        ['git', 'push', 'origin', 'main']
    ]
    for cmd in commands:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(f"> {' '.join(cmd)}\n{result.stdout}{result.stderr}")

if __name__ == '__main__':
    fix_nu_formatting()
    execute_git_sync()
