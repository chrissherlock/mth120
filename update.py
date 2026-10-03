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

        .example-card { background: #fffbeb; border: 1px solid #fde68a; border-radius: 6px; padding: 1rem 1.25rem; margin: 1rem 0; }
        .example-card h4 { margin-top: 0; color: #b45309; font-size: 0.95rem; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Deep Dive: Algebraic Structures (Groups, Rings, and Fields)</h1>
            <a href="week1.html" style="color: var(--accent); text-decoration: none; font-weight: 500;">&larr; Back to Week 1 Module</a>
        </div>

        <div class="module-content">
            <div class="intro-lead">
                In abstract algebra, we study sets equipped with operations and analyze the structural rules (axioms) they satisfy. By organizing number systems into <strong>Groups</strong>, <strong>Rings</strong>, and <strong>Fields</strong>, mathematicians establish universal theorems that apply across wildly different branches of mathematics.
            </div>

            <h2>1. The Building Blocks: Axioms with Concrete Examples</h2>
            <p>To understand the algebraic hierarchy, we build up from fundamental operational rules:</p>

            <div class="example-card">
                <h4>1. Closure</h4>
                <p><strong>Rule:</strong> Combining any two elements in the set produces another element within the set ($\forall a, b \in S, a \circ b \in S$).</p>
                <p><strong>Example in $\mathbb{Z}$:</strong> Take $4$ and $-7$. Their sum is $4 + (-7) = -3$. Since $-3 \in \mathbb{Z}$, integers are closed under addition.</p>
            </div>

            <div class="example-card">
                <h4>2. Associativity</h4>
                <p><strong>Rule:</strong> Grouping does not change the result: $(a \circ b) \circ c = a \circ (b \circ c)$.</p>
                <p><strong>Example in $\mathbb{R}$:</strong> $(2 + 3) + 4 = 5 + 4 = 9$, and $2 + (3 + 4) = 2 + 7 = 9$. Addition is associative.</p>
            </div>

            <div class="example-card">
                <h4>3. Identity Element</h4>
                <p><strong>Rule:</strong> An element $e$ exists that leaves any target element unchanged: $a \circ e = a$.</p>
                <p><strong>Example in $\mathbb{Z}$ (Addition):</strong> $0$ is the additive identity because $5 + 0 = 5$. <br>
                <strong>Example in $\mathbb{Q}$ (Multiplication):</strong> $1$ is the multiplicative identity because $\frac{3}{4} \times 1 = \frac{3}{4}$.</p>
            </div>

            <div class="example-card">
                <h4>4. Inverses</h4>
                <p><strong>Rule:</strong> Every element has a counterpart that undoes it, yielding the identity: $a \circ a^{-1} = e$.</p>
                <p><strong>Example in $\mathbb{Z}$ (Additive Inverses):</strong> For $7$, its inverse is $-7$ because $7 + (-7) = 0$.<br>
                <strong>Example in $\mathbb{Q}$ (Multiplicative Inverses):</strong> For $\frac{2}{3}$, its reciprocal is $\frac{3}{2}$ because $\frac{2}{3} \times \frac{3}{2} = 1$. (Note that $0$ has no multiplicative inverse!).</p>
            </div>

            <div class="example-card">
                <h4>5. Commutativity</h4>
                <p><strong>Rule:</strong> Order does not matter: $a \circ b = b \circ a$.</p>
                <p><strong>Example in $\mathbb{R}$:</strong> $3 \times 5 = 15$ and $5 \times 3 = 15$. Multiplication is commutative.</p>
            </div>

            <h2>2. Hierarchy Comparison Table with Examples</h2>
            <table>
                <thead>
                    <tr>
                        <th>Structure</th>
                        <th>Operations</th>
                        <th>Key Properties Required</th>
                        <th>Concrete Example</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>Group</strong></td>
                        <td>1 Operation ($+$)</td>
                        <td>Closure, Associativity, Identity, Inverses</td>
                        <td>$(\mathbb{Z}, +)$:<br>&bull; Closed ($a+b \in \mathbb{Z}$)<br>&bull; Assoc. ($(a+b)+c = a+(b+c)$)<br>&bull; Identity ($0$)<br>&bull; Inverse ($-a$)</td>
                    </tr>
                    <tr>
                        <td><strong>Commutative Ring</strong></td>
                        <td>2 Operations ($+, \times$)</td>
                        <td>Additive group, Multiplicative associativity & commutativity, Distributivity</td>
                        <td>$(\mathbb{Z}, +, \times)$:<br>&bull; Addition forms a group<br>&bull; Multiplication is associative & commutative<br>&bull; Distributive: $2(3+4) = 2(3) + 2(4)$</td>
                    </tr>
                    <tr>
                        <td><strong>Field</strong></td>
                        <td>2 Operations ($+, \times$)</td>
                        <td>Ring + every non-zero element has a multiplicative inverse (division)</td>
                        <td>$(\mathbb{Q}, +, \times)$:<br>&bull; All ring properties hold<br>&bull; Every $q \neq 0$ has $q^{-1} = \frac{1}{q}$ (e.g., $5$ has $\frac{1}{5}$)</td>
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
                    `<em>Example failure:</em> You cannot solve $x + 5 = 2$ in ℕ because $x = -3 \notin \mathbb{N}$.`;
            } else if (sys === 'Z') {
                output.innerHTML = `<strong>System: Integers (ℤ)</strong><br>` +
                    `• Addition Group? <span style="color: #10b981; font-weight: bold;">YES</span> (Closed, associative, identity 0, inverses like -5 exist).<br>` +
                    `• Commutative Ring? <span style="color: #10b981; font-weight: bold;">YES</span> (Addition forms a group, multiplication is associative/commutative, and distributes over addition).<br>` +
                    `• Field? <span style="color: #ef4444; font-weight: bold;">NO</span> (Fails multiplicative inverses).<br>` +
                    `<em>Example failure:</em> You cannot solve $3x = 1$ in ℤ because $x = \frac{1}{3} \notin \mathbb{Z}$.`;
            } else if (sys === 'Q') {
                output.innerHTML = `<strong>System: Rational Numbers (ℚ)</strong><br>` +
                    `• Addition Group? <span style="color: #10b981; font-weight: bold;">YES</span>.<br>` +
                    `• Commutative Ring? <span style="color: #10b981; font-weight: bold;">YES</span>.<br>` +
                    `• Field? <span style="color: #10b981; font-weight: bold;">YES</span>.<br>` +
                    `<em>Example success:</em> For any non-zero fraction $\\frac{a}{b} \in \mathbb{Q}$, its multiplicative reciprocal $\\frac{b}{a}$ also lives inside ℚ!`;
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
        "Add concrete numerical examples to algebraic structures subpage\n\n"
        "Expanded algebraic_structures.html with explicit mathematical examples for \n"
        "every axiom (closure, inverses, associativity) and algebraic classification \n"
        "(groups, commutative rings, and fields)."
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
    print("Writing algebraic structures subpage with examples...")
    write_structures_subpage()
    print("Updating index.html routing...")
    update_curriculum_index()
    print("Committing and pushing to GitHub...")
    execute_git_sync()
    print("Deployment complete.")
