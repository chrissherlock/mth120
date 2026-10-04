#!/usr/bin/env python3
import os
import subprocess

SHARED_CSS = r'''
        :root {
            --bg: #f8fafc; --text: #0f172a; --card: #ffffff; --border: #cbd5e1;
            --accent: #d97706; --accent-hover: #b45309;
            --font-ui: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
        }
        body { font-family: var(--font-ui); background: var(--bg); color: var(--text); line-height: 1.6; margin: 0; padding: 2rem; }
        .container { max-width: 1200px; margin: 0 auto; }
        .header { border-bottom: 2px solid var(--border); padding-bottom: 1rem; margin-bottom: 2rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem; }
        .module-content { background: var(--card); padding: 2rem; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05), 0 2px 4px -1px rgba(0,0,0,0.03); margin-bottom: 2rem; border: 1px solid var(--border); }

        .intro-lead { font-size: 1.1rem; color: #1e293b; line-height: 1.7; margin-bottom: 1.5rem; background: #f1f5f9; padding: 1.5rem; border-radius: 6px; border-left: 4px solid var(--accent); border: 1px solid var(--border); border-left-width: 4px; }
        .toc-box { background: #fffbeb; border: 1px solid #fde68a; border-left: 5px solid var(--accent); border-radius: 6px; padding: 1.25rem 1.75rem; margin: 1.75rem 0 2.5rem 0; }
        .toc-box h4 { margin: 0 0 0.75rem 0; color: #92400e; font-size: 1.05rem; }
        .toc-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 0.5rem 1.5rem; margin: 0; padding-left: 1.25rem; }
        .toc-grid li { margin-bottom: 0.35rem; font-size: 0.95rem; }
        .toc-grid a { color: #b45309; text-decoration: none; font-weight: 500; }
        .toc-grid a:hover { text-decoration: underline; color: var(--accent-hover); }

        h2 { border-bottom: 2px solid var(--border); padding-bottom: 0.5rem; margin-top: 2.5rem; color: #0f172a; font-family: var(--font-ui); scroll-margin-top: 2rem; }
        h3 { color: #1e293b; margin-top: 1.5rem; font-family: var(--font-ui); scroll-margin-top: 2rem; }

        .infobox { background: #f8fafc; border: 1px solid var(--border); border-left: 5px solid var(--accent); border-radius: 6px; padding: 1.25rem 1.5rem; margin: 1.25rem 0 1.75rem 0; }
        .infobox h4 { margin: 0 0 0.85rem 0; color: #0f172a; font-size: 1rem; display: flex; align-items: center; gap: 0.5rem; font-family: var(--font-ui); }
        .notation-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(290px, 1fr)); gap: 0.85rem 1.75rem; font-size: 0.95rem; }
        .notation-item { display: grid; grid-template-columns: minmax(130px, max-content) 1fr; gap: 0.75rem; align-items: center; }
        .notation-sym { font-weight: 600; color: var(--accent); white-space: nowrap; display: flex; justify-content: center; align-items: center; text-align: center; }
        .notation-desc { min-width: 0; word-break: break-word; line-height: 1.5; color: #334155; }
        .infobox-intro { font-size: 0.93rem; color: #475569; line-height: 1.6; margin: 0 0 1.25rem 0; padding-bottom: 0.85rem; border-bottom: 1px solid #e2e8f0; }

        .definition-box { background: #f8fafc; border-left: 4px solid var(--accent); padding: 1rem 1.5rem; margin: 1rem 0; border-radius: 0 6px 6px 0; border: 1px solid var(--border); border-left-width: 4px; }
        .aside-box { background: #fffbeb; border: 1px solid #fde68a; border-left: 4px solid var(--b45309, #b45309); padding: 1.25rem 1.5rem; margin: 1.5rem 0; border-radius: 0 6px 6px 0; }
        .aside-box h4 { margin-top: 0; color: #b45309; font-size: 1rem; display: flex; align-items: center; gap: 0.5rem; }

        .worked-example-box { background: #f0fdf4; border: 1px solid #bbf7d0; border-left: 5px solid #10b981; padding: 1.25rem 1.5rem; margin: 1.5rem 0; border-radius: 0 6px 6px 0; }
        .worked-example-box h4 { margin-top: 0; color: #047857; font-size: 1rem; display: flex; align-items: center; gap: 0.5rem; }
        .worked-example-box p, .worked-example-box li { color: #0f172a !important; }

        .lecture-card { background: #ffffff; border: 1px solid var(--border); border-radius: 8px; padding: 1.5rem; margin-bottom: 1.5rem; transition: transform 0.15s ease, box-shadow 0.15s ease; }
        .lecture-card:hover { transform: translateY(-2px); box-shadow: 0 6px 12px -2px rgba(0,0,0,0.08); border-color: var(--accent); }
        .lecture-card h3 { margin-top: 0; color: #0f172a; }
        .lecture-badge { display: inline-block; background: var(--accent); color: white; padding: 0.2rem 0.55rem; border-radius: 4px; font-weight: 700; font-size: 0.8rem; text-transform: uppercase; margin-bottom: 0.5rem; }
'''

def build_head_markup(page_title):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{page_title}</title>
    <!-- KaTeX Integration -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"
            onload="renderMathInElement(document.body, {{delimiters: [{{left: '$$', right: '$$', display: true}}, {{left: '$', right: '$', display: false}}]}});"></script>
    <style>{SHARED_CSS}    </style>
