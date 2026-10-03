#!/usr/bin/env python3
import os
import subprocess

def write_structures_subpage():
    if os.path.exists('algebraic_structures.html'):
        os.remove('algebraic_structures.html')

    subpage_content = r"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Deep Dive: Groups, Rings, and Fields | MTHS120</title>
    <!-- KaTeX Integration -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"
            onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]});"></script>
    <style>
        :root {
            --bg: #f8fafc; --text: #0f172a; --card: #ffffff; --border: #cbd5e1;
            --accent: #d97706; --accent-hover: #b45309;
            --telemetry-bg: #0f172a; --telemetry-text: #fbbf24;
            --track1-bg: #fffbeb; --track2-bg: #fff7ed;
        }
        body { font-family: system-ui, sans-serif; background: var(--bg); color: var(--text); line-height: 1.6; margin: 0; padding: 2rem; }
        .container { max-width: 1200px; margin: 0 auto; }
        .header { border-bottom: 2px solid var(--border); padding-bottom: 1rem; margin-bottom: 2rem; }
        .module-content { background: var(--card); padding: 2rem; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05), 0 2px 4px -1px rgba(0,0,0,0.03); margin-bottom: 2rem; border: 1px solid var(--border); }

        .intro-lead { font-size: 1.1rem; color: #1e293b; line-height: 1.7; margin-bottom: 1.5rem; background: #f1f5f9; padding: 1.5rem; border-radius: 6px; border-left: 4px solid var(--accent); border-top: 1px solid var(--border); border-right: 1px solid var(--border); border-bottom: 1px solid var(--border); }

        h2 { border-bottom: 2px solid var(--border); padding-bottom: 0.5rem; margin-top: 2.5rem; color: #0f172a; }
        h3 { color: #1e293b; margin-top: 1.5rem; }

        .definition-box { background: #f8fafc; border-left: 4px solid var(--accent); padding: 1rem 1.5rem; margin: 1rem 0; border-radius: 0 6px 6px 0; border-top: 1px solid var(--border); border-right: 1px solid var(--border); border-bottom: 1px solid var(--border); }

        .interactive-box { background: #f8fafc; border: 1px solid var(--border); border-radius: 8px; padding: 1.5rem; margin: 1.5rem 0; }
        .btn-group { display: flex; gap: 1rem; margin-top: 1rem; flex-wrap: wrap; }
        button { background: var(--accent); color: white; border: none; padding: 0.5rem 1.25rem; border-radius: 4px; cursor: pointer; font-weight: bold; width: auto; transition: background 0.2s; }
        button:hover { background: var(--accent-hover); }
        .output-display { font-family: monospace; background: #ffffff; padding: 1rem; border: 1px solid var(--border); border-radius: 4px; margin-top: 1rem; color: #0f172a; }

        table { width: 100%; border-collapse: collapse; margin: 1.5rem 0; font-size: 0.95rem; }
        th, td { border: 1px solid var(--border); padding: 0.75rem; text-align: left; }
        th { background: #f1f5f9; color: #0f172a; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Deep Dive: Algebraic Structures (Groups, Rings, Fields)</h1>
            <a href="week1.html" style="color: var(--accent); text-decoration: none; font-weight: 500;">&larr; Back to Week 1 Module</a>
        </div>

        <div class="module-content">
            <div class="intro-lead">
                In abstract algebra, we study sets equipped with operations and analyze the structural rules (axioms) they satisfy. By organizing number systems into <strong>Groups</strong>, <strong>Rings</strong>, and <strong>Fields</strong>, mathematicians establish universal theorems that apply across wildly different branches of mathematics.
            </div>

            <h2>1. The Building Blocks: Axioms</h2>
            <p>To understand the algebraic hierarchy, we build up from fundamental operational rules:</p>
            <ul>
                <li><strong>Closure:</strong> Combining any two elements in the set using the operation produces another element within the set ($\forall a, b \in S, a \circ b \in S$).</li>
                <li><strong>Associativity:</strong> Grouping does not matter: $(a \circ b) \circ c = a \circ (b \circ c)$.</li>
                <li><strong>Identity Element:</strong> An element $e$ leaves others unchanged: $a \circ e = a$.</li>
                <li><strong>Inverses:</strong> Every element has an opposite or reciprocal that undoes it, yielding the identity: $a \circ a^{-1} = e$.</li>
                <li><strong>Commutativity:</strong> Order does not matter: $a \circ b = b \circ a$.</li>
            </ul>

            <h2>2. Hierarchy Comparison Table</h2>
            <table>
                <thead>
                    <tr>
                        <th>Structure</th>
                        <th>Operations</th>
                        <th>Key Properties Required</th>
                        <th>Examples</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>Group</strong></td>
                        <td>1 Operation ($+$)</td>
                        <td>Closure, Associativity, Identity, Inverses</td>
                        <td>$(\mathbb{Z}, +), (\mathbb{R}, +)$</td>
                    </tr>
                    <tr>
                        <td><strong>Commutative Ring</strong></td>
                        <td>2 Operations ($+, \times$)</td>
                        <td>Additive group, Multiplicative associativity & commutativity, Distributivity</td>
                        <td>$(\mathbb{Z}, +, \times)$</td>
                    </tr>
                    <tr>
                        <td><strong>Field</strong></td>
                        <td>2 Operations ($+, \times$)</td>
                        <td>Ring + every non-zero element has a multiplicative inverse (division)</td>
                        <td>$(\mathbb{Q}, +, \times), (\mathbb{R}, +, \times)$</td>
                    </tr>
                </tbody>
            </table>

            <div class="interactive-box">
                <h3>🧪 Interactive Algebraic Structure Inspector</h3>
                <p>Select a number system to inspect which algebraic structures it satisfies:</p>
                <div class="btn-group">
                    <button onclick="inspectSystem('N')">Natural Numbers ($\mathbb{N}$)</button>
                    <button onclick="inspectSystem('Z')">Integers ($\mathbb{Z}$)</button>
                    <button onclick="inspectSystem('Q')">Rationals ($\mathbb{Q}$)</button>
                </div>
                <div id="inspector-output" class="output-display">
                    <em>Select a number system above to inspect its algebraic classification.</em>
                </div>
            </div>
        </div>
    </div>

    <script>
        function inspectSystem(sys) {
            const output = document.getElementById('inspector-output');
            if (sys === 'N') {
                output.innerHTML = `<strong>System: Natural Numbers (ℕ)</strong><br>` +
                    `• Addition Group? <span style="color: #ef4444; font-weight: bold;">NO</span> (Lacks identity 0 and additive inverses like -1).<br>` +
                    `• Ring? <span style="color: #ef4444; font-weight: bold;">NO</span> (Fails group axioms under addition).<br>` +
                    `• Field? <span style="color: #ef4444; font-weight: bold;">NO</span>.<br>` +
                    `<em>Summary:</em> ℕ is a commutative monoid under addition and multiplication, but lacks the structural symmetry of groups or rings.`;
            } else if (sys === 'Z') {
                output.innerHTML = `<strong>System: Integers (ℤ)</strong><br>` +
                    `• Addition Group? <span style="color: #10b981; font-weight: bold;">YES</span> (Closed, associative, identity 0, inverses like -5 exist).<br>` +
                    `• Commutative Ring? <span style="color: #10b981; font-weight: bold;">YES</span> (Addition forms a group, multiplication is associative/commutative, and distributes over addition).<br>` +
                    `• Field? <span style="color: #ef4444; font-weight: bold;">NO</span> (Fails multiplicative inverses; e.g., $3x = 1$ has no integer solution).<br>` +
                    `<em>Summary:</em> ℤ is a classic commutative ring with unity, but division is not closed.`;
            } else if (sys === 'Q') {
                output.innerHTML = `<strong>System: Rational Numbers (ℚ)</strong><br>` +
                    `• Addition Group? <span style="color: #10b981; font-weight: bold;">YES</span>.<br>` +
                    `• Commutative Ring? <span style="color: #10b981; font-weight: bold;">YES</span>.<br>` +
                    `• Field? <span style="color: #10b981; font-weight: bold;">YES</span> (Every non-zero fraction $p/q$ has a reciprocal $q/p$ within ℚ).<br>` +
                    `<em>Summary:</em> ℚ is a fully fledged field, allowing unlimited addition, subtraction, multiplication, and non-zero division!`;
            }
        }
    </script>
</body>
</html>
"""
    with open('algebraic_structures.html', 'w') as f:
        f.write(subpage_content)

def update_curriculum_index():
    if not os.path.exists('index.html'):
        print("index.html not found in current directory. Please run in root.")
        return

    with open('index.html', 'r') as f:
        content = f.read()

    target = '<a href="#" class="module-link">View Module</a>'
    replacement = '<a href="${item.week === 1 ? \'week1.html\' : \'#\'}" class="module-link">View Module</a>'

    updated_content = content.replace(target, replacement)

    with open('index.html', 'w') as f:
        f.write(updated_content)

def execute_git_sync():
    commit_message = (
        "Synchronize layout and visual look of algebraic structures subpage\n\n"
        "Updated algebraic_structures.html to match the margins, card styling, typography, \n"
        "and warm amber/orange color palette of the main Week 1 module."
    )

    commands = [
        ['git', 'add', 'update.py', 'week1.html', 'algebraic_structures.html', 'index.html'],
        ['git', 'commit', '-m', commit_message],
        ['git', 'push', 'origin', 'main']
    ]

    for cmd in commands:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(f"> {' '.join(cmd)}\n{result.stdout}{result.stderr}")

if __name__ == "__main__":
    print("Writing algebraic structures subpage...")
    write_structures_subpage()
    print("Updating index.html routing...")
    update_curriculum_index()
    print("Committing and pushing to GitHub...")
    execute_git_sync()
    print("Deployment complete.")
