#!/usr/bin/env python3
import os
import subprocess

def rewrite_set_operations():
    filepath = 'week1-lecture1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_section_2 = r'''<!-- SECTION 2 -->
            <h2 id="set-operations">2. Set Operations and Products</h2>
            <p style="font-size: 1.02rem; line-height: 1.7; color: #334155;">
                Sets can be combined and partitioned using algebraic operations analogous to arithmetic. Rather than operating on numerical values, set operations act on collections of elements governed by formal logical connectives.
            </p>
            <p style="font-size: 1.02rem; line-height: 1.7; color: #334155;">
                To illustrate the mechanics of each operation, consider two concrete subsets of $\mathbb{N}$ throughout this section:
            </p>
            <div style="text-align: center; margin: 1rem 0; font-size: 1.1rem; background: #f8fafc; padding: 0.85rem; border-radius: 6px; border: 1px solid var(--border);">
                $$A = \{1, 2, 3\} \quad \text{and} \quad B = \{2, 3, 4, 5\}$$
            </div>

            <!-- OPERATION 1: UNION -->
            <div style="background: #ffffff; border: 1px solid var(--border); border-radius: 8px; padding: 1.5rem; margin-top: 1.75rem; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
                <div style="display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; gap: 0.5rem; border-bottom: 1px solid #f1f5f9; padding-bottom: 0.75rem; margin-bottom: 1rem;">
                    <h3 style="margin: 0; color: #0f172a; font-size: 1.15rem;">2.1 Union ($A \cup B$)</h3>
                    <span style="font-weight: 700; color: var(--accent); font-size: 0.95rem;">Logical Connective: Disjunction ($\lor$)</span>
                </div>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; align-items: center;">
                    <div>
                        <p style="margin-top: 0; color: #334155; line-height: 1.65;">
                            The <strong>union</strong> of two sets contains every element that belongs to at least one of the sets.
                        </p>
                        <div class="definition-box" style="margin: 0.75rem 0;">
                            $$A \cup B = \{x \mid x \in A \lor x \in B\}$$
                        </div>
                        <p style="color: #334155; line-height: 1.65; margin-bottom: 0.5rem;">
                            In formal mathematics, the disjunction $\lor$ ("or") is strictly <strong>inclusive</strong>: an element $x \in (A \cup B)$ if $x \in A$, $x \in B$, or $x$ belongs to both simultaneously. Since sets do not register duplicate elements, overlapping members are listed once.
                        </p>
                        <p style="color: #047857; font-weight: 600; margin-bottom: 0;">
                            For our sample sets: $A \cup B = \{1, 2, 3, 4, 5\}$.
                        </p>
                    </div>
                    <div style="background: #f8fafc; border: 1px solid var(--border); border-radius: 6px; padding: 1rem; text-align: center;">
                        <svg viewBox="0 0 320 180" style="width: 100%; max-width: 300px; height: auto; display: inline-block;">
                            <circle cx="120" cy="90" r="62" fill="#fde68a" fill-opacity="0.55" stroke="#d97706" stroke-width="2.5"/>
                            <circle cx="200" cy="90" r="62" fill="#fde68a" fill-opacity="0.55" stroke="#d97706" stroke-width="2.5"/>
                            <text x="85" y="45" font-family="sans-serif" font-size="14" font-weight="bold" fill="#92400e">Set A</text>
                            <text x="235" y="45" font-family="sans-serif" font-size="14" font-weight="bold" fill="#92400e">Set B</text>
                            <text x="95" y="95" font-family="sans-serif" font-size="12" fill="#451a03">1</text>
                            <text x="156" y="80" font-family="sans-serif" font-size="12" fill="#451a03">2</text>
                            <text x="156" y="108" font-family="sans-serif" font-size="12" fill="#451a03">3</text>
                            <text x="215" y="80" font-family="sans-serif" font-size="12" fill="#451a03">4</text>
                            <text x="215" y="108" font-family="sans-serif" font-size="12" fill="#451a03">5</text>
                            <rect x="85" y="152" width="150" height="22" rx="4" fill="#d97706"/>
                            <text x="160" y="167" font-family="sans-serif" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Union: A ∪ B</text>
                        </svg>
                    </div>
                </div>
            </div>

            <!-- OPERATION 2: INTERSECTION -->
            <div style="background: #ffffff; border: 1px solid var(--border); border-radius: 8px; padding: 1.5rem; margin-top: 1.5rem; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
                <div style="display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; gap: 0.5rem; border-bottom: 1px solid #f1f5f9; padding-bottom: 0.75rem; margin-bottom: 1rem;">
                    <h3 style="margin: 0; color: #0f172a; font-size: 1.15rem;">2.2 Intersection ($A \cap B$)</h3>
                    <span style="font-weight: 700; color: #0284c7; font-size: 0.95rem;">Logical Connective: Conjunction ($\land$)</span>
                </div>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; align-items: center;">
                    <div>
                        <p style="margin-top: 0; color: #334155; line-height: 1.65;">
                            The <strong>intersection</strong> of two sets gathers only those elements that belong to both sets simultaneously.
                        </p>
                        <div class="definition-box" style="margin: 0.75rem 0; border-left-color: #0284c7;">
                            $$A \cap B = \{x \mid x \in A \land x \in B\}$$
                        </div>
                        <p style="color: #334155; line-height: 1.65; margin-bottom: 0.5rem;">
                            When two sets share no common elements ($A \cap B = \emptyset$), they are formally defined as <strong>mutually disjoint</strong>.
                        </p>
                        <p style="color: #0284c7; font-weight: 600; margin-bottom: 0;">
                            For our sample sets: $A \cap B = \{2, 3\}$.
                        </p>
                    </div>
                    <div style="background: #f8fafc; border: 1px solid var(--border); border-radius: 6px; padding: 1rem; text-align: center;">
                        <svg viewBox="0 0 320 180" style="width: 100%; max-width: 300px; height: auto; display: inline-block;">
                            <defs>
                                <clipPath id="circleA-clip">
                                    <circle cx="120" cy="90" r="62"/>
                                </clipPath>
                            </defs>
                            <circle cx="120" cy="90" r="62" fill="#ffffff" stroke="#94a3b8" stroke-width="2"/>
                            <circle cx="200" cy="90" r="62" fill="#ffffff" stroke="#94a3b8" stroke-width="2"/>
                            <circle cx="200" cy="90" r="62" fill="#bae6fd" clip-path="url(#circleA-clip)"/>
                            <circle cx="120" cy="90" r="62" fill="none" stroke="#0284c7" stroke-width="2.5"/>
                            <circle cx="200" cy="90" r="62" fill="none" stroke="#0284c7" stroke-width="2.5"/>
                            <text x="85" y="45" font-family="sans-serif" font-size="14" font-weight="bold" fill="#64748b">Set A</text>
                            <text x="235" y="45" font-family="sans-serif" font-size="14" font-weight="bold" fill="#64748b">Set B</text>
                            <text x="95" y="95" font-family="sans-serif" font-size="12" fill="#94a3b8">1</text>
                            <text x="156" y="80" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0369a1">2</text>
                            <text x="156" y="108" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0369a1">3</text>
                            <text x="215" y="80" font-family="sans-serif" font-size="12" fill="#94a3b8">4</text>
                            <text x="215" y="108" font-family="sans-serif" font-size="12" fill="#94a3b8">5</text>
                            <rect x="85" y="152" width="150" height="22" rx="4" fill="#0284c7"/>
                            <text x="160" y="167" font-family="sans-serif" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Intersection: A ∩ B</text>
                        </svg>
                    </div>
                </div>
            </div>

            <!-- OPERATION 3: SET DIFFERENCE -->
            <div style="background: #ffffff; border: 1px solid var(--border); border-radius: 8px; padding: 1.5rem; margin-top: 1.5rem; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
                <div style="display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; gap: 0.5rem; border-bottom: 1px solid #f1f5f9; padding-bottom: 0.75rem; margin-bottom: 1rem;">
                    <h3 style="margin: 0; color: #0f172a; font-size: 1.15rem;">2.3 Set Difference / Relative Complement ($A \setminus B$)</h3>
                    <span style="font-weight: 700; color: #be185d; font-size: 0.95rem;">Non-Commutative Operation</span>
                </div>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; align-items: center;">
                    <div>
                        <p style="margin-top: 0; color: #334155; line-height: 1.65;">
                            The <strong>set difference</strong> $A \setminus B$ (or relative complement of $B$ in $A$) consists of all elements that belong to $A$ but do not belong to $B$.
                        </p>
                        <div class="definition-box" style="margin: 0.75rem 0; border-left-color: #be185d;">
                            $$A \setminus B = \{x \mid x \in A \land x \notin B\}$$
                        </div>
                        <p style="color: #334155; line-height: 1.65; margin-bottom: 0.5rem;">
                            Unlike union and intersection, set difference is strictly non-commutative ($A \setminus B \neq B \setminus A$):
                        </p>
                        <ul style="margin: 0.25rem 0 0.5rem 1.25rem; padding: 0; color: #334155; font-size: 0.95rem;">
                            <li>$A \setminus B = \{1\}$ (elements unique to $A$)</li>
                            <li>$B \setminus A = \{4, 5\}$ (elements unique to $B$)</li>
                        </ul>
                    </div>
                    <div style="background: #f8fafc; border: 1px solid var(--border); border-radius: 6px; padding: 1rem; text-align: center;">
                        <svg viewBox="0 0 320 180" style="width: 100%; max-width: 300px; height: auto; display: inline-block;">
                            <defs>
                                <mask id="diff-mask">
                                    <rect x="0" y="0" width="320" height="180" fill="#ffffff"/>
                                    <circle cx="200" cy="90" r="62" fill="#000000"/>
                                </mask>
                            </defs>
                            <circle cx="120" cy="90" r="62" fill="#fbcfe8" mask="url(#diff-mask)"/>
                            <circle cx="120" cy="90" r="62" fill="none" stroke="#be185d" stroke-width="2.5"/>
                            <circle cx="200" cy="90" r="62" fill="none" stroke="#94a3b8" stroke-width="2" stroke-dasharray="4"/>
                            <text x="85" y="45" font-family="sans-serif" font-size="14" font-weight="bold" fill="#9d174d">Set A</text>
                            <text x="235" y="45" font-family="sans-serif" font-size="14" font-weight="bold" fill="#64748b">Set B</text>
                            <text x="95" y="95" font-family="sans-serif" font-size="13" font-weight="bold" fill="#9d174d">1</text>
                            <text x="156" y="80" font-family="sans-serif" font-size="12" fill="#94a3b8">2</text>
                            <text x="156" y="108" font-family="sans-serif" font-size="12" fill="#94a3b8">3</text>
                            <text x="215" y="80" font-family="sans-serif" font-size="12" fill="#94a3b8">4</text>
                            <text x="215" y="108" font-family="sans-serif" font-size="12" fill="#94a3b8">5</text>
                            <rect x="85" y="152" width="150" height="22" rx="4" fill="#be185d"/>
                            <text x="160" y="167" font-family="sans-serif" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Difference: A \ B</text>
                        </svg>
                    </div>
                </div>
            </div>

            <!-- OPERATION 4: CARTESIAN PRODUCT -->
            <div style="background: #ffffff; border: 1px solid var(--border); border-radius: 8px; padding: 1.5rem; margin-top: 1.5rem; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
                <div style="display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; gap: 0.5rem; border-bottom: 1px solid #f1f5f9; padding-bottom: 0.75rem; margin-bottom: 1rem;">
                    <h3 style="margin: 0; color: #0f172a; font-size: 1.15rem;">2.4 Cartesian Product ($A \times B$)</h3>
                    <span style="font-weight: 700; color: #047857; font-size: 0.95rem;">Ordered Pairs &amp; Product Spaces</span>
                </div>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; align-items: center;">
                    <div>
                        <p style="margin-top: 0; color: #334155; line-height: 1.65;">
                            The <strong>Cartesian product</strong> $A \times B$ is the set of all ordered pairs $(a, b)$ formed by taking an element $a \in A$ and pairing it with an element $b \in B$.
                        </p>
                        <div class="definition-box" style="margin: 0.75rem 0; border-left-color: #10b981;">
                            $$A \times B = \{(a, b) \mid a \in A \land b \in B\}$$
                        </div>
                        <p style="color: #334155; line-height: 1.65; margin-bottom: 0.5rem;">
                            For finite sets, the cardinality of the product equals the product of their individual cardinalities: $|A \times B| = |A| \cdot |B|$. Here, $|A| = 3$ and $|B| = 4$, yielding exactly $3 \times 4 = 12$ ordered pairs.
                        </p>
                        <p style="color: #047857; line-height: 1.6; margin-bottom: 0;">
                            In analysis, this construction generalizes continuous spaces: the product of the real line with itself, $\mathbb{R} \times \mathbb{R} = \mathbb{R}^2$, forms the two-dimensional Euclidean plane.
                        </p>
                    </div>
                    <div style="background: #f8fafc; border: 1px solid var(--border); border-radius: 6px; padding: 1rem; text-align: center;">
                        <svg viewBox="0 0 320 200" style="width: 100%; max-width: 300px; height: auto; display: inline-block;">
                            <line x1="60" y1="150" x2="280" y2="150" stroke="#0f172a" stroke-width="2"/>
                            <line x1="60" y1="150" x2="60" y2="25" stroke="#0f172a" stroke-width="2"/>
                            <text x="285" y="154" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a">A</text>
                            <text x="56" y="18" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a">B</text>

                            <line x1="120" y1="150" x2="120" y2="35" stroke="#e2e8f0" stroke-dasharray="3"/>
                            <line x1="190" y1="150" x2="190" y2="35" stroke="#e2e8f0" stroke-dasharray="3"/>
                            <line x1="260" y1="150" x2="260" y2="35" stroke="#e2e8f0" stroke-dasharray="3"/>

                            <line x1="60" y1="120" x2="270" y2="120" stroke="#e2e8f0" stroke-dasharray="3"/>
                            <line x1="60" y1="90" x2="270" y2="90" stroke="#e2e8f0" stroke-dasharray="3"/>
                            <line x1="60" y1="60" x2="270" y2="60" stroke="#e2e8f0" stroke-dasharray="3"/>
                            <line x1="60" y1="35" x2="270" y2="35" stroke="#e2e8f0" stroke-dasharray="3"/>

                            <text x="120" y="167" font-family="sans-serif" font-size="11" fill="#475569" text-anchor="middle">1</text>
                            <text x="190" y="167" font-family="sans-serif" font-size="11" fill="#475569" text-anchor="middle">2</text>
                            <text x="260" y="167" font-family="sans-serif" font-size="11" fill="#475569" text-anchor="middle">3</text>

                            <text x="45" y="124" font-family="sans-serif" font-size="11" fill="#475569" text-anchor="end">2</text>
                            <text x="45" y="94" font-family="sans-serif" font-size="11" fill="#475569" text-anchor="end">3</text>
                            <text x="45" y="64" font-family="sans-serif" font-size="11" fill="#475569" text-anchor="end">4</text>
                            <text x="45" y="39" font-family="sans-serif" font-size="11" fill="#475569" text-anchor="end">5</text>

                            <circle cx="120" cy="120" r="4.5" fill="#10b981"/><circle cx="190" cy="120" r="4.5" fill="#10b981"/><circle cx="260" cy="120" r="4.5" fill="#10b981"/>
                            <circle cx="120" cy="90" r="4.5" fill="#10b981"/><circle cx="190" cy="90" r="4.5" fill="#10b981"/><circle cx="260" cy="90" r="4.5" fill="#10b981"/>
                            <circle cx="120" cy="60" r="4.5" fill="#10b981"/><circle cx="190" cy="60" r="4.5" fill="#10b981"/><circle cx="260" cy="60" r="4.5" fill="#10b981"/>
                            <circle cx="120" cy="35" r="4.5" fill="#10b981"/><circle cx="190" cy="35" r="4.5" fill="#10b981"/><circle cx="260" cy="35" r="4.5" fill="#10b981"/>

                            <text x="195" y="55" font-family="sans-serif" font-size="10" font-weight="bold" fill="#047857">(2, 4)</text>

                            <rect x="70" y="177" width="180" height="20" rx="3" fill="#047857"/>
                            <text x="160" y="191" font-family="sans-serif" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">A × B: 12 Ordered Pairs (a, b)</text>
                        </svg>
                    </div>
                </div>
            </div>'''

    start_delim = '<!-- SECTION 2 -->'
    end_delim = '<!-- SECTION 3 -->'

    start_idx = content.find(start_delim)
    end_idx = content.find(end_delim)

    if start_idx != -1 and end_idx != -1:
        content = content[:start_idx] + new_section_2 + '\n\n            ' + content[end_idx:]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully updated Section 2 in week1-lecture1.html with mature, collegiate exposition.")
    else:
        print("Could not locate section boundaries in week1-lecture1.html.")

def execute_git_sync():
    commit_message = (
        "Refactor Section 2 to use collegiate, rigorous mathematical tone\n\n"
        "Revised Section 2 of week1-lecture1.html to remove patronizing idioms\n"
        "and analogies while maintaining pedagogical clarity. Preserved the SVG\n"
        "Venn diagrams and coordinate grid, reframing them with standard\n"
        "undergraduate analysis terminology, rigorous set builder notation, and\n"
        "concise worked examples."
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
    rewrite_set_operations()
    execute_git_sync()
