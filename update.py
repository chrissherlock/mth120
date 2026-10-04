#!/usr/bin/env python3
import os
import re
import subprocess

def reformat_peano_infobox_vertical():
    filepath = 'week1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    vertical_infobox = r'''<h3>Building Numbers from Scratch: Peano's Axioms</h3>
            <div class="infobox">
                <h4>📜 Axiom Set: Peano's Postulates</h4>
                <div class="infobox-intro">
                    <strong>An ordered foundation:</strong> These five postulates build the natural numbers step by step from the ground up, each adding a structural constraint upon the last.
                </div>
                <div style="display: flex; flex-direction: column; gap: 0.65rem;">
                    <div style="display: grid; grid-template-columns: 85px 1fr; gap: 0.75rem; align-items: baseline; padding-bottom: 0.5rem; border-bottom: 1px solid #e2e8f0;">
                        <span style="font-weight: 700; color: var(--accent);">Axiom 1</span>
                        <span style="color: #334155;"><strong>Base Element:</strong> $0 \in \mathbb{N}$ — There is an initial starting line.</span>
                    </div>
                    <div style="display: grid; grid-template-columns: 85px 1fr; gap: 0.75rem; align-items: baseline; padding-bottom: 0.5rem; border-bottom: 1px solid #e2e8f0;">
                        <span style="font-weight: 700; color: var(--accent);">Axiom 2</span>
                        <span style="color: #334155;"><strong>Closure:</strong> $\forall n \in \mathbb{N}, \; S(n) \in \mathbb{N}$ — Every number has a well-defined next step.</span>
                    </div>
                    <div style="display: grid; grid-template-columns: 85px 1fr; gap: 0.75rem; align-items: baseline; padding-bottom: 0.5rem; border-bottom: 1px solid #e2e8f0;">
                        <span style="font-weight: 700; color: var(--accent);">Axiom 3</span>
                        <span style="color: #334155;"><strong>Injectivity:</strong> $S(m) = S(n) \implies m = n$ — Distinct steps never land on the same number (no merging paths).</span>
                    </div>
                    <div style="display: grid; grid-template-columns: 85px 1fr; gap: 0.75rem; align-items: baseline; padding-bottom: 0.5rem; border-bottom: 1px solid #e2e8f0;">
                        <span style="font-weight: 700; color: var(--accent);">Axiom 4</span>
                        <span style="color: #334155;"><strong>Root Property:</strong> $\forall n \in \mathbb{N}, \; S(n) \ne 0$ — Zero is not the successor of any number (no loops back to the start).</span>
                    </div>
                    <div style="display: grid; grid-template-columns: 85px 1fr; gap: 0.75rem; align-items: baseline;">
                        <span style="font-weight: 700; color: var(--accent);">Axiom 5</span>
                        <span style="color: #334155;"><strong>Induction:</strong> If $0 \in K$ and $[n \in K \implies S(n) \in K]$, then $K = \mathbb{N}$ — Only reachable numbers exist (no disconnected ghost chains).</span>
                    </div>
                </div>
            </div>'''

    # Match the Peano section header and whichever infobox is currently underneath it
    pattern = r"<h3>Building Numbers from Scratch: Peano's Axioms</h3>\s*<div class=\"infobox\">[\s\S]*?</div>\s*</div>"

    if re.search(pattern, content):
        # Passing a function as replacement avoids interpreting LaTeX backslashes (\in, \mathbb) as regex escapes
        content = re.sub(pattern, lambda _: vertical_infobox, content, count=1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully updated Peano's axioms infobox to a vertical layout.")
    else:
        print("Could not match the target infobox block.")

def execute_git_sync():
    commit_message = (
        "Fix re.sub escape error and stack Peano axioms vertically\n\n"
        "Avoided regex template escape errors on LaTeX backslashes by using a\n"
        "literal replacement function. Formatted Peano's axioms into a clean\n"
        "vertical column layout under the section header."
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
    reformat_peano_infobox_vertical()
    execute_git_sync()
