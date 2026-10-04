#!/usr/bin/env python3
import os
import subprocess

def merge_friendly_curriculum():
    filepath = 'week1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Sets and Functions
    old_sets = r'''<p>A <strong>set</strong> is a collection of distinct elements. New sets are formed via union ($A \cup B$), intersection ($A \cap B$), difference ($A \setminus B$), and Cartesian product <span style="white-space: nowrap;">($A \times B$)</span>.</p>

            <h3>Functions and Mappings</h3>
            <p>A <strong>function</strong> $f: X \to Y$ assigns to each element $x \in X$ (domain) one and only one value $y = f(x) \in Y$ (codomain).</p>'''

    new_sets = r'''<p>A <strong>set</strong> is simply a collection of distinct things. The number of things in a set is its <strong>cardinality</strong> (its size), written as $|A|$. The empty set $\emptyset$ has a size of 0. New sets are formed via union ($A \cup B$), intersection ($A \cap B$), difference ($A \setminus B$), and Cartesian product <span style="white-space: nowrap;">($A \times B$)</span>.</p>
            <div class="aside-box">
                <h4>💡 Infinite Sizes</h4>
                <p style="margin-bottom: 0;">Infinity actually comes in different sizes! The counting numbers ($\mathbb{N}$), integers ($\mathbb{Z}$), and fractions ($\mathbb{Q}$) are all the same "size" of infinity. But the real numbers ($\mathbb{R}$) form a strictly larger, uncountably dense infinity: $\infty = |\mathbb{N}| = |\mathbb{Z}| = |\mathbb{Q}| < |\mathbb{R}| = |\mathbb{C}|$.</p>
            </div>

            <h3>Functions and Mappings</h3>
            <p>Think of a <strong>function</strong> $f: X \to Y$ as a reliable machine. You drop an input from the <strong>domain</strong> ($X$) into the top, and it spits out exactly one output into the <strong>codomain</strong> ($Y$).</p>'''

    content = content.replace(old_sets, new_sets)

    # 2. Peano's Axioms
    old_peano = r'''<h3>Peano's Axioms for $\mathbb{N}$</h3>
            <p>Natural numbers are defined by Peano's axioms: $0 \in \mathbb{N}$, each number has a unique successor, $0$ is not a successor of any number (no loops, no branching, connected graph rooted at 0), and mathematical induction holds.</p>'''

    new_peano = r'''<h3>Building Numbers from Scratch: Peano's Axioms</h3>
            <p>Have you ever wondered what the number "1" actually is? In higher mathematics, we don't take counting for granted. We build the natural numbers ($\mathbb{N}$) using a blueprint called <strong>Peano's Axioms</strong>. Think of this as creating an infinite chain of dominoes using just a starting point and a single rule for taking the "next step" (the successor function, $S(n)$):</p>
            <ol style="margin: 0.5rem 0 1.5rem 1.25rem; padding: 0;">
                <li style="margin-bottom: 0.5rem;"><strong>The Starting Line:</strong> $0 \in \mathbb{N}$. We have to start somewhere! This gives our number system a root.</li>
                <li style="margin-bottom: 0.5rem;"><strong>The Next Step:</strong> Every number $n$ has exactly one valid next step, called its successor $S(n)$. (Intuitively, $S(n) = n + 1$).</li>
                <li style="margin-bottom: 0.5rem;"><strong>No Merging Paths (Injectivity):</strong> If two numbers take a step and land in the exact same spot, they must have started in the exact same spot. Two different numbers can never share the same successor.</li>
                <li style="margin-bottom: 0.5rem;"><strong>No Loops (The Root Property):</strong> $0$ is not the successor of <em>any</em> number. You can never take a step forward and end up back at zero. This prevents our number line from turning into a circular clock.</li>
                <li><strong>No Ghost Chains (Mathematical Induction):</strong> The only numbers that exist are the ones you can reach by starting at $0$ and stepping forward. There are no disconnected, floating "ghost" numbers. If a property is true for $0$, and taking a step always keeps it true, then it is true for <em>every</em> natural number.</li>
            </ol>'''

    content = content.replace(old_peano, new_peano)

    # 3. Completeness & Rational Gaps
    old_gaps = r'''<h3>Completeness and the Least Upper Bound Property</h3>
            <p>While rationals $\mathbb{Q}$ are dense, they contain gaps (e.g., $x^2 = 2$ has no rational solution). The real numbers $\mathbb{R}$ extend $\mathbb{Q}$ and satisfy the <strong>Axiom of Completeness</strong>: Any non-empty subset $S \subseteq \mathbb{R}$ that is bounded above has a supremum ($\sup S$) in $\mathbb{R}$. The <strong>Archimedean Axiom</strong> ensures that for any positive real numbers $x, y$, there is an $n \in \mathbb{N}$ such that $nx > y$.</p>'''

    new_gaps = r'''<h3>The Rational Gap and Completeness</h3>
            <p>Fractions (rational numbers, $\mathbb{Q}$) are incredibly dense. If you pick any two fractions, you can always find another one exactly halfway between them just by averaging them. But is the number line completely filled with fractions? <strong>No. There are holes.</strong> The most famous hole is $\sqrt{2}$.</p>

            <div class="worked-example-box">
                <h4>🎯 Why $\sqrt{2}$ isn't a fraction</h4>
                <p style="margin-bottom: 0.5rem;">Imagine $\sqrt{2}$ <em>could</em> be written as a perfectly simplified fraction $\frac{p}{q}$. If we square both sides, we get $2 = \frac{p^2}{q^2}$, which means $p^2 = 2q^2$.</p>
                <p style="margin-bottom: 0.5rem;">Every number has a unique prime factorization (its DNA). When you square a number, you double its prime factors, meaning every perfect square <em>must</em> have an <strong>even number of prime factors</strong>.</p>
                <p style="margin-bottom: 0;">So, $p^2$ has an even number of prime factors. But $2q^2$ takes $q^2$ (which is even) and multiplies it by an extra $2$, giving it an <strong>odd number of prime factors</strong>. An even number of factors cannot equal an odd number of factors! Thus, the fraction $\frac{p}{q}$ cannot exist.</p>
            </div>

            <p>Because of these holes, we created the <strong>Real Numbers ($\mathbb{R}$)</strong>. The real numbers obey the <strong>Axiom of Completeness</strong>: any non-empty subset $S \subseteq \mathbb{R}$ that has an upper limit (a ceiling) must have a <em>supremum</em> ($\sup S$, the absolute lowest possible ceiling) within $\mathbb{R}$. The real numbers have no holes. (Additionally, the <strong>Archimedean Axiom</strong> ensures that for any positive real numbers $x, y$, there is an $n \in \mathbb{N}$ such that $nx > y$).</p>'''

    content = content.replace(old_gaps, new_gaps)

    # 4. Gauss's Trick (Insert before Section 5)
    old_telescoping = r'''                    </li>
                </ol>
            </div>

            <!-- SECTION 5 -->'''

    new_telescoping = r'''                    </li>
                </ol>
            </div>

            <h3>Collapsing the Telescope (Gauss's Trick)</h3>
            <p>Because derived sequences (which we'll formally meet in the next section) act as differences between terms, adding them up causes the middle terms to cancel out—collapsing like a pirate's telescope, just as we saw in the example above!</p>
            <p>Using this concept, mathematicians derived the famous Gaussian formula for adding up the first $n$ integers (the triangular numbers). Instead of adding $1 + 2 + 3 \dots + n$ manually step-by-step, telescoping differences allow us to bypass the long addition and jump straight to the exact total:</p>
            <div class="definition-box" style="margin-bottom: 2rem;">
                <p>$$\sum_{\nu=1}^{n} \nu = \frac{n(n+1)}{2}$$</p>
            </div>

            <!-- SECTION 5 -->'''

    content = content.replace(old_telescoping, new_telescoping)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        print("Successfully woven in-depth explanations into week1.html.")

def execute_git_sync():
    commit_message = (
        "Merge in-depth foundational explanations directly into core sections\n\n"
        "Integrated beginner-friendly, conversational explanations of Peano's\n"
        "axioms, the rational gap (sqrt 2), infinite cardinalities, and Gauss's\n"
        "telescoping trick directly into the established HTML structure of\n"
        "week1.html. This preserves the interactive SVG animations and existing\n"
        "styles while significantly deepening the pedagogical value."
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
    merge_friendly_curriculum()
    execute_git_sync()
