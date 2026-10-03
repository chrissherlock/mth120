#!/usr/bin/env python3
import os
import subprocess

def update_sequence_reassurance():
    filepath = 'week1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    old_intro = (
        '<strong>Discrete modeling:</strong> Sequences are functions '
        '$f: \\mathbb{N} \\to \\mathbb{R}$ mapping indices to real values.'
    )
    new_intro = (
        '<strong>Think of a sequence simply as an endless ordered list</strong> '
        '—like a musical playlist or numbered parking spots—where every step '
        'has its own designated number.'
    )

    if old_intro in content:
        content = content.replace(old_intro, new_intro)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully updated sequence mechanics intro with friendly reassurance.")
    else:
        print("Warning: Target text not found.")

def execute_git_sync():
    commit_message = (
        "Warm up sequence mechanics intro with friendly reassurance\n\n"
        "Replaced clinical intro in week1.html with a comforting, accessible\n"
        "explanation of sequences for beginners."
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
    update_sequence_reassurance()
    execute_git_sync()
