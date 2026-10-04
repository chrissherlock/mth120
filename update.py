#!/usr/bin/env python3
import os
import subprocess

def add_welcome_narrative():
    filepath = 'index.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    target_anchor = '<div class="welcome-image-wrapper">'

    welcome_narrative = (
        '<div class="welcome-image-wrapper">\n'
        '                    <img src="images/welcome-mth120.jpeg" alt="Overview Map of Course Mathematics" class="welcome-image">\n'
        '                </div>\n\n'
        '                <!-- Reassuring Course Overview Narrative -->\n'
        '                <div style="background: #ffffff; border: 1px solid #fed7aa; border-radius: 6px; padding: 1.25rem 1.5rem; margin-bottom: 1.5rem;">\n'
        '                    <p style="margin: 0 0 0.75rem 0; color: #334155; font-size: 0.98rem; line-height: 1.65;">\n'
        '                        Whether you are meeting formal proofs for the first time or revisiting calculus from a rigorous perspective, this companion is designed to walk alongside you every step of the way. You won\'t have to navigate abstract concepts alone: each module breaks down complex ideas into intuitive visual steps, connecting the everyday mechanics of numbers and functions to the foundational logic that holds them together.\n'
        '                    </p>\n'
        '                    <p style="margin: 0; color: #334155; font-size: 0.98rem; line-height: 1.65;">\n'
        '                        Over the coming weeks, our journey is structured around four interconnected pillars—moving from the bedrock of sets and limits through continuous change, accumulation, and finally into the multidimensional geometry of linear algebra. Take your time, explore the interactive visual tools, and remember that deep mathematical understanding is built one careful question at a time.\n'
        '                    </p>\n'
        '                </div>'
    )

    if target_anchor in content and "Whether you are meeting formal proofs" not in content:
        content = content.replace(target_anchor, welcome_narrative, 1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully added the warm overview narrative beneath the hero image.")
        return True
    elif "Whether you are meeting formal proofs" in content:
        print("Overview narrative is already present in index.html.")
        return True
    else:
        print("Could not find the target welcome-image-wrapper anchor in index.html.")
        return False

def synchronize_git_changes():
    commit_message = (
        "Add welcoming course overview paragraph beneath hero image in index.html\n\n"
        "Included a warm, friendly explanatory paragraph directly beneath the\n"
        "hero image in index.html to reassure incoming students and guide their\n"
        "expectations across the four core mathematical pillars of the unit."
    )
    commands = [
        ['git', 'add', 'index.html', 'update.py'],
        ['git', 'commit', '-m', commit_message],
        ['git', 'push', 'origin', 'main']
    ]
    for cmd in commands:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(f"> {' '.join(cmd)}\n{result.stdout}{result.stderr}")

if __name__ == '__main__':
    if add_welcome_narrative():
        synchronize_git_changes()
