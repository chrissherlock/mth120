#!/usr/bin/env python3
import os
import subprocess

def add_epsilon_n_explanation():
    filepath = 'week2.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The new intuitive plain-English breakdown to insert right below the definition box
    explanation_block = r"""
            <div class="aside-box" style="margin-top: 1.5rem;">
                <h4>💡 Plain-English Breakdown: What is this formula actually saying?</h4>
                <p>If looking at $\forall \epsilon > 0, \ \exists N \in \mathbb{N} \ \text{such that} \ \forall n > N, \ |a_n - L| < \epsilon$ makes your head spin, think of it as an <strong>archery challenge</strong> or a <strong>game between two players</strong>:</p>
                <ol style="margin: 0.5rem 0 0.5rem 1.25rem; padding: 0;">
                    <li style="margin-bottom: 0.5rem;"><strong>1. The Challenger sets a tiny tolerance ($\epsilon$):</strong> Your opponent hands you a tiny positive distance $\epsilon$ (like $0.01$). They draw a narrow target band around the limit $L$: from $L - \epsilon$ up to $L + \epsilon$. They are daring you to find a point where the sequence stays inside forever.</li>
                    <li style="margin-bottom: 0.5rem;"><strong>2. You find a cutoff step ($N$):</strong> You look at the sequence and figure out how far down the list you need to walk—past some index $N$—so that everything after it settles down inside the target band.</li>
                    <li style="margin-bottom: 0.5rem;"><strong>3. The Tail Test ($|a_n - L| < \epsilon$):</strong> The absolute distance between your sequence term $a_n$ and the limit $L$ is smaller than your opponent's tolerance $\epsilon$ for <em>every single step</em> past $N$.</li>
                </ol>
                <p style="margin-top: 0.75rem; margin-bottom: 0;">If you can successfully win this game no matter how ridiculously small your opponent makes $\epsilon$, then the sequence truly converges to $L$!</p>
            </div>"""

    target = '</div>\n\n            <!-- CLAUSE STEPPER -->'
    if target in content and 'Plain-English Breakdown: What is this formula actually saying?' not in content:
        content = content.replace(target, '</div>' + explanation_block + '\n\n            <!-- CLAUSE STEPPER -->')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully added plain-English explanation to week2.html.")
    else:
        print("Target anchor not found or explanation already present.")

def execute_git_sync():
    commit_message = (
        "Add step-by-step plain-English explanation for the epsilon-N definition\n\n"
        "Expanded week2.html with an intuitive game-based walkthrough breaking down\n"
        "what each clause of the epsilon-N limit definition actually means."
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
    add_epsilon_n_explanation()
    execute_git_sync()
