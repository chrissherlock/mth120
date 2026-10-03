#!/usr/bin/env python3
import os
import subprocess

def add_top_navigation_headers():
    # 1. Update week1.html top header
    if os.path.exists('week1.html'):
        with open('week1.html', 'r', encoding='utf-8') as f:
            content = f.read()

        old_header = """        <div class="header">
            <h1>Week 1: Sets, Numbers, and Sequences</h1>
            <a href="index.html" style="color: var(--accent); text-decoration: none; font-weight: 500;">&larr; Back to Curriculum Index</a>
        </div>"""

        new_header = """        <div class="header" style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
            <div>
                <h1>Week 1: Sets, Numbers, and Sequences</h1>
                <a href="index.html" style="color: var(--accent); text-decoration: none; font-weight: 500;">&larr; Back to Curriculum Index</a>
            </div>
            <div>
                <a href="week2.html" style="background: var(--accent); color: white; padding: 0.5rem 1rem; border-radius: 6px; text-decoration: none; font-weight: 600; font-size: 0.9rem;">Next: Week 2 &rarr;</a>
            </div>
        </div>"""

        if old_header in content:
            content = content.replace(old_header, new_header)
            with open('week1.html', 'w', encoding='utf-8') as f:
                f.write(content)

    # 2. Update week2.html top header
    if os.path.exists('week2.html'):
        with open('week2.html', 'r', encoding='utf-8') as f:
            content = f.read()

        old_header = """        <div class="header">
            <h1>Week 2: Limits of Sequences | MTHS120</h1>
            <a href="index.html" style="color: var(--accent); text-decoration: none; font-weight: 500;">&larr; Back to Curriculum Index</a>
        </div>"""

        new_header = """        <div class="header" style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
            <div>
                <h1>Week 2: Limits of Sequences</h1>
                <a href="index.html" style="color: var(--accent); text-decoration: none; font-weight: 500;">&larr; Back to Curriculum Index</a>
            </div>
            <div style="display: flex; gap: 0.5rem;">
                <a href="week1.html" style="background: #64748b; color: white; padding: 0.5rem 1rem; border-radius: 6px; text-decoration: none; font-weight: 600; font-size: 0.9rem;">&larr; Prev: Week 1</a>
            </div>
        </div>"""

        if old_header in content:
            content = content.replace(old_header, new_header)
            with open('week2.html', 'w', encoding='utf-8') as f:
                f.write(content)

    print("Successfully added top navigation headers.")

def execute_git_sync():
    commit_message = (
        "Add top navigation headers to week1.html and week2.html\n\n"
        "Inserted a clean, responsive previous/next header navigation bar at the\n"
        "top of both weekly course modules alongside the page titles."
    )
    commands = [
        ['git', 'add', 'week1.html', 'week2.html', 'update.py'],
        ['git', 'commit', '-m', commit_message],
        ['git', 'push', 'origin', 'main']
    ]
    for cmd in commands:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(f"> {' '.join(cmd)}\n{result.stdout}{result.stderr}")

if __name__ == '__main__':
    add_top_navigation_headers()
    execute_git_sync()
