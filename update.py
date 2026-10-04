#!/usr/bin/env python3
import os
import subprocess
import re

def apply_option_b_lecture1_summary():
    filepath = 'week1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    option_b_text = (
        "Build your confidence with the formal language of pure mathematics. "
        "Rather than memorizing formulas, we explore how sets clarify mathematical "
        "statements, demystify what functions actually do beneath the surface, "
        "and take a look behind the scenes at how the counting numbers are built "
        "from scratch."
    )

    # Patterns to match either the original wording or an already updated Option A
    patterns = [
        # Match original text
        re.compile(
            r'Master\s+the\s+formal\s+language\s+of\s+mathematics\.\s*'
            r'We\s+explore\s+set\s+operations,\s*compare\s+different\s+sizes\s+of\s+infinity\s*'
            r'\(.*?N.*?vs.*?R.*?\),\s*'
            r'analyze\s+functions\s+as\s+reliable\s+input-output\s+machines,\s*'
            r'and\s+construct\s+the\s+natural\s+numbers\s+from\s+scratch\s+using\s+Peano\'?s\s+5\s+axioms\.',
            re.IGNORECASE | re.DOTALL
        ),
        # Match Option A if previously applied
        re.compile(
            r'Get\s+comfortable\s+with\s+the\s+foundational\s+grammar\s+of\s+mathematics\.\s*'
            r'We\s+introduce\s+set\s+operations\s+to\s+organize\s+mathematical\s+ideas\s+clearly,\s*'
            r'look\s+at\s+how\s+functions\s+create\s+unambiguous\s+pairings\s+between\s+sets,\s*'
            r'and\s+explore\s+how\s+something\s+as\s+intuitive\s+as\s+counting\s+can\s+be\s+built\s*'
            r'from\s+five\s+simple,\s+elegant\s+rules\.',
            re.IGNORECASE | re.DOTALL
        )
    ]

    for pattern in patterns:
        match = pattern.search(content)
        if match:
            content = content[:match.start()] + option_b_text + content[match.end():]
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print("Successfully updated Lecture 1 summary to Option B in week1.html.")
            return True

    # Substring fallback for variations
    for anchor in ["Master the formal language", "Get comfortable with the foundational grammar"]:
        if anchor in content:
            start_idx = content.find(anchor)
            end_idx = content.find("</p>", start_idx)
            if end_idx != -1:
                content = content[:start_idx] + option_b_text + content[end_idx:]
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print("Successfully updated Lecture 1 summary via fallback anchor.")
                return True

    print("Could not locate the Lecture 1 summary paragraph in week1.html.")
    return False

def synchronize_git_changes():
    commit_message = (
        "Update Lecture 1 summary in week1.html to supportive tone (Option B)\n\n"
        "Revised the Lecture 1 summary card in week1.html using Option B to\n"
        "emphasise building confidence with formal mathematical language,\n"
        "shifting away from formula memorisation, and demystifying foundations."
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
    if apply_option_b_lecture1_summary():
        synchronize_git_changes()
