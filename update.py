#!/usr/bin/env python3
"""
Surgically restore all truncated analytical sections in week2-lecture4.html.
Reintegrates Sections 2, 4, 5, and 6 in full while preserving all widgets and SVGs.
Uses callable replacements in re.sub to prevent regex template escape errors.
"""

from pathlib import Path
import re
import subprocess
import sys

TARGET_FILE = Path("week2-lecture4.html")
SCRIPT_FILE = Path(__file__).resolve()

COMMIT_SUBJECT = (
    "Restore foundational theorems, limit laws, and divergence proofs"
)
COMMIT_BODY = (
    "Reintegrate full analytical essays and unboxed proofs across Sections\n"
    "2, 4, 5, and 6 of week2-lecture4.html. Restore the Uniqueness of Limits\n"
    "epsilon-half proof, the Tail Invariance shift theorem and corollary,\n"
    "the Order Limit Theorem contradiction proof with midpoint buffers,\n"
    "the Proposition 5 structural guarantees, the Algebraic Limit Laws\n"
    "compositionality bridge, and the formal quantifier negation rules."
)

RESTORED_SECTION_2 = r"""            <!-- SECTION 2: UNBOXED, DETAILED, EMPATHETIC EXPLANATION -->
            <h2 id="section-quantifiers">2. Quantifier Order, Timing, and Dependencies</h2>

            <h3 style="color: #0f172a; margin-top: 1.5rem;">The Grammar of Analysis: Why Order Matters</h3>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                In everyday English, word order can be remarkably forgiving. You can say <em>"Everyone loves someone"</em> or <em>"There is someone whom everyone loves,"</em> and listeners usually piece together what you mean. But in formal mathematical analysis, the order of quantifiers is not stylistic—it is the entire logical backbone of the argument. Changing the order of two quantifiers doesn't tweak the sentence; it completely alters the reality being described.
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                When you see a long chain of symbols like:
            </p>
            <p style="text-align: center; margin: 1.25rem 0; font-size: 1.2rem;">
                $$\forall \epsilon > 0 \quad \exists N \in \mathbb{N} \quad \forall n > N, \quad |a_n - L| < \epsilon$$
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                the golden rule is to <strong>read strictly from left to right</strong>. Each quantifier establishes a distinct turn in a conversation or a sequential dialogue. A variable introduced further to the right is allowed to respond to and depend on variables to its left, but variables to the left can never look ahead to what hasn't been chosen yet.
            </p>

            <h3 style="color: #0f172a; margin-top: 1.75rem;">The "Who Knows What" Rule: Order of Information</h3>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                To see why $N$ depends on $\epsilon$, let's trace the visibility of information through the three variables from left to right:
            </p>
            <ul style="margin: 0.5rem 0 1.5rem 1.25rem; color: #334155; line-height: 1.75; font-size: 0.98rem;">
                <li style="margin-bottom: 0.85rem;">
                    <strong>The First Move ($\forall \epsilon > 0$):</strong><br>
                    $\epsilon$ is chosen first and in complete isolation. The person picking $\epsilon$ has no idea what $N$ will be, and they don't care. They can challenge you with $\epsilon = 1$, $\epsilon = 0.05$, or $\epsilon = 10^{-12}$.
                </li>
                <li style="margin-bottom: 0.85rem;">
                    <strong>The Response ($\exists N \in \mathbb{N}$):</strong><br>
                    Now it is your turn to pick $N$. Because your move happens <em>after</em> $\epsilon$ has been announced, you make your choice with <strong>full knowledge of $\epsilon$</strong>. You are responding to their move. Mathematically, this means $N$ is a function of $\epsilon$—written $N = N(\epsilon)$. If the challenger changes $\epsilon$ to a tighter tolerance, you are completely free to pick a larger $N$.
                </li>
                <li>
                    <strong>The Final Verification ($\forall n > N$):</strong><br>
                    Finally, we test the tail. The variable $n$ is evaluated only after both $\epsilon$ and $N$ are already locked into place, inspecting every single step strictly past your cutoff milestone to verify that distance stays strictly below $\epsilon$.
                </li>
            </ul>

            <h3 style="color: #0f172a; margin-top: 1.75rem;">When Can You Swap Quantifiers? (The Commutativity Rule)</h3>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                A helpful rule of thumb to keep in mind is:
            </p>
            <ul style="margin: 0.5rem 0 1.25rem 1.25rem; color: #334155; line-height: 1.7; font-size: 0.98rem;">
                <li style="margin-bottom: 0.5rem;">
                    <strong>Quantifiers of the same type always commute:</strong> You can safely swap two universal quantifiers ($\forall x \, \forall y \iff \forall y \, \forall x$) or two existential quantifiers ($\exists x \, \exists y \iff \exists y \, \exists x$) without changing the mathematical meaning.
                </li>
                <li>
                    <strong>Alternating quantifiers NEVER commute:</strong> Swapping a $\forall$ with an $\exists$ radically changes what the statement demands. In analysis, $\forall \epsilon \, \exists N$ and $\exists N \, \forall \epsilon$ describe two completely different universes.
                </li>
            </ul>

            <h3 style="color: #0f172a; margin-top: 1.75rem;">The Fatal Quantifier Swap: Why $\exists N \; \forall \epsilon$ Breaks Mathematics</h3>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                To see the power of quantifier order firsthand, let's conduct a thought experiment. What would happen if a student accidentally reversed the first two quantifiers in an exam and wrote:
            </p>
            <p style="text-align: center; margin: 1.25rem 0; font-size: 1.15rem; color: #b91c1c;">
                $$\exists N \in \mathbb{N} \quad \forall \epsilon > 0 \quad \forall n > N, \quad |a_n - L| < \epsilon \quad \text{?}$$
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Read it from left to right using our "who knows what" rule:
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                The statement now opens with $\exists N \in \mathbb{N}$. That means a single milestone number $N$ must be chosen <em>first</em>, before anyone has named $\epsilon$. Then, that same fixed $N$ must satisfy $|a_n - L| < \epsilon$ for <strong>every single positive $\epsilon$ simultaneously</strong>!
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Think about what that requires. If $|a_n - L| < \epsilon$ for every $\epsilon > 0$, what non-negative real number is strictly smaller than every positive number? Only zero! The only distance smaller than every positive tolerance is exactly zero:
            </p>
            <p style="text-align: center; margin: 1.25rem 0; font-size: 1.15rem;">
                $$|a_n - L| = 0 \implies a_n = L \quad \text{for all } n > N$$
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                By accidentally swapping those two words, the definition no longer describes sequences that approach a limit. It only describes sequences that literally <strong>freeze and become permanently constant</strong> after step $N$ (like $3, 7, 2, 5, 5, 5, 5, \dots$). A sequence like $a_n = 1/n$, which never equals $0$ but clearly converges to $0$, would fail this broken test!
            </p>

            <h3 style="color: #0f172a; margin-top: 1.75rem;">A Practical Mental Checklist for Reading Proofs</h3>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Whenever you sit down to write or read an $\epsilon\text{-}N$ proof, keep this internal dialogue running:
            </p>
            <ol style="margin: 0.5rem 0 1.5rem 1.25rem; color: #334155; line-height: 1.75; font-size: 0.98rem;">
                <li style="margin-bottom: 0.6rem;">
                    <strong>When you see $\forall \epsilon > 0$:</strong> Remind yourself, <em>"I do not choose $\epsilon$. Someone hands it to me. I must treat $\epsilon$ as an arbitrary positive constant throughout my proof."</em>
                </li>
                <li style="margin-bottom: 0.6rem;">
                    <strong>When you see $\exists N \in \mathbb{N}$:</strong> Say to yourself, <em>"Now it's my turn. I must find a formula for $N$ that uses $\epsilon$. It is completely fine if $N$ gets huge when $\epsilon$ is tiny."</em>
                </li>
                <li>
                    <strong>When you see $\forall n > N$:</strong> Say to yourself, <em>"Now I verify my work. I let $n$ be an arbitrary index past $N$ and prove that the distance inequality $|a_n - L| < \epsilon$ holds algebraically."</em>
                </li>
            </ol>"""

