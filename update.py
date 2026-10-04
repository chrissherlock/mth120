#!/usr/bin/env python3
import os
import subprocess

def inject_complete_week1_curriculum():
    filepath = 'week1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    comprehensive_curriculum = r'''            <!-- COMPREHENSIVE LECTURE 1, 2, & 3 CURRICULUM -->
            <section class="lecture-curriculum" style="margin-top: 2rem; display: flex; flex-direction: column; gap: 2rem;">

                <!-- LECTURE 1: SETS AND FUNCTIONS -->
                <div class="card" style="background: #ffffff; border: 1px solid var(--border); border-radius: 8px; padding: 1.5rem;">
                    <div style="font-weight: 700; font-size: 1.25rem; color: #0f172a; margin-bottom: 0.75rem; border-bottom: 2px solid #e2e8f0; padding-bottom: 0.5rem;">
                        Lecture 1: Sets, Operations, and Functions
                    </div>

                    <div style="font-weight: 600; font-size: 1.05rem; color: #1e293b; margin-top: 1rem;">1. Sets and Cardinality</div>
                    <p style="font-size: 0.95rem; line-height: 1.6; color: #334155;">
                        A set is an unordered collection of distinct elements. The number of elements in a set $A$ is its <strong>cardinality</strong>, denoted $|A|$.
                        The empty set is written $\emptyset = \{\}$, with $|\emptyset| = 0$.
                    </p>
                    <p style="font-size: 0.95rem; line-height: 1.6; color: #334155;">
                        Sets may have infinite cardinality. The standard number sets satisfy the inclusion chain:
                    </p>
                    <div style="text-align: center; margin: 1rem 0; font-size: 1rem;">
                        $$\mathbb{N} \subseteq \mathbb{Z} \subseteq \mathbb{Q} \subseteq \mathbb{R} \subseteq \mathbb{C}$$
                    </div>
                    <p style="font-size: 0.95rem; line-height: 1.6; color: #334155;">
                        Comparing infinite cardinalities reveals distinct sizes of infinity:
                    </p>
                    <div style="text-align: center; margin: 1rem 0; font-size: 1rem;">
                        $$\infty = |\mathbb{N}| = |\mathbb{Z}| = |\mathbb{Q}| \le |\mathbb{R}| = |\mathbb{C}|$$
                    </div>

                    <div style="font-weight: 600; font-size: 1.05rem; color: #1e293b; margin-top: 1.25rem;">2. Set Operations</div>
                    <p style="font-size: 0.95rem; line-height: 1.6; color: #334155;">Given sets $A$ and $B$:</p>
                    <ul style="font-size: 0.95rem; line-height: 1.6; color: #334155; margin-left: 1.5rem;">
                        <li><strong>Union:</strong> $A \cup B = \{x : x \in A \text{ or } x \in B\}$. Note $A \cup \emptyset = A$.</li>
                        <li><strong>Intersection:</strong> $A \cap B = \{x : x \in A \text{ and } x \in B\}$. Note $A \cap \emptyset = \emptyset$.</li>
                        <li><strong>Difference:</strong> $A \setminus B = \{x : x \in A \text{ and } x \notin B\}$. Note that $A \setminus B \ne B \setminus A$.</li>
                        <li><strong>Cartesian Product:</strong> $A \times B = \{(a, b) : a \in A, b \in B\}$ (consisting of ordered pairs). The cardinality satisfies $|A \times B| = |A| \times |B|$. The Cartesian plane is $\mathbb{R} \times \mathbb{R} = \mathbb{R}^2$.</li>
                    </ul>

                    <div style="font-weight: 600; font-size: 1.05rem; color: #1e293b; margin-top: 1.25rem;">3. Functions, Mappings, and Inverses</div>
                    <p style="font-size: 0.95rem; line-height: 1.6; color: #334155;">
                        A function $f: X \to Y$ assigns each element $x \in X$ to an element $f(x) \in Y$, where $X$ is the <strong>domain</strong> and $Y$ is the <strong>codomain</strong>. The <strong>range</strong> is $\{f(x) : x \in X\} \subseteq Y$.
                    </p>
                    <ul style="font-size: 0.95rem; line-height: 1.6; color: #334155; margin-left: 1.5rem;">
                        <li><strong>Surjective (Onto):</strong> A function is surjective if its range equals its codomain ($\text{range} = Y$).</li>
                        <li><strong>Injective (One-to-One):</strong> A function is injective if distinct inputs give distinct outputs: $x \ne y \implies f(x) \ne f(y)$. For instance, $f: \mathbb{Z} \to \mathbb{Z}$ defined by $f(x) = x^2$ is not injective because $f(-1) = 1 = f(1)$.</li>
                        <li><strong>Bijective:</strong> A function that is both injective and surjective.</li>
                        <li><strong>Composition:</strong> Given $f: X \to Y$ and $g: Y \to Z$, the composite function is $(g \circ f)(x) = g(f(x))$.</li>
                        <li><strong>Inverse Function:</strong> If $f: X \to Y$ is bijective, it possesses an inverse $f^{-1}: Y \to X$ satisfying $(f^{-1} \circ f)(x) = x$ and $(f \circ f^{-1})(y) = y$.</li>
                    </ul>
                </div>

                <!-- LECTURE 2: NUMBERS AND REAL ANALYSIS -->
                <div class="card" style="background: #ffffff; border: 1px solid var(--border); border-radius: 8px; padding: 1.5rem;">
                    <div style="font-weight: 700; font-size: 1.25rem; color: #0f172a; margin-bottom: 0.75rem; border-bottom: 2px solid #e2e8f0; padding-bottom: 0.5rem;">
                        Lecture 2: Numbers, Metric Properties, and Completeness
                    </div>

                    <div style="font-weight: 600; font-size: 1.05rem; color: #1e293b; margin-top: 1rem;">1. Density of the Rationals</div>
                    <p style="font-size: 0.95rem; line-height: 1.6; color: #334155;">
                        <strong>Proposition 1:</strong> For any two distinct rational numbers $a$ and $b$, there are infinitely many rational numbers between them.
                    </p>
                    <div style="background: #f8fafc; border-left: 4px solid #0284c7; padding: 0.75rem 1rem; margin: 0.75rem 0; font-size: 0.92rem; color: #334155;">
                        <em>Proof:</em> Assume $a < b$. The midpoint $c_1 = \frac{a+b}{2}$ is rational since $\mathbb{Q}$ is closed under addition and division. Evaluating distances:
                        $$c_1 - a = \frac{a+b}{2} - a = \frac{b-a}{2} > 0 \implies a < c_1$$
                        $$b - c_1 = b - \frac{a+b}{2} = \frac{b-a}{2} > 0 \implies c_1 < b$$
                        Repeating this construction yields $c_2 = \frac{a+c_1}{2}$ such that $a < c_2 < c_1$, generating an infinite descending chain of distinct rationals $b > c_1 > c_2 > c_3 > \dots > a$.
                    </div>

                    <div style="font-weight: 600; font-size: 1.05rem; color: #1e293b; margin-top: 1.25rem;">2. Rational Gaps and the Irrationality of $\sqrt{2}$</div>
                    <p style="font-size: 0.95rem; line-height: 1.6; color: #334155;">
                        Despite $\mathbb{Q}$ being dense, it contains structural gaps. Consider the diagonal of a unit square: by Pythagoras' theorem, $c^2 = 1^2 + 1^2 = 2 \implies c = \sqrt{2}$.
                    </p>
                    <div style="background: #f8fafc; border-left: 4px solid #0284c7; padding: 0.75rem 1rem; margin: 0.75rem 0; font-size: 0.92rem; color: #334155;">
                        <em>Proof by Contradiction:</em> Assume $\sqrt{2} = \frac{p}{q}$ for integers $p, q$ with $q \ne 0$. Then $\frac{p^2}{q^2} = 2$, meaning $p^2 = 2q^2$.
                        By the Fundamental Theorem of Arithmetic, every integer has a unique prime factorisation. In the prime factorisation of any perfect square, each prime factor appears with an even exponent.
                        Therefore, $p^2$ has an even number of prime factors (counting multiplicities), while $2q^2$ has an odd number of prime factors due to the extra factor of $2$.
                        An even integer cannot equal an odd integer, creating a contradiction. Hence $\sqrt{2} \notin \mathbb{Q}$.
                    </div>

                    <div style="font-weight: 600; font-size: 1.05rem; color: #1e293b; margin-top: 1.25rem;">3. Axiomatic Field &amp; Order Properties of $\mathbb{R}$</div>
                    <p style="font-size: 0.95rem; line-height: 1.6; color: #334155;">
                        The real numbers $\mathbb{R}$ extend $\mathbb{Q}$ by uniting rationals with irrationals. For all $a, b, c \in \mathbb{R}$:
                    </p>
                    <ul style="font-size: 0.95rem; line-height: 1.6; color: #334155; margin-left: 1.5rem;">
                        <li><strong>Identities &amp; Inverses:</strong> Additive identity $0 + a = a$, multiplicative identity $1a = a$. For each $a$, an additive inverse satisfies $a + (-a) = 0$. For $a \ne 0$, a reciprocal satisfies $a \cdot a^{-1} = 1$.</li>
                        <li><strong>Algebraic Laws:</strong> Commutativity ($a+b=b+a$, $ab=ba$), associativity, and distributivity ($(a+b)c = ac + bc$).</li>
                        <li><strong>Trichotomy:</strong> Exactly one of $a > b$, $a = b$, or $a < b$ holds.</li>
                        <li><strong>Order Preservation:</strong> If $a > b$ and $b > c$, then $a > c$. If $a > b$, then $a+c > b+c$. If $a > b$ and $c > 0$, then $ac > bc$.</li>
                    </ul>

                    <div style="font-weight: 600; font-size: 1.05rem; color: #1e293b; margin-top: 1.25rem;">4. Absolute Value and Distance</div>
                    <p style="font-size: 0.95rem; line-height: 1.6; color: #334155;">
                        The absolute value function $|\cdot|: \mathbb{R} \to \mathbb{R}$ defines Euclidean distance: $\text{dist}(a, b) = |a - b|$.
                    </p>
                    <div style="background: #f8fafc; border-left: 4px solid #0284c7; padding: 0.75rem 1rem; margin: 0.75rem 0; font-size: 0.92rem; color: #334155;">
                        <strong>Proposition 2 (Properties of Absolute Value):</strong>
                        <ol style="margin-left: 1.25rem; margin-top: 0.5rem;">
                            <li>$|a| \ge 0$, and $|a| = 0 \iff a = 0$.</li>
                            <li>$|ab| = |a| \cdot |b|$.</li>
                            <li>$|a|^2 = a^2$.</li>
                            <li><strong>Triangle Inequality:</strong> $|a + b| \le |a| + |b|$.<br>
                                <em>Proof:</em> If $a+b \ge 0$, then $|a+b| = a+b \le |a| + |b|$. If $a+b < 0$, then $|a+b| = -(a+b) = (-a) + (-b) \le |a| + |b|$ since both $x, -x \le |x|$.
                            </li>
                            <li><strong>Reverse Triangle Inequality:</strong> $||a| - |b|| \le |a - b|$.</li>
                        </ol>
                    </div>

                    <div style="font-weight: 600; font-size: 1.05rem; color: #1e293b; margin-top: 1.25rem;">5. Bounds, Intervals, and Completeness</div>
                    <p style="font-size: 0.95rem; line-height: 1.6; color: #334155;">
                        A set $S \subseteq \mathbb{R}$ is <strong>bounded above</strong> if there exists $K \in \mathbb{R}$ such that $x \le K$ for all $x \in S$ ($K$ is an upper bound). Similarly, $S$ is <strong>bounded below</strong> if there exists $k \in \mathbb{R}$ such that $k \le x$ for all $x \in S$ ($k$ is a lower bound). A set with both is <strong>bounded</strong>.
                    </p>
                    <ul style="font-size: 0.95rem; line-height: 1.6; color: #334155; margin-left: 1.5rem;">
                        <li><strong>Intervals:</strong> Bounded intervals include closed $[a, b] = \{x : a \le x \le b\}$, open $(a, b) = \{x : a < x < b\}$, and half-open $[a, b), (a, b]$. Unbounded intervals extend to infinity: $[a, \infty), (a, \infty), (-\infty, a]$.</li>
                        <li><strong>Supremum ($\sup S$):</strong> The least upper bound of $S$. Satisfies: (1) $s$ is an upper bound of $S$; (2) If $K$ is any upper bound of $S$, then $s \le K$.</li>
                        <li><strong>Infimum ($\inf S$):</strong> The greatest lower bound of $S$.</li>
                        <li><strong>The Completeness Axiom:</strong> Every non-empty subset of $\mathbb{R}$ that is bounded above has a supremum in $\mathbb{R}$.</li>
                    </ul>
                    <p style="font-size: 0.95rem; line-height: 1.6; color: #334155;">
                        <strong>The Rational Incompleteness Counterexample:</strong> Consider $S = \{x \in \mathbb{Q} : x^2 < 2\} \subseteq \mathbb{Q}$. $S$ is bounded above in $\mathbb{Q}$ (e.g., by 2 or 10), but has no supremum within $\mathbb{Q}$ because $\sqrt{2} \notin \mathbb{Q}$.
                    </p>
                </div>

                <!-- LECTURE 3: SEQUENCES AND DERIVED SEQUENCES -->
                <div class="card" style="background: #ffffff; border: 1px solid var(--border); border-radius: 8px; padding: 1.5rem;">
                    <div style="font-weight: 700; font-size: 1.25rem; color: #0f172a; margin-bottom: 0.75rem; border-bottom: 2px solid #e2e8f0; padding-bottom: 0.5rem;">
                        Lecture 3: Sequences, Monotonicity, and Derived Sequences
                    </div>

                    <div style="font-weight: 600; font-size: 1.05rem; color: #1e293b; margin-top: 1rem;">1. Formal Sequence Definitions</div>
                    <p style="font-size: 0.95rem; line-height: 1.6; color: #334155;">
                        A sequence is a function $f: \mathbb{N} \to \mathbb{R}$, written using indexed notation as an ordered list:
                    </p>
                    <div style="text-align: center; margin: 1rem 0; font-size: 1rem;">
                        $$(a_n)_{n=0}^\infty = (a_0, a_1, a_2, \dots)$$
                    </div>
                    <ul style="font-size: 0.95rem; line-height: 1.6; color: #334155; margin-left: 1.5rem;">
                        <li><strong>Arithmetic Sequence:</strong> $c_n = an + b$, adding fixed difference $a$ at each step.</li>
                        <li><strong>Geometric Sequence:</strong> $c_n = aq^n$ (with $a \ne 0, q \ne 0, 1$), scaling by ratio $q$ at each step.</li>
                        <li><strong>Monotonicity Classifications:</strong>
                            A sequence is <em>constant</em> if $\exists c \in \mathbb{R}$ such that $\forall n, a_n = c$;
                            <em>positive</em> (non-negative) if $\forall n, a_n > 0$ ($a_n \ge 0$);
                            <em>strictly increasing</em> (increasing) if $\forall n, a_{n+1} > a_n$ ($a_{n+1} \ge a_n$);
                            <em>strictly decreasing</em> (decreasing) if $\forall n, a_{n+1} < a_n$ ($a_{n+1} \le a_n$).
                        </li>
                    </ul>

                    <div style="font-weight: 600; font-size: 1.05rem; color: #1e293b; margin-top: 1.25rem;">2. The Derived Sequence ($a'_n$)</div>
                    <p style="font-size: 0.95rem; line-height: 1.6; color: #334155;">
                        For any sequence $(a_n)_{n=0}^\infty$, its <strong>derived sequence</strong> $(a'_n)_{n=0}^\infty$ is defined by discrete forward differences:
                    </p>
                    <div style="text-align: center; margin: 1rem 0; font-size: 1rem;">
                        $$a'_n = a_{n+1} - a_n \implies (a'_n)_{n=0}^\infty = (a_1 - a_0, a_2 - a_1, a_3 - a_2, \dots)$$
                    </div>

                    <div style="background: #f8fafc; border-left: 4px solid #0284c7; padding: 0.75rem 1rem; margin: 0.75rem 0; font-size: 0.92rem; color: #334155;">
                        <strong>Proposition 4 (Monotonicity &amp; Constancy via Derived Sequences):</strong>
                        <ul style="margin-left: 1.25rem; margin-top: 0.5rem;">
                            <li>$(a_n)$ is constant $\iff a'_n = 0$ for all $n$.</li>
                            <li>$(a_n)$ is (strictly) increasing $\iff a'_n \ge 0$ ($a'_n > 0$) for all $n$.</li>
                            <li>$(a_n)$ is (strictly) decreasing $\iff a'_n \le 0$ ($a'_n < 0$) for all $n$.</li>
                        </ul>
                        <em>Proof of Constancy:</em> If $a_n = c$ for all $n$, then $a'_n = a_{n+1} - a_n = c - c = 0$.
                        Conversely, suppose $a'_n = 0$ for all $n$. Let $a_0 = c$. By induction, assume $a_k = c$. Then $a_{k+1} = a_k + (a_{k+1} - a_k) = a_k + a'_k = c + 0 = c$. Thus $a_n = c$ for all $n$.
                    </div>

                    <div style="font-weight: 600; font-size: 1.05rem; color: #1e293b; margin-top: 1.25rem;">3. Derived Sequences of Standard Functions</div>
                    <ul style="font-size: 0.95rem; line-height: 1.6; color: #334155; margin-left: 1.5rem;">
                        <li><strong>Arithmetic ($c_n = an + b$):</strong> $c'_n = [a(n+1) + b] - [an + b] = a$.</li>
                        <li><strong>Geometric ($c_n = aq^n$):</strong> $c'_n = aq^{n+1} - aq^n = aq^n(q - 1)$.</li>
                        <li><strong>Quadratic ($c_n = n^2$):</strong> $c'_n = (n+1)^2 - n^2 = (n^2 + 2n + 1) - n^2 = 2n + 1$.</li>
                    </ul>

                    <div style="font-weight: 600; font-size: 1.05rem; color: #1e293b; margin-top: 1.25rem;">4. Inversion via Telescoping Sums and Gauss's Formula</div>
                    <p style="font-size: 0.95rem; line-height: 1.6; color: #334155;">
                        Given a derived sequence $(a'_n)$, the original sequence terms are recovered via telescoping summation:
                    </p>
                    <div style="text-align: center; margin: 1rem 0; font-size: 1rem;">
                        $$a_n = a_0 + \sum_{k=0}^{n-1} a'_k = a_0 + (a'_0 + a'_1 + \dots + a'_{n-1})$$
                    </div>
                    <p style="font-size: 0.95rem; line-height: 1.6; color: #334155;">
                        <strong>Derivation of Gauss's Summation Formula:</strong> Suppose we seek $a_n$ whose derived sequence is $a'_n = n$.
                        Since $(n^2)' = 2n + 1$ and $(n)' = 1$, by linearity the derived sequence of $(n^2 - n)$ is $(2n+1) - 1 = 2n$.
                        Dividing by 2 gives:
                    </p>
                    <div style="text-align: center; margin: 1rem 0; font-size: 1rem;">
                        $$\left(\frac{n^2 - n}{2}\right)' = n \implies \sum_{k=0}^{n-1} k = \frac{n(n-1)}{2}$$
                    </div>
                    <p style="font-size: 0.95rem; line-height: 1.6; color: #334155;">
                        Shifting the index range gives the standard Gaussian summation formula:
                    </p>
                    <div style="text-align: center; margin: 1rem 0; font-size: 1rem;">
                        $$\sum_{k=1}^n k = \frac{n(n+1)}{2}$$
                    </div>
                </div>

            </section>'''

    marker = '</section>'
    if 'Lecture 1: Sets, Operations, and Functions' in content:
        print("Comprehensive curriculum is already present in week1.html.")
        return

    # Find the closing main content or module section
    last_section_idx = content.rfind(marker)
    if last_section_idx != -1:
        content = content[:last_section_idx] + comprehensive_curriculum + '\n\n' + content[last_section_idx:]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully injected all curriculum topics from Lectures 1, 2, and 3 into week1.html.")
    else:
        print("Could not find insertion marker '</section>' in week1.html.")

def execute_git_sync():
    commit_message = (
        "Incorporate complete lecture topics into week1.html\n\n"
        "Injected comprehensive content from Lectures 1, 2, and 3 into week1.html\n"
        "covering sets, cardinality, function mappings, rational density, sqrt(2)\n"
        "prime factorisation, field axioms, metric distance, triangle inequality,\n"
        "bounds, completeness, derived sequences, and Gaussian inversion."
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
    inject_complete_week1_curriculum()
    execute_git_sync()
