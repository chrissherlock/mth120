#!/usr/bin/env python3
import os
import subprocess

def fix_summation_notation_reference():
    filepath = 'week1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Target cramped index expressions in summation notation references
    cramped_patterns = [
        ('$\\nu=0$or1', '$\\nu = 0$ or $1$'),
        ('$\\nu = 0$or1', '$\\nu = 0$ or $1$'),
        ('ν=0or1', '$\\nu = 0$ or $1$'),
        ('ν = 0or1', '$\\nu = 0$ or $1$'),
        ('ν=0 or 1', '$\\nu = 0$ or $1$'),
        ('$\\nu=0$', '$\\nu = 0$'),
        ('ν=0', '$\\nu = 0$'),
    ]

    updated = content
    for old, new in cramped_patterns:
        if old in updated:
            updated = updated.replace(old, new)

    # Also check broader patterns in summation notation table cells
    if 'Summation Mechanics' in updated or 'Summation' in updated:
        # Ensure any instances of nu=0 or 1 are properly spaced with math blocks
        updated = updated.replace('ν = 0or 1', '$\\nu = 0$ or $1$')
        updated = updated.replace('ν=0 or 1', '$\\nu = 0$ or $1$')

    if updated != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated)
        print("Successfully fixed spacing in Summation Notation Reference in week1.html.")
    else:
        print("No exact cramped summation notation pattern matched; performing targeted regex replacement.")
        import re
        # Regex to catch any variant of nu=0 or 1 in table cells
        pattern = r'(?:\\nu|ν)\s*=\s*0\s*or\s*1'
        replacement = r'$\nu = 0$ or $1$'
        updated_regex, count = re.subn(pattern, replacement, updated)
        if count > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(updated_regex)
            print(f"Successfully replaced {count} cramped expression(s) via regex in week1.html.")
        else:
            print("No matches found via regex either.")

def execute_git_sync():
    commit_message = (
        "Fix spacing and KaTeX formatting in Summation Notation Reference\n\n"
        "Updated index variable expressions (nu = 0 or 1) in week1.html to ensure\n"
        "clean rendering without cramped spacing."
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
    fix_summation_notation_reference()
    execute_git_sync()
