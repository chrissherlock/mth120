#!/usr/bin/env python3
import os
import subprocess
import re

def update_week1_overview():
    filepath = 'week1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found in current directory.")
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_intro = (
        "<p style=\"font-size: 1.02rem; line-height: 1.7; color: #334155; margin-bottom: 1rem;\">\n"
        "                Transitioning from computational calculus to formal analysis can feel like "
        "learning a completely new language. In earlier courses, you learned how to calculate answers; "
        "here, we explore why those calculations hold true and how to construct airtight proofs from "
        "the ground up.\n"
        "            </p>\n"
        "            <p style=\"font-size: 1.02rem; line-height: 1.7; color: #334155; margin-bottom: 1.25rem;\">\n"
        "                Because rebuilding your mathematical foundation from first principles is "
        "conceptually demanding, Week 1 is deliberately broken into three progressive stages. "
        "Rather than rushing straight into limits, each lecture focuses on mastering one layer of the "
        "foundation before building the next:\n"
        "            </p>"
    )

    pattern = re.compile(
        r'<p[^>]*>\s*To\s+make\s+studying\s+manageable\s+and\s+maintain\s+deep\s+conceptual\s+clarity,\s*'
        r'the\s+material\s+is\s+organi[sz]ed\s+into\s+three\s+focused\s+lectures:?\s*</p>',
        re.IGNORECASE | re.DOTALL
    )

    match = pattern.search(content)
    if match:
        content = content[:match.start()] + new_intro + content[match.end():]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully updated the roadmap introduction in week1.html.")
        return True

    # Fallback to bare sentence match if not enclosed in standard <p> tags
    core_pattern = re.compile(
        r'To\s+make\s+studying\s+manageable\s+and\s+maintain\s+deep\s+conceptual\s+clarity,\s*'
        r'the\s+material\s+is\s+organi[sz]ed\s+into\s+three\s+focused\s+lectures:?',
        re.IGNORECASE | re.DOTALL
    )
    core_match = core_pattern.search(content)
    if core_match:
        content = content[:core_match.start()] + new_intro + content[core_match.end():]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully updated the roadmap introduction in week1.html (via core match).")
        return True

    print("Diagnostic: Could not match the roadmap phrase in week1.html.")
    for line in content.splitlines():
        if any(term in line.lower() for term in ["manageable", "three focused lectures", "three lectures"]):
            print(f"  FOUND LINE: {repr(line)}")
    return False

def synchronize_git_changes():
    commit_message = (
        "Revise Week 1 roadmap in week1.html with pedagogical framing\n\n"
        "Replaced the logistical roadmap sentence in week1.html with a\n"
        "supportive introduction explaining why the week is divided into three\n"
        "progressive lectures to ease the transition from calculus to analysis."
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
    if update_week1_overview():
        synchronize_git_changes()
