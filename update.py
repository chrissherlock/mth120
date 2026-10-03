#!/usr/bin/env python3
import os
import subprocess

def expand_squeeze_theorem_explanation():
    filepath = 'week2.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Old concise text snippet for the Squeeze Theorem intro
    old_squeeze_intro = '''            <h3 style="margin-top: 2rem;">The Squeeze Theorem (Sandwich Theorem)</h3>
            <p>Sometimes a sequence is too complex or oscillatory to evaluate directly, but it can be trapped between two simpler sequences that share the exact same limit. This is formalized by the <strong>Squeeze Theorem</strong>:</p>'''

    # Expanded, rigorous, and intuitive replacement block
    expanded_squeeze_intro = '''            <h3 style="margin-top: 2rem;">The Squeeze Theorem (Sandwich Theorem)</h3>
            <p>Sometimes a sequence is too wild, complex, or oscillatory to evaluate directly using standard arithmetic laws. However, if we can bound it—trapping it from above by a larger sequence and from below by a smaller sequence that both converge to the <em>exact same limit</em>—the middle sequence has nowhere else to go. This powerful principle is formalized as the <strong>Squeeze Theorem</strong> (also known as the Sandwich Theorem):</p>
            <p><strong>Geometric Intuition:</strong> Imagine two tracker curves or enclosing walls closing in symmetrically from the ceiling and floor toward a common target $L$. As $n$ approaches infinity, the gap between the upper and lower bounds vanishes to zero. Any sequence forced to live inside that narrowing gap is mathematically compressed into sharing that exact same limit.</p>'''

    if old_squeeze_intro in content:
        content = content.replace(old_squeeze_intro, expanded_squeeze_intro)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully expanded Squeeze Theorem explanation in week2.html.")
    else:
        print("Squeeze Theorem intro anchor not found in week2.html.")

def execute_git_sync():
    commit_message = (
        "Expand Squeeze Theorem explanation and intuition in week2.html\n\n"
        "Added detailed geometric and physical intuition for the Squeeze Theorem\n"
        "before presenting the formal limit inequalities in week2.html."
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
    expand_squeeze_theorem_explanation()
    execute_git_sync()
