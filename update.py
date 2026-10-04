#!/usr/bin/env python3
import os
import subprocess

def apply_biography_box_style():
    filepath = 'week1-lecture1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add CSS class if not present
    bio_css = (
        "\n        .biography-box { background: #f5f3ff; border: 1px solid #ddd6fe; "
        "border-left: 5px solid #6366f1; padding: 1.25rem 1.5rem; margin: 2rem 0; "
        "border-radius: 0 6px 6px 0; }\n"
        "        .biography-box h4 { margin-top: 0; color: #3730a3; font-size: 1.05rem; "
        "display: flex; align-items: center; gap: 0.5rem; }\n"
        "        .biography-box p, .biography-box li { color: #0f172a !important; }"
    )

    style_end_tag = '</style>'
    if '.biography-box' not in content and style_end_tag in content:
        content = content.replace(style_end_tag, bio_css + '\n    ' + style_end_tag, 1)

    # 2. Update Peano box container to use .biography-box
    old_box_start = (
        '<!-- HISTORICAL CONTEXT: GIUSEPPE PEANO -->\n'
        '            <div class="infobox" style="margin-top: 2rem; margin-bottom: 2rem;">\n'
        '                <h4>📖 Who was Giuseppe Peano?</h4>'
    )

    new_box_start = (
        '<!-- HISTORICAL CONTEXT: GIUSEPPE PEANO -->\n'
        '            <div class="biography-box">\n'
        '                <h4>🏛️ Who was Giuseppe Peano?</h4>'
    )

    if old_box_start in content:
        content = content.replace(old_box_start, new_box_start, 1)
        # Update link color inside to match indigo scheme
        content = content.replace(
            'style="color: var(--accent); text-decoration: underline;"',
            'style="color: #4f46e5; text-decoration: underline;"'
        )
        content = content.replace(
            'style="color: var(--accent); font-style: italic; text-decoration: underline;"',
            'style="color: #4f46e5; font-style: italic; text-decoration: underline;"'
        )

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully applied .biography-box to Giuseppe Peano in week1-lecture1.html.")
    else:
        print("Could not find the target Peano markup block in week1-lecture1.html.")

def synchronize_git_changes():
    commit_message = (
        "Add dedicated styling for biographical and historical infoboxes\n\n"
        "Introduced .biography-box with an indigo and soft lavender palette to\n"
        "distinguish historical profiles from mathematical definitions and\n"
        "worked examples. Updated the Giuseppe Peano biography in\n"
        "week1-lecture1.html to adopt the new style."
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
    apply_biography_box_style()
    synchronize_git_changes()