</head>
<body>
    <div class="container">'''

def build_week1_hub_html():
    head = build_head_markup("Week 1: Sets, Numbers, and Sequences | MTHS120")
    return head + r'''
        <!-- TOP NAVIGATION HEADER -->
        <div class="header">
            <div>
                <h1>Week 1: Sets, Numbers, and Sequences</h1>
                <a href="index.html" style="color: var(--accent); text-decoration: none; font-weight: 500;">&larr; Back to Curriculum Index</a>
            </div>
            <div>
                <a href="week2.html" style="background: var(--accent); color: white; padding: 0.5rem 1rem; border-radius: 6px; text-decoration: none; font-weight: 600; font-size: 0.9rem;">Next: Week 2 &rarr;</a>
            </div>
        </div>

        <div class="module-content">
            <!-- HERO IMAGE -->
            <div style="margin-bottom: 2rem; border-radius: 8px; overflow: hidden; border: 1px solid var(--border); box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05), 0 2px 4px -1px rgba(0,0,0,0.03);">
                <img src="images/chapter1-hero.jpg" alt="Week 1: Sets, Numbers, and Sequences - UNE Campus Discovery Trail" style="width: 100%; height: auto; display: block;">
            </div>

            <div class="intro-lead">
                Welcome to Week 1 of MTHS120. This unit establishes the foundational language of pure mathematics across three core lectures: the grammar of set theory, the complete continuum of real numbers, and the dynamics of sequences and sums.
            </div>

            <div style="margin: 2rem 0;">
                <h2 style="margin-top: 0;">Weekly Lecture Modules</h2>
                <p style="color: #475569; font-size: 1.05rem;">To make studying manageable and maintain deep conceptual clarity, the material is organised into three focused lectures:</p>
            </div>

            <!-- LECTURE 1 CARD -->
            <div class="lecture-card">
                <span class="lecture-badge">Lecture 1</span>
                <h3><a href="week1-lecture1.html" style="color: inherit; text-decoration: none;">Sets, Operations, Functions, and Peano's Foundations &rarr;</a></h3>
                <p style="color: #334155; margin-bottom: 1rem;">
                    Master the formal language of mathematics. We explore set operations, compare different sizes of infinity ($|\mathbb{N}|$ vs $|\mathbb{R}|$), analyze functions as reliable input-output machines, and construct the natural numbers from scratch using Peano's 5 axioms.
                </p>
                <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
                    <a href="week1-lecture1.html" style="background: var(--accent); color: white; padding: 0.45rem 0.9rem; border-radius: 5px; text-decoration: none; font-weight: 600; font-size: 0.88rem;">Open Lecture 1 &rarr;</a>
                </div>
            </div>

            <!-- LECTURE 2 CARD -->
            <div class="lecture-card">
                <span class="lecture-badge">Lecture 2</span>
                <h3><a href="week1-lecture2.html" style="color: inherit; text-decoration: none;">Number Systems, Metric Properties, and Completeness &rarr;</a></h3>
                <p style="color: #334155; margin-bottom: 1rem;">
                    Discover why fractions ($\mathbb{Q}$) leave tiny gaps along the line, examine the classical proof that $\sqrt{2}$ is irrational, investigate distance metrics and the Triangle Inequality, and study the Axiom of Completeness that guarantees the continuum of real numbers.
                </p>
                <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
                    <a href="week1-lecture2.html" style="background: var(--accent); color: white; padding: 0.45rem 0.9rem; border-radius: 5px; text-decoration: none; font-weight: 600; font-size: 0.88rem;">Open Lecture 2 &rarr;</a>
                </div>
            </div>

            <!-- LECTURE 3 CARD -->
            <div class="lecture-card">
                <span class="lecture-badge">Lecture 3</span>
                <h3><a href="week1-lecture3.html" style="color: inherit; text-decoration: none;">Sequences, Differences, and Sums &rarr;</a></h3>
                <p style="color: #334155; margin-bottom: 1rem;">
                    Step into the infinite. We examine sequences through dual lenses (ordered lists vs. functions on $\mathbb{N}$), observe finite samples versus infinite tails via an interactive SVG visualization, analyze discrete rate of change with derived sequences, and collapse telescoping sums to discover Gauss's formula.
                </p>
                <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
                    <a href="week1-lecture3.html" style="background: var(--accent); color: white; padding: 0.45rem 0.9rem; border-radius: 5px; text-decoration: none; font-weight: 600; font-size: 0.88rem;">Open Lecture 3 &rarr;</a>
                </div>
            </div>

            <!-- FOOTER -->
            <div style="margin-top: 3rem; padding-top: 1.5rem; border-top: 1px solid var(--border); display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
                <a href="index.html" style="color: var(--accent); text-decoration: none; font-weight: 600;">&larr; Curriculum Index</a>
                <a href="week1-lecture1.html" style="background: var(--accent); color: white; padding: 0.6rem 1.2rem; border-radius: 6px; text-decoration: none; font-weight: 600;">Begin Lecture 1 &rarr;</a>
            </div>
        </div>
    </div>
