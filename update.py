#!/usr/bin/env python3
import os
import subprocess

def replace_functions_mappings_section():
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
                    <div class="notation-item"><span class="notation-sym">$f(X)$ or $\text{ran}(f)$</span><span class="notation-desc">Range: actual set of achieved output values $\{f(x) \mid x \in X\}$</span></div>
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
                            <path d="M 64,75 C 130,55 170,75 220,88" fill="none" stroke="#0284c7" stroke-width="1.6" marker-end="url(#arr)"/>
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
                <p style="margin-top: 0; color: #334155; line-height: 1.65;">
                    The behavior of a mapping is classified by how its arrows leave the domain and land in the codomain:
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

            <!-- SUBSECTION 3.3: INVERTIBILITY AND COMPOSITION -->
            <div style="background: #ffffff; border: 1px solid var(--border); border-radius: 8px; padding: 1.5rem; margin-top: 1.5rem; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
                <div style="display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; gap: 0.5rem; border-bottom: 1px solid #f1f5f9; padding-bottom: 0.75rem; margin-bottom: 1rem;">
                    <h3 style="margin: 0; color: #0f172a; font-size: 1.15rem;">3.3 Invertibility and Composition</h3>
                    <span style="font-weight: 700; color: var(--accent); font-size: 0.92rem;">Two-Way Streets &amp; Pipeline Chains</span>
                </div>
                <p style="margin-top: 0; color: #334155; line-height: 1.65;">
                    Why do mathematicians insist that a function must be bijective before it has an inverse? Consider what happens if you try to run the arrows backward:
                </p>
                <ul style="margin: 0.25rem 0 1rem 1.25rem; padding: 0; color: #334155; font-size: 0.95rem; line-height: 1.65;">
                    <li><strong>If $f$ is not injective:</strong> Two different inputs share the same output. Reversing the arrow forces a single input to point to two different outputs, violating the definition of a function.</li>
                    <li><strong>If $f$ is not surjective:</strong> Some elements in $Y$ were never hit. Reversing the arrows leaves those elements stranded with nowhere to go.</li>
                </ul>
                <div class="definition-box" style="margin-bottom: 1.25rem;">
                    <strong>Theorem: Existence of Inverse Functions:</strong><br>
                    A function $f: X \to Y$ possesses a two-sided inverse $f^{-1}: Y \to X$ such that $(f^{-1} \circ f)(x) = x$ and $(f \circ f^{-1})(y) = y$ <strong>if and only if</strong> $f$ is bijective.
                </div>

                <h4 style="color: #0f172a; margin: 1.25rem 0 0.5rem 0; font-size: 1.05rem;">Chaining Operations: Function Composition ($g \circ f$)</h4>
                <p style="color: #334155; line-height: 1.65; margin-bottom: 0.5rem;">
                    Given two mappings $f: X \to Y$ and $g: Y \to Z$, their <strong>composition</strong> $g \circ f: X \to Z$ creates an immediate path from $X$ to $Z$:
                </p>
                <div style="text-align: center; margin: 0.75rem 0; font-size: 1.05rem;">
                    $$(g \circ f)(x) = g(f(x))$$
                </div>
                <p style="color: #334155; line-height: 1.65; margin-bottom: 0;">
                    <em>Remember the evaluation order:</em> Although $g$ is written first on the left, $f$ acts on $x$ first. Think of $g \circ f$ as saying <em>"apply $f$, then apply $g$ to the result."</em> For composition to be valid, the range of $f$ must be contained within the domain of $g$.
                </p>
            </div>'''

    start_delim = '<!-- SECTION 3 -->'
    end_delim = '<!-- SECTION 4 -->'

    start_idx = content.find(start_delim)
    end_idx = content.find(end_delim)

    if start_idx != -1 and end_idx != -1:
        content = content[:start_idx] + new_section_3 + '\n\n            ' + content[end_idx:]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully updated Section 3 in week1-lecture1.html with collegiate exposition and SVG diagrams.")
    else:
        print("Could not locate section boundaries for Section 3 in week1-lecture1.html.")

def synchronize_repository():
    commit_message = (
        "Expand Section 3 on functions with collegiate exposition and diagrams\n\n"
        "Expanded Section 3 in week1-lecture1.html to provide a reassuring,\n"
        "conceptually rich breakdown of functions and mappings for undergraduates.\n"
        "Preserved the notation reference infobox while introducing clear\n"
        "explanations and inline SVG diagrams for codomain vs range, injectivity,\n"
        "surjectivity, and bijective invertibility."
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
    replace_functions_mappings_section()
    synchronize_repository()
