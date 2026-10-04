#!/usr/bin/env python3
import os
import subprocess

def simplify_domain_intro():
    filepath = 'week1-lecture1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    old_text = (
        "In computational calculus, domain and range are often treated as "
        "afterthought restrictions discovered by dodging division by zero or "
        "negative square roots. In pure analysis, we invert that mindset: a "
        "mapping is defined by its source and target sets right from the start."
    )

    new_text = (
        "Previously, domain and range were mostly an afterthought—something "
        "you checked to avoid dividing by zero. In pure analysis, we declare "
        "them upfront: a function cannot exist without an explicit starting "
        "set and target set."
    )

    if old_text in content:
        content = content.replace(old_text, new_text, 1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully simplified the introductory phrasing in Subsection 3.1.")
    else:
        print("Could not locate the exact phrase in week1-lecture1.html.")

def synchronize_git_changes():
    commit_message = (
        "Simplify domain/range contrast phrasing in Subsection 3.1\n\n"
        "Streamlined the opening paragraph of Subsection 3.1 in\n"
        "week1-lecture1.html to remove cumbersome phrasing regarding division by\n"
        "zero, keeping the conversational tone collegiate and punchy."
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
    simplify_domain_intro()
    synchronize_git_changes()
