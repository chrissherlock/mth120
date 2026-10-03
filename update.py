#!/usr/bin/env python3
import re
import subprocess
import sys

def patch_subset_readability():
    filepath = 'week1.html'
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: {filepath} not found.")
        sys.exit(1)

    target_pattern = r'<p>A set \$A\$ is a <strong>subset</strong> of \$B\$[\s\S]*?satisfies \$\\emptyset \\subseteq A\$ for every set \$A\$\.</p>'

    replacement = r'''<div class="definition-box">
                <p><strong>Subsets and Proper Subsets:</strong></p>
                <ul>
                    <li>
                        <strong>Subset ($A \subseteq B$):</strong> Every element of $A$ belongs to $B$. Formally, if $x \in A$, then $x \in B$.
                    </li>
                    <li>
                        <strong>Proper Subset ($A \subset B$):</strong> $A \subseteq B$ and $A \neq B$. In other words, every element of $A$ is in $B$, but $B$ contains at least one element not in $A$.
                    </li>
                    <li>
                        <strong>The Empty Set ($\emptyset \subseteq A$):</strong> The empty set contains no elements, so the conditional requirement for subset inclusion is never broken. Thus, $\emptyset \subseteq A$ holds for every set $A$.
                    </li>
                </ul>
            </div>'''

    new_content, count = re.subn(target_pattern, lambda _: replacement, content)

    if count == 0:
        # Fallback search if spacing or tags vary slightly
        fallback_pattern = r'A set \$A\$ is a <strong>subset</strong> of \$B\$[\s\S]*?for every set \$A\$\.'
        new_content, count = re.subn(fallback_pattern, lambda _: replacement, content)

    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Successfully updated subset section in {filepath}.")
    else:
        print("Warning: Target paragraph not found. No changes made.")

def execute_git_sync():
    commit_message = (
        "Format subset and empty set definitions into structured list\n\n"
        "Replaced dense prose block in week1.html with an itemized breakdown of\n"
        "subsets, proper subsets, and empty set properties for readability."
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
    patch_subset_readability()
    execute_git_sync()
