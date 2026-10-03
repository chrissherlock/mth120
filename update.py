#!/usr/bin/env python3
import os
import subprocess

def add_intro_explanation_before_definition():
    filepath = 'week2.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The explanatory bridge text to insert right before the formal definition paragraph
    intro_bridge = r'''
            <p>Before looking at the formal symbols, let's build the intuition: Saying a sequence converges to $L$ means that if you look far enough down the list, every subsequent term gets arbitrarily close to $L$ and stays there. We want a mathematical way to guarantee this "trapping" behavior.</p>
            <p>A sequence $(a_n)$ converges to a limit $L$, written $\lim_{n\to\infty} a_n = L$, if:</p>'''

    old_target = r'''<p>A sequence $(a_n)$ converges to a limit $L$, written $\lim_{n\to\infty} a_n = L$, if:</p>'''

    if old_target in content and 'Before looking at the formal symbols' not in content:
        content = content.replace(old_target, intro_bridge, 1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully added introductory explanation before formal definition in week2.html.")
    else:
        print("Target not found or introductory text already present.")

def execute_git_sync():
    commit_message = (
        "Add intuitive preparatory conceptual bridge before formal epsilon-N definition\n\n"
        "Expanded week2.html with an explanatory introductory paragraph right before\n"
        "the formal limit definition to clarify what convergence means intuitively."
    )
    commands = [
        ['git', 'add', 'week2.html', 'update.py'],
        ['git', 'commit', '-m', commit_message],
        ['git', 'push', 'origin', 'main']
    ]
    for cmd in commands:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(f"> {' '.join(cmd)}\n{result.stdout}{result.stderr}")

if __name__ == '__main__':
    add_intro_explanation_before_definition()
    execute_git_sync()
