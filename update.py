#!/usr/bin/env python3
import os
import subprocess

def prevent_cartesian_wrap():
    filepath = 'week1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace instances of ($A \times B$) or (A x B) in key headings/prose with nowrap spans
    content = content.replace('Cartesian Product ($A \\times B$)', 'Cartesian Product <span style="white-space: nowrap;">($A \\times B$)</span>')
    content = content.replace('Cartesian Products ($A \\times B$)', 'Cartesian Products <span style="white-space: nowrap;">($A \\times B$)</span>')
    content = content.replace('($A \\times B$)', '<span style="white-space: nowrap;">($A \\times B$)</span>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully added nowrap styling to Cartesian product notation.")

def execute_git_sync():
    commit_message = (
        "Prevent line-wrapping for Cartesian product notation in week1.html\n\n"
        "Wrapped instances of (A x B) in nowrap spans to ensure clean inline\n"
        "rendering across responsive viewports."
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
    prevent_cartesian_wrap()
    execute_git_sync()
