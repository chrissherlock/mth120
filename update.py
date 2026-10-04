#!/usr/bin/env python3
import os
import subprocess
import re

def soften_lecture2_description():
    filepath = 'week1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_description = (
        "Uncover why fractions alone cannot capture every point on the number "
        "line. We look at the classic argument showing why numbers like "
        r"$\sqrt{2}$ cannot be written as simple fractions, introduce intuitive "
        "geometric tools for measuring distance, and see how the real numbers "
        "provide a seamless, gap-free continuum for the calculus ahead."
    )

    # Match across whitespace, newlines, and variations in math rendering for Q and sqrt(2)
    pattern = re.compile(
        r'Discover\s+why\s+fractions\s*\(.*?Q.*?\)\s*leave\s+tiny\s+gaps\s+along\s+the\s+line,\s*'
        r'examine\s+the\s+classical\s+proof\s+that\s*.*?2.*?\s*is\s+irrational,\s*'
        r'investigate\s+distance\s+metrics\s+and\s+the\s+Triangle\s+Inequality,\s*'
        r'and\s+study\s+the\s+Axiom\s+of\s+Completeness\s+that\s+guarantees\s+the\s+continuum\s+of\s+real\s+numbers\.',
        re.IGNORECASE | re.DOTALL
    )

    match = pattern.search(content)
    if match:
        content = content[:match.start()] + new_description + content[match.end():]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully updated Lecture 2 summary in week1.html.")
        return True

    # Substring fallback
    for anchor in ["Discover why fractions", "leave tiny gaps along the line"]:
        if anchor in content:
            start_idx = content.find(anchor)
            end_idx = content.find("</p>", start_idx)
            if end_idx != -1:
                content = content[:start_idx] + new_description + content[end_idx:]
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print("Successfully updated Lecture 2 summary via fallback anchor.")
                return True

    print("Could not find the original Lecture 2 description in week1.html.")
    return False

def synchronize_git_changes():
    commit_message = (
        "Revise Lecture 2 overview in week1.html to supportive tone\n\n"
        "Softened the description of Lecture 2 in week1.html to make the jump\n"
        "from rational numbers to the real continuum approachable, framing the\n"
        "irrationality of sqrt(2) and completeness as resolving natural geometric\n"
        "puzzles rather than abstract formal hurdles."
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
    if soften_lecture2_description():
        synchronize_git_changes()
