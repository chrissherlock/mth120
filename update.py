#!/usr/bin/env python3
import os
import subprocess

def update_number_systems_reassurance():
    filepath = 'week1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    old_intro = (
        '<strong>Number systems and real analysis:</strong> Building from '
        'Peano\'s axioms for $\\mathbb{N}$ to the completeness of $\\mathbb{R}$.'
    )
    new_intro = (
        '<strong>Taking it one step at a time:</strong> Every time numbers felt complete, '
        'mathematics found a new gap—from counting on our fingers to fractions, '
        'and finally to the seamless real number line.'
    )

    if old_intro in content:
        content = content.replace(old_intro, new_intro)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully updated number systems intro with friendly reassurance.")
    else:
        print("Warning: Target text not found.")

def execute_git_sync():
    commit_message = (
        "Warm up number systems intro with friendly reassurance\n\n"
        "Replaced clinical intro in week1.html with a comforting, accessible\n"
        "explanation of number system expansion for beginners."
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
    update_number_systems_reassurance()
    execute_git_sync()
