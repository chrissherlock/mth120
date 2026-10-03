#!/usr/bin/env python3
import os
import subprocess

def fix_section_heading():
    filepath = 'week2.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace malformed heading
    old_heading = '<h2 id="section-limits">1. Formal $\\epsilon\\text–}N$ Convergence</h2>'
    new_heading = '<h2 id="section-limits">1. Formal $\\epsilon\\text{-}N$ Convergence</h2>'

    toc_old = '<li><a href="#section-limits">1. Formal $\\epsilon\\text–}N$ Convergence</a></li>'
    toc_new = '<li><a href="#section-limits">1. Formal $\\epsilon\\text{-}N$ Convergence</a></li>'

    updated = False
    if old_heading in content:
        content = content.replace(old_heading, new_heading)
        updated = True
    if toc_old in content:
        content = content.replace(toc_old, toc_new)
        updated = True

    if updated:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully fixed Section 1 heading in week2.html.")
    else:
        print("Heading target not found or already fixed.")

def execute_git_sync():
    commit_message = (
        "Fix KaTeX syntax error in Section 1 heading in week2.html\n\n"
        "Corrected the malformed math delimiter in the section heading from\n"
        "\\epsilon\\text–}N to \\epsilon\\text{-}N."
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
    fix_section_heading()
    execute_git_sync()
