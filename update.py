#!/usr/bin/env python3
import os
import re
import subprocess

def clean_index_citations():
    filepath = 'index.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Strip all patterns from index.html
    cleaned_content = re.sub(r'\s*\+\]', '', content)

    if cleaned_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(cleaned_content)
        print("Successfully removed citations from index.html.")
    else:
        print("No citations found in index.html.")

def execute_git_sync():
    commit_message = (
        "Remove all citation markers from index.html\n\n"
        "Cleaned up index.html by stripping out stray reference\n"
        "markers to maintain a citation-free course interface."
    )
    commands = [
        ['git', 'add', 'index.html', 'update.py'],
        ['git', 'commit', '-m', commit_message],
        ['git', 'push', 'origin', 'main']
    ]
    for cmd in commands:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(f"> {' '.join(cmd)}\n{result.stdout}{result.stderr}")

if __name__ == '__main__':
    clean_index_citations()
    execute_git_sync()
