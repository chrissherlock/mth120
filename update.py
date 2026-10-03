#!/usr/bin/env python3
import os
import subprocess

def add_archery_svg_to_week2():
    filepath = 'week2.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    archery_svg = r'''
                <div style="display: flex; justify-content: center; margin: 1.25rem 0 0.5rem 0;">
                    <svg viewBox="0 0 220 140" style="max-width: 200px; height: auto;">
                        <!-- Target Board Outer Ring -->
                        <circle cx="110" cy="70" r="55" fill="#e2e8f0" stroke="#cbd5e1" stroke-width="2"/>
                        <!-- Epsilon Tolerance Band -->
                        <circle cx="110" cy="70" r="38" fill="#fef3c7" stroke="#f59e0b" stroke-width="2"/>
                        <text x="110" y="42" font-family="sans-serif" font-size="9" font-weight="bold" fill="#d97706" text-anchor="middle">±ε Tolerance</text>
                        <!-- Bullseye (Limit L) -->
                        <circle cx="110" cy="70" r="18" fill="#fee2e2" stroke="#ef4444" stroke-width="2"/>
                        <circle cx="110" cy="70" r="6" fill="#ef4444"/>
                        <text x="110" y="66" font-family="sans-serif" font-size="8" font-weight="bold" fill="#991b1b" text-anchor="middle">L</text>

                        <!-- Arrow Shaft & Feathers (Diagonal Accent) -->
                        <line x1="30" y1="20" x2="105" y2="65" stroke="#0f172a" stroke-width="3" stroke-linecap="round"/>
                        <polygon points="105,65 95,60 100,55" fill="#0f172a"/>
                        <!-- Feather tail -->
                        <line x1="30" y1="20" x2="22" y2="15" stroke="#b45309" stroke-width="2"/>
                        <line x1="35" y1="25" x2="27" y2="20" stroke="#b45309" stroke-width="2"/>
                    </svg>
                </div>'''

    target_anchor = '<h4>💡 Plain-English Breakdown: What is this formula actually saying?</h4>'

    if target_anchor in content and 'Archery target' not in content and '<svg viewBox="0 0 220 140"' not in content:
        content = content.replace(target_anchor, target_anchor + '\n' + archery_svg)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully added archery SVG to week2.html.")
    else:
        print("Target anchor not found or SVG already present.")

def execute_git_sync():
    commit_message = (
        "Add decorative SVG archery target illustration to epsilon-N explanation\n\n"
        "Embedded a visual archery board graphic into week2.html to reinforce\n"
        "the target-band analogy used for the epsilon-N limit definition."
    )
    commands = [
        ['git', 'add', 'week2.html', 'update.py'],
        ['git', 'commit', '-m', commit_message],
        ['git', 'push', 'origin', 'main']
    ]
    for cmd in commands:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(f"> {' '.join(cmd)}\n{result.stdout}{result.stderr}")

if __name__ == '__main__':
    add_archery_svg_to_week2()
    execute_git_sync()
