#!/usr/bin/env python3
import os
import re
import subprocess

def fix_epsilon_boundary_arrows():
    filepath = 'week2.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The new replacement block with horizontal arrows pointing to the bounds
    new_block = r'''// --- UPDATED: L+eps and L-eps Labels pointing horizontally to the boundaries ---
            svgContent += `
                <!-- Top Boundary Label & Horizontal Arrow -->
                <text x="${originX - 65}" y="${topY + 4}" font-family="sans-serif" font-size="11" font-weight="bold" fill="#d97706">L+&epsilon;</text>
                <line x1="${originX - 35}" y1="${topY}" x2="${originX - 6}" y2="${topY}" stroke="#d97706" stroke-width="1.5"/>
                <polygon points="${originX - 2},${topY} ${originX - 8},${topY - 3.5} ${originX - 8},${topY + 3.5}" fill="#d97706"/>

                <!-- Bottom Boundary Label & Horizontal Arrow -->
                <text x="${originX - 63}" y="${bottomY + 4}" font-family="sans-serif" font-size="11" font-weight="bold" fill="#d97706">L-&epsilon;</text>
                <line x1="${originX - 35}" y1="${bottomY}" x2="${originX - 6}" y2="${bottomY}" stroke="#d97706" stroke-width="1.5"/>
                <polygon points="${originX - 2},${bottomY} ${originX - 8},${bottomY - 3.5} ${originX - 8},${bottomY + 3.5}" fill="#d97706"/>
            `;
            // -------------------------------------------------------------------------'''

    # Locate the old vertical arrow block and replace it
    pattern = r'// --- NEW: L\+eps and L-eps Labels with Arrows ---[\s\S]*?// -----------------------------------------------'

    if re.search(pattern, content):
        content = re.sub(pattern, lambda _: new_block, content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully updated arrows to point horizontally at the region boundaries in week2.html.")
    else:
        print("Could not locate the previous arrow block in week2.html.")

def execute_git_sync():
    commit_message = (
        "Fix epsilon region boundary arrows in week2.html\n\n"
        "Changed the L±ε arrows from vertical distance spans to horizontal pointers. \n"
        "The arrows now originate from the text labels and point directly at the \n"
        "top and bottom dashed boundary lines of the tolerance band."
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
    fix_epsilon_boundary_arrows()
    execute_git_sync()
