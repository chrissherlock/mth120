#!/usr/bin/env python3
import os
import re
import subprocess

def inject_week2_orientation():
    filepath = 'week2.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    unboxed_intro = r'''            <!-- ORIENTATION & ROADMAP -->
            <div style="margin: 2.25rem 0 2rem 0;">
                <h3 style="margin-top: 0; color: #0f172a;">Bridging the Gap: From Intuition to Epsilon-N Rigor</h3>
                <p>In introductory calculus, we are often told that a limit is a value that a sequence "approaches" or "gets closer and closer to" as $n$ marches toward infinity. While that intuition helps picture motion, pure mathematics demands precision: exactly how close is "close," and after what point is that proximity permanently guaranteed?</p>
                <p>This week transitions from intuitive hand-waving to rigorous analytical thinking across four foundational themes:</p>
                <ul style="margin: 0.5rem 0 1rem 1.5rem; padding: 0;">
                    <li style="margin-bottom: 0.5rem;"><strong>The $\epsilon\text{-}N$ Definition:</strong> Turning limits into an exact challenge. You name any tiny tolerance $\epsilon > 0$, and the sequence produces a cutoff index $N$ beyond which every term stays trapped within that narrow window forever.</li>
                    <li style="margin-bottom: 0.5rem;"><strong>Limit Laws &amp; Squeeze Theorem:</strong> Building an algebraic toolkit that allows us to evaluate composite limits without having to build an $\epsilon\text{-}N$ scratchpad proof from scratch each time.</li>
                    <li style="margin-bottom: 0.5rem;"><strong>Monotone Convergence &amp; Recursion:</strong> Proving that a sequence must settle down simply because it is trapped and moving in a single direction—giving us the legal right to solve recursive limits algebraically.</li>
                    <li><strong>Divergence to Infinity:</strong> Distinguishing chaotic oscillation from systematic, unbounded growth using the $M\text{-}N$ towering floor test.</li>
                </ul>
                <p>Take your time with the scratchpad method. Working backwards to discover $N$ before writing out the formal proof forwards is a core skill in real analysis, and it becomes second nature with practice.</p>
            </div>'''

    # Check if an orientation section is already present
    pattern_existing = r'[ \t]*<!-- ORIENTATION & ROADMAP -->[\s\S]*?</div>[ \t]*(?=\n\s*<!-- SECTION 1 -->)'
    if re.search(pattern_existing, content):
        content = re.sub(pattern_existing, lambda _: unboxed_intro.strip(), content)
        print("Updated existing orientation section in week2.html.")
    else:
        target = '<!-- SECTION 1 -->'
        if target in content:
            content = content.replace(target, unboxed_intro + '\n\n            <!-- SECTION 1 -->', 1)
            print("Inserted unboxed orientation before Section 1 in week2.html.")
        else:
            print("Target anchor '<!-- SECTION 1 -->' not found in week2.html.")
            return

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def execute_git_sync():
    commit_message = (
        "Add unboxed orientation section after TOC in week2.html\n\n"
        "Inserted an accessible roadmap beneath the Table of Contents to bridge\n"
        "the transition from intuitive limits to epsilon-N analysis in week2.html."
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
    inject_week2_orientation()
    execute_git_sync()