</body>
</html>'''

def build_lecture1_html():
    head = build_head_markup("Week 1, Lecture 1: Sets, Functions, and Peano's Foundations | MTHS120")
    return head + r'''
        <!-- TOP NAVIGATION HEADER -->
        <div class="header">
            <div>
                <h1>Week 1, Lecture 1: Sets, Functions, and Peano's Foundations</h1>
                <a href="week1.html" style="color: var(--accent); text-decoration: none; font-weight: 500;">&larr; Week 1 Overview Hub</a>
            </div>
            <div>
                <a href="week1-lecture2.html" style="background: var(--accent); color: white; padding: 0.5rem 1rem; border-radius: 6px; text-decoration: none; font-weight: 600; font-size: 0.9rem;">Next: Lecture 2 &rarr;</a>
            </div>
        </div>

        <div class="module-content">
            <!-- HERO IMAGE -->
            <div style="margin-bottom: 2rem; border-radius: 8px; overflow: hidden; border: 1px solid var(--border); box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05), 0 2px 4px -1px rgba(0,0,0,0.03);">
                <img src="images/chapter1-hero.jpg" alt="Week 1: Sets, Numbers, and Sequences - UNE Campus Discovery Trail" style="width: 100%; height: auto; display: block;">
            </div>

            <div class="intro-lead">
                Welcome to Lecture 1. Here we explore the fundamental grammar of pure mathematics: gathering objects into sets, mapping them through functions, and constructing our counting numbers from scratch using Peano's axioms.
            </div>

            <!-- TABLE OF CONTENTS -->
            <div class="toc-box">
                <h4>📌 Lecture 1 Topics</h4>
                <ul class="toc-grid">
                    <li><a href="#sets-cardinality">1. Sets and Infinite Cardinality</a></li>
                    <li><a href="#set-operations">2. Set Operations and Products</a></li>
                    <li><a href="#functions-mappings">3. Functions and Mappings</a></li>
                    <li><a href="#peano-axioms">4. Peano's Axioms for Natural Numbers</a></li>
                </ul>
            </div>

            <!-- SECTION 1 -->
            <h2 id="sets-cardinality">1. Sets and Infinite Cardinality</h2>
            <div class="infobox">
                <h4>📖 Notation Reference: Sets &amp; Elements</h4>
                <div class="infobox-intro">
                    <strong>Don't worry if this feels abstract at first:</strong> Set theory is simply the friendly art of grouping things together without worrying about duplicate items or their order.
                </div>
                <div class="notation-grid">
                    <div class="notation-item"><span class="notation-sym">$x \in A$</span><span class="notation-desc">$x$ is an element of set $A$</span></div>
                    <div class="notation-item"><span class="notation-sym">$A \subseteq B$</span><span class="notation-desc">$A$ is a subset of $B$</span></div>
                    <div class="notation-item"><span class="notation-sym">$\emptyset$</span><span class="notation-desc">The empty set (contains no elements, $|\emptyset| = 0$)</span></div>
                    <div class="notation-item"><span class="notation-sym">$|A|$</span><span class="notation-desc">Cardinality: the number of distinct elements in $A$</span></div>
                </div>
            </div>

            <p>A <strong>set</strong> is simply an unordered collection of distinct elements. The order in which elements are listed does not matter, and repeating an element changes nothing:</p>
            <div style="text-align: center; margin: 1rem 0; font-size: 1.05rem;">
                $$\{1, 2, 3\} = \{3, 2, 1\} = \{1, 1, 1, 2, 2, 3\}$$
            </div>
            <p>The number of elements in a set $A$ is called its <strong>cardinality</strong>, denoted $|A|$. The unique set containing zero elements is the <strong>empty set</strong>, written $\emptyset = \{\}$, with $|\emptyset| = 0$.</p>

            <div class="aside-box">
                <h4>💡 Infinity Comes in Different Sizes!</h4>
                <p>The standard number systems satisfy the subset inclusion chain:</p>
                <div style="text-align: center; margin: 0.5rem 0;">
                    $$\mathbb{N} \subseteq \mathbb{Z} \subseteq \mathbb{Q} \subseteq \mathbb{R} \subseteq \mathbb{C}$$
                </div>
                <p style="margin-bottom: 0;">
                    Remarkably, their infinite cardinalities do not increase at every step! The counting numbers ($\mathbb{N}$), integers ($\mathbb{Z}$), and rational fractions ($\mathbb{Q}$) all share the exact same countable size of infinity. However, the continuous real line ($\mathbb{R}$) is strictly larger:
                </p>
                <div style="text-align: center; margin: 0.5rem 0;">
                    $$\infty = |\mathbb{N}| = |\mathbb{Z}| = |\mathbb{Q}| < |\mathbb{R}| = |\mathbb{C}|$$
                </div>
            </div>

            <!-- SECTION 2 -->
            <h2 id="set-operations">2. Set Operations and Products</h2>
            <p>Given subsets $A$ and $B$, we combine and slice them using standard operations:</p>
            <ul>
                <li><strong>Union ($A \cup B$):</strong> All elements in $A$ or in $B$ (or both). Note $A \cup \emptyset = A$.</li>
                <li><strong>Intersection ($A \cap B$):</strong> Elements that belong to both $A$ and $B$ simultaneously. Note $A \cap \emptyset = \emptyset$.</li>
                <li><strong>Difference ($A \setminus B$):</strong> Elements that belong to $A$ but do <em>not</em> belong to $B$. Note that set difference is strictly non-commutative: $A \setminus B \ne B \setminus A$.</li>
                <li><strong>Cartesian Product ($A \times B$):</strong> The set of all ordered pairs $(a, b)$ with $a \in A$ and $b \in B$. Its size satisfies $|A \times B| = |A| \cdot |B|$. When applied to the real numbers, $\mathbb{R} \times \mathbb{R} = \mathbb{R}^2$ forms the two-dimensional coordinate plane.</li>
            </ul>

            <!-- SECTION 3 -->
            <h2 id="functions-mappings">3. Functions and Mappings</h2>
            <div class="infobox">
                <h4>📖 Notation Reference: Functions &amp; Composition</h4>
                <div class="infobox-intro">
                    <strong>Functions as reliable machines:</strong> An input from the domain drops in, a rule processes it, and an output is delivered into the codomain.
                </div>
                <div class="notation-grid">
                    <div class="notation-item"><span class="notation-sym">$f: X \to Y$</span><span class="notation-desc">Function $f$ with domain $X$ and codomain $Y$</span></div>
                    <div class="notation-item"><span class="notation-sym">$f^{-1}(y)$</span><span class="notation-desc">Preimage of an output element $y$</span></div>
                    <div class="notation-item"><span class="notation-sym">$g \circ f$</span><span class="notation-desc">Composition: $(g \circ f)(x) = g(f(x))$</span></div>
                    <div class="notation-item"><span class="notation-sym">$f^{-1}$</span><span class="notation-desc">Inverse function (exists if and only if $f$ is bijective)</span></div>
                </div>
            </div>

            <p>A <strong>function</strong> $f: X \to Y$ assigns to each element $x \in X$ (domain) exactly one output value $y = f(x) \in Y$ (codomain).</p>
            <ul>
                <li><strong>Range:</strong> The set of values actually produced: $R = \{f(x) \mid x \in X\} \subseteq Y$.</li>
                <li><strong>Surjective (Onto):</strong> The range completely covers the codomain ($R = Y$), meaning every element in $Y$ is hit at least once.</li>
                <li><strong>Injective (1-to-1):</strong> Distinct inputs produce distinct outputs: $x_1 \neq x_2 \implies f(x_1) \neq f(x_2)$.
                    <br><em>Non-example:</em> $f: \mathbb{Z} \to \mathbb{Z}$ defined by $f(x) = x^2$ is not injective because $f(-2) = 4 = f(2)$.
                </li>
                <li><strong>Bijective:</strong> Both injective and surjective. Because every input pairs with exactly one unique output, the mapping is completely reversible, which is the necessary and sufficient condition for an <strong>inverse function</strong> $f^{-1}: Y \to X$ to exist.</li>
                <li><strong>Composition:</strong> For $f: X \to Y$ and $g: Y \to Z$, the composition $g \circ f: X \to Z$ maps $x \mapsto g(f(x))$.</li>
            </ul>

            <!-- SECTION 4 -->
            <h2 id="peano-axioms">4. Peano's Axioms for Natural Numbers</h2>
            <h3>Building Numbers from Scratch: Peano's Axioms</h3>
            <p>Have you ever wondered what the number "1" actually is? In higher mathematics, we don't take counting for granted. We build the natural numbers ($\mathbb{N}$) using a blueprint called <strong>Peano's Axioms</strong>. Think of this as creating an infinite chain of dominoes using just a starting point and a single rule for taking the "next step" (the successor function, $S(n)$):</p>
            <ol style="margin: 0.5rem 0 1.5rem 1.25rem; padding: 0;">
                <li style="margin-bottom: 0.5rem;"><strong>The Starting Line:</strong> $0 \in \mathbb{N}$. We have to start somewhere! This gives our number system a root.</li>
                <li style="margin-bottom: 0.5rem;"><strong>The Next Step:</strong> Every number $n$ has exactly one valid next step, called its successor $S(n)$. (Intuitively, $S(n) = n + 1$).</li>
                <li style="margin-bottom: 0.5rem;"><strong>No Merging Paths (Injectivity):</strong> If two numbers take a step and land in the exact same spot, they must have started in the exact same spot. Two different numbers can never share the same successor.</li>
                <li style="margin-bottom: 0.5rem;"><strong>No Loops (The Root Property):</strong> $0$ is not the successor of <em>any</em> number. You can never take a step forward and end up back at zero. This prevents our number line from turning into a circular clock.</li>
                <li><strong>No Ghost Chains (Mathematical Induction):</strong> The only numbers that exist are the ones you can reach by starting at $0$ and stepping forward. There are no disconnected, floating "ghost" numbers. If a property is true for $0$, and taking a step always keeps it true, then it is true for <em>every</em> natural number.</li>
            </ol>

            <div class="infobox">
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
            </div>

            <div class="definition-box" style="margin-top: 1.5rem;">
                <strong>Constructing Arithmetic with Primitive Recursion:</strong>
                <p style="margin: 0.5rem 0 0.25rem 0;">From these five simple rules, we construct all arithmetic recursively:</p>
                <ul style="margin: 0 0 0 1.25rem;">
                    <li><strong>Addition ($+$):</strong> $n + 0 = n$, and $n + S(m) = S(n + m)$.</li>
                    <li><strong>Multiplication ($\cdot$):</strong> $n \cdot 0 = 0$, and $n \cdot S(m) = (n \cdot m) + n$.</li>
                </ul>
            </div>

            <!-- FOOTER NAVIGATION -->
            <div style="margin-top: 3rem; padding-top: 1.5rem; border-top: 1px solid var(--border); display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
                <a href="week1.html" style="color: var(--accent); text-decoration: none; font-weight: 600;">&larr; Back to Week 1 Overview</a>
                <a href="week1-lecture2.html" style="background: var(--accent); color: white; padding: 0.6rem 1.2rem; border-radius: 6px; text-decoration: none; font-weight: 600;">Next: Lecture 2 (Numbers &amp; Completeness) &rarr;</a>
            </div>
        </div>
    </div>
