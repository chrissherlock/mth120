#!/usr/bin/env python3
import os
import subprocess

def insert_inverse_mapping_diagram():
    filepath = 'week1-lecture1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    target_anchor = r'''                <div style="text-align: center; margin: 0.75rem 0; font-size: 1.05rem;">
                    $$(f^{-1} \circ f)(x) = x \quad \text{and} \quad (f \circ f^{-1})(y) = y$$
                </div>'''

    inverse_diagram_markup = r'''                <div style="text-align: center; margin: 0.75rem 0; font-size: 1.05rem;">
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
                </div>'''

    if target_anchor in content:
        if "VISUALIZATION: The Inversion Round Trip" in content:
            print("Inverse diagram is already present in week1-lecture1.html.")
            return

        content = content.replace(target_anchor, inverse_diagram_markup, 1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully integrated the inverse mapping diagram into week1-lecture1.html.")
    else:
        print("Could not locate the target anchor in week1-lecture1.html.")

def execute_git_sync():
    commit_message = (
        "Add inverse function round-trip diagram to Lecture 1\n\n"
        "Integrated an inline SVG diagram illustrating inverse mappings into\n"
        "Section 3.3 of week1-lecture1.html. Visually depicts the two-way loop\n"
        "between domain and codomain, reinforcing the identity equations\n"
        "(f⁻¹ ∘ f)(x) = x and (f ∘ f⁻¹)(y) = y for bijective functions."
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
    insert_inverse_mapping_diagram()
    execute_git_sync()