COMPLETE_SECTIONS_4_5_6 = r"""            <!-- SECTION 4: UNBOXED, DETAILED, EMPATHETIC EXPLANATION -->
            <h2 id="section-prop5">4. Properties of Convergent Sequences (Proposition 5) &amp; Foundational Theorems</h2>

            <h3 style="color: #0f172a; margin-top: 1.5rem;">Structural Guarantees: The Free Gifts of Convergence</h3>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Writing an $\epsilon\text{-}N$ proof from scratch every time you encounter a new sequence would be exhausting. Mathematicians don't rebuild every argument from raw definitions; instead, they prove <strong>structural theorems</strong>. These are universal guarantees: once you know a sequence converges, you automatically inherit powerful properties for free, without ever needing to guess a cutoff index again.
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                In this section, we explore Proposition 5 along with three foundational theorems that solidify the logical architecture of limits: Uniqueness, Tail Invariance, and the Order Limit Theorem.
            </p>

            <h3 style="color: #0f172a; margin-top: 1.75rem;">Theorem: Uniqueness of Limits</h3>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Before writing $\lim a_n = L$, we must guarantee that a sequence cannot have two different limits. If a sequence settles down, its destination is uniquely determined.
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                <strong>The Theorem:</strong> If a sequence $(a_n)$ converges to $L$ and also converges to $M$, then $L = M$.
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                <strong>The Proof Strategy (The $\epsilon/2$ Technique):</strong><br>
                Let $\epsilon > 0$ be given. Because $a_n \to L$, there is a cutoff $N_1$ where $|a_n - L| < \epsilon/2$. Because $a_n \to M$, there is a cutoff $N_2$ where $|a_n - M| < \epsilon/2$. Let $N = \max(N_1, N_2)$. For any index $n > N$, both inequalities hold. Using the triangle inequality on the fixed distance $|L - M|$:
            </p>
            <p style="text-align: center; margin: 1.25rem 0; font-size: 1.15rem;">
                $$\begin{aligned}
                |L - M| &= |(L - a_n) + (a_n - M)| \\
                &\le |a_n - L| + |a_n - M| \\
                &< \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon
                \end{aligned}$$
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                We have shown that the non-negative real number $|L - M|$ is strictly smaller than <em>every</em> positive number $\epsilon$. The only non-negative number with that property is zero. Thus, $|L - M| = 0$, which proves $L = M$. $\blacksquare$
            </p>

            <h3 style="color: #0f172a; margin-top: 1.75rem;">Theorem: Tail Invariance (The Shift &amp; Truncation Theorem)</h3>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Real analysis teaches us an empowering truth: <strong>initial terms do not matter</strong> for convergence. If you are ever worried about a sequence having a few messy starting terms, this theorem provides absolute peace of mind.
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                There are two common ways mathematicians state this principle:
            </p>
            <ul style="margin: 0.5rem 0 1.25rem 1.25rem; color: #334155; line-height: 1.75; font-size: 0.98rem;">
                <li style="margin-bottom: 0.6rem;">
                    <strong>1. The Finite Modification Form:</strong> Let $(a_n)$ and $(b_n)$ be two sequences. If there exists some cutoff index $N_0 \in \mathbb{N}$ such that $a_n = b_n$ for all $n > N_0$, then either both sequences converge to the exact same limit, or both diverge:
                    $$\lim_{n\to\infty} a_n = \lim_{n\to\infty} b_n$$
                </li>
                <li>
                    <strong>2. The Index Shift Form:</strong> Let $(a_n)_{n=0}^\infty$ be a sequence, and let $k \in \mathbb{N}$ be any fixed integer shift. Then $(a_n)$ converges to $L$ if and only if the shifted sequence $(a_{n+k})_{n=0}^\infty$ converges to $L$:
                    $$\lim_{n\to\infty} a_n = L \iff \lim_{n\to\infty} a_{n+k} = L$$
                </li>
            </ul>

            <h4 style="color: #0f172a; margin-top: 1.5rem;">The Proof of the Finite Modification Form</h4>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Suppose $(a_n)$ converges to limit $L$. We want to prove that $(b_n)$ also converges to $L$.
            </p>
            <ol style="margin: 0.5rem 0 1.5rem 1.25rem; color: #334155; line-height: 1.75; font-size: 0.98rem;">
                <li style="margin-bottom: 0.6rem;">
                    Let $\epsilon > 0$ be arbitrary.
                </li>
                <li style="margin-bottom: 0.6rem;">
                    Because $a_n \to L$, the definition of convergence provides a cutoff $N_a \in \mathbb{N}$ such that:
                    $$n > N_a \implies |a_n - L| < \epsilon$$
                </li>
                <li style="margin-bottom: 0.6rem;">
                    We are given that $a_n = b_n$ for all $n > N_0$. Now, choose the master cutoff:
                    $$N = \max(N_a, N_0)$$
                </li>
                <li>
                    For any index $n > N$, both conditions hold simultaneously:
                    $$\begin{aligned}
                    n > N_0 &\implies b_n = a_n \\
                    n > N_a &\implies |a_n - L| < \epsilon
                    \end{aligned}$$
                    Substituting $b_n$ for $a_n$ yields $|b_n - L| = |a_n - L| < \epsilon$. Therefore, $(b_n)$ converges to $L$. By symmetry, if $(b_n)$ converges to $L$, then $(a_n)$ must converge to $L$. $\blacksquare$
                </li>
            </ol>

            <h4 style="color: #0f172a; margin-top: 1.5rem;">Why Tail Invariance Is a Superpower for Beginners</h4>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                This theorem gives you three practical mathematical liberties:
            </p>
            <ul style="margin: 0.5rem 0 1.5rem 1.25rem; color: #334155; line-height: 1.75; font-size: 0.98rem;">
                <li style="margin-bottom: 0.6rem;">
                    <strong>Early Singularities Don't Matter:</strong> Consider $a_n = \frac{n}{n-2}$. At $n=2$, this formula divides by zero and is undefined! But for all $n \ge 3$, it is perfectly well-behaved. The Tail Invariance Theorem tells us we can simply define the sequence starting at $n=3$ without altering its limit in any way.
                </li>
                <li style="margin-bottom: 0.6rem;">
                    <strong>Starting Indices Don't Matter:</strong> Whether a lecturer writes $(a_n)_{n=0}^\infty$, $(a_n)_{n=1}^\infty$, or $(a_n)_{n=100}^\infty$, the limit is identical. You never need to worry about index shifting changing the convergence.
                </li>
                <li>
                    <strong>Chaotic Warmups Can Be Discarded:</strong> A sequence could jump wildly between $-10^6$ and $+10^6$ for the first million terms. As long as it eventually settles down into an $\epsilon$-corridor, those initial terms are discarded as finite history.
                </li>
            </ul>

            <h3 style="color: #0f172a; margin-top: 1.75rem;">Theorem: Order Limit Theorem (Inequality Preservation)</h3>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                One of the most comforting features of limits is that they respect relative order. If one sequence always stays below another on the number line, its eventual limit cannot leap ahead of the other sequence's limit.
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                <strong>The Formal Statement:</strong> Let $(a_n)$ and $(b_n)$ be convergent sequences with limits $K, L \in \mathbb{R}$:
            </p>
            <p style="text-align: center; margin: 1.25rem 0; font-size: 1.15rem;">
                $$\lim_{n\to\infty} a_n = K \quad \text{and} \quad \lim_{n\to\infty} b_n = L$$
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                If there exists an index $N_0 \in \mathbb{N}$ such that $a_n \le b_n$ for all $n > N_0$, then:
            </p>
            <p style="text-align: center; margin: 1.25rem 0; font-size: 1.15rem;">
                $$K \le L$$
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                <em>Special Single-Sequence Corollary:</em> If $a_n \ge 0$ for all $n > N_0$ and $\lim a_n = K$, then $K \ge 0$. A non-negative sequence cannot converge to a negative number.
            </p>

            <h4 style="color: #0f172a; margin-top: 1.5rem;">The Proof Strategy: Proof by Contradiction via the Midpoint Moat</h4>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                How do we prove this? Proving an inequality directly with $\epsilon\text{-}N$ can feel clumsy. Instead, mathematicians use <strong>Proof by Contradiction</strong>: we assume the opposite—that $K > L$—and watch the system contradict itself.
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                <strong>The Geometric Picture:</strong> If $K > L$, there is a positive gap between them of width $K - L > 0$. If we choose a tolerance equal to half this gap, $\epsilon = \frac{K - L}{2}$, the target windows around $K$ and $L$ will never overlap! Their common boundary will be their exact midpoint, $M = \frac{K + L}{2}$.
            </p>
            <ol style="margin: 0.5rem 0 1.5rem 1.25rem; color: #334155; line-height: 1.75; font-size: 0.98rem;">
                <li style="margin-bottom: 0.6rem;">
                    Assume, for contradiction, that $K > L$. Then $K - L > 0$.
                </li>
                <li style="margin-bottom: 0.6rem;">
                    Set $\epsilon = \frac{K - L}{2} > 0$. Note that $L + \epsilon = \frac{K + L}{2} = K - \epsilon$.
                </li>
                <li style="margin-bottom: 0.6rem;">
                    Since $a_n \to K$, there exists $N_1 \in \mathbb{N}$ such that for all $n > N_1$:
                    $$|a_n - K| < \epsilon \implies a_n > K - \epsilon = \frac{K + L}{2}$$
                </li>
                <li style="margin-bottom: 0.6rem;">
                    Since $b_n \to L$, there exists $N_2 \in \mathbb{N}$ such that for all $n > N_2$:
                    $$|b_n - L| < \epsilon \implies b_n < L + \epsilon = \frac{K + L}{2}$$
                </li>
                <li>
                    Now choose the master cutoff $N = \max(N_0, N_1, N_2)$. For any index $n > N$, all conditions hold at once:
                    $$b_n < \frac{K + L}{2} < a_n \implies b_n < a_n$$
                    This directly contradicts our hypothesis that $a_n \le b_n$ for all $n > N_0$!
                    Therefore, our assumption that $K > L$ must be false. We conclude that $K \le L$. $\blacksquare$
                </li>
            </ol>

            <h4 style="color: #0f172a; margin-top: 1.5rem;">⚠️ The Classic Trap: Why Strict Inequalities Become Non-Strict</h4>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                There is one critical warning every beginner must know, because exam questions love testing it:
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem; font-weight: 600; color: #b91c1c;">
                Strict inequalities between terms are NOT preserved in the limit!
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                If $a_n < b_n$ strictly for every single term in the sequence, you can only conclude that $\lim a_n \le \lim b_n$. You <strong>cannot</strong> claim that $\lim a_n < \lim b_n$.
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                <strong>Why does this happen? The "Pinch Point" Phenomenon:</strong><br>
                Two sequences can maintain a strict gap between themselves at every finite step, but as they travel to infinity, that gap can shrink down to zero. The limits can "touch" at infinity even though no finite pair of terms ever touches.
            </p>
            <ul style="margin: 0.5rem 0 1.5rem 1.25rem; color: #334155; line-height: 1.75; font-size: 0.98rem;">
                <li style="margin-bottom: 0.6rem;">
                    <strong>Counterexample 1:</strong> Let $a_n = 0$ and $b_n = \frac{1}{n}$. Clearly, $0 < \frac{1}{n}$ strictly holds for every $n \in \mathbb{N}^+$. Yet in the limit:
                    $$\lim_{n\to\infty} 0 = 0 \quad \text{and} \quad \lim_{n\to\infty} \frac{1}{n} = 0 \implies 0 \le 0$$
                    The strict inequality has collapsed into equality!
                </li>
                <li>
                    <strong>Counterexample 2:</strong> Let $a_n = -\frac{1}{n}$ and $b_n = \frac{1}{n}$. At every finite index $n$, $a_n$ is strictly negative and $b_n$ is strictly positive ($-\frac{1}{n} < \frac{1}{n}$). Yet both meet at the exact same limit: $0 = 0$.
                </li>
            </ul>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Keep this in mind: limits weaken strict bounds into non-strict bounds ($<$ becomes $\le$, and $>$ becomes $\ge$). This property is the direct precursor to the famous <strong>Squeeze Theorem</strong>, which we will explore in Lecture 5!
            </p>

            <!-- DIAGRAM: Order Limit Theorem -->
            <div style="background: #ffffff; border: 1px solid var(--border); border-radius: 8px; margin: 1.5rem 0; padding: 1.5rem;">
                <h5 style="margin-top: 0; margin-bottom: 1rem; color: #334155; font-size: 0.95rem;">Visualization: Inequality Preservation ($a_n \le b_n \implies K \le L$)</h5>
                <svg viewBox="0 0 740 180" style="width: 100%; height: auto;">
                    <line x1="40" y1="150" x2="700" y2="150" stroke="#cbd5e1" stroke-width="1.5" />
                    <!-- b_n converging to L -->
                    <line x1="40" y1="50" x2="700" y2="50" stroke="#10b981" stroke-dasharray="4" />
                    <text x="705" y="54" font-family="sans-serif" font-size="12" fill="#10b981" font-weight="bold">Limit L</text>
                    <!-- a_n converging to K -->
                    <line x1="40" y1="100" x2="700" y2="100" stroke="#3b82f6" stroke-dasharray="4" />
                    <text x="705" y="104" font-family="sans-serif" font-size="12" fill="#3b82f6" font-weight="bold">Limit K</text>

                    <!-- b_n points (top) -->
                    <circle cx="80" cy="20" r="4" fill="#10b981" />
                    <circle cx="160" cy="35" r="4" fill="#10b981" />
                    <circle cx="240" cy="45" r="4" fill="#10b981" />
                    <circle cx="320" cy="52" r="4" fill="#10b981" />
                    <circle cx="400" cy="49" r="4" fill="#10b981" />
                    <circle cx="480" cy="50.5" r="4" fill="#10b981" />

                    <!-- a_n points (bottom) -->
                    <circle cx="80" cy="140" r="4" fill="#3b82f6" />
                    <circle cx="160" cy="120" r="4" fill="#3b82f6" />
                    <circle cx="240" cy="108" r="4" fill="#3b82f6" />
                    <circle cx="320" cy="98" r="4" fill="#3b82f6" />
                    <circle cx="400" cy="101" r="4" fill="#3b82f6" />
                    <circle cx="480" cy="99.5" r="4" fill="#3b82f6" />

                    <!-- Vertical constraint lines -->
                    <line x1="80" y1="28" x2="80" y2="132" stroke="#94a3b8" stroke-dasharray="2" />
                    <line x1="160" y1="43" x2="160" y2="112" stroke="#94a3b8" stroke-dasharray="2" />
                    <line x1="240" y1="53" x2="240" y2="100" stroke="#94a3b8" stroke-dasharray="2" />
                    <text x="85" y="85" font-family="sans-serif" font-size="10" fill="#64748b">a₁ &le; b₁</text>
                </svg>
            </div>

            <h3 style="color: #0f172a; margin-top: 2rem;">Proposition 5: Fundamental Sequence Properties</h3>

            <h4 style="color: #0f172a; margin-top: 1.25rem;">Property 1: Absolute Value Stabilization ($a_n \to L \implies |a_n| \to |L|$)</h4>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                The first property says that if a sequence of numbers settles down to a limit $L$, then taking the absolute values of those numbers causes them to settle down to $|L|$.
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                <strong>Why does this make intuitive sense?</strong> Absolute value measures distance from the origin $0$. If the points $a_n$ are crowding closer and closer to $L$, their distance from zero must naturally crowd closer and closer to $L$'s distance from zero.
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                <strong>The Rigorous Proof:</strong> The proof relies on a handy tool known as the <em>Reverse Triangle Inequality</em>, which states that for any real numbers $x$ and $y$:
            </p>
            <p style="text-align: center; margin: 1.25rem 0; font-size: 1.15rem;">
                $$\big| |x| - |y| \big| \le |x - y|$$
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Notice what this inequality tells us: the distance between $|a_n|$ and $|L|$ is <em>always smaller than or equal to</em> the distance between $a_n$ and $L$. Therefore, whenever we choose an index $N$ such that $|a_n - L| < \epsilon$, we automatically get:
            </p>
            <p style="text-align: center; margin: 1.25rem 0; font-size: 1.15rem;">
                $$\big| |a_n| - |L| \big| \le |a_n - L| < \epsilon$$
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                The exact same cutoff index $N$ that worked for $a_n$ works immediately for $|a_n|$!
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem; background: #fffbeb; border-left: 4px solid var(--accent); padding: 0.85rem 1.15rem; border-radius: 4px;">
                ⚠️ <strong>A Classic Beginner Trap (The Converse Fails!):</strong> Does $|a_n| \to |L|$ imply that $a_n \to L$? <em>No!</em> Consider the sequence $a_n = (-1)^n = (-1, 1, -1, 1, \dots)$. Taking absolute values gives $|a_n| = 1$, which obviously converges to $1$. But the sequence $a_n$ itself never converges because it permanently oscillates. The only exception where the converse works is when the limit is zero: $|a_n| \to 0 \iff a_n \to 0$.
            </p>

            <h4 style="color: #0f172a; margin-top: 1.75rem;">Property 2: Convergence Implies Boundedness (The Prefix vs. Tail Strategy)</h4>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                The second property is one of the most celebrated cornerstones of analysis:
            </p>
            <p style="text-align: center; margin: 1rem 0; font-size: 1.15rem; font-weight: 600; color: #0f172a;">
                Every convergent sequence is bounded.
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                That is, there exists some positive real number $M > 0$ such that $|a_n| \le M$ for every single index $n \in \mathbb{N}$. In other words, a sequence that converges can never run off to $+\infty$ or $-\infty$.
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                <strong>The Conceptual Dilemma:</strong> An infinite sequence has infinitely many terms. How could we possibly build a single finite fence $[-M, M]$ that holds infinitely many numbers, especially when earlier terms might have jumped around wildly?
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                <strong>The Proof Strategy (Divide and Conquer):</strong> Mathematicians solve this using a two-step technique: we split the sequence into a <em>finite prefix</em> and an <em>infinite tail</em>.
            </p>
            <ol style="margin: 0.5rem 0 1.5rem 1.25rem; color: #334155; line-height: 1.75; font-size: 0.98rem;">
                <li style="margin-bottom: 0.75rem;">
                    <strong>Trapping the Infinite Tail:</strong> Because $a_n \to L$, we can choose <em>any</em> tolerance we like. Let's make our lives easy and simply pick $\epsilon = 1$. By the definition of convergence, there exists some cutoff index $N$ such that:
                    $$n > N \implies |a_n - L| < 1$$
                    Applying the triangle inequality gives $|a_n| = |(a_n - L) + L| \le |a_n - L| + |L| < 1 + |L|$. <em>All infinitely many terms past index $N$ are trapped below the number $|L| + 1$!</em>
                </li>
                <li style="margin-bottom: 0.75rem;">
                    <strong>Checking the Finite Prefix:</strong> What about the terms before the cutoff: $\{a_0, a_1, a_2, \dots, a_N\}$? There are only finitely many of them! Any finite list of real numbers has a guaranteed largest absolute value.
                </li>
                <li>
                    <strong>Building the Global Fence ($M$):</strong> We simply take the maximum over the finite prefix and our tail bound:
                    $$M = \max\Big(|a_0|, |a_1|, |a_2|, \dots, |a_N|, |L| + 1\Big)$$
                    Because every term in the prefix is $\le M$ by definition of a maximum, and every term in the tail is $< |L| + 1 \le M$, the number $M$ bounds the entire infinite sequence. $\blacksquare$
                </li>
            </ol>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                <strong>Does the converse hold?</strong> Again, ask yourself: if a sequence is bounded, does it have to converge? No! Boundedness is a <em>necessary</em> condition for convergence, but not a <em>sufficient</em> one. The sequence $a_n = (-1)^n$ is safely trapped inside $[-1, 1]$, yet it never converges.
            </p>

            <!-- DIAGRAM: Boundedness -->
            <div style="background: #ffffff; border: 1px solid var(--border); border-radius: 8px; margin: 1.5rem 0; padding: 1.5rem;">
                <h5 style="margin-top: 0; margin-bottom: 1rem; color: #334155; font-size: 0.95rem;">Visualization: Prefix/Tail Split for Bounded Sequences</h5>
                <svg viewBox="0 0 740 200" style="width: 100%; height: auto;">
                    <line x1="40" y1="160" x2="700" y2="160" stroke="#cbd5e1" stroke-width="1.5" />

                    <!-- Limit L and Epsilon Band -->
                    <rect x="260" y="80" width="440" height="40" fill="#fde68a" opacity="0.3" stroke="#f59e0b" stroke-dasharray="2" />
                    <line x1="40" y1="100" x2="700" y2="100" stroke="#64748b" stroke-dasharray="4" />
                    <text x="705" y="104" font-family="sans-serif" font-size="12" fill="#64748b">L</text>

                    <!-- Master Fence M -->
                    <line x1="40" y1="30" x2="700" y2="30" stroke="#ef4444" stroke-width="2" opacity="0.5" />
                    <text x="705" y="34" font-family="sans-serif" font-size="12" fill="#ef4444" font-weight="bold">+M</text>

                    <!-- N Cutoff -->
                    <line x1="260" y1="20" x2="260" y2="160" stroke="#0f172a" stroke-dasharray="4" />
                    <text x="265" y="155" font-family="sans-serif" font-size="11" fill="#0f172a">Cutoff N</text>

                    <!-- Prefix Points -->
                    <circle cx="80" cy="140" r="4" fill="#94a3b8" />
                    <circle cx="140" cy="40" r="5" fill="#ef4444" />
                    <text x="140" y="25" font-family="sans-serif" font-size="10" fill="#ef4444" text-anchor="middle">Max of Prefix</text>
                    <circle cx="200" cy="120" r="4" fill="#94a3b8" />
                    <!-- Tail Points -->
                    <circle cx="300" cy="110" r="4" fill="#10b981" />
                    <circle cx="360" cy="90" r="4" fill="#10b981" />
                    <circle cx="420" cy="105" r="4" fill="#10b981" />
                    <circle cx="480" cy="95" r="4" fill="#10b981" />

                    <!-- Labels -->
                    <text x="150" y="180" font-family="sans-serif" font-size="11" fill="#64748b" text-anchor="middle">Finite Prefix (Checked Manually)</text>
                    <text x="480" y="180" font-family="sans-serif" font-size="11" fill="#10b981" text-anchor="middle">Infinite Tail (Trapped by ϵ=1)</text>
                </svg>
            </div>

            <h4 style="color: #0f172a; margin-top: 1.75rem;">Property 3: Preservation of Sign (The Buffer Zone)</h4>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                The third property provides peace of mind when working with signs:
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                If a sequence converges to a strictly positive limit ($L > 0$), then eventually all of its terms must become strictly positive and stay bounded away from zero. Specifically, there is an index $N_0$ such that:
            </p>
            <p style="text-align: center; margin: 1.25rem 0; font-size: 1.15rem;">
                $$a_n > \frac{L}{2} > 0 \quad \text{for all } n > N_0$$
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                (Likewise, if $L < 0$, then eventually $a_n < \frac{L}{2} < 0$).
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                <strong>Why do we care so much about this?</strong> Think ahead to the Algebraic Limit Laws in the next section. When we want to prove that $\lim \frac{a_n}{b_n} = \frac{K}{L}$, we need to divide by $b_n$. But you cannot divide by zero! Even worse, if the numbers $b_n$ got closer and closer to zero, $1/b_n$ would explode to infinity. The preservation of sign property guarantees that if $L \neq 0$, the terms $b_n$ eventually build an impenetrable moat of width $L/2$ between themselves and zero.
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                <strong>The Geometric Proof:</strong> If $L > 0$, the distance from $L$ to zero is exactly $L$. Since we can choose any positive $\epsilon$ in the definition of convergence, let's deliberately choose a tolerance that doesn't reach zero: set $\epsilon = \frac{L}{2}$.
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                By the definition of convergence, there is an index $N_0$ such that for all $n > N_0$, we have $|a_n - L| < \frac{L}{2}$. Unpacking the absolute value bars:
            </p>
            <p style="text-align: center; margin: 1.25rem 0; font-size: 1.15rem;">
                $$-\frac{L}{2} < a_n - L < \frac{L}{2} \implies L - \frac{L}{2} < a_n < L + \frac{L}{2} \implies \frac{L}{2} < a_n < \frac{3L}{2}$$
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Look at the left-hand inequality: $a_n > \frac{L}{2}$. Because $L > 0$, $\frac{L}{2}$ is strictly positive. Every term in the tail is trapped above $\frac{L}{2}$ forever, completely insulated from zero! $\blacksquare$
            </p>

            <!-- SECTION 5: UNBOXED, DETAILED, EMPATHETIC EXPLANATION -->
            <h2 id="section-theorems">5. Algebraic Limit Laws and Proofs (Theorem 1)</h2>

            <h3 style="color: #0f172a; margin-top: 1.5rem;">The Architecture of Compositionality</h3>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Take a moment to appreciate where we are in our journey. In Section 1 and Section 3, we learned how to prove limits from first principles using the $\epsilon\text{-}N$ definition. While that fundamental machinery gives pure mathematics its rock-solid rigor, using it directly on every single function would be painfully slow.
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Consider an expression like $\lim_{n\to\infty} \frac{5n^3 - 2n + 7}{3n^3 + 4}$. Writing a raw $\epsilon\text{-}N$ scratchpad proof for that rational expression would involve taming messy cubic polynomials and estimating complex cross-terms.
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                This is where mathematical maturity steps in. Analysis doesn't ask us to suffer through tedious algebra for every problem. Instead, we establish <strong>Theorem 1: The Algebraic Limit Laws</strong>. This theorem proves that limits respect all standard arithmetic operations: addition, subtraction, multiplication, scalar scaling, division, and integer powers. Once we prove these laws once and for all, we can calculate complicated limits compositionally—simply by breaking them down into familiar building blocks like $\lim 1/n = 0$ and $\lim c = c$.
            </p>

            <h3 style="color: #0f172a; margin-top: 1.75rem;">Theorem 1: The Algebraic Limit Laws</h3>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Suppose $(a_n)$ and $(b_n)$ are convergent sequences with limits $K, L \in \mathbb{R}$:
            </p>
            <p style="text-align: center; margin: 1.25rem 0; font-size: 1.15rem;">
                $$\lim_{n\to\infty} a_n = K \quad \text{and} \quad \lim_{n\to\infty} b_n = L$$
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Let $c \in \mathbb{R}$ be any fixed constant. Then the following algebraic rules hold:
            </p>
            <ul style="margin: 0.5rem 0 1.5rem 1.25rem; color: #334155; line-height: 1.75; font-size: 0.98rem;">
                <li style="margin-bottom: 0.75rem;">
                    <strong>1. The Constant Rule:</strong> $\lim_{n\to\infty} c = c$<br>
                    A sequence that never changes remains permanently at its starting value.
                </li>
                <li style="margin-bottom: 0.75rem;">
                    <strong>2. The Scalar Multiple Rule:</strong> $\lim_{n\to\infty} (c \cdot a_n) = c \cdot K$<br>
                    Constants pull cleanly out of the limit operator.
                </li>
                <li style="margin-bottom: 0.75rem;">
                    <strong>3. The Sum and Difference Rule:</strong> $\lim_{n\to\infty} (a_n \pm b_n) = K \pm L$<br>
                    The limit of a sum is the sum of the individual limits.
                </li>
                <li style="margin-bottom: 0.75rem;">
                    <strong>4. The Product Rule:</strong> $\lim_{n\to\infty} (a_n \cdot b_n) = K \cdot L$<br>
                    The limit of a product is the product of the individual limits.
                </li>
                <li style="margin-bottom: 0.75rem;">
                    <strong>5. The Quotient Rule:</strong> $\lim_{n\to\infty} \left(\frac{a_n}{b_n}\right) = \frac{K}{L}$<br>
                    Provided that $L \neq 0$ and $b_n \neq 0$ for all $n$.
                </li>
                <li>
                    <strong>6. The Power Rule:</strong> $\lim_{n\to\infty} (a_n)^p = K^p$ for any integer exponent $p \in \mathbb{N}$.
                </li>
            </ul>

            <h3 style="color: #0f172a; margin-top: 1.75rem;">The "$\epsilon/2$ Trick" and the Sum Law Proof</h3>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Let's study the proof of the Sum Law ($\lim (a_n + b_n) = K + L$). This is the very first time an analysis student encounters the famous <strong>$\epsilon/2$ strategy</strong>—an elegant technique that you will use constantly throughout your mathematics degree.
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                <strong>The Mental Model (The Shared Error Budget):</strong><br>
                A challenger hands you an overall target error $\epsilon > 0$. You want to ensure that:
            </p>
            <p style="text-align: center; margin: 1rem 0; font-size: 1.15rem;">
                $$|(a_n + b_n) - (K + L)| < \epsilon$$
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Notice that you are dealing with two separate moving parts: $a_n$ is wobbling around $K$, and $b_n$ is wobbling around $L$. If both sequences are permitted to wobble by almost $\epsilon$, their combined sum could drift by nearly $2\epsilon$, failing the skeptic's test!
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                The solution is simple: <strong>split the error budget in half</strong>. We demand that $a_n$ stay within $\epsilon/2$ of $K$, and $b_n$ stay within $\epsilon/2$ of $L$. When we add them together:
            </p>
            <p style="text-align: center; margin: 1rem 0; font-size: 1.15rem;">
                $$\frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon$$
            </p>

            <h4 style="color: #0f172a; margin-top: 1.5rem;">The Synchronization Problem: Why We Take $N = \max(N_1, N_2)$</h4>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Here is a subtle hurdle that every beginner wonders about:
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Because $a_n \to K$, we can find a cutoff $N_1$ so that $|a_n - K| < \epsilon/2$ for all $n > N_1$. Separately, because $b_n \to L$, we can find a cutoff $N_2$ so that $|b_n - L| < \epsilon/2$ for all $n > N_2$.
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                What if $N_1 = 10$, but $N_2 = 500$? At step $n = 50$, sequence $a_n$ has settled down nicely, but sequence $b_n$ is still wandering around wildly!
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                To solve this, we define a master cutoff:
            </p>
            <p style="text-align: center; margin: 1rem 0; font-size: 1.15rem;">
                $$N = \max(N_1, N_2)$$
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                For any index $n$ strictly past $N$, we are guaranteed that $n > N_1$ <em>and</em> $n > N_2$ simultaneously. Both sequences are synchronized and locked inside their respective $\epsilon/2$ cages!
            </p>

            <h4 style="color: #0f172a; margin-top: 1.5rem;">The Formal Proof of the Sum Law</h4>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Now we assemble the complete deductive argument:
            </p>
            <ol style="margin: 0.5rem 0 1.5rem 1.25rem; color: #334155; line-height: 1.75; font-size: 0.98rem;">
                <li style="margin-bottom: 0.6rem;">
                    Let $\epsilon > 0$ be arbitrary. Then $\frac{\epsilon}{2} > 0$.
                </li>
                <li style="margin-bottom: 0.6rem;">
                    Since $\lim a_n = K$, there exists $N_1 \in \mathbb{N}$ such that $n > N_1 \implies |a_n - K| < \frac{\epsilon}{2}$.
                </li>
                <li style="margin-bottom: 0.6rem;">
                    Since $\lim b_n = L$, there exists $N_2 \in \mathbb{N}$ such that $n > N_2 \implies |b_n - L| < \frac{\epsilon}{2}$.
                </li>
                <li style="margin-bottom: 0.6rem;">
                    Set $N = \max(N_1, N_2)$. For any index $n > N$, both inequalities hold at the same time.
                </li>
                <li>
                    We now measure the total distance between $(a_n + b_n)$ and $(K + L)$. Regrouping terms and applying the Triangle Inequality yields:
                    $$\begin{aligned}
                    |(a_n + b_n) - (K + L)| &= |(a_n - K) + (b_n - L)| \\
                    &\le |a_n - K| + |b_n - L| \\
                    &< \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon. \quad \blacksquare
                    \end{aligned}$$
                </li>
            </ol>

            <h3 style="color: #0f172a; margin-top: 1.75rem;">The "Add-and-Subtract Bridge": Proving the Product Law</h3>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Why is the Product Law ($\lim (a_n \cdot b_n) = K \cdot L$) trickier than the Sum Law?
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                When we look at the difference $|a_n b_n - K L|$, the terms do not naturally group into $(a_n - K)$ and $(b_n - L)$. If you try to expand $(a_n - K)(b_n - L)$, you get $a_n b_n - a_n L - b_n K + K L$, which has unwanted middle terms.
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                To bridge this gap, analysis uses one of its most famous creative maneuvers: <strong>we add zero in the form of $+a_n L - a_n L$</strong>.
            </p>
            <p style="text-align: center; margin: 1.25rem 0; font-size: 1.15rem;">
                $$\begin{aligned}
                a_n b_n - K L &= a_n b_n \mathbf{- a_n L + a_n L} - K L \\
                &= a_n (b_n - L) + L (a_n - K)
                \end{aligned}$$
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Applying the triangle inequality to this bridged expression gives:
            </p>
            <p style="text-align: center; margin: 1.25rem 0; font-size: 1.15rem;">
                $$|a_n b_n - K L| \le |a_n| |b_n - L| + |L| |a_n - K|$$
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Now observe the brilliance of this decomposition:
            </p>
            <ul style="margin: 0.5rem 0 1.5rem 1.25rem; color: #334155; line-height: 1.75; font-size: 0.98rem;">
                <li style="margin-bottom: 0.6rem;">
                    $|b_n - L|$ can be made arbitrarily tiny because $b_n \to L$.
                </li>
                <li style="margin-bottom: 0.6rem;">
                    $|a_n - K|$ can be made arbitrarily tiny because $a_n \to K$.
                </li>
                <li>
                    $|L|$ is just a fixed constant number.
                </li>
            </ul>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                <strong>Where Boundedness Saves the Day:</strong> What about that lone factor of $|a_n|$? It is not a fixed constant—it changes with every step $n$! If $a_n$ could grow without bound, it could multiply $|b_n - L|$ by huge numbers and ruin our proof.
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                But remember <strong>Proposition 5 from Section 4</strong>! We proved that every convergent sequence is bounded: there is a constant $M > 0$ such that $|a_n| \le M$ for all $n$. Therefore:
            </p>
            <p style="text-align: center; margin: 1.25rem 0; font-size: 1.15rem;">
                $$|a_n b_n - K L| \le M |b_n - L| + |L| |a_n - K|$$
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                By demanding that $|b_n - L| < \frac{\epsilon}{2M}$ and $|a_n - K| < \frac{\epsilon}{2(|L| + 1)}$, both pieces stay under $\epsilon/2$, and their sum stays strictly less than $\epsilon$. The Product Law is proven!
            </p>

            <h3 style="color: #0f172a; margin-top: 1.75rem;">Guarding the Denominator: The Quotient Law</h3>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Finally, we consider the Quotient Law: $\lim \left(\frac{a_n}{b_n}\right) = \frac{K}{L}$.
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Because $\frac{a_n}{b_n} = a_n \cdot \frac{1}{b_n}$, we can combine the Product Law with a simpler rule: proving that $\lim \frac{1}{b_n} = \frac{1}{L}$ whenever $L \neq 0$.
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Investigating the distance:
            </p>
            <p style="text-align: center; margin: 1.25rem 0; font-size: 1.15rem;">
                $$\left|\frac{1}{b_n} - \frac{1}{L}\right| = \left|\frac{L - b_n}{b_n L}\right| = \frac{|b_n - L|}{|b_n| |L|}$$
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Notice the danger lurking in the denominator: $|b_n|$. If terms $b_n$ were allowed to flirt with zero, the fraction $\frac{1}{|b_n|}$ would blow up to infinity!
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Here again, Section 4 comes to our rescue. By the <strong>Preservation of Sign property</strong>, because $L \neq 0$, there exists an index $N_0$ past which $|b_n| > \frac{|L|}{2}$. Inverting this inequality flips the direction:
            </p>
            <p style="text-align: center; margin: 1.25rem 0; font-size: 1.15rem;">
                $$\frac{1}{|b_n|} < \frac{2}{|L|}$$
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                The dangerous denominator is now securely capped by a fixed constant! We substitute this bound into our expression:
            </p>
            <p style="text-align: center; margin: 1.25rem 0; font-size: 1.15rem;">
                $$\left|\frac{1}{b_n} - \frac{1}{L}\right| < \frac{2}{|L|^2} |b_n - L|$$
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Because $|b_n - L|$ can be made arbitrarily small, the entire distance collapses below $\epsilon$. The Algebraic Limit Laws form an airtight, beautiful system: each theorem rests securely on the foundational properties we established in the sections before it.
            </p>

            <!-- SECTION 6: UNBOXED, DETAILED, EMPATHETIC EXPLANATION -->
            <h2 id="section-divergence-test">6. Proving Non-Existence of Limits</h2>

            <h3 style="color: #0f172a; margin-top: 1.5rem;">The Flip Side: Defeating the Target Game</h3>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                So far, we have focused entirely on proving that limits exist. But what happens when a sequence simply refuses to settle down? How do you prove that a sequence like $a_n = (-1)^n = (-1, 1, -1, 1, \dots)$ does <em>not</em> converge?
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                For beginning students, this often triggers immediate anxiety: <em>"How could I possibly prove that a limit doesn't exist? There are infinitely many real numbers! Do I have to test every single number on the real line and show none of them work?"</em>
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                The answer is yes in spirit, but no in practice. You don't test numbers one by one. Instead, you employ the power of <strong>formal logical negation</strong> combined with <strong>geometric separation</strong>. Once you understand how to negate an $\epsilon\text{-}N$ statement, proving divergence becomes just as structured and predictable as proving convergence.
            </p>

            <h3 style="color: #0f172a; margin-top: 1.75rem;">The Anatomy of Negation: Flipping the Quantifiers</h3>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Let's recall what it means for a sequence to converge to a specific candidate limit $L$:
            </p>
            <p style="text-align: center; margin: 1rem 0; font-size: 1.15rem;">
                $$\forall \epsilon > 0 \quad \exists N \in \mathbb{N} \quad \forall n > N, \quad |a_n - L| < \epsilon$$
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                In the rules of formal logic, whenever you negate a statement, every universal quantifier ($\forall$) turns into an existential quantifier ($\exists$), every existential quantifier ($\exists$) turns into a universal quantifier ($\forall$), and the final condition is replaced by its logical opposite ($< \epsilon$ becomes $\ge \epsilon$).
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Let's walk through that transformation step by step from left to right:
            </p>
            <ul style="margin: 0.5rem 0 1.5rem 1.25rem; color: #334155; line-height: 1.75; font-size: 0.98rem;">
                <li style="margin-bottom: 0.75rem;">
                    <strong>Original:</strong> <em>"For all tolerances $\epsilon > 0$..."</em><br>
                    <strong>Negation ($\exists \epsilon > 0$):</strong> To show the claim fails, we don't have to win for every tolerance. We only need to find <strong>one stubborn tolerance</strong> $\epsilon_0 > 0$ where the sequence breaks down.
                </li>
                <li style="margin-bottom: 0.75rem;">
                    <strong>Original:</strong> <em>"...there exists a cutoff milestone $N$..."</em><br>
                    <strong>Negation ($\forall N \in \mathbb{N}$):</strong> We must show that <strong>every conceivable cutoff $N$ fails</strong>. No matter how huge of a number someone chooses—whether $N = 100$, $N = 10^6$, or $N = 10^{99}$—it will never be far enough down the line.
                </li>
                <li>
                    <strong>Original:</strong> <em>"...such that for all $n > N$, $|a_n - L| < \epsilon$."</em><br>
                    <strong>Negation ($\exists n > N \text{ with } |a_n - L| \ge \epsilon$):</strong> We prove that somewhere past that proposed cutoff $N$, there is <strong>always an index $n > N$ that escapes</strong> the target corridor, landing at a distance of at least $\epsilon$ away from $L$.
                </li>
            </ul>

            <h3 style="color: #0f172a; margin-top: 1.75rem;">Disproving Every Real Candidate at Once ($\forall L \in \mathbb{R}$)</h3>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Saying that a sequence <em>diverges</em> means it does not converge to <em>any</em> real number. Therefore, we quantify over all candidate limits:
            </p>
            <div style="padding: 1.25rem 1.5rem; margin: 1.5rem 0; background: #f8fafc; border: 1px solid var(--border); border-radius: 8px; text-align: center;">
                <span style="font-size: 1.1rem; color: #0f172a; font-weight: 600; display: block; margin-bottom: 0.5rem;">
                    Formal Definition: Non-Convergence (Divergence)
                </span>
                <span style="font-size: 1.05rem; color: #0f172a;">
                    A sequence $(a_n)$ does not converge to any limit in $\mathbb{R}$ if and only if:
                </span>
                <p style="margin: 1rem 0 0.5rem 0; font-size: 1.2rem;">
                    $$\forall L \in \mathbb{R}, \quad \exists \epsilon > 0 \quad \text{such that} \quad \forall N \in \mathbb{N}, \quad \exists n > N \quad \text{with} \quad |a_n - L| \ge \epsilon$$
                </p>
            </div>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                In the game analogy, the roles have swapped:
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                A believer claims, <em>"I bet the sequence converges to $L$!"</em> Your job as the skeptic is to produce a tolerance $\epsilon > 0$ such that no matter what cutoff $N$ the believer proposes, the sequence perpetually breaks out of their target window.
            </p>

            <h3 style="color: #0f172a; margin-top: 1.75rem;">A Detailed Walkthrough: Proving That $a_n = (-1)^n$ Has No Limit</h3>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Consider the classic alternating sequence $a_n = (-1)^n$:
            </p>
            <p style="text-align: center; margin: 1rem 0; font-size: 1.15rem;">
                $$(a_n) = (-1, 1, -1, 1, -1, 1, \dots)$$
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Intuitively, this sequence cannot converge because it bounces indefinitely between $-1$ and $+1$. But how do we turn that intuition into an airtight mathematical proof?
            </p>

            <h4 style="color: #0f172a; margin-top: 1.5rem;">The Geometric Insight (The Impossible Choice of $L$)</h4>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Notice that the distance between the two values the sequence visits is:
            </p>
            <p style="text-align: center; margin: 1rem 0; font-size: 1.15rem;">
                $$|1 - (-1)| = 2$$
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Now think about what happens if someone proposes a candidate limit $L$. By the Triangle Inequality, the total distance between $1$ and $-1$ cannot exceed the distance from $1$ to $L$ plus the distance from $L$ to $-1$:
            </p>
            <p style="text-align: center; margin: 1.25rem 0; font-size: 1.15rem;">
                $$2 = |1 - (-1)| = |(1 - L) + (L - (-1))| \le |1 - L| + |-1 - L|$$
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Look at what that inequality says: <strong>the sum of the two distances must be at least 2</strong>! It is physically impossible for a single point $L$ to be within distance $\epsilon = 1$ of both numbers simultaneously. If $L$ is close to $+1$, it is far from $-1$. If $L$ is close to $-1$, it is far from $+1$. And if $L = 0$, it is distance 1 from both!
            </p>

            <h4 style="color: #0f172a; margin-top: 1.5rem;">The Formal Case Analysis</h4>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Let $L \in \mathbb{R}$ be an arbitrary candidate limit. We set our lethal tolerance to $\epsilon = 1$. Let $N \in \mathbb{N}$ be any cutoff index proposed by our opponent.
            </p>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                We now examine the two possibilities for where $L$ might sit on the number line:
            </p>
            <ul style="margin: 0.5rem 0 1.5rem 1.25rem; color: #334155; line-height: 1.75; font-size: 0.98rem;">
                <li style="margin-bottom: 0.85rem;">
                    <strong>Case 1 ($L \le 0$):</strong><br>
                    Suppose the candidate limit is zero or negative. We simply pick any <strong>even</strong> integer $n > N$ (for instance, $n = 2N + 2$). For this even index, $a_n = 1$. The distance is:
                    $$|a_n - L| = |1 - L| = 1 - L \ge 1 = \epsilon$$
                    Because $L \le 0$, the distance between $a_n$ and $L$ is at least 1. The even terms escape the tolerance band!
                </li>
                <li>
                    <strong>Case 2 ($L > 0$):</strong><br>
                    Suppose the candidate limit is strictly positive. We simply pick any <strong>odd</strong> integer $n > N$ (for instance, $n = 2N + 1$). For this odd index, $a_n = -1$. The distance is:
                    $$|a_n - L| = |-1 - L| = |-(1 + L)| = 1 + L > 1 = \epsilon$$
                    Because $L > 0$, the distance between $a_n$ and $L$ is strictly greater than 1. The odd terms escape the tolerance band!
                </li>
            </ul>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                <strong>The Conclusion:</strong> In both cases, past any proposed cutoff $N$, there are always subsequent indices where the sequence lies at a distance of at least $\epsilon = 1$ from $L$. Because $L$ was arbitrary, no real number can serve as a limit. Therefore, $a_n = (-1)^n$ diverges. $\blacksquare$
            </p>

            <h3 style="color: #0f172a; margin-top: 1.75rem;">Summary Checklist: How to Disprove a Limit</h3>
            <p style="color: #334155; line-height: 1.75; font-size: 1rem;">
                Whenever a homework or exam problem asks you to show that a sequence does not converge, remember this 4-step blueprint:
            </p>
            <ol style="margin: 0.5rem 0 1.75rem 1.25rem; color: #334155; line-height: 1.75; font-size: 0.98rem;">
                <li style="margin-bottom: 0.6rem;">
                    <strong>State that $L \in \mathbb{R}$ is arbitrary:</strong> Never fix a specific candidate like $L = 0$ unless the problem specifically asks you to disprove that particular number.
                </li>
                <li style="margin-bottom: 0.6rem;">
                    <strong>Identify the oscillation gap:</strong> Look at the values the sequence alternates between (e.g., $A$ and $B$). Choose $\epsilon$ to be half the distance between them: $\epsilon = \frac{|A - B|}{2}$.
                </li>
                <li style="margin-bottom: 0.6rem;">
                    <strong>Let $N \in \mathbb{N}$ be arbitrary:</strong> You must defeat every proposed cutoff milestone.
                </li>
                <li>
                    <strong>Find the breakout index:</strong> Select an index $n > N$ (often depending on whether $n$ is even or odd) that forces $|a_n - L| \ge \epsilon$, demonstrating asymptotic instability.
                </li>
            </ol>

            <!-- DIAGRAM: Divergence Oscillation -->
            <div style="background: #ffffff; border: 1px solid var(--border); border-radius: 8px; margin: 1.5rem 0; padding: 1.5rem;">
                <h5 style="margin-top: 0; margin-bottom: 1rem; color: #334155; font-size: 0.95rem;">Visualization: Divergence of Alternating Sequence $(-1)^n$</h5>
                <svg viewBox="0 0 740 220" style="width: 100%; height: auto;">
                    <line x1="40" y1="110" x2="700" y2="110" stroke="#cbd5e1" stroke-width="1.5" />
                    <text x="705" y="114" font-family="sans-serif" font-size="12" fill="#94a3b8">0</text>

                    <line x1="40" y1="40" x2="700" y2="40" stroke="#cbd5e1" stroke-dasharray="2" />
                    <text x="705" y="44" font-family="sans-serif" font-size="12" fill="#64748b">+1</text>

                    <line x1="40" y1="180" x2="700" y2="180" stroke="#cbd5e1" stroke-dasharray="2" />
                    <text x="705" y="184" font-family="sans-serif" font-size="12" fill="#64748b">-1</text>

                    <!-- Candidate L = 0.3 (y=89) -->
                    <line x1="40" y1="89" x2="700" y2="89" stroke="#b45309" stroke-width="1.5" />
                    <text x="705" y="87" font-family="sans-serif" font-size="12" fill="#b45309" font-weight="bold">Candidate L</text>

                    <!-- Epsilon = 1 band (height 140px, +/- 70px) -->
                    <rect x="40" y="19" width="660" height="140" fill="#fef3c7" opacity="0.4" stroke="#f59e0b" stroke-dasharray="4" />

                    <!-- Points -->
                    <circle cx="100" cy="180" r="5" fill="#ef4444" stroke="#b91c1c" stroke-width="1.5" />
                    <circle cx="180" cy="40" r="5" fill="#10b981" />
                    <circle cx="260" cy="180" r="5" fill="#ef4444" stroke="#b91c1c" stroke-width="1.5" />
                    <circle cx="340" cy="40" r="5" fill="#10b981" />
                    <circle cx="420" cy="180" r="5" fill="#ef4444" stroke="#b91c1c" stroke-width="1.5" />
                    <circle cx="500" cy="40" r="5" fill="#10b981" />

                    <!-- Annotations -->
                    <text x="260" y="200" font-family="sans-serif" font-size="11" fill="#ef4444" font-weight="bold" text-anchor="middle">Fails: Escapes ϵ-window!</text>
                    <text x="180" y="25" font-family="sans-serif" font-size="11" fill="#10b981" font-weight="bold" text-anchor="middle">Captured</text>
                </svg>
            </div>
"""


