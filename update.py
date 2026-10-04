#!/usr/bin/env python3
import os
import subprocess
import re

def update_russell_clarification():
    filepath = 'week1-lecture1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Target old phrasing and new clarified phrasing
    old_target = "formulated <strong><a href=\"https://en.wikipedia.org/wiki/Russell%27s_paradox\" target=\"_blank\" rel=\"noopener noreferrer\" style=\"color: #4f46e5; text-decoration: underline;\">Russell's Paradox</a></strong>, considering the set $R$"
    new_replacement = "formulated <strong><a href=\"https://en.wikipedia.org/wiki/Russell%27s_paradox\" target=\"_blank\" rel=\"noopener noreferrer\" style=\"color: #4f46e5; text-decoration: underline;\">Russell's Paradox</a></strong> — the set of all sets that don't contain themselves — considering the set $R$"

    if new_replacement in content:
        print("Clarification already present in week1-lecture1.html.")
        return True

    if old_target in content:
        content = content.replace(old_target, new_replacement, 1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully added Russell's Paradox set definition clarification in week1-lecture1.html.")
        return True

    print("Error: Could not locate the target phrasing in week1-lecture1.html.")
    return False

def synchronize_git_changes():
    commit_message = (
        "Clarify Russell's Paradox definition in Cantor biographical box\n\n"
        "Appended \"- the set of all sets that don't contain themselves -\" directly\n"
        "after Russell's Paradox in the Cantor biographical card in week1-lecture1.html."
    )
    commands = [
        ['git', 'add', 'week1-lecture1.html', 'update.py'],
        ['git', 'commit', '-m', commit_message],
        ['git', 'push', 'origin', 'main']
    ]
    for cmd in commands:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(f"> {' '.join(cmd)}\n{result.stdout}{result.stderr}")

if __name__ == '__main__':
    if update_russell_clarification():
        synchronize_git_changes()
