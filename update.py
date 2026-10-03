#!/usr/bin/env python3
import os
import subprocess

def fix_sequence_definition():
    filepath = 'week1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    old_text = 'A sequence is an ordered list of numbers mapping indices from $\\mathbb{N}$ to $\\mathbb{R}$. We can define them explicitly with a closed-form rule or recursively relative to previous terms.'
    new_text = 'A sequence is an ordered list of numbers indexed by $\\mathbb{N}$ (formally, a function mapping $\\mathbb{N}$ to $\\mathbb{R}$). We can define them explicitly with a closed-form rule or recursively relative to previous terms.'

    if old_text in content:
        content = content.replace(old_text, new_text)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully updated sequence definition in week1.html.")
    else:
        print("Exact sequence text not found.")

def execute_git_sync():
    commit_message = (
        "Refine sequence definition wording in week1.html\n\n"
        "Corrected imprecise phrasing regarding domain mapping and index sets\n"
        "in Section 3 of week1.html."
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
    fix_sequence_definition()
    execute_git_sync()
