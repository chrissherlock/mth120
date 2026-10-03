#!/usr/bin/env python3
import os
import subprocess

def update_friendly_reassurance():
    filepath = 'week1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    old_intro = (
        '<strong>The language of science:</strong> Set theory provides the foundational '
        'grammar for modern mathematics. Functions map inputs from a domain to outputs in a codomain.'
    )
    new_intro = (
        '<strong>Don\'t worry if this feels abstract at first:</strong> '
        'Set theory is simply the friendly art of grouping things together, '
        'and functions are just reliable rules that match an input to an output.'
    )

    if old_intro in content:
        content = content.replace(old_intro, new_intro)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully updated set theory intro with friendly reassurance.")
    else:
        print("Warning: Target text not found.")

def execute_git_sync():
    commit_message = (
        "Warm up set theory and function intro with friendly reassurance\n\n"
        "Replaced clinical introductory text in week1.html with a comforting,\n"
        "accessible explanation for beginners."
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
    update_friendly_reassurance()
    execute_git_sync()
