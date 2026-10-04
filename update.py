#!/usr/bin/env python3
import os
import subprocess

def retitle_descartes_box():
    filepath = 'week1-lecture1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    old_heading = '<h4>🏛️ Who was René Descartes?</h4>'
    new_heading = '<h4>🏛️ Why is it called a "Cartesian" Product? (René Descartes)</h4>'

    if old_heading in content:
        content = content.replace(old_heading, new_heading, 1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully retitled the Descartes biographical infobox.")
    elif new_heading in content:
        print("Descartes infobox is already using the updated heading.")
    else:
        print("Could not find the target heading in week1-lecture1.html.")

def synchronize_git_changes():
    commit_message = (
        "Refactor Descartes infobox title to focus on Cartesian origin\n\n"
        "Retitled the Section 2 biographical card in week1-lecture1.html from\n"
        "\"Who was René Descartes?\" to \"Why is it called a 'Cartesian' Product?\n"
        "(René Descartes)\" to provide a natural pedagogical connection to the\n"
        "preceding material on ordered pairs."
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
    retitle_descartes_box()
    synchronize_git_changes()
