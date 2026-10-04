#!/usr/bin/env python3
import os
import subprocess

def update_roadmap_introduction():
    filepath = 'week1-lecture1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    old_intro = (
        "To make studying manageable and maintain deep conceptual clarity, "
        "the material is organised into three focused lectures:"
    )

    new_intro = (
        "Transitioning from computational calculus to formal analysis can feel like "
        "learning a completely new language. In earlier courses, you learned how to "
        "calculate answers; here, we explore why those calculations hold true and "
        "how to construct airtight proofs from the ground up.\n\n"
        "            Because rebuilding your mathematical foundation from first principles "
        "is conceptually demanding, Week 1 is deliberately broken into three progressive stages. "
        "Rather than rushing straight into limits, each lecture focuses on mastering one layer "
        "of the foundation before building the next:"
    )

    if old_intro in content:
        content = content.replace(old_intro, new_intro, 1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully updated the roadmap introduction with pedagogical framing.")
    else:
        print("Could not find the target roadmap sentence in week1-lecture1.html.")

def synchronize_git_changes():
    commit_message = (
        "Revise Week 1 roadmap with reassuring pedagogical rationale\n\n"
        "Replaced the terse logistical roadmap sentence in week1-lecture1.html\n"
        "with a supportive, collegiate introduction explaining the pedagogical\n"
        "rationale behind dividing Week 1 into three progressive lectures."
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
    update_roadmap_introduction()
    synchronize_git_changes()
