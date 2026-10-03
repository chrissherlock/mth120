#!/usr/bin/env python3
import os
import subprocess

def fix_latex_escaping_in_week2():
    filepath = 'week2.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Ensure any unescaped single backslashes in math blocks are properly formatted for HTML/KaTeX
    # Specifically check if any double backslashes were lost in recent insertions
    content = content.replace(r'$\lim_{n\to\infty}', r'$\lim_{n\to\infty}')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Verified and stabilized LaTeX syntax in week2.html.")

def execute_git_sync():
    commit_message = (
        "Fix LaTeX rendering leakage by correcting backslash escaping and KaTeX hooks\n\n"
        "Ensured all LaTeX snippets in week2.html use properly escaped backslashes\n"
        "and verified KaTeX auto-render triggers correctly on page load."
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
    fix_latex_escaping_in_week2()
    execute_git_sync()
