#!/usr/bin/env python3
import os
import subprocess
import re

def soften_lecture3_description():
    filepath = 'week1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_description = (
        "See how simple lists open the door to limits. We explore sequences "
        "both as everyday ordered lists and as functions on the counting numbers, "
        "use visual tools to observe how their long-term behavior unfolds, "
        "and discover clever algebraic patterns—like telescoping sums and "
        "Gauss's formula—that make large calculations surprisingly clean."
    )

    # Match across whitespace, newlines, and variations in math rendering for N
    pattern = re.compile(
        r'Step\s+into\s+the\s+infinite\.\s*'
        r'We\s+examine\s+sequences\s+through\s+dual\s+lenses\s*'
        r'\(ordered\s+lists\s+vs\.\s+functions\s+on\s*.*?N.*?\),\s*'
        r'observe\s+finite\s+samples\s+versus\s+infinite\s+tails\s+via\s+an\s+interactive\s+SVG\s+visualization,\s*'
        r'analyze\s+discrete\s+rate\s+of\s+change\s+with\s+derived\s+sequences,\s*'
        r'and\s+collapse\s+telescoping\s+sums\s+to\s+discover\s+Gauss\'?s\s+formula\.',
        re.IGNORECASE | re.DOTALL
    )

    match = pattern.search(content)
    if match:
        content = content[:match.start()] + new_description + content[match.end():]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully updated Lecture 3 summary in week1.html.")
        return True

    # Substring fallback
    for anchor in ["Step into the infinite", "examine sequences through dual lenses"]:
        if anchor in content:
            start_idx = content.find(anchor)
            end_idx = content.find("</p>", start_idx)
            if end_idx != -1:
                content = content[:start_idx] + new_description + content[end_idx:]
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print("Successfully updated Lecture 3 summary via fallback anchor.")
                return True

    print("Could not find the original Lecture 3 description in week1.html.")
    return False

def synchronize_git_changes():
    commit_message = (
        "Revise Lecture 3 overview in week1.html to supportive tone\n\n"
        "Softened the description of Lecture 3 in week1.html to make the study\n"
        "of sequences approachable, highlighting intuitive list-based thinking,\n"
        "visual long-term behavior, and satisfying algebraic sum patterns."
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
    if soften_lecture3_description():
        synchronize_git_changes()
