#!/usr/bin/env python3
import re
import subprocess
import sys

def patch_geometric_gap_heading():
    filepath = 'week1.html'
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: {filepath} not found.")
        sys.exit(1)

    pattern = r'<h5>The Geometric Gap:\s*Constructing\s*(?:&radic;2|\\?\$?\\sqrt\{2\}\\?\$?|2)\s*on the Number Line</h5>'
    replacement = '<h5>The Geometric Gap: Constructing &radic;2 on the Number Line</h5>'

    new_content, count = re.subn(pattern, replacement, content)

    if count == 0:
        fallback_pattern = r'<h5>The Geometric Gap:[^<]*</h5>'
        new_content, count = re.subn(fallback_pattern, replacement, content)

    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Successfully updated heading in {filepath} ({count} occurrence(s)).")
    else:
        print("Warning: Heading pattern not found. No changes made.")

def execute_git_sync():
    commit_message = (
        "Use entity-encoded square root in geometric gap heading\n\n"
        "Replaced the heading in week1.html to use &radic;2 for reliable\n"
        "cross-browser rendering without LaTeX delimiters."
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
    patch_geometric_gap_heading()
    execute_git_sync()
