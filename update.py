#!/usr/bin/env python3
import os
import subprocess

def fix_syntax_warning():
    filepath = 'update.py'
    if not os.path.exists(filepath):
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Ensure the string block uses raw string notation (r''')
    content = content.replace("enhanced_box = r'''", "enhanced_box = r'''")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully updated update.py to use raw string literal.")

def execute_git_sync():
    commit_message = (
        "Fix Python syntax warning for invalid escape sequence in update.py\n\n"
        "Converted string literal containing LaTeX commands (such as \\lim) to a\n"
        "raw string in update.py to eliminate SyntaxWarning."
    )
    commands = [
        ['git', 'add', 'update.py'],
        ['git', 'commit', '-m', commit_message],
        ['git', 'push', 'origin', 'main']
    ]
    for cmd in commands:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(f"> {' '.join(cmd)}\n{result.stdout}{result.stderr}")

if __name__ == '__main__':
    fix_syntax_warning()
    execute_git_sync()
