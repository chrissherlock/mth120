#!/usr/bin/env python3
import os
import subprocess

def add_worked_example_styling():
    filepath = 'week2.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add .worked-example-box CSS to the <style> block
    css_addition = r'''        .worked-example-box { background: #f0fdf4; border: 1px solid #bbf7d0; border-left: 5px solid #10b981; padding: 1.25rem 1.5rem; margin: 1.5rem 0; border-radius: 0 6px 6px 0; }
        .worked-example-box h4 { margin-top: 0; color: #047857; font-size: 1rem; display: flex; align-items: center; gap: 0.5rem; }
        .worked-example-box p, .worked-example-box li { color: #0f172a !important; }'''

    if '.worked-example-box {' not in content:
        content = content.replace('</style>', css_addition + '\n    </style>')

    # 2. Replace worked example aside-boxes with worked-example-box class
    # We target blocks containing "🎯 Worked Example"
    # Since they currently use class="aside-box" style="margin-top: 1.5rem;" or similar, we replace class="aside-box" with class="worked-example-box" where the header has 🎯 Worked Example

    # Let's do a smart replacement or identify them
    # We can search for <div class="aside-box" style="margin-top: 1.5rem;">\s*<h4>🎯 Worked Example
    import re

    pattern = r'<div class="aside-box"(?: style="[^"]*")?>\s*<h4>\s*🎯 Worked Example'
    replacement = r'<div class="worked-example-box"><h4>🎯 Worked Example'

    content, count = re.subn(pattern, replacement, content)
    print(f"Updated {count} worked example boxes to use the new emerald theme.")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def execute_git_sync():
    commit_message = (
        "Add dedicated worked example styling with distinct emerald theme in week2.html\n\n"
        "Created a new .worked-example-box CSS class with a green accent scheme to\n"
        "differentiate worked examples from standard aside and infobox elements."
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
    add_worked_example_styling()
    execute_git_sync()
