#!/usr/bin/env python3
import os
import re
import subprocess

def fix_peano_infobox_placement():
    filepath = 'week1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Strip out the infobox if it was already inserted to prevent duplicates
    infobox_pattern = r'\s*<div class="infobox">\s*<h4>📖 Notation Reference: Peano\'s Axioms</h4>[\s\S]*?</div>\s*'
    content = re.sub(infobox_pattern, '\n\n            ', content)

    # 2. Re-insert it exactly beneath the H3 tag
    h3_target = r"<h3>Building Numbers from Scratch: Peano's Axioms</h3>"

    correct_placement = r'''<h3>Building Numbers from Scratch: Peano's Axioms</h3>
            <div class="infobox">
                <h4>📖 Notation Reference: Peano's Axioms</h4>
                <div class="infobox-intro">
                    <strong>The DNA of counting:</strong> These five rules define the natural numbers exactly, ensuring we have a solid starting point and an unbroken, non-looping chain of steps.
                </div>
                <div class="notation-grid">
                    <div class="notation-item"><span class="notation-sym">$0 \in \mathbb{N}$</span><span class="notation-desc">Zero is a natural number (the starting line).</span></div>
                    <div class="notation-item"><span class="notation-sym">$S(n) \in \mathbb{N}$</span><span class="notation-desc">Every number has a unique successor (the next step).</span></div>
                    <div class="notation-item"><span class="notation-sym"><span style="white-space: nowrap;">$S(m) = S(n) \implies m = n$</span></span><span class="notation-desc">No merging paths (injectivity).</span></div>
                    <div class="notation-item"><span class="notation-sym">$S(n) \ne 0$</span><span class="notation-desc">No loops (zero is not a successor).</span></div>
                    <div class="notation-item"><span class="notation-sym">Induction</span><span class="notation-desc">No ghost chains (minimality condition).</span></div>
                </div>
            </div>'''

    if h3_target in content:
        content = content.replace(h3_target, correct_placement, 1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully placed the Peano's Axioms infobox beneath the heading.")
    else:
        print("Could not locate the Peano's Axioms heading.")

def execute_git_sync():
    commit_message = (
        "Move Peano's Axioms infobox below the section heading\n\n"
        "Relocated the Peano's Axioms notation infobox to appear directly beneath\n"
        "the \"Building Numbers from Scratch\" heading rather than above it. This\n"
        "improves the visual hierarchy and pedagogical flow of the section."
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
    fix_peano_infobox_placement()
    execute_git_sync()
