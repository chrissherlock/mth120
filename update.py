#!/usr/bin/env python3
import os
import subprocess

def update_hero_image_path():
    filepath = 'week1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    correct_src = 'src="images/chapter1-hero.jpg"'
    incorrect_src = 'src="chapter1-hero.jpg"'

    if correct_src in content:
        print("Image source is already correctly set to images/chapter1-hero.jpg.")
        return

    if incorrect_src in content:
        content = content.replace(incorrect_src, correct_src, 1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated existing hero image path to images/chapter1-hero.jpg.")
        return

    # If the image was not present at all, inject it cleanly above the intro-lead
    hero_markup = r'''            <!-- HERO IMAGE -->
            <div style="margin-bottom: 2rem; border-radius: 8px; overflow: hidden; border: 1px solid var(--border); box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05), 0 2px 4px -1px rgba(0,0,0,0.03);">
                <img src="images/chapter1-hero.jpg" alt="Week 1: Sets, Numbers, and Sequences - UNE Campus Discovery Trail" style="width: 100%; height: auto; display: block;">
            </div>

            <div class="intro-lead">'''

    target = '<div class="intro-lead">'
    if target in content:
        content = content.replace(target, hero_markup, 1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Injected hero banner with source images/chapter1-hero.jpg into week1.html.")
    else:
        print("Could not find insertion target '<div class=\"intro-lead\">' in week1.html.")

def execute_git_sync():
    commit_message = (
        "Fix hero image path to images/chapter1-hero.jpg in week1.html\n\n"
        "Corrected the relative path for the Week 1 campus discovery hero banner\n"
        "to load from the images/ assets directory."
    )
    commands = [
        ['git', 'add', 'week1.html', 'images/', 'update.py'],
        ['git', 'commit', '-m', commit_message],
        ['git', 'push', 'origin', 'main']
    ]
    for cmd in commands:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(f"> {' '.join(cmd)}\n{result.stdout}{result.stderr}")

if __name__ == '__main__':
    update_hero_image_path()
    execute_git_sync()
