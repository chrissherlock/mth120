#!/usr/bin/env python3
import os
import subprocess

def expand_nested_quantifier_mechanics():
    filepath = 'week2.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    expanded_scoping_box = r'''            <!-- QUANTIFIER ORDER & SCOPING -->
            <div class="scoping-box">
                <h4>💡 Quantifier Order, Scope, and Dependency</h4>
                <p>In formal analysis, statements often string together multiple quantifiers: $\forall \epsilon > 0 \quad \exists N \in \mathbb{N} \quad \forall n > N \dots$ To parse these without getting lost, think of them as <strong>nested scopes</strong> and <strong>sequential turns in a game</strong>.</p>

                <!-- 3 Mechanics of Nested Quantifiers -->
                <div style="background: #ffffff; border: 1px solid #fed7aa; border-radius: 6px; padding: 1rem 1.25rem; margin-bottom: 1.25rem;">
                    <h5 style="margin: 0 0 0.65rem 0; color: #92400e; font-size: 0.98rem;">⚙️ How Chained Quantifiers Actually Work</h5>
                    <ol style="margin: 0 0 0 1.25rem; padding: 0; font-size: 0.92rem; line-height: 1.6; color: #1e293b;">
                        <li style="margin-bottom: 0.5rem;">
                            <strong>Left-to-Right Evaluation Order:</strong> Quantifiers execute strictly from left to right like lines in a computer program. You cannot jump ahead to inner variables until all outer variables have already been instantiated.
                        </li>
                        <li style="margin-bottom: 0.5rem;">
                            <strong>Lexical Scope &amp; Function Dependency:</strong> Every quantifier opens a scope that wraps around everything to its right. Inner existential variables are allowed to "see" and depend on all previously declared variables:
                            <div style="margin: 0.35rem 0; padding: 0.4rem 0.75rem; background: #f8fafc; border-left: 3px solid #0284c7; border-radius: 3px; font-family: monospace; font-size: 0.88rem;">
                                &forall; &epsilon; &gt; 0 { &exist; N = N(&epsilon;) { &forall; n &gt; N { |a_n - L| &lt; &epsilon; } } }
                            </div>
                            Because $N$ sits inside the scope of $\epsilon$, it is mathematically a <em>function</em> of $\epsilon$ ($N(\epsilon)$).
                        </li>
                        <li>
                            <strong>The Commutativity Rule (Same vs. Alternating):</strong>
                            Quantifiers of the same type commute freely without changing meaning ($\forall x \, \forall y \equiv \forall y \, \forall x$). However, <strong>alternating quantifiers ($\forall \exists$ vs. $\exists \forall$) cannot be swapped</strong> because swapping inverts who gets to react to whom.
                        </li>
                    </ol>
                </div>

                <table class="scoping-table">
                    <thead>
                        <tr><th>Variable</th><th>Scope</th><th>Dependency Rule</th></tr>
                    </thead>
                    <tbody>
                        <tr><td><strong>$\epsilon$</strong></td><td>$\forall \epsilon > 0$</td><td>Outer scope. Chosen independently of everything that follows.</td></tr>
                        <tr><td><strong>$N$</strong></td><td>$\exists N \in \mathbb{N}$</td><td>Inner to $\epsilon$. Chosen <em>after</em> inspecting $\epsilon$ ($N = N(\epsilon)$).</td></tr>
                        <tr><td><strong>$n$</strong></td><td>$\forall n > N$</td><td>Inner to both $\epsilon$ and $N$. Runs over all indices strictly past cutoff $N$.</td></tr>
                    </tbody>
                </table>

                <div style="margin-top: 1.25rem; padding-top: 1rem; border-top: 1px dashed #fed7aa;">
                    <h5 style="margin: 0 0 0.5rem 0; color: #92400e; font-size: 0.98rem;">⚠️ The Concrete Consequence: The Fatal Quantifier Swap</h5>
                    <p style="margin: 0 0 0.75rem 0; font-size: 0.93rem; line-height: 1.6; color: #1e293b;">
                        Notice what happens to the dependency chain when you swap the first two quantifiers:
                    </p>

                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; margin-bottom: 0.75rem;">
                        <div style="background: #ffffff; border: 1px solid #bbf7d0; border-left: 4px solid #10b981; border-radius: 4px; padding: 0.85rem;">
                            <strong style="color: #047857; font-size: 0.9rem;">Correct Definition ($\forall \epsilon \; \exists N$):</strong>
                            <p style="margin: 0.35rem 0 0 0; font-size: 0.88rem; color: #1e293b;">
                                <em>"For every tolerance $\epsilon > 0$, there exists an index $N$..."</em><br>
                                $N$ is allowed to react to $\epsilon$. Shrink $\epsilon \to 0$, and $N$ simply walks further down the sequence ($N = \lceil 1/\epsilon \rceil$).
                            </p>
                        </div>
                        <div style="background: #ffffff; border: 1px solid #fecaca; border-left: 4px solid #ef4444; border-radius: 4px; padding: 0.85rem;">
                            <strong style="color: #b91c1c; font-size: 0.9rem;">Illegal Swap ($\exists N \; \forall \epsilon$):</strong>
                            <p style="margin: 0.35rem 0 0 0; font-size: 0.88rem; color: #1e293b;">
                                <em>"There exists a single index $N$ such that for every $\epsilon > 0$..."</em><br>
                                Because $N$ is now declared outer to $\epsilon$, it cannot react to $\epsilon$. It must be chosen blindly upfront to satisfy <em>all</em> positive $\epsilon$ at once.
                            </p>
                        </div>
                    </div>

                    <p style="margin: 0; font-size: 0.9rem; color: #475569; line-height: 1.5;">
                        <strong>Why this destroys convergence:</strong> If $|a_n - L| < \epsilon$ holds for <em>all</em> $\epsilon > 0$ past some fixed $N$, the only non-negative distance strictly smaller than every positive number is zero ($|a_n - L| = 0$). That means $a_n = L$ for all $n > N$. The swapped condition is so restrictive that it only holds for sequences that become <strong>permanently constant</strong>. For typical convergent sequences like $a_n = \frac{1}{n}$, no single $N$ can work for all $\epsilon$, showing that nesting order dictates mathematical meaning.
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
    print("Successfully expanded nested quantifier evaluation mechanics in week2.html.")

def execute_git_sync():
    commit_message = (
        "Add comprehensive nested quantifier evaluation mechanics to week2.html\n\n"
        "Expanded the scoping section in week2.html with a detailed breakdown \n"
        "of how nested quantifiers operate, explaining left-to-right evaluation,\n"
        "lexical scoping dependencies, and the alternating quantifier rule."
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
    expand_nested_quantifier_mechanics()
    execute_git_sync()
