#!/usr/bin/env python3
import os
import subprocess
import re

def restore_cartesian_product_material():
    filepath = 'week1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Locate the end of the set operations diagrams block
    target_anchor = r'<!-- SECTION 2 NOTATION INFOBOX -->'

    cartesian_section = r'''<h3>The Cartesian Product ($A \times B$)</h3>
            <p>Named in honour of René Descartes, the <strong>Cartesian product</strong> constructs a new set of <em>ordered pairs</em> from two constituent sets.</p>

            <div class="definition-box">
                <p><strong>Formal Definition:</strong></p>
                <p>$$A \times B = \{ (a, b) \mid a \in A \text{ and } b \in B \}$$</p>
                <ul>
                    <li><strong>Ordered Pairs:</strong> In a pair $(a, b)$, order matters: $(a, b) = (c, d)$ if and only if $a = c$ and $b = d$. Unless $A = B$ or one set is empty, $A \times B \neq B \times A$.</li>
                    <li><strong>Product Cardinality:</strong> If $A$ and $B$ are finite sets with $|A| = m$ and $|B| = n$, the total number of ordered pairs is the product of their sizes:
                    $$|A \times B| = |A| \cdot |B| = mn$$</li>
                </ul>
            </div>

            <p>For example, if $A = \{1, 2, 3\}$ and $B = \{x, y\}$, then:</p>
            <p>$$A \times B = \{ (1, x), (1, y), (2, x), (2, y), (3, x), (3, y) \}$$</p>
            <p>Here $|A| = 3$ and $|B| = 2$, yielding $|A \times B| = 3 \times 2 = 6$ ordered pairs. This operation forms the foundation of coordinate geometry: the 2D Cartesian plane is simply the self-product of the real line, $\mathbb{R}^2 = \mathbb{R} \times \mathbb{R}$.</p>

            <!-- SECTION 2 NOTATION INFOBOX -->'''

    if target_anchor in content and 'The Cartesian Product ($A \times B$)' not in content:
        content = content.replace(target_anchor, cartesian_section)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Successfully restored Cartesian product material to {filepath}.")
    elif 'The Cartesian Product ($A \times B$)' in content:
        print("Cartesian product material is already present.")
    else:
        print("Target anchor not found. Please verify file structure.")

def execute_git_sync():
    commit_message = (
        "Restore comprehensive Cartesian product section in week1.html\n\n"
        "Restored the formal definition, ordered pair mechanics, cardinality\n"
        "rule |A x B| = mn, and Descartes coordinate connection in Section 1."
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
    restore_cartesian_product_material()
    execute_git_sync()
