#!/usr/bin/env python3
import os
import subprocess

def insert_composition_pipeline_diagram():
    filepath = 'week1-lecture1.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    target_anchor = r'''                <p style="color: #334155; line-height: 1.65; margin-bottom: 1.25rem;">
                    <strong>Read from right to left:</strong> Although $g$ is written on the left, $f$ acts on $x$ first. Think of $(g \circ f)(x)$ as saying: <em>"evaluate $f(x)$ first, then pass that output into $g$."</em>
                </p>'''

    pipeline_diagram_markup = r'''                <p style="color: #334155; line-height: 1.65; margin-bottom: 1.25rem;">
                    <strong>Read from right to left:</strong> Although $g$ is written on the left, $f$ acts on $x$ first. Think of $(g \circ f)(x)$ as saying: <em>"evaluate $f(x)$ first, then pass that output into $g$."</em>
                </p>

                <!-- FUNCTION COMPOSITION PIPELINE DIAGRAM -->
                <div style="background: #f8fafc; border: 1px solid var(--border); border-radius: 6px; padding: 1.25rem; margin: 1.25rem 0 1.75rem 0; text-align: center;">
                    <p style="font-size: 0.85rem; font-weight: 700; color: #64748b; margin-top: 0; margin-bottom: 0.75rem;">VISUALIZATION: The Composition Pipeline ($X \xrightarrow{f} Y \xrightarrow{g} Z$)</p>
                    <svg viewBox="0 0 720 220" style="width: 100%; max-width: 680px; height: auto; display: inline-block;">
                        <defs>
                            <!-- Arrowhead Markers -->
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
                </div>'''

    if target_anchor in content:
        if "VISUALIZATION: The Composition Pipeline" in content:
            print("Pipeline diagram is already present in week1-lecture1.html.")
            return

        content = content.replace(target_anchor, pipeline_diagram_markup, 1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully integrated the composition pipeline diagram into week1-lecture1.html.")
    else:
        print("Could not locate the target anchor in week1-lecture1.html.")

def sync_git_repository():
    commit_message = (
        "Add function composition pipeline diagram to Lecture 1\n\n"
        "Integrated an inline SVG pipeline diagram into Section 3.3 of\n"
        "week1-lecture1.html. Visually resolves the common stumbling block\n"
        "between the left-to-right reading order of (g ∘ f) and the\n"
        "right-to-left execution order x ↦ f(x) ↦ g(f(x))."
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
    insert_composition_pipeline_diagram()
    sync_git_repository()