def restore_lecture_content(content: str) -> str:
    """Atomically restore Sections 2, 4, 5, and 6 in week2-lecture4.html."""

    # 1. Restore Section 2 (Quantifier Order, Timing, and Dependencies)
    sec2_pattern = re.compile(
        r'(?:<!-- SECTION 2: UNBOXED, DETAILED, EMPATHETIC EXPLANATION -->|<h2 id="section-quantifiers">).*?'
        r'(?=<!-- SECTION 3)',
        re.DOTALL
    )
    if sec2_pattern.search(content):
        content = sec2_pattern.sub(lambda _: RESTORED_SECTION_2 + "\n\n            ", content)

    # 2. Restore Sections 4, 5, and 6
    sec4_to_end_pattern = re.compile(
        r'(?:<!-- SECTION 4: UNBOXED, DETAILED, EMPATHETIC EXPLANATION -->|<h2 id="section-prop5">).*?'
        r'(?=<!-- FOOTER NAVIGATION -->)',
        re.DOTALL
    )
    if sec4_to_end_pattern.search(content):
        content = sec4_to_end_pattern.sub(lambda _: COMPLETE_SECTIONS_4_5_6 + "\n            ", content)

    return content


def update_lecture_document(file_path: Path) -> None:
    """Read target HTML, apply full restoration, and write back to disk."""
    if not file_path.exists():
        print(f"Error: Target file '{file_path}' does not exist.", file=sys.stderr)
        sys.exit(1)

    raw_text = file_path.read_text(encoding="utf-8")
    updated_text = restore_lecture_content(raw_text)

    if raw_text == updated_text:
        print("Notice: No changes needed; document is already fully up to date.")
        return

    lines_before = len(raw_text.splitlines())
    lines_after = len(updated_text.splitlines())
    file_path.write_text(updated_text, encoding="utf-8")
    print(
        f"Successfully restored '{file_path.name}'.\n"
        f"Lines before: {lines_before} -> Lines after: {lines_after} "
        f"(+{lines_after - lines_before} lines restored)."
    )


