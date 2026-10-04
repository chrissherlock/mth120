#!/usr/bin/env python3
import os
import subprocess

def restructure_peano_infobox():
    filepath = 'week1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    old_infobox = r'''<h3>Building Numbers from Scratch: Peano's Axioms</h3>
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

    new_infobox = r'''<h3>Building Numbers from Scratch: Peano's Axioms</h3>
            <div class="infobox">
                <h4>📜 Axiom Set: Peano's Postulates</h4>
                <div class="infobox-intro">
                    <strong>An ordered foundation:</strong> Rather than just a dictionary of symbols, these are five sequential, logical postulates that build the natural numbers step by step from the ground up.
                </div>
                <div class="notation-grid">
                    <div class="notation-item"><span class="notation-sym">Axiom 1</span><span class="notation-desc"><strong>Base Element:</strong> $0 \in \mathbb{N}$ (There is a starting line).</span></div>
                    <div class="notation-item"><span class="notation-sym">Axiom 2</span><span class="notation-desc"><strong>Closure:</strong> $S(n) \in \mathbb{N}$ (Every number has a valid next step).</span></div>
                    <div class="notation-item"><span class="notation-sym">Axiom 3</span><span class="notation-desc"><strong>Injectivity:</strong> $S(m) = S(n) \implies m = n$ (No merging paths).</span></div>
                    <div class="notation-item"><span class="notation-sym">Axiom 4</span><span class="notation-desc"><strong>Root Property:</strong> $S(n) \ne 0$ (No loops back to the start).</span></div>
                    <div class="notation-item"><span class="notation-sym">Axiom 5</span><span class="notation-desc"><strong>Induction:</strong> If a property holds for $0$ and is preserved by $S(n)$, it holds for all $\mathbb{N}$ (No ghost chains).</span></div>
                </div>
            </div>'''

    if old_infobox in content:
        content = content.replace(old_infobox, new_infobox)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully refactored the Peano's Axioms infobox to an ordered axiom set.")
    else:
        print("Could not find the original Peano's Axioms infobox. Ensure the file state matches the previous step.")

def execute_git_sync():
    commit_message = (
        "Refactor Peano infobox to emphasize ordered axiomatic progression\n\n"
        "Updated the Peano's Axioms infobox in week1.html to frame the content\n"
        "as a sequential set of postulates (Axiom 1 through 5) instead of a\n"
        "disconnected notation glossary. This reinforces the logical dependency\n"
        "of the mathematical foundation."
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
    restructure_peano_infobox()
    execute_git_sync()
