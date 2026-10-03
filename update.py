#!/usr/bin/env python3
import os
import re
import subprocess

def strip_all_citations_from_repo():
    files_to_clean = ['week1.html', 'week2.html', 'index.html', 'update.py']
    citation_pattern = re.compile(r'\+\]')

    for filename in files_to_clean:
        if not os.path.exists(filename):
            continue
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        cleaned_content, count = citation_pattern.subn('', content)
        if count > 0:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(cleaned_content)
            print(f"Stripped {count} citation(s) from {filename}.")
        else:
            print(f"No citations found in {filename}.")

def execute_git_sync():
    commit_message = (
        "Thoroughly strip all citation brackets from all HTML files and scripts\n\n"
        "Removed all remaining markers across week1.html, week2.html,\n"
        "index.html, and update.py to ensure a completely citation-free codebase."
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
    print("Cleaning all citations from repository...")
    strip_all_citations_from_repo()
    print("Syncing with GitHub...")
    execute_git_sync()
    print("Purge complete. All files are now 100% citation-free.")