def check_staged_changes() -> bool:
    """Return True if changes exist in the git staging index."""
    result = subprocess.run(["git", "diff", "--cached", "--quiet"])
    return result.returncode != 0


def sync_git_repository(target_path: Path, script_path: Path) -> None:
    """Stage modified lecture file and script, commit, and push."""
    commit_message = f"{COMMIT_SUBJECT}\n\n{COMMIT_BODY}"

    print(f"Staging {target_path.name} and {script_path.name}...")
    subprocess.run(["git", "add", str(target_path), str(script_path)], check=True)

    if not check_staged_changes():
        print("No staged changes to commit. Working tree is clean.")
        return

    print("Creating git commit...")
    subprocess.run(["git", "commit", "-m", commit_message], check=True)

    print("Pushing to remote repository...")
    subprocess.run(["git", "push"], check=True)
    print("Done! Repository successfully synchronized.")


if __name__ == "__main__":
    try:
        update_lecture_document(TARGET_FILE)
        sync_git_repository(TARGET_FILE, SCRIPT_FILE)
    except subprocess.CalledProcessError as git_err:
        print(f"Git execution error: {git_err}", file=sys.stderr)
        sys.exit(1)
    except OSError as err:
        print(f"File system error: {err}", file=sys.stderr)
        sys.exit(1)
