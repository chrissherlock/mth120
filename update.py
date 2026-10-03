#!/usr/bin/env python3
import re
import subprocess
import sys

def patch_algebraic_structures():
    filepath = 'week1.html'
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: {filepath} not found.")
        sys.exit(1)

    replacement = r'''<!-- ALGEBRAIC STRUCTURES & EQUATIONS ASIDE -->
            <div class="aside-box">
                <h4>💡 Algebraic Structures: How Groups, Rings, and Fields Anchor the Course</h4>
                <p>Throughout MTHS120, number systems and vector spaces are defined by the algebraic axioms their operations satisfy:</p>
                <ul>
                    <li>
                        <strong>Additive Group $(\mathbb{Z}, +)$:</strong> A set with an associative operation, an identity ($0$), and inverses ($-a$).
                        <em>Course connection:</em> Resolves subtraction. Equations of the form $x + 5 = 2$ fail in $\mathbb{N}$ but have solution $x = -3$ in the group $\mathbb{Z}$.
                    </li>
                    <li>
                        <strong>Commutative Ring $(\mathbb{Z}, +, \times)$:</strong> A set where addition is an abelian group, and multiplication is associative, commutative, and distributive over addition.
                        <em>Course connection:</em> Lacks multiplicative inverses. Equations like $2x = 3$ have no solution in the ring $\mathbb{Z}$, motivating expansion. (In linear algebra, $n \times n$ matrices $M_n(\mathbb{R})$ form a non-commutative ring where matrix multiplication is associative and distributive, but $AB \neq BA$).
                    </li>
                    <li>
                        <strong>Field $(\mathbb{Q}, +, \times)$ &amp; $(\mathbb{R}, +, \times)$:</strong> A commutative ring where every non-zero element has a multiplicative inverse ($a^{-1} = 1/a$).
                        <em>Course connection:</em> Guarantees non-zero division, solving linear systems $ax = b$. In linear algebra, vector spaces $\mathbb{R}^n$ require scalars to come from a field so that Gaussian row reduction and pivot division are valid.
                    </li>
                    <li>
                        <strong>Algebraic Closure &amp; The Field $(\mathbb{C}, +, \cdot)$:</strong> Real completeness fills geometric gaps like $\sqrt{2}$, but $\mathbb{R}$ cannot solve $x^2 + 1 = 0$. In linear algebra and complex numbers, $\mathbb{C}$ forms an algebraically closed field where every polynomial of degree $n \ge 1$ has roots (Fundamental Theorem of Algebra).
                    </li>
                </ul>
                <p style="margin-top: 1rem;"><a href="algebraic_structures.html" style="color: var(--accent); font-weight: bold; text-decoration: none;">&rarr; Explore our Interactive Deep Dive on Groups, Rings, and Fields</a></p>
            </div>'''

    target_pattern = r'<!-- (?:ALGEBRAIC STRUCTURES & EQUATIONS ASIDE|ASIDE:\s*SOLVING EQUATIONS) -->[\s\S]*?</div>\s*</div>'

    # Using lambda _: replacement prevents Python's re template parser from evaluating LaTeX backslashes
    new_content, count = re.subn(target_pattern, lambda _: replacement, content)

    if count == 0:
        fallback_pattern = r'<div class="aside-box">[\s\S]*?<h4>💡 Aside: (?:Groups, Rings, Fields, and Solvability|Context: Expanding Systems to Solve Equations)</h4>[\s\S]*?</div>'
        new_content, count = re.subn(fallback_pattern, lambda _: replacement, content)

    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Successfully linked algebraic structures to course content in {filepath}.")
    else:
        print("Warning: Target aside box not found. No modifications made.")

def execute_git_sync():
    commit_message = (
        "Link groups, rings, fields, and solvability to course syllabus\n\n"
        "Updated aside-box in week1.html to explicitly tie algebraic structures\n"
        "to number expansions, Gaussian pivot division in vector spaces, and C."
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
    patch_algebraic_structures()
    execute_git_sync()
