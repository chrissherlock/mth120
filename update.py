#!/usr/bin/env python3
import os
import subprocess

def restore_nested_quantifiers():
    filepath = 'week2.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    expanded_scoping_box = r'''            <!-- QUANTIFIER ORDER & SCOPING -->
            <div class="scoping-box">
                <h4>💡 Quantifier Order, Scope, and Dependency</h4>
                <p>Quantifiers are read strictly from left to right, creating a hierarchy of scope and dependency:</p>
                <table class="scoping-table">
                    <thead>
                        <tr><th>Variable</th><th>Scope</th><th>Dependency Rule</th></tr>
                    </thead>
                    <tbody>
                        <tr><td><strong>$\epsilon$</strong></td><td>$\forall \epsilon > 0$</td><td>Arbitrary positive tolerance, chosen independently of $N$.</td></tr>
                        <tr><td><strong>$N$</strong></td><td>$\exists N \in \mathbb{N}$</td><td>Chosen <em>after</em> inspecting $\epsilon$ ($N = N(\epsilon)$).</td></tr>
                        <tr><td><strong>$n$</strong></td><td>$\forall n > N$</td><td>Runs over all indices strictly past cutoff $N$.</td></tr>
                    </tbody>
                </table>

                <div style="margin-top: 1.25rem; padding-top: 1rem; border-top: 1px dashed #fed7aa;">
                    <h5 style="margin: 0 0 0.5rem 0; color: #92400e; font-size: 0.98rem;">⚠️ Why Order Matters: The Fatal Quantifier Swap</h5>
                    <p style="margin: 0 0 0.75rem 0; font-size: 0.93rem; line-height: 1.6; color: #1e293b;">
                        In standard English, changing word order often preserves meaning. In mathematical logic, <strong>swapping nested quantifiers completely breaks the definition</strong>. Compare these two statements:
                    </p>

                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; margin-bottom: 0.75rem;">
                        <div style="background: #ffffff; border: 1px solid #bbf7d0; border-left: 4px solid #10b981; border-radius: 4px; padding: 0.85rem;">
                            <strong style="color: #047857; font-size: 0.9rem;">Correct Definition ($\forall \epsilon \; \exists N$):</strong>
                            <p style="margin: 0.35rem 0 0 0; font-size: 0.88rem; color: #1e293b;">
                                <em>"For every tolerance $\epsilon > 0$, there exists an index $N$..."</em><br>
                                $N$ is allowed to react to $\epsilon$. Make $\epsilon$ smaller, and $N$ can push further down the sequence ($N = \lceil 1/\epsilon \rceil$).
                            </p>
                        </div>
                        <div style="background: #ffffff; border: 1px solid #fecaca; border-left: 4px solid #ef4444; border-radius: 4px; padding: 0.85rem;">
                            <strong style="color: #b91c1c; font-size: 0.9rem;">Illegal Swap ($\exists N \; \forall \epsilon$):</strong>
                            <p style="margin: 0.35rem 0 0 0; font-size: 0.88rem; color: #1e293b;">
                                <em>"There exists a single index $N$ such that for every $\epsilon > 0$..."</em><br>
                                Demands a single, fixed cutoff index that beats <em>every positive number simultaneously</em>.
                            </p>
                        </div>
                    </div>

                    <p style="margin: 0; font-size: 0.9rem; color: #475569; line-height: 1.5;">
                        <strong>The consequence:</strong> If $|a_n - L| < \epsilon$ holds for <em>all</em> $\epsilon > 0$ past some fixed $N$, the only non-negative distance strictly less than every positive real is zero ($|a_n - L| = 0$). The swapped statement only holds for sequences that are <strong>eventually constant</strong> ($a_n = L$). For ordinary convergent sequences like $a_n = \frac{1}{n}$, no single $N$ can satisfy all $\epsilon$, proving order is essential.
                    </p>
                </div>
            </div>'''

    start_marker = '<!-- QUANTIFIER ORDER & SCOPING -->'
    end_marker = '<div class="widget-instructions">'

    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)

    if start_idx == -1 or end_idx == -1:
        print("Could not find the scoping box section in week2.html.")
        return

    content = content[:start_idx] + expanded_scoping_box + '\n\n            ' + content[end_idx:]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully restored nested quantifier dependency and illegal swap contrast in week2.html.")

def execute_git_sync():
    commit_message = (
        "Restore quantifier nesting and illegal swap contrast to week2.html\n\n"
        "Restored the pedagogical explanation detailing quantifier dependency and\n"
        "the illegal order reversal (forall-exists vs exists-forall) within the\n"
        "scoping box of week2.html."
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
    restore_nested_quantifiers()
    execute_git_sync()
