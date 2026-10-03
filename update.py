#!/usr/bin/env python3
import os
import subprocess

def add_diagrams_to_week1():
    filepath = 'week1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # SVG Diagram for Section 4 (Partial Sums)
    sums_diagram = r"""
            <div class="diagram-card" style="margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
                <h5>Partial Sums: Accumulating a Running Total ($s_n = \sum_{\nu=0}^n b_\nu$)</h5>
                <svg viewBox="0 0 740 180">
                    <rect x="15" y="10" width="710" height="160" rx="10" fill="#fffbeb" stroke="#fde68a" stroke-width="1.5"/>
                    <text x="35" y="35" font-family="ui-sans-serif, system-ui, sans-serif" font-size="13" fill="#92400e" font-weight="bold">Individual Terms (b₈): [2, 3, 5, 1]</text>

                    <g transform="translate(45, 55)">
                        <rect x="0" y="0" width="135" height="45" rx="6" fill="#ffffff" stroke="#d97706" stroke-width="1.2"/>
                        <text x="67.5" y="27" font-family="ui-sans-serif, system-ui, sans-serif" font-size="13" fill="#b45309" font-weight="bold" text-anchor="middle">b₀ = 2</text>
                        <text x="67.5" y="75" font-family="ui-sans-serif, system-ui, sans-serif" font-size="12" fill="#0f172a" font-weight="600" text-anchor="middle">s₀ = 2</text>
                    </g>
                    <g transform="translate(200, 55)">
                        <rect x="0" y="0" width="135" height="45" rx="6" fill="#ffffff" stroke="#d97706" stroke-width="1.2"/>
                        <text x="67.5" y="27" font-family="ui-sans-serif, system-ui, sans-serif" font-size="13" fill="#b45309" font-weight="bold" text-anchor="middle">b₁ = 3</text>
                        <text x="67.5" y="75" font-family="ui-sans-serif, system-ui, sans-serif" font-size="12" fill="#0f172a" font-weight="600" text-anchor="middle">s₁ = 2+3 = 5</text>
                    </g>
                    <g transform="translate(355, 55)">
                        <rect x="0" y="0" width="135" height="45" rx="6" fill="#ffffff" stroke="#d97706" stroke-width="1.2"/>
                        <text x="67.5" y="27" font-family="ui-sans-serif, system-ui, sans-serif" font-size="13" fill="#b45309" font-weight="bold" text-anchor="middle">b₂ = 5</text>
                        <text x="67.5" y="75" font-family="ui-sans-serif, system-ui, sans-serif" font-size="12" fill="#0f172a" font-weight="600" text-anchor="middle">s₂ = 5+5 = 10</text>
                    </g>
                    <g transform="translate(510, 55)">
                        <rect x="0" y="0" width="185" height="45" rx="6" fill="#ffffff" stroke="#d97706" stroke-width="1.2"/>
                        <text x="92.5" y="27" font-family="ui-sans-serif, system-ui, sans-serif" font-size="13" fill="#b45309" font-weight="bold" text-anchor="middle">b₃ = 1</text>
                        <text x="92.5" y="75" font-family="ui-sans-serif, system-ui, sans-serif" font-size="12" fill="#0f172a" font-weight="600" text-anchor="middle">s₃ = 10+1 = 11</text>
                    </g>
                </svg>
            </div>"""

    # SVG Diagram for Section 5 (Derived Sequences)
    derived_diagram = r"""
            <div class="diagram-card" style="margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
                <h5>Derived Sequence Gaps: Measuring Step-by-Step Jump Size ($a_n' = a_{n+1} - a_n$)</h5>
                <svg viewBox="0 0 740 190">
                    <defs>
                        <marker id="gap-arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="4" markerHeight="4" orient="auto-start-reverse">
                            <path d="M 0 0 L 10 5 L 0 10 z" fill="#d97706"/>
                        </marker>
                    </defs>
                    <rect x="15" y="10" width="710" height="170" rx="10" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
                    <text x="35" y="35" font-family="ui-sans-serif, system-ui, sans-serif" font-size="13" fill="#b45309" font-weight="bold">Sequence aₙ = n²: [1, 4, 9, 16]</text>

                    <!-- Nodes -->
                    <circle cx="100" cy="120" r="8" fill="#d97706"/>
                    <text x="100" y="150" font-family="sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">a₁ = 1</text>

                    <circle cx="280" cy="90" r="8" fill="#d97706"/>
                    <text x="280" y="150" font-family="sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">a₂ = 4</text>

                    <circle cx="460" cy="60" r="8" fill="#d97706"/>
                    <text x="460" y="150" font-family="sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">a₃ = 9</text>

                    <circle cx="640" cy="30" r="8" fill="#d97706"/>
                    <text x="640" y="150" font-family="sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">a₄ = 16</text>

                    <!-- Jump Gaps (Derived sequence values) -->
                    <line x1="100" y1="120" x2="280" y2="90" stroke="#94a3b8" stroke-dasharray="3" stroke-width="1.5"/>
                    <text x="190" y="98" font-family="sans-serif" font-size="12" font-weight="bold" fill="#d97706" text-anchor="middle">Gap: +3 (a₁')</text>

                    <line x1="280" y1="90" x2="460" y2="60" stroke="#94a3b8" stroke-dasharray="3" stroke-width="1.5"/>
                    <text x="370" y="68" font-family="sans-serif" font-size="12" font-weight="bold" fill="#d97706" text-anchor="middle">Gap: +5 (a₂')</text>

                    <line x1="460" y1="60" x2="640" y2="30" stroke="#94a3b8" stroke-dasharray="3" stroke-width="1.5"/>
                    <text x="550" y="38" font-family="sans-serif" font-size="12" font-weight="bold" fill="#d97706" text-anchor="middle">Gap: +7 (a₃')</text>
                </svg>
            </div>"""

    # Insert into week1.html if not already present
    if 'Partial Sums: Accumulating a Running Total' not in content:
        content = content.replace('<h3>Partial Sums: The Running Total</h3>', sums_diagram + '\n\n            <h3>Partial Sums: The Running Total</h3>')

    if 'Derived Sequence Gaps: Measuring Step-by-Step Jump Size' not in content:
        content = content.replace('<h3>Worked Example: Squares and Differences</h3>', derived_diagram + '\n\n            <h3>Worked Example: Squares and Differences</h3>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully added visual diagrams to week1.html.")

def execute_git_sync():
    commit_message = (
        "Add SVG visual diagrams for Sums and Derived Sequences\n\n"
        "Embedded custom diagram cards into week1.html to visually illustrate\n"
        "partial sum accumulation and derived sequence gap jumps."
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
    add_diagrams_to_week1()
    execute_git_sync()