</body>
</html>'''

def build_lecture2_html():
    head = build_head_markup("Week 1, Lecture 2: Numbers, Metric Properties, and Completeness | MTHS120")
    return head + r'''
        <!-- TOP NAVIGATION HEADER -->
        <div class="header">
            <div>
                <h1>Week 1, Lecture 2: Numbers, Metric Properties, and Completeness</h1>
                <a href="week1.html" style="color: var(--accent); text-decoration: none; font-weight: 500;">&larr; Week 1 Overview Hub</a>
            </div>
            <div>
                <a href="week1-lecture3.html" style="background: var(--accent); color: white; padding: 0.5rem 1rem; border-radius: 6px; text-decoration: none; font-weight: 600; font-size: 0.9rem;">Next: Lecture 3 &rarr;</a>
            </div>
        </div>

        <div class="module-content">
            <!-- HERO IMAGE -->
            <div style="margin-bottom: 2rem; border-radius: 8px; overflow: hidden; border: 1px solid var(--border); box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05), 0 2px 4px -1px rgba(0,0,0,0.03);">
                <img src="images/chapter1-hero.jpg" alt="Week 1: Sets, Numbers, and Sequences - UNE Campus Discovery Trail" style="width: 100%; height: auto; display: block;">
            </div>

            <div class="intro-lead">
                Welcome to Lecture 2. Here we examine the numerical continuum: proving why rational numbers leave infinite gaps on the line, measuring distance with absolute value, and defining the complete real numbers through suprema and infima.
            </div>

            <!-- TABLE OF CONTENTS -->
            <div class="toc-box">
                <h4>📌 Lecture 2 Topics</h4>
                <ul class="toc-grid">
                    <li><a href="#density-rationals">1. Density of the Rational Numbers</a></li>
                    <li><a href="#rational-gaps">2. Rational Gaps and the Irrationality of $\sqrt{2}$</a></li>
                    <li><a href="#field-order">3. Axiomatic Field and Order Properties of $\mathbb{R}$</a></li>
                    <li><a href="#absolute-value">4. Absolute Value and Distance Metrics</a></li>
                    <li><a href="#completeness-bounds">5. Bounds, Suprema, and Completeness</a></li>
                </ul>
            </div>

            <!-- SECTION 1 -->
            <h2 id="density-rationals">1. Density of the Rational Numbers</h2>
            <div class="infobox">
                <h4>📖 Notation Reference: Number Sets &amp; Bounds</h4>
                <div class="infobox-intro">
                    <strong>The numbers we stand on:</strong> From counting numbers up to the unbroken real line, each extension repairs a specific structural limitation.
                </div>
                <div class="notation-grid">
                    <div class="notation-item"><span class="notation-sym">$\mathbb{N}$</span><span class="notation-desc">Natural numbers $\{0, 1, 2, \dots\}$</span></div>
                    <div class="notation-item"><span class="notation-sym">$\mathbb{Z}$</span><span class="notation-desc">Integers $\{\dots, -1, 0, 1, \dots\}$</span></div>
                    <div class="notation-item"><span class="notation-sym">$\mathbb{Q}$</span><span class="notation-desc">Rational numbers $\{p/q \mid p \in \mathbb{Z}, q \in \mathbb{Z}_+\}$</span></div>
                    <div class="notation-item"><span class="notation-sym">$\mathbb{R}$</span><span class="notation-desc">Real numbers (complete ordered field)</span></div>
                    <div class="notation-item"><span class="notation-sym">$|x|$</span><span class="notation-desc">Absolute value (distance to origin)</span></div>
                    <div class="notation-item"><span class="notation-sym">$\sup S$</span><span class="notation-desc">Supremum (least upper bound) of set $S$</span></div>
                    <div class="notation-item"><span class="notation-sym">$\inf S$</span><span class="notation-desc">Infimum (greatest lower bound) of set $S$</span></div>
                </div>
            </div>

            <p>Fractions (rational numbers, $\mathbb{Q}$) are packed incredibly tightly along the number line.</p>
            <div class="definition-box">
                <strong>Proposition 1 (Density of $\mathbb{Q}$):</strong> For any two distinct rational numbers $a$ and $b$ with $a < b$, there exist infinitely many rational numbers strictly between them.
            </div>
            <p>
                <em>Proof Construction:</em> The arithmetic midpoint $c_1 = \frac{a+b}{2}$ is rational because $\mathbb{Q}$ is closed under addition and division. Since $a < c_1 < b$, we can repeat this process on $a$ and $c_1$ to find $c_2 = \frac{a+c_1}{2}$. Repeating this construction generates an infinite descending sequence of distinct rationals between $a$ and $b$:
            </p>
            <div style="text-align: center; margin: 1rem 0;">
                $$b > c_1 > c_2 > c_3 > \dots > a$$
            </div>

            <!-- SECTION 2 -->
            <h2 id="rational-gaps">2. Rational Gaps and the Irrationality of $\sqrt{2}$</h2>
            <p>Even though fractions are infinitely dense, the rational line is filled with holes. Consider a right triangle with unit legs ($1$ and $1$). By Pythagoras' theorem, the hypotenuse $c$ satisfies $c^2 = 1^2 + 1^2 = 2 \implies c = \sqrt{2}$.</p>

            <div class="worked-example-box">
                <h4>🎯 Why $\sqrt{2}$ isn't a fraction (Proof by Contradiction)</h4>
                <p style="margin-bottom: 0.5rem;">Assume $\sqrt{2}$ <em>could</em> be written as a simplified rational fraction $\frac{p}{q}$ for integers $p, q$ with $q \neq 0$. Squaring both sides yields:</p>
                <div style="text-align: center; margin: 0.5rem 0;">
                    $$\frac{p^2}{q^2} = 2 \implies p^2 = 2q^2$$
                </div>
                <p style="margin-bottom: 0.5rem;">
                    By the Fundamental Theorem of Arithmetic, every integer has a unique prime factorisation. When you square any number, all prime factor exponents double, meaning every perfect square must contain an <strong>even number of prime factors</strong> (counting multiplicities).
                </p>
                <p style="margin-bottom: 0;">
                    Therefore, $p^2$ contains an <strong>even</strong> number of prime factors. Meanwhile, $2q^2$ takes $q^2$ (which has an even number of factors) and multiplies it by one additional 2, giving it an <strong>odd</strong> number of prime factors. An even number cannot equal an odd number! Hence $p^2 = 2q^2$ is impossible, proving that $\sqrt{2} \notin \mathbb{Q}$.
                </p>
            </div>

            <!-- SECTION 3 -->
            <h2 id="field-order">3. Axiomatic Field and Order Properties of $\mathbb{R}$</h2>
            <p>To patch the gaps in $\mathbb{Q}$, we construct the real numbers $\mathbb{R}$ uniting rationals and irrationals into a complete ordered field:</p>
            <ul>
                <li><strong>Field Axioms:</strong> Commutativity and associativity of addition and multiplication; distributivity ($(a+b)c = ac + bc$); additive identity $0$ and multiplicative identity $1 \ne 0$; additive inverse $-a$; reciprocal $a^{-1}$ (for $a \ne 0$).</li>
                <li><strong>Trichotomy:</strong> For any $a, b \in \mathbb{R}$, exactly one of $a < b$, $a = b$, or $a > b$ holds.</li>
                <li><strong>Order Transitivity:</strong> $a > b \text{ and } b > c \implies a > c$.</li>
                <li><strong>Order Preservation:</strong> If $a > b$, then $a + c > b + c$ for all $c$. If $a > b$ and $c > 0$, then $ac > bc$.</li>
            </ul>

            <!-- SECTION 4 -->
            <h2 id="absolute-value">4. Absolute Value and Distance Metrics</h2>
            <p>The absolute value function $|\cdot|: \mathbb{R} \to \mathbb{R}$ measures distance along the real line: $\text{dist}(a, b) = |a - b|$.</p>
            <div class="definition-box">
                <strong>Proposition 2 (Properties of Absolute Value):</strong>
                <ol style="margin-left: 1.25rem; margin-top: 0.5rem;">
                    <li>$|a| \ge 0$, and $|a| = 0 \iff a = 0$.</li>
                    <li>$|ab| = |a| \cdot |b|$.</li>
                    <li>$|a|^2 = a^2$.</li>
                    <li><strong>Triangle Inequality:</strong> $|a + b| \le |a| + |b|$.</li>
                    <li><strong>Reverse Triangle Inequality:</strong> $||a| - |b|| \le |a - b|$.</li>
                </ol>
            </div>
            <div class="aside-box">
                <h4>📐 Proving the Triangle Inequality</h4>
                <p>Because $-|x| \le x \le |x|$ for any real number $x$, we check the sum $a+b$:</p>
                <ul style="margin: 0.25rem 0 0 1.25rem;">
                    <li>If $a+b \ge 0$, then $|a+b| = a+b \le |a| + |b|$ because $a \le |a|$ and $b \le |b|$.</li>
                    <li>If $a+b < 0$, then $|a+b| = -(a+b) = (-a) + (-b) \le |a| + |b|$ because $-a \le |a|$ and $-b \le |b|$.</li>
                </ul>
            </div>

            <!-- SECTION 5 -->
            <h2 id="completeness-bounds">5. Bounds, Suprema, and Completeness</h2>
            <p>Let $S \subseteq \mathbb{R}$ be a non-empty subset of real numbers:</p>
            <ul>
                <li><strong>Upper Bound:</strong> A number $K$ such that $x \le K$ for all $x \in S$. If $K$ exists, $S$ is <em>bounded above</em>.</li>
                <li><strong>Lower Bound:</strong> A number $k$ such that $k \le x$ for all $x \in S$. If $k$ exists, $S$ is <em>bounded below</em>.</li>
                <li><strong>Bounded Set:</strong> A set that is bounded both above and below.</li>
                <li><strong>Supremum ($\sup S$):</strong> The least upper bound of $S$ (the lowest ceiling).</li>
                <li><strong>Infimum ($\inf S$):</strong> The greatest lower bound of $S$ (the highest floor).</li>
            </ul>

            <div class="definition-box">
                <strong>The Axiom of Completeness of $\mathbb{R}$:</strong> Every non-empty subset of real numbers that is bounded above has a supremum in $\mathbb{R}$.
            </div>
            <p>
                <strong>The Rational Defect:</strong> Notice why $\mathbb{Q}$ is incomplete. The set $S = \{x \in \mathbb{Q} \mid x^2 < 2\}$ is bounded above in $\mathbb{Q}$ (for example, by 2 or 10), but has no supremum within $\mathbb{Q}$ because the ceiling $\sqrt{2}$ is not rational!
            </p>

            <!-- FOOTER NAVIGATION -->
            <div style="margin-top: 3rem; padding-top: 1.5rem; border-top: 1px solid var(--border); display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
                <a href="week1-lecture1.html" style="color: var(--accent); text-decoration: none; font-weight: 600;">&larr; Lecture 1: Sets &amp; Functions</a>
                <a href="week1-lecture3.html" style="background: var(--accent); color: white; padding: 0.6rem 1.2rem; border-radius: 6px; text-decoration: none; font-weight: 600;">Next: Lecture 3 (Sequences &amp; Sums) &rarr;</a>
            </div>
        </div>
    </div>
