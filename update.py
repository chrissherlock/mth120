#!/usr/bin/env python3
import os
import subprocess

def add_density_stepper_widget():
    filepath = 'week1-lecture2.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # We will insert the interactive widget right after the midpoint explanation paragraph
    target_anchor = (
        '            <div style="text-align: center; margin: 1rem 0;">\n'
        '                $$a < c_3 < c_2 < c_1 < b$$\n'
        '            </div>'
    )

    widget_code = (
        '\n\n            <!-- INTERACTIVE RATIONAL DENSITY STEPPER -->\n'
        '            <div style="background: #f8fafc; border: 1px solid var(--border); border-radius: 8px; padding: 1.5rem; margin: 1.75rem 0; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">\n'
        '                <div style="display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; gap: 0.5rem; border-bottom: 1px solid #f1f5f9; padding-bottom: 0.75rem; margin-bottom: 1rem;">\n'
        '                    <h3 style="margin: 0; color: #0f172a; font-size: 1.1rem;">Interactive Walkthrough: The Infinite Midpoint Nesting</h3>\n'
        '                    <span id="density-telemetry" style="font-weight: 600; color: var(--accent); font-size: 0.88rem; background: #fffbeb; padding: 0.2rem 0.6rem; border-radius: 4px; border: 1px solid #fde68a;">Phase: Initial Interval [0.3, 0.4]</span>\n'
        '                </div>\n\n'
        '                <!-- SVG VISUAL CANVAS -->\n'
        '                <div style="background: #ffffff; border: 1px solid var(--border); border-radius: 6px; padding: 1rem; text-align: center; margin-bottom: 1.25rem;">\n'
        '                    <svg id="density-svg" viewBox="0 0 700 130" style="width: 100%; max-width: 660px; height: auto; display: inline-block;">\n'
        '                        <!-- Main Number Line Axis -->\n'
        '                        <line x1="50" y1="75" x2="650" y2="75" stroke="#0f172a" stroke-width="2.5"/>\n'
        '                        <!-- Ticks for 0.3 and 0.4 -->\n'
        '                        <line x1="100" y1="65" x2="100" y2="85" stroke="#0f172a" stroke-width="2"/>\n'
        '                        <line x1="600" y1="65" x2="600" y2="85" stroke="#0f172a" stroke-width="2"/>\n'
        '                        <text x="100" y="105" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">a = 0.3</text>\n'
        '                        <text x="600" y="105" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">b = 0.4</text>\n\n'
        '                        <!-- Dynamic Midpoint Markers -->\n'
        '                        <g id="marker-c1" style="display: none;">\n'
        '                            <line x1="350" y1="50" x2="350" y2="100" stroke="#d97706" stroke-width="2" stroke-dasharray="3"/>\n'
        '                            <circle cx="350" cy="75" r="6" fill="#d97706"/>\n'
        '                            <text x="350" y="38" font-family="sans-serif" font-size="11.5" font-weight="bold" fill="#b45309" text-anchor="middle">c₁ = 0.35</text>\n'
        '                        </g>\n'
        '                        <g id="marker-c2" style="display: none;">\n'
        '                            <line x1="225" y1="50" x2="225" y2="100" stroke="#0284c7" stroke-width="2" stroke-dasharray="3"/>\n'
        '                            <circle cx="225" cy="75" r="6" fill="#0284c7"/>\n'
        '                            <text x="225" y="38" font-family="sans-serif" font-size="11.5" font-weight="bold" fill="#0369a1" text-anchor="middle">c₂ = 0.325</text>\n'
        '                        </g>\n'
        '                        <g id="marker-c3" style="display: none;">\n'
        '                            <line x1="162.5" y1="50" x2="162.5" y2="100" stroke="#10b981" stroke-width="2" stroke-dasharray="3"/>\n'
        '                            <circle cx="162.5" cy="75" r="6" fill="#10b981"/>\n'
        '                            <text x="162.5" y="38" font-family="sans-serif" font-size="11.5" font-weight="bold" fill="#047857" text-anchor="middle">c₃ = 0.3125</text>\n'
        '                        </g>\n'
        '                    </svg>\n'
        '                </div>\n\n'
        '                <!-- NAVIGATION CONTROLS -->\n'
        '                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.25rem; flex-wrap: wrap; gap: 0.75rem;">\n'
        '                    <div style="display: flex; gap: 0.5rem;">\n'
        '                        <button onclick="densityPrev()" id="density-prev-btn" style="background: #e2e8f0; color: #475569; border: none; padding: 0.45rem 1rem; border-radius: 4px; font-weight: 600; cursor: pointer; font-size: 0.9rem;" disabled>&larr; Previous</button>\n'
        '                        <button onclick="densityNext()" id="density-next-btn" style="background: var(--accent); color: white; border: none; padding: 0.45rem 1rem; border-radius: 4px; font-weight: 600; cursor: pointer; font-size: 0.9rem;">Next Step &rarr;</button>\n'
        '                    </div>\n'
        '                    <button onclick="densityReset()" style="background: transparent; color: #64748b; border: 1px solid var(--border); padding: 0.45rem 0.85rem; border-radius: 4px; font-weight: 500; cursor: pointer; font-size: 0.85rem;">Reset View</button>\n'
        '                </div>\n\n'
        '                <!-- PAIRED ANALYTICAL PANES -->\n'
        '                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem;">\n'
        '                    <div style="background: #ffffff; border: 1px solid var(--border); border-radius: 6px; padding: 1rem; border-left: 3px solid #0284c7;">\n'
        '                        <h4 style="margin: 0 0 0.4rem 0; color: #0369a1; font-size: 0.95rem;">1. What Is Happening</h4>\n'
        '                        <p id="pane-what" style="margin: 0; font-size: 0.9rem; color: #334155; line-height: 1.5;">\n'
        '                            We start with interval $[0.3, 0.4]$. No fractions are plotted yet. The line appears continuous, but infinitely many rational points are waiting between the endpoints.\n'
        '                        </p>\n'
        '                    </div>\n'
        '                    <div style="background: #ffffff; border: 1px solid var(--border); border-radius: 6px; padding: 1rem; border-left: 3px solid #d97706;">\n'
        '                        <h4 style="margin: 0 0 0.4rem 0; color: #92400e; font-size: 0.95rem;">2. Why The System Does This</h4>\n'
        '                        <p id="pane-why" style="margin: 0; font-size: 0.9rem; color: #334155; line-height: 1.5;">\n'
        '                            Demonstrating closure under division: any arithmetic average of two rationals is strictly guaranteed to generate a brand new, valid rational number.\n'
        '                        </p>\n'
        '                    </div>\n'
        '                </div>\n'
        '            </div>\n\n'
        '            <!-- STEPPER JAVASCRIPT -->\n'
        '            <script>\n'
        '                let densityStep = 0;\n'
        '                function updateDensityWidget() {\n'
        '                    const markerC1 = document.getElementById("marker-c1");\n'
        '                    const markerC2 = document.getElementById("marker-c2");\n'
        '                    const markerC3 = document.getElementById("marker-c3");\n'
        '                    const prevBtn = document.getElementById("density-prev-btn");\n'
        '                    const nextBtn = document.getElementById("density-next-btn");\n'
        '                    const telemetry = document.getElementById("density-telemetry");\n'
        '                    const paneWhat = document.getElementById("pane-what");\n'
        '                    const paneWhy = document.getElementById("pane-why");\n\n'
        '                    markerC1.style.display = densityStep >= 1 ? "block" : "none";\n'
        '                    markerC2.style.display = densityStep >= 2 ? "block" : "none";\n'
        '                    markerC3.style.display = densityStep >= 3 ? "block" : "none";\n'
        '                    prevBtn.disabled = densityStep === 0;\n'
        '                    nextBtn.disabled = densityStep === 3;\n'
        '                    nextBtn.style.opacity = densityStep === 3 ? "0.5" : "1";\n\n'
        '                    if (densityStep === 0) {\n'
        '                        telemetry.innerText = "Phase: Initial Interval [0.3, 0.4]";\n'
        '                        paneWhat.innerText = "We start with interval [0.3, 0.4]. No fractions are plotted yet. The line appears solid, but infinitely many rational points are waiting between the endpoints.";\n'
        '                        paneWhy.innerText = "Demonstrating closure under division: any arithmetic average of two rationals is strictly guaranteed to generate a brand new, valid rational number.";\n'
        '                    } else if (densityStep === 1) {\n'
        '                        telemetry.innerText = "Phase: Step 1 (First Midpoint)";\n'
        '                        paneWhat.innerText = "Calculated first midpoint: c₁ = (0.3 + 0.4) / 2 = 0.35. A new rational marker is dropped exactly halfway between a and b.";\n'
        '                        paneWhy.innerText = "Even though we inserted a point, we haven\'t filled the gap; we now have two smaller sub-intervals, each containing infinitely more fractions.";\n'
        '                    } else if (densityStep === 2) {\n'
        '                        telemetry.innerText = "Phase: Step 2 (Zooming In)";\n'
        '                        paneWhat.innerText = "Calculated second midpoint on the left interval: c₂ = (0.3 + 0.35) / 2 = 0.325. Notice how densely points are beginning to cluster near 0.3.";\n'
        '                        paneWhy.innerText = "The midpoint construction is recursive. You can repeat this division infinitely without ever running out of fresh rational numbers.";\n'
        '                    } else if (densityStep === 3) {\n'
        '                        telemetry.innerText = "Phase: Step 3 (Infinite Nesting)";\n'
        '                        paneWhat.innerText = "Calculated third midpoint: c₃ = (0.3 + 0.325) / 2 = 0.3125. The sequence accumulates towards 0.3 from the right.";\n'
        '                        paneWhy.innerText = "This infinite nesting proves density, yet microscopic pinprick holes (like irrational numbers) still remain unplotted between these markers!";\n'
        '                    }\n'
        '                }\n'
        '                function densityNext() { if (densityStep < 3) { densityStep++; updateDensityWidget(); } }\n'
        '                function densityPrev() { if (densityStep > 0) { densityStep--; updateDensityWidget(); } }\n'
        '                function densityReset() { densityStep = 0; updateDensityWidget(); }\n'
        '            </script>'
    )

    if target_anchor in content:
        content = content.replace(target_anchor, target_anchor + widget_code, 1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully added interactive rational density stepper widget to week1-lecture2.html.")
        return True

    print("Error: Could not locate target anchor in week1-lecture2.html.")
    return False

def synchronize_git_changes():
    commit_message = """Add interactive rational density stepper widget to week1-lecture2.html

Embedded an interactive SVG step-through widget in week1-lecture2.html to
illustrate the midpoint construction (c1, c2, c3) dynamically, complete with
live state telemetry and paired analytical explanation panes."""
    commands = [
        ['git', 'add', 'week1-lecture2.html', 'update.py'],
        ['git', 'commit', '-m', commit_message],
        ['git', 'push', 'origin', 'main']
    ]
    for cmd in commands:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(f"> {' '.join(cmd)}\n{result.stdout}{result.stderr}")

if __name__ == '__main__':
    if add_density_stepper_widget():
        synchronize_git_changes()
