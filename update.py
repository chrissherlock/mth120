#!/usr/bin/env python3
import os
import subprocess

def correct_descartes_image_path():
    filepath = 'week1-lecture1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    old_src = 'src="images/decartes.jpg"'
    new_src = 'src="images/descartes.jpg"'

    if old_src in content:
        content = content.replace(old_src, new_src, 1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully updated Descartes image path to images/descartes.jpg.")
    elif new_src in content:
        print("Image path is already set to images/descartes.jpg.")
    else:
        print("Could not find Descartes image tag in week1-lecture1.html.")

def synchronize_git_changes():
    commit_message = (
        "Fix image filename path for René Descartes portrait\n\n"
        "Corrected the image path for René Descartes from images/decartes.jpg to\n"
        "images/descartes.jpg in week1-lecture1.html so the portrait loads\n"
        "reliably in the Section 2 biography box."
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
    correct_descartes_image_path()
    synchronize_git_changes()