</body>
</html>'''

def build_lecture3_html():
    head = build_head_markup("Week 1, Lecture 3: Sequences, Differences, and Sums | MTHS120")
    return head + r'''
        <!-- TOP NAVIGATION HEADER -->
        <div class="header">
            <div>
                <h1>Week 1, Lecture 3: Sequences, Differences, and Sums</h1>
                <a href="week1.html" style="color: var(--accent); text-decoration: none; font-weight: 500;">&larr; Week 1 Overview Hub</a>
            </div>
            <div>
                <a href="week2.html" style="background: var(--accent); color: white; padding: 0.5rem 1rem; border-radius: 6px; text-decoration: none; font-weight: 600; font-size: 0.9rem;">Next: Week 2 &rarr;</a>
            </div>
        </div>

        <div class="module-content">
            <!-- HERO IMAGE -->
            <div style="margin-bottom: 2rem; border-radius: 8px; overflow: hidden; border: 1px solid var(--border); box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05), 0 2px 4px -1px rgba(0,0,0,0.03);">
                <img src="images/chapter1-hero.jpg" alt="Week 1: Sets, Numbers, and Sequences - UNE Campus Discovery Trail" style="width: 100%; height: auto; display: block;">
            </div>

            <div class="intro-lead">
                Welcome to Lecture 3. Here we step into discrete calculus: treating sequences as functions over the natural numbers, observing how finite samples relate to infinite tails, measuring change with derived sequences, and evaluating series through telescoping sums.
            </div>

            <!-- TABLE OF CONTENTS -->
            <div class="toc-box">
                <h4>📌 Lecture 3 Topics</h4>
                <ul class="toc-grid">
                    <li><a href="#sequences-intro">1. Sequences and Progressions</a></li>
                    <li><a href="#finite-infinite-viz">2. Finite Sample vs. The Infinite Sequence</a></li>
                    <li><a href="#sums-partial">3. Sums and Partial Sums</a></li>
                    <li><a href="#derived-sequences">4. Derived Sequences (The Speedometer)</a></li>
                    <li><a href="#telescoping-gauss">5. Telescoping Inversion and Gauss's Formula</a></li>
                </ul>
            </div>

            <!-- SECTION 1 -->
            <h2 id="sequences-intro">1. Sequences and Progressions</h2>
            <div class="infobox">
                <h4>📖 Notation Reference: Sequence Mechanics</h4>
                <div class="infobox-intro">
                    <strong>Think of a sequence simply as an endless ordered list</strong> —like a musical playlist or numbered parking spots—where every step has its own designated number.
                </div>
                <div class="notation-grid">
                    <div class="notation-item"><span class="notation-sym">$(a_n)$</span><span class="notation-desc">Sequence $(a_0, a_1, a_2, \dots)$</span></div>
                    <div class="notation-item"><span class="notation-sym">$an + b$</span><span class="notation-desc">Arithmetic progression</span></div>
                    <div class="notation-item"><span class="notation-sym">$aq^n$</span><span class="notation-desc">Geometric progression</span></div>
                </div>
            </div>

            <p>To truly grasp what a sequence is, look at it through two complementary lenses:</p>
            <ul style="margin: 0.5rem 0 1rem 1.25rem; padding: 0;">
                <li style="margin-bottom: 0.6rem;"><strong>1. The List View (Intuitive):</strong> An endless, ordered string of numbers $(a_n) = (a_1, a_2, a_3, a_4, \dots)$. Order matters deeply: $(1, 2, 3, \dots)$ is completely different from $(3, 2, 1, \dots)$.</li>
                <li style="margin-bottom: 0.6rem;"><strong>2. The Function View (Rigorous):</strong> Formally, a sequence is a function whose domain is the natural numbers $\mathbb{N}$ and whose codomain is the real numbers $\mathbb{R}$. Instead of $f(n)$, we write $a_n$:
                    <ul style="margin: 0.3rem 0 0.3rem 1.25rem; padding: 0;">
                        <li><strong>Input ($n$):</strong> The position or index ($0, 1, 2, 3, \dots$).</li>
                        <li><strong>Output ($a_n$):</strong> The actual real number sitting at that position.</li>
                    </ul>
                </li>
            </ul>

            <div class="aside-box">
                <h4>💡 Recipe Analogy: Explicit vs. Recursive Formulas</h4>
                <ul>
                    <li><strong>Explicit Formula (Instant Recipe):</strong> Tells you how to compute the 100th term right now without computing the first 99 (e.g., $a_n = 3n + 2$).</li>
                    <li><strong>Recursive Formula (Step-by-Step Recipe):</strong> Tells you, <em>"Take yesterday's term and add two extra to it."</em> You must know the previous term to find the next (e.g., $a_1 = 5, a_n = a_{n-1} + 2$).</li>
                </ul>
            </div>

            <!-- SECTION 2 -->
            <h2 id="finite-infinite-viz">2. Finite Sample vs. The Infinite Sequence</h2>
            <div id="finite-sample-container" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 6px; padding: 1.25rem; margin-top: 1.5rem; margin-bottom: 1.5rem;">
                <p style="font-size: 0.85rem; font-weight: 700; color: #64748b; margin-top: 0; margin-bottom: 0.75rem; text-align: center;">VISUALIZATION: Finite Sample vs. The Infinite Sequence</p>
                <svg viewBox="0 0 800 290" style="width: 100%; height: auto; display: block;">
                    <!-- Background Grid -->
                    <line x1="80" y1="230" x2="760" y2="230" stroke="#f1f5f9" stroke-width="1"/>
                    <line x1="80" y1="170" x2="760" y2="170" stroke="#f1f5f9" stroke-width="1" stroke-dasharray="3"/>
                    <line x1="80" y1="110" x2="760" y2="110" stroke="#f1f5f9" stroke-width="1" stroke-dasharray="3"/>
                    <line x1="80" y1="50" x2="760" y2="50" stroke="#f1f5f9" stroke-width="1" stroke-dasharray="3"/>

                    <!-- Axes -->
                    <line x1="80" y1="230" x2="760" y2="230" stroke="#0f172a" stroke-width="2"/>
                    <line x1="80" y1="25" x2="80" y2="245" stroke="#0f172a" stroke-width="2"/>
                    <text x="725" y="250" font-size="11" font-weight="bold" fill="#64748b">Index n</text>
                    <text x="35" y="35" font-size="11" font-weight="bold" fill="#64748b">Value a_n</text>

                    <!-- Finite Sample Shading (Left Side) -->
                    <rect x="85" y="40" width="375" height="185" fill="#f0f9ff" opacity="0.6" rx="4"/>
                    <text x="210" y="58" font-size="11" font-weight="bold" fill="#0284c7">Observed Finite Sample (n = 1 to 6)</text>

                    <!-- Infinite Tail Shading (Right Side) -->
                    <rect x="470" y="40" width="280" height="185" fill="#f0fdf4" opacity="0.6" rx="4"/>
                    <text x="535" y="58" font-size="11" font-weight="bold" fill="#047857">Infinite Continuation Tail</text>

                    <!-- Vertical Projection Guidelines -->
                    <line x1="125" y1="230" x2="125" y2="200" stroke="#cbd5e1" stroke-dasharray="2"/>
                    <line x1="180" y1="230" x2="180" y2="170" stroke="#cbd5e1" stroke-dasharray="2"/>
                    <line x1="235" y1="230" x2="235" y2="148" stroke="#cbd5e1" stroke-dasharray="2"/>
                    <line x1="290" y1="230" x2="290" y2="132" stroke="#cbd5e1" stroke-dasharray="2"/>
                    <line x1="345" y1="230" x2="345" y2="120" stroke="#cbd5e1" stroke-dasharray="2"/>
                    <line x1="400" y1="230" x2="400" y2="110" stroke="#cbd5e1" stroke-dasharray="2"/>

                    <!-- Finite Sample Points (Sky Blue) -->
                    <circle class="fs-pt" cx="125" cy="200" r="5" fill="#0284c7" opacity="0" style="transition: opacity 0.3s ease;"/>
                    <circle class="fs-pt" cx="180" cy="170" r="5" fill="#0284c7" opacity="0" style="transition: opacity 0.3s ease;"/>
                    <circle class="fs-pt" cx="235" cy="148" r="5" fill="#0284c7" opacity="0" style="transition: opacity 0.3s ease;"/>
                    <circle class="fs-pt" cx="290" cy="132" r="5" fill="#0284c7" opacity="0" style="transition: opacity 0.3s ease;"/>
                    <circle class="fs-pt" cx="345" cy="120" r="5" fill="#0284c7" opacity="0" style="transition: opacity 0.3s ease;"/>
                    <circle class="fs-pt" cx="400" cy="110" r="5" fill="#0284c7" opacity="0" style="transition: opacity 0.3s ease;"/>

                    <!-- Index Numbers on X Axis -->
                    <text x="121" y="248" font-size="10" fill="#64748b">1</text>
                    <text x="176" y="248" font-size="10" fill="#64748b">2</text>
                    <text x="231" y="248" font-size="10" fill="#64748b">3</text>
                    <text x="286" y="248" font-size="10" fill="#64748b">4</text>
                    <text x="341" y="248" font-size="10" fill="#64748b">5</text>
                    <text x="396" y="248" font-size="10" fill="#64748b">6</text>

                    <!-- SEPARATOR LINE -->
                    <line x1="465" y1="35" x2="465" y2="235" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4"/>

                    <!-- GREEN CONTINUATION DOTS (THE INFINITE TAIL) -->
                    <g id="green-tail-dots">
                        <circle class="fs-pt" cx="490" cy="102" r="5.5" fill="#10b981" opacity="0" style="transition: opacity 0.3s ease;"/>
                        <circle class="fs-pt" cx="535" cy="95" r="5.5" fill="#10b981" opacity="0" style="transition: opacity 0.3s ease;"/>
                        <circle class="fs-pt" cx="580" cy="89" r="5.5" fill="#10b981" opacity="0" style="transition: opacity 0.3s ease;"/>
                        <circle class="fs-pt" cx="625" cy="84" r="5.5" fill="#10b981" opacity="0" style="transition: opacity 0.3s ease;"/>
                        <circle class="fs-pt" cx="670" cy="80" r="5.5" fill="#10b981" opacity="0" style="transition: opacity 0.3s ease;"/>
                        <circle class="fs-pt" cx="715" cy="77" r="5.5" fill="#10b981" opacity="0" style="transition: opacity 0.3s ease;"/>
                        <text class="fs-pt" x="735" y="80" font-size="16" font-weight="bold" fill="#10b981" opacity="0" style="transition: opacity 0.3s ease;">...</text>
                    </g>
                    <text x="486" y="248" font-size="10" font-weight="bold" fill="#047857">7</text>
                    <text x="531" y="248" font-size="10" font-weight="bold" fill="#047857">8</text>
                    <text x="576" y="248" font-size="10" font-weight="bold" fill="#047857">9</text>
                    <text x="621" y="248" font-size="10" font-weight="bold" fill="#047857">10</text>
                    <text x="662" y="248" font-size="10" font-weight="bold" fill="#047857">n &rarr; &infin;</text>
                </svg>
                <div style="margin-top: 0.85rem; padding: 0.75rem 1rem; background: #f0fdf4; border: 1px solid #bbf7d0; border-left: 4px solid #10b981; border-radius: 4px; font-size: 0.9rem; color: #065f46;">
                    <strong>The Infinite Reality:</strong> Any computational plot only ever reveals a <em>finite sample</em> (the blue terms $a_1, \dots, a_6$). The <strong style="color: #047857;">emerald green dots</strong> represent the infinite tail ($a_7, a_8, a_9, \dots$) which continues without end for every $n \in \mathbb{N}$.
                </div>

                <script>
                    window.addEventListener('DOMContentLoaded', () => {
                        const points = document.querySelectorAll('.fs-pt');
                        points.forEach((pt, index) => {
                            setTimeout(() => {
                                pt.style.opacity = '1';
                            }, 300 + (index * 200));
                        });
                    });
                </script>
            </div>

            <!-- SECTION 3 -->
            <h2 id="sums-partial">3. Sums and Partial Sums</h2>
            <div class="infobox">
                <h4>📖 Notation Reference: Summation Mechanics</h4>
                <div class="infobox-intro">
                    <strong>Meet the sigma machine:</strong> The Greek letter sigma ($\sum$) is shorthand for adding up a string of numbers without having to write out endless plus signs.
                </div>
                <div class="notation-grid">
                    <div class="notation-item"><span class="notation-sym">$\sum$</span><span class="notation-desc">Sigma operator: instruction to sum terms together</span></div>
                    <div class="notation-item"><span class="notation-sym">$\nu = 0$ or $1$</span><span class="notation-desc">Lower limit: starting index value</span></div>
                    <div class="notation-item"><span class="notation-sym">$n$</span><span class="notation-desc">Upper limit: final index value where the sum stops</span></div>
                    <div class="notation-item"><span class="notation-sym">$s_n$</span><span class="notation-desc">Partial sum: the running total score up to index $n$</span></div>
                </div>
            </div>

            <p>Writing out $b_0 + b_1 + \dots + b_n$ becomes messy, so we define <strong>partial sums</strong> ($s_n$):</p>
            <div class="definition-box">
                <p>$$s_n = \sum_{\nu=0}^{n} b_\nu = b_0 + b_1 + b_2 + \dots + b_n$$</p>
            </div>

            <p>Two essential summation formulas appear repeatedly:</p>
            <ul>
                <li><strong>Triangular Numbers:</strong> $\sum_{\nu=1}^{n} \nu = 1 + 2 + \dots + n = \frac{n(n+1)}{2}$</li>
                <li><strong>Geometric Series:</strong> $\sum_{\nu=0}^{n-1} q^\nu = \frac{1 - q^n}{1 - q} \quad (q \neq 1)$</li>
            </ul>

            <div class="worked-example-box">
                <h4>🎯 Worked Example: Telescoping Cancellations</h4>
                <p>Evaluate $\sum_{k=1}^{n} \left(\frac{1}{k} - \frac{1}{k+1}\right)$ by expanding terms:</p>
                <div style="text-align: center; margin: 0.5rem 0;">
                    $$\left(1 - \frac{1}{2}\right) + \left(\frac{1}{2} - \frac{1}{3}\right) + \left(\frac{1}{3} - \frac{1}{4}\right) + \dots + \left(\frac{1}{n} - \frac{1}{n+1}\right)$$
                </div>
                <p style="margin-bottom: 0;">All interior terms cancel out, leaving only the first and last: $1 - \frac{1}{n+1} = \frac{n}{n+1}$.</p>
            </div>

            <!-- SECTION 4 -->
            <h2 id="derived-sequences">4. Derived Sequences (The Speedometer)</h2>
            <div class="aside-box" style="background: #f1f5f9; border-left: 4px solid #0284c7; border-color: #cbd5e1;">
                <h4 style="color: #0369a1;">⚖️ Side-by-Side: Derived Sequences vs. Partial Sums</h4>
                <ul>
                    <li><strong>Derived Sequences ($a_n'$):</strong> Look <em>locally</em> at immediate neighbors to measure <strong>change / speed / slope</strong> ($a_{n+1} - a_n$).</li>
                    <li><strong>Partial Sums ($s_n$):</strong> Look <em>cumulatively</em> backward at everything that came before to measure <strong>total accumulation / area</strong> ($\sum b_\nu$).</li>
                </ul>
            </div>

            <div class="infobox">
                <h4>📖 Notation Reference: Derived Sequences</h4>
                <div class="infobox-intro">
                    <strong>The Speedometer Analogy:</strong> While a sequence tells you your position (odometer), a derived sequence tells you how fast you are jumping from step to step (speedometer).
                </div>
                <div class="notation-grid">
                    <div class="notation-item"><span class="notation-sym">$a_n'$</span><span class="notation-desc">Derived sequence: $a_n' = a_{n+1} - a_n$</span></div>
                </div>
            </div>

            <div class="worked-example-box">
                <h4>🎯 Worked Example: Squares and Differences</h4>
                <p>For $(a_n) = (1, 4, 9, 16, 25, \dots)$ where $a_n = n^2$:</p>
                <ul style="margin: 0.4rem 0 0 1.25rem;">
                    <li>$a_1' = 4 - 1 = 3$</li>
                    <li>$a_2' = 9 - 4 = 5$</li>
                    <li>$a_3' = 16 - 9 = 7$</li>
                    <li>$a_4' = 25 - 16 = 9$</li>
                </ul>
                <p style="margin-top: 0.5rem; margin-bottom: 0;">The derived sequence is $(3, 5, 7, 9, \dots)$, with explicit formula $a_n' = 2n + 1$.</p>
            </div>

            <div class="definition-box">
                <strong>Proposition 4 (Monotonicity Tests via $a_n'$):</strong>
                <ul style="margin: 0.35rem 0 0 1.25rem;">
                    <li>$(a_n)$ is constant $\iff a_n' = 0$ for all $n$.</li>
                    <li>$(a_n)$ is increasing (strictly increasing) $\iff a_n' \ge 0$ ($a_n' > 0$) for all $n$.</li>
                    <li>$(a_n)$ is decreasing (strictly decreasing) $\iff a_n' \le 0$ ($a_n' < 0$) for all $n$.</li>
                </ul>
            </div>

            <!-- SECTION 5 -->
            <h2 id="telescoping-gauss">5. Telescoping Inversion and Gauss's Formula</h2>
            <p>Because derived sequences act as discrete differences, we invert them via telescoping summation:</p>
            <div style="text-align: center; margin: 1rem 0;">
                $$\sum_{k=0}^{n-1} a_k' = (a_1 - a_0) + (a_2 - a_1) + \dots + (a_n - a_{n-1}) = a_n - a_0$$
            </div>
            <p>Rearranging yields the original sequence reconstruction formula:</p>
            <div style="text-align: center; margin: 1rem 0;">
                $$a_n = a_0 + \sum_{k=0}^{n-1} a_k'$$
            </div>

            <div class="worked-example-box">
                <h4>🎯 Deriving Gauss's Formula via Difference Inversion</h4>
                <p>We wish to evaluate $\sum_{k=0}^{n-1} k$, finding a sequence $a_n$ whose derived difference is $a_n' = n$ with $a_0 = 0$.</p>
                <p>Since $(n^2)' = 2n + 1$ and $(n)' = 1$, by linearity:</p>
                <div style="text-align: center; margin: 0.5rem 0;">
                    $$(n^2 - n)' = (2n + 1) - 1 = 2n \implies \left(\frac{n^2 - n}{2}\right)' = n$$
                </div>
                <p>By telescoping inversion, $\sum_{k=0}^{n-1} k = \frac{n(n-1)}{2}$. Shifting indices $k \mapsto k+1$ gives Gauss's famous formula:</p>
                <div style="text-align: center; margin: 0.5rem 0; font-size: 1.1rem;">
                    $$\sum_{k=1}^n k = \frac{n(n+1)}{2}$$
                </div>
            </div>

            <!-- FOOTER NAVIGATION -->
            <div style="margin-top: 3rem; padding-top: 1.5rem; border-top: 1px solid var(--border); display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
                <a href="week1-lecture2.html" style="color: var(--accent); text-decoration: none; font-weight: 600;">&larr; Lecture 2: Numbers &amp; Completeness</a>
                <a href="week2.html" style="background: var(--accent); color: white; padding: 0.6rem 1.2rem; border-radius: 6px; text-decoration: none; font-weight: 600;">Next: Week 2 Module &rarr;</a>
            </div>
        </div>
    </div>
