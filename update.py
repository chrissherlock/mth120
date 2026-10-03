#!/usr/bin/env python3
import os
import re
import subprocess

def fix_summation_or_spacing():
    filepath = 'week1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find and fix any cramped 'or' patterns like 0or1, 1or0, ν=0or1, etc.
    # We can use regex to find digits or math variables adjacent to 'or' without spaces.

    # Example patterns to fix:
    # 0or1 -> $\nu = 0$ or $1$
    # $\nu=0$or1 -> $\nu = 0$ or $1$

    patterns_to_fix = [
        (r'(\d)or(\d)', r'\1 or \2'),
        (r'(\$\\nu\s*=\s*\d+\$)\s*or\s*(\d)', r'\1 or $\2$'),
        (r'ν\s*=\s*0\s*or\s*1', r'$\nu = 0$ or $1$'),
        (r'\\nu\s*=\s*0\s*or\s*1', r'$\nu = 0$ or $1$'),
    ]

    updated = content

    # General regex for any number or variable stuck to 'or' without spaces
    # e.g., "0or1", "1or0", "ν=0or1"
    updated = re.sub(r'([0-9νν])or([0-91])', r'\1 or \2', updated)
    updated = re.sub(r'(\$\\[a-zA-Z]+\s*=\s*\d+)\s*or\s*(\d+\$)', r'\1 or $\2$', updated)

    # Specific targeted replacements for summation index references
    replacements = {
        '0or1': '0 or 1',
        '1or0': '1 or 0',
        'ν=0or1': '$\nu = 0$ or $1$',
        '\\nu=0or1': '$\\nu = 0$ or $1$',
        '$\nu=0$or1': '$\\nu = 0$ or $1$',
        '$\nu = 0$or1': '$\\nu = 0$ or $1$',
        'ν = 0or1': '$\\nu = 0$ or $1$',
    }

    for target, replacement in replacements.items():
        if target in updated:
            updated = updated.replace(target, replacement)

    if updated != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated)
        print("Successfully fixed spacing around 'or' in week1.html.")
    else:
        print("No exact static string match found; applying broad regex cleanup for 'or' spacing.")
        # Catch any remaining 0or1 or similar instances
        updated = re.sub(r'(\d)\s*or\s*(\d)', r'\1 or \2', updated)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated)
        print("Applied regex cleanup to week1.html.")

def execute_git_sync():
    commit_message = (
        "Fix spacing around 'or' in summation index references in week1.html\n\n"
        "Scanned and replaced any occurrences of unspaced 'or' expressions\n"
        "(such as 0or1) with properly formatted and spaced KaTeX blocks."
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
    fix_summation_or_spacing()
    execute_git_sync()
