#!/usr/bin/env python3
"""
Surgically restore all truncated analytical sections in week2-lecture4.html.
Uses callable replacements in re.sub to prevent regex template escape errors
with LaTeX backslashes.
"""

from pathlib import Path
import re
import subprocess
import sys

TARGET_FILE = Path("week2-lecture4.html")
SCRIPT_FILE = Path(__file__).resolve()

COMMIT_SUBJECT = (
    "Fix regex replacement escape error and restore Lecture 4 prose"
)
COMMIT_BODY = (
    "Use callable lambda replacements in re.sub to prevent regex template\n"
    "escape parsing errors with LaTeX backslashes. Switch multiline prose\n"
    "blocks to raw strings to eliminate Python 3.14 invalid escape syntax\n"
    "warnings, and fully restore the unboxed sections in Lecture 4."
)

RESTORED_PROP5_BLOCK = r"""
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
            </p>"""

RESTORED_SIGN_BLOCK = r"""
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
            </p>"""

RESTORED_SECTION_5 = r"""            <!-- SECTION 5: UNBOXED, DETAILED, EMPATHETIC EXPLANATION -->
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
            </p>"""

RESTORED_SECTION_6_PREAMBLE = r"""            <!-- SECTION 6: UNBOXED, DETAILED, EMPATHETIC EXPLANATION -->
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
            </ol>"""


def restore_sections_in_lecture4(content: str) -> str:
    """Restores full explanatory prose and proofs across Sections 4, 5, and 6."""

    # 1. Restore Proposition 5 detailed proofs before the Boundedness SVG diagram
    if "Reverse Triangle Inequality" not in content:
        prop5_pattern = re.compile(
            r'(<h3[^>]*>Proposition 5:[^<]*</h3>\s*<ul[^>]*>.*?</ul>)',
            re.DOTALL
        )
        content = prop5_pattern.sub(lambda _: RESTORED_PROP5_BLOCK, content, count=1)

    # 2. Restore Sign Preservation buffer zone proof after the Boundedness SVG diagram
    if "Preservation of Sign (The Buffer Zone)" not in content:
        match = re.search(r'(<!-- DIAGRAM: Boundedness -->.*?</svg>\s*</div>)', content, re.DOTALL)
        if match:
            content = content[:match.end()] + "\n" + RESTORED_SIGN_BLOCK + content[match.end():]

    # 3. Restore Section 5 (Algebraic Limit Laws)
    sec5_pattern = re.compile(
        r'<!-- SECTION 5(?:.*?)-->\s*<h2 id="section-theorems">.*?</h2>.*?'
        r'(?=<!-- SECTION 6)',
        re.DOTALL
    )
    if sec5_pattern.search(content):
        content = sec5_pattern.sub(lambda _: RESTORED_SECTION_5 + "\n\n", content)

    # 4. Restore Section 6 (Proving Non-Existence / Negation)
    sec6_pattern = re.compile(
        r'<!-- SECTION 6(?:.*?)-->\s*<h2 id="section-divergence-test">.*?</h2>.*?'
        r'(?=<!-- DIAGRAM: Divergence Oscillation -->)',
        re.DOTALL
    )
    if sec6_pattern.search(content):
        content = sec6_pattern.sub(lambda _: RESTORED_SECTION_6_PREAMBLE + "\n\n            ", content)

    return content


def update_lecture_document(file_path: Path) -> None:
    """Reads target HTML, applies full restoration, and writes back to disk."""
    if not file_path.exists():
        print(f"Error: Target file '{file_path}' does not exist.", file=sys.stderr)
        sys.exit(1)

    raw_text = file_path.read_text(encoding="utf-8")
    updated_text = restore_sections_in_lecture4(raw_text)

    if raw_text == updated_text:
        print("Notice: No changes applied. File may already contain restored sections.")
        return

    lines_before = len(raw_text.splitlines())
    lines_after = len(updated_text.splitlines())
    file_path.write_text(updated_text, encoding="utf-8")
    print(f"Successfully restored '{file_path.name}'.")
    print(f"Lines before: {lines_before} -> Lines after: {lines_after} (+{lines_after - lines_before} lines).")


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
