#!/usr/bin/env python3
import os
import subprocess

def fix_right_macro():
    filepath = 'week2.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace malformed ight with \right
    content = content.replace(r'ight)', r'\right)')
    content = content.replace('ight)', r'\right)')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully repaired \right macro in week2.html.")

def execute_git_sync():
    commit_message = (
        "Fix broken \\right macro in Squeeze Theorem example\n\n"
        "Replaced malformed 'ight' with proper '\\right' in week2.html limit parentheses."
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
    fix_right_macro()
    execute_git_sync()
