#!/usr/bin/env python3
import os
import subprocess

def upgrade_week1_to_perfection():
    filepath = 'week1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Section 1 to include Set Difference SVG and Cartesian Product table
    old_diagrams_block = r'''            <div class="diagram-grid">
                <div class="diagram-card">
                    <h5>Intersection ($A \cap B$) &mdash; "And"</h5>
                    <svg viewBox="0 0 360 170">
                        <rect x="10" y="10" width="340" height="150" rx="8" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1.2"/>
                        <text x="25" y="32" font-family="ui-sans-serif, system-ui, sans-serif" font-size="12" fill="#64748b" font-weight="600">Shared Overlap (A ∩ B)</text>
                        <circle cx="145" cy="95" r="52" fill="#ffffff" stroke="#d97706" stroke-width="1.2"/>
                        <circle cx="215" cy="95" r="52" fill="#ffffff" stroke="#d97706" stroke-width="1.2"/>
                        <path d="M 180 57 A 52 52 0 0 1 180 133 A 52 52 0 0 1 180 57 Z" fill="#d97706" opacity="0.75"/>
                        <text x="125" y="100" font-family="ui-sans-serif, system-ui, sans-serif" font-size="16" fill="#b45309" font-weight="bold">A</text>
                        <text x="230" y="100" font-family="ui-sans-serif, system-ui, sans-serif" font-size="16" fill="#b45309" font-weight="bold">B</text>
                    </svg>
                </div>
                <div class="diagram-card">
                    <h5>Complement ($A^c = U \setminus A$)</h5>
                    <svg viewBox="0 0 360 170">
                        <defs>
                            <mask id="complement-mask">
                                <rect x="10" y="10" width="340" height="150" fill="white"/>
                                <circle cx="180" cy="95" r="48" fill="black"/>
                            </mask>
                        </defs>
                        <rect x="10" y="10" width="340" height="150" rx="8" fill="#fde68a" opacity="0.55" mask="url(#complement-mask)"/>
                        <rect x="10" y="10" width="340" height="150" rx="8" fill="none" stroke="#cbd5e1" stroke-width="1.2"/>
                        <text x="25" y="32" font-family="ui-sans-serif, system-ui, sans-serif" font-size="12" fill="#92400e" font-weight="600">Aᶜ (Shaded Region Outside A)</text>
                        <circle cx="180" cy="95" r="48" fill="#ffffff" stroke="#d97706" stroke-width="1.2"/>
                        <text x="175" y="101" font-family="ui-sans-serif, system-ui, sans-serif" font-size="16" fill="#b45309" font-weight="bold">A</text>
                    </svg>
                </div>
            </div>'''

    new_diagrams_block = r'''            <div class="diagram-grid">
                <div class="diagram-card">
                    <h5>Intersection ($A \cap B$) &mdash; "And"</h5>
                    <svg viewBox="0 0 360 170">
                        <rect x="10" y="10" width="340" height="150" rx="8" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1.2"/>
                        <text x="25" y="32" font-family="ui-sans-serif, system-ui, sans-serif" font-size="12" fill="#64748b" font-weight="600">Shared Overlap (A ∩ B)</text>
                        <circle cx="145" cy="95" r="52" fill="#ffffff" stroke="#d97706" stroke-width="1.2"/>
                        <circle cx="215" cy="95" r="52" fill="#ffffff" stroke="#d97706" stroke-width="1.2"/>
                        <path d="M 180 57 A 52 52 0 0 1 180 133 A 52 52 0 0 1 180 57 Z" fill="#d97706" opacity="0.75"/>
                        <text x="125" y="100" font-family="ui-sans-serif, system-ui, sans-serif" font-size="16" fill="#b45309" font-weight="bold">A</text>
                        <text x="230" y="100" font-family="ui-sans-serif, system-ui, sans-serif" font-size="16" fill="#b45309" font-weight="bold">B</text>
                    </svg>
                </div>
                <div class="diagram-card">
                    <h5>Set Difference ($A \setminus B$) &mdash; "In A, Not B"</h5>
                    <svg viewBox="0 0 360 170">
                        <defs>
                            <mask id="diff-mask">
                                <circle cx="145" cy="95" r="52" fill="white"/>
                                <circle cx="215" cy="95" r="52" fill="black"/>
                            </mask>
                        </defs>
                        <rect x="10" y="10" width="340" height="150" rx="8" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1.2"/>
                        <text x="25" y="32" font-family="ui-sans-serif, system-ui, sans-serif" font-size="12" fill="#64748b" font-weight="600">Difference (A ∖ B)</text>
                        <circle cx="145" cy="95" r="52" fill="#fde68a" mask="url(#diff-mask)"/>
                        <circle cx="145" cy="95" r="52" fill="none" stroke="#d97706" stroke-width="1.2"/>
                        <circle cx="215" cy="95" r="52" fill="none" stroke="#d97706" stroke-width="1.2"/>
                        <text x="120" y="100" font-family="ui-sans-serif, system-ui, sans-serif" font-size="16" fill="#b45309" font-weight="bold">A</text>
                        <text x="230" y="100" font-family="ui-sans-serif, system-ui, sans-serif" font-size="16" fill="#b45309" font-weight="bold">B</text>
                    </svg>
                </div>
            </div>

            <div class="diagram-grid">
                <div class="diagram-card">
                    <h5>Universal Complement ($A^c = U \setminus A$)</h5>
                    <svg viewBox="0 0 360 170">
                        <defs>
                            <mask id="complement-mask">
                                <rect x="10" y="10" width="340" height="150" fill="white"/>
                                <circle cx="180" cy="95" r="48" fill="black"/>
                            </mask>
                        </defs>
                        <rect x="10" y="10" width="340" height="150" rx="8" fill="#fde68a" opacity="0.55" mask="url(#complement-mask)"/>
                        <rect x="10" y="10" width="340" height="150" rx="8" fill="none" stroke="#cbd5e1" stroke-width="1.2"/>
                        <text x="25" y="32" font-family="ui-sans-serif, system-ui, sans-serif" font-size="12" fill="#92400e" font-weight="600">Aᶜ (Shaded Region Outside A)</text>
                        <circle cx="180" cy="95" r="48" fill="#ffffff" stroke="#d97706" stroke-width="1.2"/>
                        <text x="175" y="101" font-family="ui-sans-serif, system-ui, sans-serif" font-size="16" fill="#b45309" font-weight="bold">A</text>
                    </svg>
                </div>
                <div class="diagram-card">
                    <h5>Cartesian Product ($A \times B$)</h5>
                    <svg viewBox="0 0 360 170">
                        <rect x="10" y="10" width="340" height="150" rx="8" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1.2"/>
                        <text x="25" y="32" font-family="ui-sans-serif, system-ui, sans-serif" font-size="12" fill="#64748b" font-weight="600">Ordered Pairs: {1, 2} × {x, y}</text>
                        <rect x="50" y="55" width="120" height="40" rx="4" fill="#ffffff" stroke="#fed7aa"/>
                        <text x="110" y="80" font-family="ui-sans-serif, system-ui, sans-serif" font-size="13" fill="#b45309" font-weight="bold" text-anchor="middle">(1, x)</text>
                        <rect x="190" y="55" width="120" height="40" rx="4" fill="#ffffff" stroke="#fed7aa"/>
                        <text x="250" y="80" font-family="ui-sans-serif, system-ui, sans-serif" font-size="13" fill="#b45309" font-weight="bold" text-anchor="middle">(1, y)</text>
                        <rect x="50" y="105" width="120" height="40" rx="4" fill="#ffffff" stroke="#fed7aa"/>
                        <text x="110" y="130" font-family="ui-sans-serif, system-ui, sans-serif" font-size="13" fill="#b45309" font-weight="bold" text-anchor="middle">(2, x)</text>
                        <rect x="190" y="105" width="120" height="40" rx="4" fill="#ffffff" stroke="#fed7aa"/>
                        <text x="250" y="130" font-family="ui-sans-serif, system-ui, sans-serif" font-size="13" fill="#b45309" font-weight="bold" text-anchor="middle">(2, y)</text>
                    </svg>
                </div>
            </div>'''

    if old_diagrams_block in content:
        content = content.replace(old_diagrams_block, new_diagrams_block)
        print("Updated set operation diagrams with A \\ B and A x B.")

    # 2. Update Notation infobox in Section 2 to clarify 0 in N
    old_n_desc = r'<div class="notation-item"><span class="notation-sym">$\mathbb{N}$</span><span class="notation-desc">Natural numbers: counting numbers $\{1, 2, 3, \dots\}$</span></div>'
    new_n_desc = (
        r'<div class="notation-item"><span class="notation-sym">$\mathbb{N}$</span>'
        r'<span class="notation-desc">Natural numbers: $\{0, 1, 2, \dots\}$ (in MTHS120, $0 \in \mathbb{N}$)</span></div>'
        r'\n                    <div class="notation-item"><span class="notation-sym">$\mathbb{Z}_+$</span>'
        r'<span class="notation-desc">Positive integers: $\{1, 2, 3, \dots\}$</span></div>'
    )

    if old_n_desc in content:
        content = content.replace(old_n_desc, new_n_desc)
        print("Updated natural number definition to reflect 0 in N convention.")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def execute_git_sync():
    commit_message = (
        "Upgrade Week 1 pedagogical scaffolding to 10/10 standard\n\n"
        "Added dedicated set difference SVG diagram, Cartesian product grid, and\n"
        "clarified the 0 in N convention matching the official lecture notes."
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
    upgrade_week1_to_perfection()
    execute_git_sync()
