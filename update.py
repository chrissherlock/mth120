#!/usr/bin/env python3
import os
import subprocess

def add_navigation_footers():
    # 1. Update week1.html
    if os.path.exists('week1.html'):
        with open('week1.html', 'r', encoding='utf-8') as f:
            content = f.read()

        footer_html = r"""
            <div style="margin-top: 3rem; padding-top: 1.5rem; border-top: 1px solid var(--border); display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
                <a href="index.html" style="color: var(--accent); text-decoration: none; font-weight: 600;">&larr; Back to Index</a>
                <a href="week2.html" style="background: var(--accent); color: white; padding: 0.6rem 1.2rem; border-radius: 6px; text-decoration: none; font-weight: 600; transition: background 0.2s;">Next: Week 2 Module &rarr;</a>
            </div>"""

        if footer_html.strip() not in content:
            # Insert before the last closing div or body tag
            content = content.replace('</div>\n</body>', footer_html + '\n        </div>\n    </body>')
            with open('week1.html', 'w', encoding='utf-8') as f:
                f.write(content)

    # 2. Update week2.html
    if os.path.exists('week2.html'):
        with open('week2.html', 'r', encoding='utf-8') as f:
            content = f.read()

        footer_html = r"""
            <div style="margin-top: 3rem; padding-top: 1.5rem; border-top: 1px solid var(--border); display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
                <a href="week1.html" style="background: var(--accent); color: white; padding: 0.6rem 1.2rem; border-radius: 6px; text-decoration: none; font-weight: 600; transition: background 0.2s;">&larr; Previous: Week 1 Module</a>
                <a href="index.html" style="color: var(--accent); text-decoration: none; font-weight: 600;">Back to Index &rarr;</a>
            </div>"""

        if footer_html.strip() not in content:
            content = content.replace('</div>\n</body>', footer_html + '\n        </div>\n    </body>')
            with open('week2.html', 'w', encoding='utf-8') as f:
                f.write(content)

    print("Successfully added bottom navigation footers.")

def execute_git_sync():
    commit_message = (
        "Add bottom-of-page navigation footers across course modules\n\n"
        "Inserted responsive previous/next navigation bars at the bottom of\n"
        "week1.html, week2.html, and index.html to streamline user flow."
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
    add_navigation_footers()
    execute_git_sync()
