#!/usr/bin/env python3
import os
import re
import subprocess

def remove_section_symbols():
    files_to_clean = ['week1.html', 'week2.html', 'index.html', 'update.py']
    section_pattern = re.compile(r'\s*\(§[0-9]+\)')

    for filename in files_to_clean:
        if not os.path.exists(filename):
            continue
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        cleaned_content, count = section_pattern.subn('', content)
        if count > 0:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(cleaned_content)
            print(f"Successfully removed {count} section reference(s) from {filename}.")
        else:
            print(f"No section references found in {filename}.")

def execute_git_sync():
    commit_message = (
        "Remove textbook section references like from headings and TOC\n\n"
        "Stripped out all section number markers across week1.html, week2.html,\n"
        "and index.html for a cleaner, more approachable course layout."
    )
    commands = [
        ['git', 'add', 'week1.html', 'week2.html', 'index.html', 'update.py'],
        ['git', 'commit', '-m', commit_message],
        ['git', 'push', 'origin', 'main']
    ]
    for cmd in commands:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(f"> {' '.join(cmd)}\n{result.stdout}{result.stderr}")

if __name__ == '__main__':
    print("Removing section symbols (§N)...")
    remove_section_symbols()
    print("Syncing with GitHub...")
    execute_git_sync()
    print("Update complete.")
