#!/usr/bin/env python3
import os
import subprocess

def insert_week2_hero():
    filepath = 'week2.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    hero_markup = r'''            <!-- HERO IMAGE -->
            <div style="margin-bottom: 2rem; border-radius: 8px; overflow: hidden; border: 1px solid var(--border); box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05), 0 2px 4px -1px rgba(0,0,0,0.03);">
                <img src="images/chapter2-hero.jpg" alt="Week 2: Limits of Sequences - UNE Campus Discovery Trail" style="width: 100%; height: auto; display: block;">
            </div>

            <div class="intro-lead">'''

    target = '<div class="intro-lead">'

    if 'images/chapter2-hero.jpg' in content:
        print("Hero image is already present in week2.html.")
        return

    if target in content:
        content = content.replace(target, hero_markup, 1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully added images/chapter2-hero.jpg to week2.html.")
    else:
        print("Could not find insertion target '<div class=\"intro-lead\">' in week2.html.")

def execute_git_sync():
    commit_message = (
        "Add campus discovery hero image to Week 2 module\n\n"
        "Integrated images/chapter2-hero.jpg as the top hero banner in\n"
        "week2.html, mirroring the styling and layout of Week 1."
    )
    commands = [
        ['git', 'add', 'week2.html', 'images/chapter2-hero.jpg', 'update.py'],
        ['git', 'commit', '-m', commit_message],
        ['git', 'push', 'origin', 'main']
    ]
    for cmd in commands:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(f"> {' '.join(cmd)}\n{result.stdout}{result.stderr}")

if __name__ == '__main__':
    insert_week2_hero()
    execute_git_sync()
