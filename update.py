#!/usr/bin/env python3
import os
import subprocess

def update_week1_with_clarity():
    filepath = 'week1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add Bouncer Analogy in Section 1 after Set-Builder explanation
    bouncer_analogy = r"""
            <div class="aside-box">
                <h4>💡 Intuitive Guide: The Club Bouncer Analogy for Set-Builder Notation</h4>
                <p>If set-builder notation looks intimidating, think of it as a bouncer checking IDs at a club door:</p>
                <ul>
                    <li><strong>The Pool ($S$):</strong> The entire crowd waiting in line outside (e.g., all real numbers $\mathbb{R}$).</li>
                    <li><strong>The Candidate ($x$):</strong> An individual person stepping up to the door.</li>
                    <li><strong>The Bouncer ($\mid$ or $:$):</strong> The vertical bar reads aloud as <strong>"such that"</strong>—the strict gatekeeper.</li>
                    <li><strong>The Rule ($P(x)$):</strong> The entry requirement (e.g., "must be greater than 2"). If you pass, you get inside the set curly braces!</li>
                </ul>
            </div>"""

    target_s1 = '<h3>Anatomy of Set-Builder Notation</h3>'
    if target_s1 in content and 'Club Bouncer Analogy' not in content:
        content = content.replace(target_s1, target_s1 + bouncer_analogy)

    # 2. Add Recipe Analogy in Section 3 under Sequences
    recipe_analogy = r"""
            <div class="aside-box">
                <h4>💡 Recipe Analogy: Explicit vs. Recursive Formulas</h4>
                <ul>
                    <li><strong>Explicit Formula (Instant Recipe):</strong> Tells you exactly how to bake the 100th cake right now without baking the first 99 (e.g., $a_n = 3n + 2$).</li>
                    <li><strong>Recursive Formula (Step-by-Step Recipe):</strong> Tells you, <em>"Take yesterday's cake and add two extra strawberries to it."</em> You must know the previous term to find the next one (e.g., $a_1 = 5, a_n = a_{n-1} + 2$).</li>
                </ul>
            </div>"""

    target_s3 = '<p>A sequence is an ordered list of numbers mapping indices from $\mathbb{N}$ to $\mathbb{R}$. We can define them explicitly with a closed-form rule or recursively relative to previous terms.</p>'
    if target_s3 in content and 'Recipe Analogy' not in content:
        content = content.replace(target_s3, target_s3 + recipe_analogy)

    # 3. Add Side-by-Side Comparison Box between Sums (Section 4) and Derived Sequences (Section 5)
    comparison_box = r"""
            <div class="aside-box" style="background: #f1f5f9; border-left: 4px solid #0284c7; border-color: #cbd5e1; margin-top: 2rem;">
                <h4 style="color: #0369a1;">⚖️ Side-by-Side Comparison: Derived Sequences vs. Partial Sums</h4>
                <p>It is very common to mix these two up because both involve mathematical operations on sequences. Here is how to keep them straight:</p>
                <ul>
                    <li><strong>Derived Sequences ($a_n'$):</strong> Look <em>locally</em> at immediate neighbors to measure <strong>change / speed / slope</strong> ($a_{n+1} - a_n$).</li>
                    <li><strong>Partial Sums ($s_n$):</strong> Look <em>cumulatively</em> backward at everything that came before to measure <strong>total accumulation / area</strong> ($\sum b_\nu$).</li>
                </ul>
            </div>"""

    target_between = '<h2 id="section-derived">5. Derived Sequences</h2>'
    if target_between in content and 'Side-by-Side Comparison' not in content:
        content = content.replace(target_between, comparison_box + '\n\n            ' + target_between)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully incorporated clarity analogies into week1.html.")

def execute_git_sync():
    commit_message = (
        "Incorporate intuitive analogies for set-builder, recipes, and comparison\n\n"
        "Added the club bouncer analogy for sets, the recipe analogy for sequences,\n"
        "and a side-by-side contrast box for derived sequences vs. partial sums."
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
    update_week1_with_clarity()
    execute_git_sync()
