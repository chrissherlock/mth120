#!/usr/bin/env python3
import os
import re
import subprocess

def strip_cautionary_contrast():
    filepath = 'week2-lecture5.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match the horizontal line, explanatory text, and the SVG container block
    pattern = (
        r'\s*<hr style="border: none; border-top: 1px solid #fde68a; margin: 1\.25rem 0;">\s*'
        r'<p><strong>Cautionary Contrast: What about \$\\frac\{n\}\{\\sin\(n\)\}\?</strong>.*?</p>\s*'
        r'<!-- Embedded Wild Divergence SVG -->\s*'
        r'<div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 6px; padding: 1rem; margin-top: 1rem;">\s*'
        r'<svg viewBox="0 0 800 240"[\s\S]*?</svg>\s*'
        r'</div>'
    )

    if re.search(pattern, content):
        content = re.sub(pattern, '', content, count=1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully removed the cautionary contrast section from week2-lecture5.html.")
    else:
        print("Could not match the cautionary contrast section. Check if it was already removed.")

def update_generator_script():
    script_path = 'update.py'
    if not os.path.exists(script_path):
        return

    with open(script_path, 'r', encoding='utf-8') as f:
        script_content = f.read()

    # Also remove it from the generate_lecture5_html() string template if present
    pattern = (
        r'\s*<hr style="border: none; border-top: 1px solid #fde68a; margin: 1\.25rem 0;">\s*'
        r'<p><strong>Cautionary Contrast: What about \$\\frac\{n\}\{\\sin\(n\)\}\?</strong>.*?</p>\s*'
        r'<!-- Embedded Wild Divergence SVG -->\s*'
        r'<div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 6px; padding: 1rem; margin-top: 1rem;">\s*'
        r'<svg viewBox="0 0 800 240"[\s\S]*?</svg>\s*'
        r'</div>'
    )

    if re.search(pattern, script_content):
        script_content = re.sub(pattern, '', script_content, count=1)
        with open(script_path, 'w', encoding='utf-8') as f:
            f.write(script_content)
        print("Updated template in update.py to omit cautionary contrast on future builds.")

def execute_git_sync():
    commit_message = (
        "Remove cautionary contrast section from week2-lecture5.html\n\n"
        "Excised the cautionary contrast paragraph and its accompanying wild\n"
        "divergence SVG graph for n / sin(n) from Lecture 5. This streamlines\n"
        "the Squeeze Theorem visualization to focus strictly on converging\n"
        "bounds."
    )
    commands = [
        ['git', 'add', 'week2-lecture5.html', 'update.py'],
        ['git', 'commit', '-m', commit_message],
        ['git', 'push', 'origin', 'main']
    ]
    for cmd in commands:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(f"> {' '.join(cmd)}\n{result.stdout}{result.stderr}")

if __name__ == '__main__':
    strip_cautionary_contrast()
    update_generator_script()
    execute_git_sync()
