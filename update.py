#!/usr/bin/env python3
import os
import subprocess

def add_sin_graph_to_squeeze_example():
    filepath = 'week2.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Target the spot right after the first part of the Squeeze Theorem classic example
    target_snippet = '''                <p>Since $\\lim_{n\\to\\infty} \\left(-\\frac{1}{n}\\right) = 0$ and $\\lim_{n\\to\\infty} \\left(\\frac{1}{n}\\right) = 0$, the Squeeze Theorem forces our middle sequence to also converge:</p>
                <p style="text-align: center; margin-top: 0.75rem;">$$\\lim_{n\\to\\infty} \\frac{\\sin(n)}{n} = 0$$</p>'''

    # Replacement including the new SVG graph visualization for sin(n)/n convergence
    replacement_content = r'''                <p>Since $\lim_{n\to\infty} \left(-\frac{1}{n}\right) = 0$ and $\lim_{n\to\infty} \left(\frac{1}{n}\right) = 0$, the Squeeze Theorem forces our middle sequence to also converge:</p>
                <p style="text-align: center; margin-top: 0.75rem;">$$\lim_{n\to\infty} \frac{\sin(n)}{n} = 0$$</p>

                <!-- Embedded SVG Graph of sin(n) / n convergence -->
                <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 6px; padding: 1rem; margin-top: 1rem; margin-bottom: 1.25rem;">
                    <p style="font-size: 0.85rem; font-weight: 700; color: #64748b; margin-top: 0; margin-bottom: 0.5rem; text-align: center;">VISUALIZATION: Squeezing $\frac{\sin(n)}{n}$ between $-\frac{1}{n}$ and $\frac{1}{n}$ ($n = 1 \dots 30$)</p>
                    <svg viewBox="0 0 800 280" style="width: 100%; height: auto; display: block;">
                        <!-- Center Axis (L = 0) -->
                        <line x1="50" y1="140" x2="760" y2="140" stroke="#94a3b8" stroke-width="1.5"/>
                        <text x="710" y="130" font-size="11" font-weight="bold" fill="#64748b">L = 0</text>

                        <!-- Upper Bound Curve (1/n) -->
                        <path d="M 70,20 Q 200,90 350,120 T 730,136" fill="none" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4"/>
                        <text x="600" y="105" font-size="10" font-weight="bold" fill="#d97706">Upper Bound: +1/n</text>

                        <!-- Lower Bound Curve (-1/n) -->
                        <path d="M 70,260 Q 200,190 350,160 T 730,144" fill="none" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4"/>
                        <text x="600" y="175" font-size="10" font-weight="bold" fill="#d97706">Lower Bound: -1/n</text>

                        <!-- Oscillating Points for sin(n)/n (n = 1 to 30 mapped to x: 70 to 730) -->
                        <g>
                            <circle cx="92" cy="70" r="4.5" fill="#059669"/><circle cx="114" cy="185" r="4.5" fill="#059669"/>
                            <circle cx="136" cy="172" r="4.5" fill="#059669"/><circle cx="158" cy="115" r="4.5" fill="#059669"/>
                            <circle cx="180" cy="120" r="4.5" fill="#059669"/><circle cx="202" cy="160" r="4.5" fill="#059669"/>
                            <circle cx="224" cy="155" r="4.5" fill="#059669"/><circle cx="246" cy="130" r="4.5" fill="#059669"/>
                            <circle cx="268" cy="133" r="4.5" fill="#059669"/><circle cx="290" cy="148" r="4.5" fill="#059669"/>
                            <circle cx="312" cy="146" r="4.5" fill="#059669"/><circle cx="334" cy="138" r="4.5" fill="#059669"/>
                            <circle cx="356" cy="139" r="4.5" fill="#059669"/><circle cx="378" cy="143" r="4.5" fill="#059669"/>
                            <circle cx="400" cy="142" r="4.5" fill="#059669"/><circle cx="422" cy="139" r="4.5" fill="#059669"/>
                            <circle cx="444" cy="140" r="4.5" fill="#059669"/><circle cx="466" cy="141" r="4.5" fill="#059669"/>
                            <circle cx="488" cy="141" r="4.5" fill="#059669"/><circle cx="510" cy="140" r="4.5" fill="#059669"/>
                            <circle cx="532" cy="140" r="4.5" fill="#059669"/><circle cx="554" cy="140" r="4.5" fill="#059669"/>
                            <circle cx="576" cy="140" r="4.5" fill="#059669"/><circle cx="598" cy="140" r="4.5" fill="#059669"/>
                            <circle cx="620" cy="140" r="4.5" fill="#059669"/><circle cx="642" cy="140" r="4.5" fill="#059669"/>
                            <circle cx="664" cy="140" r="4.5" fill="#059669"/><circle cx="686" cy="140" r="4.5" fill="#059669"/>
                            <circle cx="708" cy="140" r="4.5" fill="#059669"/><circle cx="730" cy="140" r="4.5" fill="#059669"/>
                        </g>
                        <text x="70" y="275" font-size="10" fill="#64748b">n=1</text>
                        <text x="715" y="275" font-size="10" fill="#64748b">n=30</text>
                    </svg>
                </div>'''

    if target_snippet in content and 'VISUALIZATION: Squeezing' not in content:
        content = content.replace(target_snippet, replacement_content, 1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully added sin(n)/n convergence graph to week2.html.")
    else:
        print("Target snippet not found or graph already present.")

def execute_git_sync():
    commit_message = (
        "Add sin(n)/n convergence SVG graph to Squeeze Theorem classic example\n\n"
        "Inserted an inline SVG visualization showing how sin(n)/n is squeezed\n"
        "between -1/n and 1/n and converges to zero in week2.html."
    )
    commands = [
        ['git', 'add', 'week2.html', 'update.py'],
        ['git', 'commit', '-m', commit_message],
        ['git', 'push', 'origin', 'main']
    ]
    for cmd in commands:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(f"> {' '.join(cmd)}\n{result.stdout}{result.stderr}")

if __name__ == '__main__':
    add_sin_graph_to_squeeze_example()
    execute_git_sync()
