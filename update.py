#!/usr/bin/env python3
import os
import subprocess

def expand_sequence_definition():
    filepath = 'week1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    old_target = 'A sequence is an ordered list of numbers indexed by $\\mathbb{N}$ (formally, a function mapping $\\mathbb{N}$ to $\\mathbb{R}$). We can define them explicitly with a closed-form rule or recursively relative to previous terms.'

    new_expansion = r'''<p>To truly grasp what a sequence is, it helps to look at it through two complementary lenses—one intuitive and one rigorous:</p>
            <ul style="margin: 0.5rem 0 1rem 1.25rem; padding: 0;">
                <li style="margin-bottom: 0.6rem;"><strong>1. The List View (Intuitive):</strong> An endless, ordered string of numbers written as $(a_n) = (a_1, a_2, a_3, a_4, \dots)$. Order matters deeply here: the sequence $(1, 2, 3, \dots)$ is entirely different from $(3, 2, 1, \dots)$. Every number has a definite position.</li>
                <li style="margin-bottom: 0.6rem;"><strong>2. The Function View (Rigorous):</strong> Formally, a sequence is a function whose domain is the natural numbers $\mathbb{N}$ (or $\mathbb{Z}_+$) and whose codomain is the real numbers $\mathbb{R}$. Instead of writing $f(n)$, mathematicians use subscript notation $a_n$:
                    <ul style="margin: 0.3rem 0 0.3rem 1.25rem; padding: 0;">
                        <li><strong>Input ($n$):</strong> The position or index (e.g., $1, 2, 3, \dots$).</li>
                        <li><strong>Output ($a_n$):</strong> The actual real number sitting at that position.</li>
                    </ul>
                </li>
            </ul>
            <p>We can define these mappings either explicitly with a closed-form rule or recursively relative to previous terms.</p>'''

    if old_target in content:
        content = content.replace(old_target, new_expansion)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully expanded sequence definition in week1.html.")
    else:
        print("Old target text not found in week1.html.")

def execute_git_sync():
    commit_message = (
        "Expand and clarify sequence definition in week1.html\n\n"
        "Added a detailed breakdown explaining sequences through both an intuitive\n"
        "list view and a rigorous function mapping view in week1.html."
    )
    commands = [
        ['git', 'add', 'week1.html', 'update.py'],
        ['git', 'commit', '-m', commit_message],
        ['git', 'push', 'origin', 'main']
    ]
    for cmd in commands:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(f"> {' '.join(cmd)}\n{result.stdout}{result.stderr}")

if __name__ == '__main__':
    expand_sequence_definition()
    execute_git_sync()
