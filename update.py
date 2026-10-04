#!/usr/bin/env python3
import os
import subprocess

def add_peano_infobox():
    filepath = 'week1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    target_anchor = r"<h3>Building Numbers from Scratch: Peano's Axioms</h3>"

    peano_infobox = r'''<div class="infobox">
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
            </div>

            <h3>Building Numbers from Scratch: Peano's Axioms</h3>'''

    if target_anchor in content:
        content = content.replace(target_anchor, peano_infobox, 1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully inserted the Peano's Axioms infobox into week1.html.")
    else:
        print("Could not locate the Peano's Axioms heading to insert the infobox.")

def execute_git_sync():
    commit_message = (
        "Add Peano's Axioms notation infobox to week1.html\n\n"
        "Inserted a standardized infobox above the Peano's Axioms section to\n"
        "summarize the formal notation (base element, successor closure, \n"
        "injectivity, root property, and induction) alongside brief intuitive\n"
        "descriptions."
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
    add_peano_infobox()
    execute_git_sync()
