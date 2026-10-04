#!/usr/bin/env python3
import os
import subprocess

def insert_peano_wiki_links():
    filepath = 'week1-lecture1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Targets within the biography card
    old_author = "<strong>Giuseppe Peano</strong> was an Italian mathematician"
    new_author = (
        '<strong><a href="https://en.wikipedia.org/wiki/Giuseppe_Peano" '
        'target="_blank" rel="noopener noreferrer" '
        'style="color: var(--accent); text-decoration: underline;">Giuseppe Peano</a></strong> '
        'was an Italian mathematician'
    )

    old_treatise = "<em>Arithmetices principia, nova methodo exposita</em>"
    new_treatise = (
        '<a href="https://en.wikipedia.org/wiki/Arithmetices_principia,_nova_methodo_exposita" '
        'target="_blank" rel="noopener noreferrer" '
        'style="color: var(--accent); font-style: italic; text-decoration: underline;">'
        'Arithmetices principia, nova methodo exposita</a>'
    )

    if old_author in content and old_treatise in content:
        content = content.replace(old_author, new_author, 1)
        content = content.replace(old_treatise, new_treatise, 1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully integrated Wikipedia reference links into week1-lecture1.html.")
    else:
        print("Target biography text not found. The links may have already been applied.")

def synchronize_git_changes():
    commit_message = (
        "Add Wikipedia reference links to Giuseppe Peano infobox\n\n"
        "Added external links to Wikipedia for Giuseppe Peano and his 1889\n"
        "treatise Arithmetices principia, nova methodo exposita within the\n"
        "biographical card in week1-lecture1.html."
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
    insert_peano_wiki_links()
    synchronize_git_changes()
