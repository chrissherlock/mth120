#!/usr/bin/env python3
import os
import re
import subprocess

def merge_friendly_curriculum():
    filepath = 'week1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_material = r'''
    <!-- IN-DEPTH & BEGINNER-FRIENDLY LECTURE MATERIAL -->
    <section class="topic-section" style="margin-top: 4rem; padding-top: 2rem; border-top: 2px dashed var(--border);">
        <div class="topic-header">
            <span class="topic-badge">Deep Dive</span>
            <div class="topic-title">Foundations: From Counting to Calculus</div>
        </div>
        <p style="font-size: 1.1rem; color: var(--text-muted); margin-bottom: 2rem;">
            Before we can analyze complex limits, we need to make sure the very ground we are standing on is solid. Let's take a beginner-friendly walk through how we build numbers from scratch, how we measure them, and how we analyze patterns.
        </p>

        <!-- PEANO AXIOMS -->
        <div class="content-block">
            <h3>1. Building Numbers from Scratch: Peano's Axioms</h3>
            <p>
                Have you ever wondered what the number "1" actually is? In higher mathematics, we don't take counting for granted. We build the natural numbers ($\mathbb{N}$) using a blueprint called <strong>Peano's Axioms</strong>. Think of this as creating an infinite chain of dominoes using just a starting point and a single rule for taking the "next step" (the successor function, $S(n)$).
            </p>
            <ol class="clean-list" style="margin-top: 1rem; padding-left: 1rem;">
                <li><strong>The Starting Line:</strong> $0 \in \mathbb{N}$. We have to start somewhere! This gives our number system a root.</li>
                <li><strong>The Next Step:</strong> Every number $n$ has exactly one valid next step, called its successor $S(n)$. (Intuitively, $S(n) = n + 1$).</li>
                <li><strong>No Merging Paths (Injectivity):</strong> If two numbers take a step and land in the exact same spot, they must have started in the exact same spot. Two different numbers can never share the same successor.</li>
                <li><strong>No Loops (The Root Property):</strong> $0$ is not the successor of <em>any</em> number. You can never take a step forward and end up back at zero. This prevents our number line from turning into a circular clock.</li>
                <li><strong>No Ghost Chains (Mathematical Induction):</strong> The only numbers that exist are the ones you can reach by starting at $0$ and stepping forward. There are no disconnected, floating "ghost" numbers out there. If a property is true for $0$, and taking a step always keeps it true, then it is true for <em>every</em> natural number.</li>
            </ol>
            <p>
                From these simple rules, we can define addition (taking multiple steps) and multiplication (taking repeated groups of steps) without ever relying on circular logic!
            </p>
        </div>

        <!-- SETS AND FUNCTIONS -->
        <div class="content-block" style="margin-top: 2.5rem;">
            <h3>2. Sets, Sizes, and Machines (Functions)</h3>
            <p>
                A <strong>set</strong> is just a collection of distinct things. The number of things in a set is its <strong>cardinality</strong> (its size), written as $|A|$. The empty set $\emptyset$ has a size of 0.
            </p>
            <p>
                But what about infinite sets? It turns out, infinity comes in different sizes! The counting numbers ($\mathbb{N}$), the integers ($\mathbb{Z}$), and the fractions ($\mathbb{Q}$) are all the same "size" of infinity. But the real numbers ($\mathbb{R}$) are a strictly larger, uncountably dense infinity:
            </p>
            <div style="text-align: center; margin: 1rem 0; font-size: 1.1rem; background: #f8fafc; padding: 1rem; border-radius: 8px;">
                $$\infty = |\mathbb{N}| = |\mathbb{Z}| = |\mathbb{Q}| < |\mathbb{R}| = |\mathbb{C}|$$
            </div>

            <h4 style="margin-top: 1.5rem; color: var(--text);">Functions as Machines</h4>
            <p>
                A function $f: X \to Y$ is like a machine. You drop an input from the <strong>domain</strong> ($X$) into the top, and it spits out an output into the <strong>codomain</strong> ($Y$). The actual pile of outputs it ends up creating is called the <strong>range</strong>.
            </p>
            <ul class="clean-list">
                <li><strong>Injective (One-to-One):</strong> The machine never assigns two different inputs to the same output. Every output has a unique fingerprint.</li>
                <li><strong>Surjective (Onto):</strong> The machine's range completely fills the codomain. Nothing is left out.</li>
                <li><strong>Bijective:</strong> The machine is perfectly balanced—it is both injective and surjective. Because every input pairs perfectly with one output, the machine is completely <strong>reversible</strong> (it has an inverse, $f^{-1}$).</li>
            </ul>
        </div>

        <!-- THE RATIONAL GAP -->
        <div class="content-block" style="margin-top: 2.5rem;">
            <h3>3. The Rational Gap and Completeness</h3>
            <p>
                Fractions (rational numbers, $\mathbb{Q}$) are incredibly dense. If you pick any two fractions, you can always find another one exactly halfway between them just by averaging them. You can do this forever! So, is the number line completely filled with fractions?
            </p>
            <p>
                <strong>No. There are holes.</strong> The most famous hole is $\sqrt{2}$.
            </p>
            <div class="proof-box">
                <strong class="proof-label">Why $\sqrt{2}$ isn't a fraction</strong>
                Imagine $\sqrt{2}$ <em>could</em> be written as a perfectly simplified fraction $\frac{p}{q}$. If we square both sides, we get $2 = \frac{p^2}{q^2}$, which means $p^2 = 2q^2$.<br><br>
                Every number has a unique prime factorization (its DNA). When you square a number, you double its prime factors, meaning every perfect square <em>must</em> have an <strong>even number of prime factors</strong>. <br><br>
                So, $p^2$ has an even number of prime factors. But $2q^2$ takes $q^2$ (which is even) and multiplies it by an extra $2$, giving it an <strong>odd number of prime factors</strong>. An even number of factors cannot equal an odd number of factors! The fraction $\frac{p}{q}$ cannot exist.
            </div>
            <p>
                Because of these holes, we created the <strong>Real Numbers ($\mathbb{R}$)</strong>. The real numbers obey the <strong>Axiom of Completeness</strong>: if a set of numbers has any upper limit (a ceiling), it must have a <em>supremum</em> (the absolute lowest possible ceiling). The real numbers have no holes.
            </p>
        </div>

        <!-- SEQUENCES -->
        <div class="content-block" style="margin-top: 2.5rem;">
            <h3>4. Sequences and their "Speed"</h3>
            <p>
                A sequence is just an infinite, ordered list of numbers: $a_0, a_1, a_2, a_3 \dots$<br>
                In calculus, we look at derivatives to find the speed of a curve. For discrete sequences, we look at the <strong>derived sequence</strong> ($a'_n$), which simply measures the jump from one term to the next:
            </p>
            <div style="text-align: center; margin: 1rem 0; font-size: 1.1rem; background: #f8fafc; padding: 1rem; border-radius: 8px;">
                $$a'_n = a_{n+1} - a_n$$
            </div>
            <p>
                This tells us exactly how the sequence behaves over time:
            </p>
            <ul class="clean-list">
                <li>If the jump is always zero ($a'_n = 0$), the sequence is <strong>constant</strong>. It's not moving!</li>
                <li>If the jump is always positive ($a'_n > 0$), the sequence is <strong>strictly increasing</strong>.</li>
                <li>If the jump is always negative ($a'_n < 0$), the sequence is <strong>strictly decreasing</strong>.</li>
            </ul>

            <h4 style="margin-top: 1.5rem; color: var(--text);">Collapsing the Telescope (Gauss's Trick)</h4>
            <p>
                Because the derived sequence is just differences, if we add up a bunch of these jumps, the middle terms cancel each other out—collapsing like a pirate's telescope!
            </p>
            <div style="text-align: center; margin: 1rem 0;">
                $$(a_1 - a_0) + (a_2 - a_1) + (a_3 - a_2) = a_3 - a_0$$
            </div>
            <p>
                This is called a <strong>telescoping sum</strong>. Using this concept, mathematicians derived the famous Gaussian formula for adding up the first $n$ integers. Instead of adding $1 + 2 + 3 \dots$ manually, telescoping allows us to jump straight to the answer:
            </p>
            <div style="text-align: center; margin: 1rem 0; font-size: 1.1rem; background: #f8fafc; padding: 1rem; border-radius: 8px;">
                $$\sum_{k=1}^n k = \frac{n(n+1)}{2}$$
            </div>
        </div>
    </section>
    '''

    # Look for a safe place to inject: right before the footer navigation, or before closing container/body
    footer_pattern = r'(<div class="nav-footer">|<!-- FOOTER NAV -->)'

    if re.search(footer_pattern, content):
        # Insert right before the footer
        content = re.sub(footer_pattern, lambda m: new_material + '\n    ' + m.group(1), content, count=1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully merged beginner-friendly material into week1.html before the footer.")
    else:
        # Fallback: insert before </body>
        if '</body>' in content:
            content = content.replace('</body>', new_material + '\n</body>')
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print("Successfully merged beginner-friendly material into week1.html at the end of the document.")
        else:
            print("Could not find a safe insertion point in week1.html. No changes made.")

def execute_git_sync():
    commit_message = (
        "Safely merge beginner-friendly foundational concepts into week1.html\n\n"
        "Appended conversational, in-depth explanations of Peano's axioms, set \n"
        "theory, function mappings, real completeness, and derived sequences to \n"
        "the existing week1.html structure without overwriting core content."
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
