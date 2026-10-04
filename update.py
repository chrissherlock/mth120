#!/usr/bin/env python3
import os
import subprocess
import re

def update_index_subtitle_option_1():
    filepath = 'index.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_subtitle = (
        "A companion guide to real analysis—designed to build your "
        "mathematical intuition through clear explanations, interactive visuals, "
        "and step-by-step proofs."
    )

    pattern = re.compile(
        r'Personal\s+reference\s+companion,\s*interactive\s+pedagogical\s+tools,\s*'
        r'and\s+derivations\s+aligned\s+with\s+the\s+unit\s+schedule\.?',
        re.IGNORECASE | re.DOTALL
    )

    match = pattern.search(content)
    if match:
        content = content[:match.start()] + new_subtitle + content[match.end():]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully updated course subtitle in index.html to Option 1.")
        return True

    anchor = "Personal reference companion"
    if anchor in content:
        start_idx = content.find(anchor)
        end_idx = content.find("</p>", start_idx)
        if end_idx == -1:
            end_idx = content.find("</div>", start_idx)
        if end_idx != -1:
            content = content[:start_idx] + new_subtitle + content[end_idx:]
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print("Successfully updated course subtitle in index.html via fallback anchor.")
            return True

    print("Could not locate the target subtitle in index.html.")
    return False

def synchronize_git_changes():
    commit_message = (
        "Apply Option 1 to course subtitle in index.html\n\n"
        "Replaced the administrative subtitle in index.html with a welcoming\n"
        "tagline emphasizing mathematical intuition, clear explanations,\n"
        "interactive visual tools, and step-by-step proofs."
    )
    commands = [
        ['git', 'add', 'index.html', 'update.py'],
        ['git', 'commit', '-m', commit_message],
        ['git', 'push', 'origin', 'main']
    ]
    for cmd in commands:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(f"> {' '.join(cmd)}\n{result.stdout}{result.stderr}")

if __name__ == '__main__':
    if update_index_subtitle_option_1():
        synchronize_git_changes()
