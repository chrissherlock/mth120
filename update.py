#!/usr/bin/env python3
import os
import subprocess

def update_section3_introductions():
    filepath = 'week1-lecture1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_section_3 = r'''<!-- SECTION 3 -->
            <h2 id="functions-mappings">3. Functions and Mappings</h2>
            <div class="infobox">
                <h4>📖 Notation Reference: Functions &amp; Composition</h4>
                <div class="infobox-intro">
                    <strong>Functions as structured mappings:</strong> In analysis, a function is not just an algebraic calculation; it is a contract between two sets ensuring every input has a uniquely determined output.
                </div>
                <div class="notation-grid">
                    <div class="notation-item"><span class="notation-sym">$f: X \to Y$</span><span class="notation-desc">Function $f$ with domain $X$ and codomain $Y$</span></div>
                    <div class="notation-item"><span class="notation-sym" style="gap: 0.35rem;">$f(X)$ <span style="margin: 0 0.35rem; font-weight: 500; font-size: 0.9rem; color: #64748b;">or</span> $\text{ran}(f)$</span><span class="notation-desc">Range: actual set of achieved output values $\{f(x) \mid x \in X\}$</span></div>
                    <div class="notation-item"><span class="notation-sym">$f^{-1}(y)$</span><span class="notation-desc">Preimage: the set of inputs that map to $y$</span></div>
                    <div class="notation-item"><span class="notation-sym">$g \circ f$</span><span class="notation-desc">Composition: $(g \circ f)(x) = g(f(x))$</span></div>
                    <div class="notation-item"><span class="notation-sym">$f^{-1}$</span><span class="notation-desc">Inverse function (exists if and only if $f$ is bijective)</span></div>
                </div>
            </div>

            <p style="font-size: 1.02rem; line-height: 1.7; color: #334155;">
                In high school and introductory calculus, functions are usually introduced as algebraic recipes: you write $f(x) = x^2$, plug in a number, and compute an answer. In real analysis, we broaden our perspective. A <strong>function</strong> (or <em>mapping</em>) is a structural link between two sets that assigns to every member of the first set exactly one member of the second.
            </p>
            <p style="font-size: 1.02rem; line-height: 1.7; color: #334155;">
                This shift matters because throughout this course, sequences, limits, derivatives, and integrals will all be defined as functions. Gaining confidence with how domain, codomain, and invertibility interact will keep you grounded when the inputs become infinite lists or functions themselves.
            </p>

            <!-- SUBSECTION 3.1: DOMAIN, CODOMAIN, RANGE -->
            <div style="background: #ffffff; border: 1px solid var(--border); border-radius: 8px; padding: 1.5rem; margin-top: 1.75rem; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
                <div style="display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; gap: 0.5rem; border-bottom: 1px solid #f1f5f9; padding-bottom: 0.75rem; margin-bottom: 1rem;">
                    <h3 style="margin: 0; color: #0f172a; font-size: 1.15rem;">3.1 The Anatomy of a Mapping: Domain, Codomain, and Range</h3>
                    <span style="font-weight: 700; color: var(--accent); font-size: 0.92rem;">Key Distinction: Codomain vs. Range</span>
                </div>

                <p style="font-size: 1rem; line-height: 1.7; color: #334155; margin-top: 0; margin-bottom: 1rem;">
                    It is completely normal if the distinction between where a function <em>could</em> go (its codomain) and where it <em>actually</em> lands (its range) feels unfamiliar at first. In computational calculus, domain and range are often treated as afterthought restrictions discovered by dodging division by zero or negative square roots. In pure analysis, we invert that mindset: a mapping is defined by its source and target sets right from the start. Taking a moment to distinguish between the available target space and the elements actually hit will save you considerable confusion later.
                </p>

                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; align-items: center;">
                    <div>
                        <p style="margin-top: 0; color: #334155; line-height: 1.65;">
                            When declaring a function $f: X \to Y$, three distinct sets are involved:
                        </p>
                        <ul style="margin: 0.25rem 0 0.75rem 1.25rem; padding: 0; color: #334155; font-size: 0.95rem; line-height: 1.6;">
                            <li><strong>Domain ($X$):</strong> The source set of all valid inputs. Every single $x \in X$ must have an assigned output.</li>
                            <li><strong>Codomain ($Y$):</strong> The target universe where outputs are allowed to land.</li>
                            <li><strong>Range ($f(X)$):</strong> The subset of $Y$ consisting of values actually hit by the mapping: $f(X) = \{f(x) \mid x \in X\} \subseteq Y$.</li>
                        </ul>
                        <div class="definition-box" style="margin: 0.75rem 0;">
                            <strong>A Classic Example:</strong> Consider $f: \mathbb{R} \to \mathbb{R}$ defined by $f(x) = x^2$.<br>
                            The codomain is all of $\mathbb{R}$, but negative numbers are never produced. The actual range is $[0, \infty)$.
                        </div>
                    </div>
                    <div style="background: #f8fafc; border: 1px solid var(--border); border-radius: 6px; padding: 1rem; text-align: center;">
                        <svg viewBox="0 0 340 190" style="width: 100%; max-width: 320px; height: auto; display: inline-block;">
                            <!-- Domain Oval -->
                            <ellipse cx="75" cy="95" rx="55" ry="75" fill="#f8fafc" stroke="#64748b" stroke-width="2"/>
                            <text x="75" y="40" font-family="sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Domain X</text>
                            <circle cx="60" cy="75" r="4" fill="#0284c7"/><text x="48" y="79" font-family="sans-serif" font-size="11" fill="#0369a1">x₁</text>
                            <circle cx="65" cy="110" r="4" fill="#0284c7"/><text x="53" y="114" font-family="sans-serif" font-size="11" fill="#0369a1">x₂</text>
                            <circle cx="95" cy="135" r="4" fill="#0284c7"/><text x="83" y="139" font-family="sans-serif" font-size="11" fill="#0369a1">x₃</text>

                            <!-- Codomain Oval -->
                            <ellipse cx="250" cy="95" rx="75" ry="85" fill="#ffffff" stroke="#94a3b8" stroke-width="2"/>
                            <text x="250" y="32" font-family="sans-serif" font-size="13" font-weight="bold" fill="#64748b" text-anchor="middle">Codomain Y</text>

                            <!-- Range Sub-Oval -->
                            <ellipse cx="235" cy="100" rx="45" ry="55" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
                            <text x="235" y="68" font-family="sans-serif" font-size="11" font-weight="bold" fill="#92400e" text-anchor="middle">Range f(X)</text>

                            <!-- Target points inside Range -->
                            <circle cx="225" cy="90" r="4" fill="#d97706"/><text x="235" y="93" font-family="sans-serif" font-size="10" fill="#92400e">f(x₁)</text>
                            <circle cx="230" cy="125" r="4" fill="#d97706"/><text x="240" y="128" font-family="sans-serif" font-size="10" fill="#92400e">f(x₂)=f(x₃)</text>

                            <!-- Unhit points in Codomain -->
                            <circle cx="285" cy="85" r="3.5" fill="#94a3b8"/>
                            <circle cx="280" cy="140" r="3.5" fill="#94a3b8"/>
                            <text x="295" y="143" font-family="sans-serif" font-size="9" fill="#64748b">unhit</text>

                            <!-- Mapping Arrows -->
                            <path d="M 64,75 C 130,55 170,75 220,88" fill="none" stroke="#0284c7" stroke-width="1.6"/>
                            <path d="M 69,110 C 130,110 160,118 225,123" fill="none" stroke="#0284c7" stroke-width="1.6"/>
                            <path d="M 99,135 C 150,140 180,135 225,126" fill="none" stroke="#0284c7" stroke-width="1.6"/>
                        </svg>
                    </div>
                </div>
            </div>

            <!-- SUBSECTION 3.2: INJECTIVE, SURJECTIVE, BIJECTIVE -->
            <div style="background: #ffffff; border: 1px solid var(--border); border-radius: 8px; padding: 1.5rem; margin-top: 1.5rem; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
                <div style="display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; gap: 0.5rem; border-bottom: 1px solid #f1f5f9; padding-bottom: 0.75rem; margin-bottom: 1rem;">
                    <h3 style="margin: 0; color: #0f172a; font-size: 1.15rem;">3.2 Structural Properties: Injective, Surjective, and Bijective</h3>
                    <span style="font-weight: 700; color: #0284c7; font-size: 0.92rem;">Classifying Mappings</span>
                </div>

                <p style="font-size: 1rem; line-height: 1.7; color: #334155; margin-top: 0; margin-bottom: 1rem;">
                    Terms like <em>injective</em>, <em>surjective</em>, and <em>bijective</em> can initially sound like heavy academic jargon, but they simply represent three practical diagnostic checks on how arrows travel between sets: <em>Do distinct inputs ever collide at the same output? Does the mapping reach every corner of the codomain?</em> and <em>Can the relationship be paired off one-to-one?</em> Approaching these definitions as structural quality checks makes verifying them straightforward and methodical.
                </p>

                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.25rem; margin: 1rem 0;">
                    <!-- INJECTIVE -->
                    <div style="background: #f8fafc; border: 1px solid var(--border); border-left: 4px solid #0284c7; border-radius: 6px; padding: 1rem;">
                        <h4 style="margin: 0 0 0.5rem 0; color: #0369a1; font-size: 1rem;">Injective (1-to-1): "No Collisions"</h4>
                        <p style="margin: 0 0 0.5rem 0; font-size: 0.92rem; color: #334155; line-height: 1.55;">
                            Distinct inputs always yield distinct outputs:
                        </p>
                        <div style="font-size: 0.9rem; text-align: center; margin-bottom: 0.5rem;">
                            $$x_1 \neq x_2 \implies f(x_1) \neq f(x_2)$$
                        </div>
                        <p style="margin: 0; font-size: 0.88rem; color: #475569;">
                            <em>Contrapositive proof form:</em> $f(a) = f(b) \implies a = b$. No two arrows ever merge into the same destination point.
                        </p>
                    </div>

                    <!-- SURJECTIVE -->
                    <div style="background: #f8fafc; border: 1px solid var(--border); border-left: 4px solid #d97706; border-radius: 6px; padding: 1rem;">
                        <h4 style="margin: 0 0 0.5rem 0; color: #92400e; font-size: 1rem;">Surjective (Onto): "No Stranded Targets"</h4>
                        <p style="margin: 0 0 0.5rem 0; font-size: 0.92rem; color: #334155; line-height: 1.55;">
                            Every element in the codomain is hit by at least one arrow:
                        </p>
                        <div style="font-size: 0.9rem; text-align: center; margin-bottom: 0.5rem;">
                            $$\forall y \in Y, \; \exists x \in X \text{ such that } f(x) = y$$
                        </div>
                        <p style="margin: 0; font-size: 0.88rem; color: #475569;">
                            In other words, the range completely covers the codomain: $f(X) = Y$. No target is left unhit.
                        </p>
                    </div>

                    <!-- BIJECTIVE -->
                    <div style="background: #f8fafc; border: 1px solid var(--border); border-left: 4px solid #10b981; border-radius: 6px; padding: 1rem;">
                        <h4 style="margin: 0 0 0.5rem 0; color: #047857; font-size: 1rem;">Bijective: "The Perfect Pairing"</h4>
                        <p style="margin: 0 0 0.5rem 0; font-size: 0.92rem; color: #334155; line-height: 1.55;">
                            A mapping that is <strong>both injective and surjective</strong>:
                        </p>
                        <div style="font-size: 0.9rem; text-align: center; margin-bottom: 0.5rem;">
                            $$\text{Injective} + \text{Surjective} \iff \text{Bijective}$$
                        </div>
                        <p style="margin: 0; font-size: 0.88rem; color: #475569;">
                            Establishes a 1-to-1 correspondence. Every element in $X$ matches with exactly one unique element in $Y$, with none left over.
                        </p>
                    </div>
                </div>

                <!-- COMPARISON SVG DIAGRAM -->
                <div style="background: #f8fafc; border: 1px solid var(--border); border-radius: 6px; padding: 1.25rem; margin-top: 1rem; text-align: center;">
                    <p style="font-size: 0.85rem; font-weight: 700; color: #64748b; margin-top: 0; margin-bottom: 0.75rem;">VISUAL COMPARISON: Mapping Structures</p>
                    <svg viewBox="0 0 760 210" style="width: 100%; height: auto; display: block;">
                        <!-- PANEL 1: INJECTIVE ONLY -->
                        <g transform="translate(10, 0)">
                            <text x="110" y="22" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0369a1" text-anchor="middle">Injective (Not Surjective)</text>
                            <ellipse cx="50" cy="115" rx="35" ry="65" fill="#ffffff" stroke="#94a3b8" stroke-width="1.5"/>
                            <ellipse cx="170" cy="115" rx="35" ry="65" fill="#ffffff" stroke="#94a3b8" stroke-width="1.5"/>
                            <circle cx="50" cy="80" r="4" fill="#0284c7"/><circle cx="50" cy="115" r="4" fill="#0284c7"/><circle cx="50" cy="150" r="4" fill="#0284c7"/>
                            <circle cx="170" cy="70" r="4" fill="#0284c7"/><circle cx="170" cy="105" r="4" fill="#0284c7"/><circle cx="170" cy="135" r="4" fill="#0284c7"/><circle cx="170" cy="165" r="4" fill="#94a3b8"/>
                            <line x1="54" y1="80" x2="164" y2="70" stroke="#0284c7" stroke-width="1.5"/>
                            <line x1="54" y1="115" x2="164" y2="105" stroke="#0284c7" stroke-width="1.5"/>
                            <line x1="54" y1="150" x2="164" y2="135" stroke="#0284c7" stroke-width="1.5"/>
                            <text x="110" y="195" font-family="sans-serif" font-size="10.5" fill="#64748b" text-anchor="middle">No collisions, but one unhit target</text>
                        </g>

                        <!-- PANEL 2: SURJECTIVE ONLY -->
                        <g transform="translate(265, 0)">
                            <text x="110" y="22" font-family="sans-serif" font-size="12" font-weight="bold" fill="#b45309" text-anchor="middle">Surjective (Not Injective)</text>
                            <ellipse cx="50" cy="115" rx="35" ry="65" fill="#ffffff" stroke="#94a3b8" stroke-width="1.5"/>
                            <ellipse cx="170" cy="115" rx="35" ry="65" fill="#ffffff" stroke="#94a3b8" stroke-width="1.5"/>
                            <circle cx="50" cy="75" r="4" fill="#d97706"/><circle cx="50" cy="105" r="4" fill="#d97706"/><circle cx="50" cy="135" r="4" fill="#d97706"/><circle cx="50" cy="160" r="4" fill="#d97706"/>
                            <circle cx="170" cy="85" r="4" fill="#d97706"/><circle cx="170" cy="120" r="4" fill="#d97706"/><circle cx="170" cy="155" r="4" fill="#d97706"/>
                            <line x1="54" y1="75" x2="164" y2="85" stroke="#d97706" stroke-width="1.5"/>
                            <line x1="54" y1="105" x2="164" y2="85" stroke="#d97706" stroke-width="1.5"/>
                            <line x1="54" y1="135" x2="164" y2="120" stroke="#d97706" stroke-width="1.5"/>
                            <line x1="54" y1="160" x2="164" y2="155" stroke="#d97706" stroke-width="1.5"/>
                            <text x="110" y="195" font-family="sans-serif" font-size="10.5" fill="#64748b" text-anchor="middle">All targets hit, but a collision occurs</text>
                        </g>

                        <!-- PANEL 3: BIJECTIVE -->
                        <g transform="translate(520, 0)">
                            <text x="110" y="22" font-family="sans-serif" font-size="12" font-weight="bold" fill="#047857" text-anchor="middle">Bijective (Invertible)</text>
                            <ellipse cx="50" cy="115" rx="35" ry="65" fill="#ffffff" stroke="#94a3b8" stroke-width="1.5"/>
                            <ellipse cx="170" cy="115" rx="35" ry="65" fill="#ffffff" stroke="#94a3b8" stroke-width="1.5"/>
                            <circle cx="50" cy="80" r="4" fill="#10b981"/><circle cx="50" cy="115" r="4" fill="#10b981"/><circle cx="50" cy="150" r="4" fill="#10b981"/>
                            <circle cx="170" cy="80" r="4" fill="#10b981"/><circle cx="170" cy="115" r="4" fill="#10b981"/><circle cx="170" cy="150" r="4" fill="#10b981"/>
                            <line x1="54" y1="80" x2="164" y2="80" stroke="#10b981" stroke-width="1.5"/>
                            <line x1="54" y1="115" x2="164" y2="115" stroke="#10b981" stroke-width="1.5"/>
                            <line x1="54" y1="150" x2="164" y2="150" stroke="#10b981" stroke-width="1.5"/>
                            <text x="110" y="195" font-family="sans-serif" font-size="10.5" fill="#64748b" text-anchor="middle">1-to-1 matching: cleanly reversible</text>
                        </g>
                    </svg>
                </div>
            </div>

            <!-- SUBSECTION 3.3: COMPOSITION AND INVERTIBILITY -->
            <div style="background: #ffffff; border: 1px solid var(--border); border-radius: 8px; padding: 1.5rem; margin-top: 1.5rem; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
                <div style="display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; gap: 0.5rem; border-bottom: 1px solid #f1f5f9; padding-bottom: 0.75rem; margin-bottom: 1rem;">
                    <h3 style="margin: 0; color: #0f172a; font-size: 1.15rem;">3.3 Composition and Invertibility</h3>
                    <span style="font-weight: 700; color: var(--accent); font-size: 0.92rem;">Pipelines &amp; Reverse Paths</span>
                </div>

                <p style="font-size: 1rem; line-height: 1.7; color: #334155; margin-top: 0; margin-bottom: 1rem;">
                    Chaining functions together and reversing their actions is where set theory turns into practical analytical machinery. If tracking intermediate domains or reading composite notation from right to left feels slightly unnatural at first, take heart—it trips up almost every beginner. Visualising composition as a sequential pipeline and inversion as an unbroken round trip makes it easy to see exactly why bijectivity is required to undo a function without ambiguity.
                </p>

                <h4 style="margin: 0 0 0.5rem 0; color: #0f172a; font-size: 1.02rem;">1. Composition ($g \circ f$): Chaining Actions in Series</h4>
                <p style="margin: 0 0 0.75rem 0; color: #334155; line-height: 1.65;">
                    Composition connects two functions like links in a pipeline: the output of the first function feeds directly as the input into the second. If $f: X \to Y$ and $g: Y \to Z$, their composite $g \circ f: X \to Z$ creates a single direct leap from $X$ to $Z$:
                </p>
                <div class="definition-box" style="margin: 0.75rem 0;">
                    $$(g \circ f)(x) = g(f(x))$$
                </div>
                <p style="color: #334155; line-height: 1.65; margin-bottom: 1.25rem;">
                    <strong>Read from right to left:</strong> Although $g$ is written on the left, $f$ acts on $x$ first. Think of $(g \circ f)(x)$ as saying: <em>"evaluate $f(x)$ first, then pass that output into $g$."</em>
                </p>

                <!-- FUNCTION COMPOSITION PIPELINE DIAGRAM -->
                <div style="background: #f8fafc; border: 1px solid var(--border); border-radius: 6px; padding: 1.25rem; margin: 1.25rem 0 1.75rem 0; text-align: center;">
                    <p style="font-size: 0.85rem; font-weight: 700; color: #64748b; margin-top: 0; margin-bottom: 0.75rem;">VISUALIZATION: The Composition Pipeline ($X \xrightarrow{f} Y \xrightarrow{g} Z$)</p>
                    <svg viewBox="0 0 720 220" style="width: 100%; max-width: 680px; height: auto; display: inline-block;">
                        <defs>
                            <marker id="arrow-blue" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                                <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#0284c7"/>
                            </marker>
                            <marker id="arrow-amber" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                                <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#d97706"/>
                            </marker>
                            <marker id="arrow-green" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
                                <path d="M 0 1 L 9 5 L 0 9 z" fill="#10b981"/>
                            </marker>
                        </defs>

                        <!-- SET X (Domain of f) -->
                        <ellipse cx="100" cy="130" rx="55" ry="60" fill="#ffffff" stroke="#94a3b8" stroke-width="2"/>
                        <text x="100" y="90" font-family="sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Set X</text>
                        <circle cx="100" cy="140" r="4.5" fill="#0284c7"/>
                        <text x="90" y="144" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0369a1" text-anchor="end">x</text>

                        <!-- SET Y (Codomain of f / Domain of g) -->
                        <ellipse cx="360" cy="130" rx="55" ry="60" fill="#ffffff" stroke="#94a3b8" stroke-width="2"/>
                        <text x="360" y="90" font-family="sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Set Y</text>
                        <circle cx="360" cy="140" r="4.5" fill="#d97706"/>
                        <text x="360" y="160" font-family="sans-serif" font-size="11.5" font-weight="bold" fill="#92400e" text-anchor="middle">f(x)</text>

                        <!-- SET Z (Codomain of g) -->
                        <ellipse cx="620" cy="130" rx="55" ry="60" fill="#ffffff" stroke="#94a3b8" stroke-width="2"/>
                        <text x="620" y="90" font-family="sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Set Z</text>
                        <circle cx="620" cy="140" r="4.5" fill="#10b981"/>
                        <text x="632" y="144" font-family="sans-serif" font-size="12" font-weight="bold" fill="#047857" text-anchor="start">g(f(x))</text>

                        <!-- FORWARD HOP 1: f -->
                        <path d="M 112 138 C 180 120, 270 120, 346 138" fill="none" stroke="#0284c7" stroke-width="2.2" marker-end="url(#arrow-blue)"/>
                        <text x="230" y="118" font-family="sans-serif" font-size="13" font-weight="bold" fill="#0284c7" text-anchor="middle">Step 1: f</text>

                        <!-- FORWARD HOP 2: g -->
                        <path d="M 372 138 C 440 120, 530 120, 606 138" fill="none" stroke="#d97706" stroke-width="2.2" marker-end="url(#arrow-amber)"/>
                        <text x="490" y="118" font-family="sans-serif" font-size="13" font-weight="bold" fill="#d97706" text-anchor="middle">Step 2: g</text>

                        <!-- OVERARCHING BYPASS: g ∘ f -->
                        <path d="M 100 126 C 220 18, 500 18, 614 126" fill="none" stroke="#10b981" stroke-width="2.8" stroke-dasharray="5,3" marker-end="url(#arrow-green)"/>
                        <rect x="290" y="16" width="140" height="24" rx="4" fill="#ecfdf5" stroke="#10b981" stroke-width="1.2"/>
                        <text x="360" y="32" font-family="sans-serif" font-size="12" font-weight="bold" fill="#047857" text-anchor="middle">Composite: (g ∘ f)</text>

                        <!-- SUBTITLE EXPLANATION AT BOTTOM -->
                        <text x="360" y="206" font-family="sans-serif" font-size="11" fill="#64748b" text-anchor="middle">The output of f serves directly as the input for g, bypassing the intermediate state.</text>
                    </svg>
                </div>

                <h4 style="margin: 1.25rem 0 0.5rem 0; color: #0f172a; font-size: 1.02rem; border-top: 1px solid #f1f5f9; padding-top: 1rem;">2. Inverses ($f^{-1}$): The "Undo" Operation</h4>
                <p style="margin: 0 0 0.75rem 0; color: #334155; line-height: 1.65;">
                    An <strong>inverse function</strong> $f^{-1}: Y \to X$ simply undoes what $f$ did. Composing a function with its inverse brings you right back to your starting point:
                </p>
                <div style="text-align: center; margin: 0.75rem 0; font-size: 1.05rem;">
                    $$(f^{-1} \circ f)(x) = x \quad \text{and} \quad (f \circ f^{-1})(y) = y$$
                </div>

                <!-- INVERSE FUNCTION ROUND-TRIP DIAGRAM -->
                <div style="background: #f8fafc; border: 1px solid var(--border); border-radius: 6px; padding: 1.25rem; margin: 1.25rem 0 1.75rem 0; text-align: center;">
                    <p style="font-size: 0.85rem; font-weight: 700; color: #64748b; margin-top: 0; margin-bottom: 0.75rem;">VISUALIZATION: The Inversion Round Trip ($X \underset{f^{-1}}{\overset{f}{\rightleftharpoons}} Y$)</p>
                    <svg viewBox="0 0 680 210" style="width: 100%; max-width: 640px; height: auto; display: inline-block;">
                        <defs>
                            <marker id="inv-arrow-blue" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                                <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#0284c7"/>
                            </marker>
                            <marker id="inv-arrow-amber" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                                <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#d97706"/>
                            </marker>
                        </defs>

                        <!-- SET X (Domain of f / Codomain of f⁻¹) -->
                        <ellipse cx="140" cy="105" rx="65" ry="70" fill="#ffffff" stroke="#94a3b8" stroke-width="2"/>
                        <text x="140" y="60" font-family="sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Set X</text>
                        <text x="140" y="76" font-family="sans-serif" font-size="10" fill="#64748b" text-anchor="middle">Domain of f</text>
                        <circle cx="140" cy="112" r="4.5" fill="#0284c7"/>
                        <text x="128" y="116" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0369a1" text-anchor="end">x</text>

                        <!-- SET Y (Codomain of f / Domain of f⁻¹) -->
                        <ellipse cx="540" cy="105" rx="65" ry="70" fill="#ffffff" stroke="#94a3b8" stroke-width="2"/>
                        <text x="540" y="60" font-family="sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Set Y</text>
                        <text x="540" y="76" font-family="sans-serif" font-size="10" fill="#64748b" text-anchor="middle">Codomain of f</text>
                        <circle cx="540" cy="112" r="4.5" fill="#d97706"/>
                        <text x="552" y="116" font-family="sans-serif" font-size="12" font-weight="bold" fill="#92400e" text-anchor="start">y = f(x)</text>

                        <!-- FORWARD PATH (f): Top Arc -->
                        <path d="M 155 92 C 255 35, 425 35, 525 92" fill="none" stroke="#0284c7" stroke-width="2.2" marker-end="url(#inv-arrow-blue)"/>
                        <rect x="290" y="24" width="100" height="22" rx="4" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.2"/>
                        <text x="340" y="39" font-family="sans-serif" font-size="11.5" font-weight="bold" fill="#0369a1" text-anchor="middle">Forward: f</text>

                        <!-- REVERSE PATH (f⁻¹): Bottom Arc -->
                        <path d="M 525 125 C 425 180, 255 180, 155 125" fill="none" stroke="#d97706" stroke-width="2.2" marker-end="url(#inv-arrow-amber)"/>
                        <rect x="285" y="162" width="110" height="22" rx="4" fill="#fffbeb" stroke="#d97706" stroke-width="1.2"/>
                        <text x="340" y="177" font-family="sans-serif" font-size="11.5" font-weight="bold" fill="#92400e" text-anchor="middle">Reverse: f⁻¹</text>

                        <!-- CENTER IDENTITY BADGE -->
                        <text x="340" y="98" font-family="sans-serif" font-size="11.5" font-weight="bold" fill="#0f172a" text-anchor="middle">(f⁻¹ ∘ f)(x) = x</text>
                        <text x="340" y="114" font-family="sans-serif" font-size="10" fill="#64748b" text-anchor="middle">Unbroken round trip</text>
                    </svg>
                </div>

                <p style="color: #334155; line-height: 1.65; margin-bottom: 0.5rem;">
                    Why must a function be <strong>bijective</strong> to have an inverse? It comes down to what happens when you try to walk the arrows backward:
                </p>
                <ul style="margin: 0.25rem 0 0.75rem 1.25rem; padding: 0; color: #334155; font-size: 0.95rem; line-height: 1.65;">
                    <li><strong>Must be Injective (No Ambiguity):</strong> If two inputs merged to the same output, walking backward leaves you at a fork with no unique answer for where you came from.</li>
                    <li><strong>Must be Surjective (No Dead Ends):</strong> If an element in $Y$ was never hit by an arrow, the reverse path is undefined for that point.</li>
                </ul>
                <div class="definition-box" style="margin-top: 0.75rem; margin-bottom: 0;">
                    <strong>Core Takeaway:</strong> A mapping $f: X \to Y$ has a two-sided inverse $f^{-1}: Y \to X$ <strong>if and only if</strong> it is bijective.
                </div>
            </div>'''

    start_delim = '<!-- SECTION 3 -->'
    end_delim = '<!-- SECTION 4 -->'

    start_idx = content.find(start_delim)
    end_idx = content.find(end_delim)

    if start_idx != -1 and end_idx != -1:
        content = content[:start_idx] + new_section_3 + '\n\n            ' + content[end_idx:]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully updated Subsections 3.1, 3.2, and 3.3 in week1-lecture1.html with reassuring intros.")
    else:
        print("Could not locate boundaries for Section 3 in week1-lecture1.html.")

def synchronize_git_changes():
    commit_message = (
        "Add reassuring conceptual introductions to Subsections 3.1-3.3\n\n"
        "Introduced supportive, collegiate introductory leads to Subsections 3.1,\n"
        "3.2, and 3.3 in week1-lecture1.html. Normalises the conceptual shift from\n"
        "formula-based calculus to set-theoretic mappings, framing injectivity,\n"
        "surjectivity, and invertibility as intuitive structural checks."
    )
    commands = [
        ['git', 'add', 'week1-lecture1.html', 'update.py'],
        ['git', 'commit', '-m', commit_message],
        ['git', 'push', 'origin', 'main']
    ]
    for cmd in commands:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(f"> {' '.join(cmd)}\n{result.stdout}{result.stderr}")

if __name__ == '__main__':
    update_section3_introductions()
    synchronize_git_changes()
