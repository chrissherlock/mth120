#!/usr/bin/env python3
import os
import subprocess

def reposition_peano_infobox():
    filepath = 'week1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    infobox_markup = r'''            <div class="infobox">
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

    old_section = r'''            <h3>Building Numbers from Scratch: Peano's Axioms</h3>
''' + infobox_markup + r'''

            <p>Have you ever wondered what the number "1" actually is? In higher mathematics, we don't take counting for granted. We build the natural numbers ($\mathbb{N}$) using a blueprint called <strong>Peano's Axioms</strong>. Think of this as creating an infinite chain of dominoes using just a starting point and a single rule for taking the "next step" (the successor function, $S(n)$):</p>
            <ol style="margin: 0.5rem 0 1.5rem 1.25rem; padding: 0;">
                <li style="margin-bottom: 0.5rem;"><strong>The Starting Line:</strong> $0 \in \mathbb{N}$. We have to start somewhere! This gives our number system a root.</li>
                <li style="margin-bottom: 0.5rem;"><strong>The Next Step:</strong> Every number $n$ has exactly one valid next step, called its successor $S(n)$. (Intuitively, $S(n) = n + 1$).</li>
                <li style="margin-bottom: 0.5rem;"><strong>No Merging Paths (Injectivity):</strong> If two numbers take a step and land in the exact same spot, they must have started in the exact same spot. Two different numbers can never share the same successor.</li>
                <li style="margin-bottom: 0.5rem;"><strong>No Loops (The Root Property):</strong> $0$ is not the successor of <em>any</em> number. You can never take a step forward and end up back at zero. This prevents our number line from turning into a circular clock.</li>
                <li><strong>No Ghost Chains (Mathematical Induction):</strong> The only numbers that exist are the ones you can reach by starting at $0$ and stepping forward. There are no disconnected, floating "ghost" numbers. If a property is true for $0$, and taking a step always keeps it true, then it is true for <em>every</em> natural number.</li>
            </ol>'''

    new_section = r'''            <h3>Building Numbers from Scratch: Peano's Axioms</h3>
            <p>Have you ever wondered what the number "1" actually is? In higher mathematics, we don't take counting for granted. We build the natural numbers ($\mathbb{N}$) using a blueprint called <strong>Peano's Axioms</strong>. Think of this as creating an infinite chain of dominoes using just a starting point and a single rule for taking the "next step" (the successor function, $S(n)$):</p>
            <ol style="margin: 0.5rem 0 1.5rem 1.25rem; padding: 0;">
                <li style="margin-bottom: 0.5rem;"><strong>The Starting Line:</strong> $0 \in \mathbb{N}$. We have to start somewhere! This gives our number system a root.</li>
                <li style="margin-bottom: 0.5rem;"><strong>The Next Step:</strong> Every number $n$ has exactly one valid next step, called its successor $S(n)$. (Intuitively, $S(n) = n + 1$).</li>
                <li style="margin-bottom: 0.5rem;"><strong>No Merging Paths (Injectivity):</strong> If two numbers take a step and land in the exact same spot, they must have started in the exact same spot. Two different numbers can never share the same successor.</li>
                <li style="margin-bottom: 0.5rem;"><strong>No Loops (The Root Property):</strong> $0$ is not the successor of <em>any</em> number. You can never take a step forward and end up back at zero. This prevents our number line from turning into a circular clock.</li>
                <li><strong>No Ghost Chains (Mathematical Induction):</strong> The only numbers that exist are the ones you can reach by starting at $0$ and stepping forward. There are no disconnected, floating "ghost" numbers. If a property is true for $0$, and taking a step always keeps it true, then it is true for <em>every</em> natural number.</li>
            </ol>

''' + infobox_markup

    if old_section in content:
        content = content.replace(old_section, new_section, 1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully moved Peano's Postulates infobox below the narrative text.")
    else:
        print("Could not match exact target block to reposition infobox.")

def execute_git_sync():
    commit_message = (
        "Relocate Peano's Postulates infobox beneath narrative explanation\n\n"
        "Shifted the Peano's Postulates infobox in week1.html to appear directly\n"
        "after the conversational breakdown of the axioms, allowing students to\n"
        "grasp the intuition before referencing the formal notation."
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
    reposition_peano_infobox()
    execute_git_sync()