</body>
</html>'''

def generate_week1_pages():
    files = {
        'week1.html': build_week1_hub_html(),
        'week1-lecture1.html': build_lecture1_html(),
        'week1-lecture2.html': build_lecture2_html(),
        'week1-lecture3.html': build_lecture3_html()
    }
    for filename, content in files.items():
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Generated {filename}")

def execute_git_sync():
    commit_message = (
        "Split Week 1 curriculum into three dedicated lecture pages\n\n"
        "Decomposed week1.html into a dedicated overview hub and three distinct\n"
        "lecture modules: Lecture 1 (Sets, Functions, and Peano's Axioms),\n"
        "Lecture 2 (Numbers, Metric Properties, and Completeness), and Lecture 3\n"
        "(Sequences, Differences, and Sums). Preserved all interactive SVG\n"
        "animations, responsive infoboxes, and friendly pedagogical narratives."
    )
    commands = [
        ['git', 'add', 'week1.html', 'week1-lecture1.html', 'week1-lecture2.html', 'week1-lecture3.html', 'update.py'],
        ['git', 'commit', '-m', commit_message],
        ['git', 'push', 'origin', 'main']
    ]
    for cmd in commands:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(f"> {' '.join(cmd)}\n{result.stdout}{result.stderr}")

if __name__ == '__main__':
    generate_week1_pages()
    execute_git_sync()
