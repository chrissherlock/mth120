#!/usr/bin/env python3
import os
import re
import subprocess

def purge_all_citations():
    files_to_clean = ['week1.html', 'week2.html', 'index.html', 'update.py'
    # Corrected pattern targeting blocks
    citation_pattern = re.compile(r'\*\')

    for filename in files_to_clean:
        if not os.path.exists(filename):
            continue
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        cleaned_content, count = citation_pattern.subn('', content)
        if count > 0:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(cleaned_content)
            print(f"Successfully purged {count} citation(s) from {filename}.")
        else:
            print(f"No citations found in {filename}.")

def execute_git_sync():
    commit_message = (
        "Fix regex pattern to thoroughly purge all bracketed citations\n\n"
        "Updated citation regex from escaped plus/bracket to*\n"
        "to successfully strip all remaining reference markers from the repo."
    )
    commands = [
        ['git', 'add', 'week1.html', 'week2.html', 'index.html', 'update.py',
        ['git', 'commit', '-m', commit_message,
        ['git', 'push', 'origin', 'main'
    
    for cmd in commands:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(f"> {' '.join(cmd)}\n{result.stdout}{result.stderr}")

if __name__ == '__main__':
    print("Purging all citations with correct regex...")
    purge_all_citations()
    print("Syncing with GitHub...")
    execute_git_sync()
    print("Purge complete.")
