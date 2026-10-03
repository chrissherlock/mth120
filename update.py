#!/usr/bin/env python3
import os
import subprocess

def add_nbsp_around_or():
    filepath = 'week1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace any cramped variations around 'or' with non-breaking spaces
    targets = [
        'or',
        'or',
        'or',
        'or',
        'or',
        'or'
    ]

    updated = content
    # Look for patterns where 'or' is preceded or followed by digits/variables without proper spaces
    # and explicitly insert &nbsp;
    import re

    # Replace instances like "0 or 1", "0or1", "1or0" etc. in summation contexts with explicit &nbsp;or&nbsp;
    updated = re.sub(r'(\d)\s*or\s*(\d)', r'\1&nbsp;or&nbsp;\2', updated)
    updated = re.sub(r'(\d)\s*or\s*(\d)', r'\1&nbsp;or&nbsp;\2', updated)

    # Also catch any literal "or" sitting between numbers or math symbols and wrap with &nbsp;
    updated = updated.replace(' 0 or 1 ', ' 0&nbsp;or&nbsp;1 ')
    updated = updated.replace(' 1 or 0 ', ' 1&nbsp;or&nbsp;0 ')
    updated = updated.replace('v = 0 or 1', 'ν&nbsp;=&nbsp;0&nbsp;or&nbsp;1')

    if updated != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated)
        print("Successfully added non-breaking spaces around 'or' in week1.html.")
    else:
        print("No matching text found for replacement.")

def execute_git_sync():
    commit_message = (
        "Add non-breaking spaces around 'or' in summation notation in week1.html\n\n"
        "Replaced instances of 'or' in week1.html with &nbsp;or&nbsp; to guarantee\n"
        "proper visual spacing."
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
    add_nbsp_around_or()
    execute_git_sync()
