#!/usr/bin/env python3
import os
import subprocess
import re

def update_cantor_biography():
    filepath = 'week1-lecture1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The new paragraph to append inside Cantor's biographical card
    russell_paragraph = (
        '                        <p style="color: #334155; line-height: 1.65; font-size: 0.96rem; margin-bottom: 0;">\n'
        '                            <strong>The Shadow of Paradox:</strong> However, allowing any arbitrary property to define a set ("naive set theory") soon revealed cracks in paradise. In 1901, philosopher and logician Bertrand Russell formulated <strong><a href="https://en.wikipedia.org/wiki/Russell%27s_paradox" target="_blank" rel="noopener noreferrer" style="color: #4f46e5; text-decoration: underline;">Russell\'s Paradox</a></strong>, considering the set $R$ of all sets that do not contain themselves ($R = \\{x \\mid x \\notin x\\}$). Asking whether $R \\in R$ leads to an inescapable contradiction ($R \\in R \\iff R \\notin R$). This stunning realization proved that set theory needed rigorous axiomatic guardrails—inspiring the modern Zermelo-Fraenkel foundations that keep our mathematical house standing today.\n'
        '                        </p>\n'
    )

    # Check if already added
    if "Russell's Paradox" in content:
        print("Russell's Paradox correspondence is already present in week1-lecture1.html.")
        return True

    # Target anchor: the closing tags of the last paragraph inside Cantor's bio box
    # We look for Cantor's section header and find the paragraph containing "paradise that Cantor has created"
    anchor_pattern = re.compile(
        r'(Georg Cantor.*?David Hilbert to declare:\s*<em>"No one shall expel us from the paradise that Cantor has created\."</em>\s*</p>\s*)',
        re.DOTALL | re.IGNORECASE
    )

    match = anchor_pattern.search(content)
    if match:
        insertion_point = match.end()
        content = content[:insertion_point] + russell_paragraph + content[insertion_point:]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully added Russell's Paradox to Georg Cantor's biography in week1-lecture1.html.")
        return True

    print("Error: Could not locate the target anchor in Cantor's biography block.")
    return False

def synchronize_git_changes():
    commit_message = (
        "Add Russell's Paradox correspondence to Cantor biographical box\n\n"
        "Expanded the Georg Cantor biography box in week1-lecture1.html to include\n"
        "a discussion on Russell's Paradox and its foundational impact on naive set\n"
        "theory, complete with a Wikipedia hyperlink."
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
    if update_cantor_biography():
        synchronize_git_changes()
