#!/usr/bin/env python3
import os
import subprocess

def update_rational_gaps_section():
    filepath = 'week1-lecture2.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Old Section 2 block to replace
    old_section_2 = (
        '            <!-- SECTION 2 -->\n'
        '            <h2 id="rational-gaps">2. Rational Gaps and the Irrationality of $\\sqrt{2}$</h2>\n'
        '            <p>Even though fractions are infinitely dense, the rational line is filled with holes. Consider a right triangle with unit legs ($1$ and $1$). By Pythagoras\' theorem, the hypotenuse $c$ satisfies $c^2 = 1^2 + 1^2 = 2 \\implies c = \\sqrt{2}$.</p>\n\n'
        '            <div class="worked-example-box">\n'
        '                <h4>🎯 Why $\\sqrt{2}$ isn\'t a fraction (Proof by Contradiction)</h4>\n'
        '                <p style="margin-bottom: 0.5rem;">Assume $\\sqrt{2}$ <em>could</em> be written as a simplified rational fraction $\\frac{p}{q}$ for integers $p, q$ with $q \\neq 0$. Squaring both sides yields:</p>\n'
        '                <div style="text-align: center; margin: 0.5rem 0;">\n'
        '                    $$\\frac{p^2}{q^2} = 2 \\implies p^2 = 2q^2$$\n'
        '                </div>\n'
        '                <p style="margin-bottom: 0.5rem;">\n'
        '                    By the Fundamental Theorem of Arithmetic, every integer has a unique prime factorisation. When you square any number, all prime factor exponents double, meaning every perfect square must contain an <strong>even number of prime factors</strong> (counting multiplicities).\n'
        '                </p>\n'
        '                <p style="margin-bottom: 0;">\n'
        '                    Therefore, $p^2$ contains an <strong>even</strong> number of prime factors. Meanwhile, $2q^2$ takes $q^2$ (which has an even number of factors) and multiplies it by one additional 2, giving it an <strong>odd</strong> number of prime factors. An even number cannot equal an odd number! Hence $p^2 = 2q^2$ is impossible, proving that $\\sqrt{2} \\notin \\mathbb{Q}$.\n'
        '                </p>\n'
        '            </div>'
    )

    # Enhanced Section 2 block with beginner narrative and interactive gap widget
    new_section_2 = (
        '            <!-- SECTION 2 -->\n'
        '            <h2 id="rational-gaps">2. Rational Gaps and the Irrationality of $\\sqrt{2}$</h2>\n'
        '            <p style="font-size: 1.02rem; line-height: 1.7; color: #334155;">\n'
        '                In Section 1, we saw that the rational numbers ($\\mathbb{Q}$) are dense&mdash;you can always squeeze another fraction between any two. It is tempting to look at that infinite crowding and assume the number line is completely solid. But ancient Greek mathematicians discovered a shocking geometric reality that shattered this illusion.\n'
        '            </p>\n'
        '            <p style="font-size: 1.02rem; line-height: 1.7; color: #334155;">\n'
        '                Imagine drawing a simple right-angled triangle with both legs measuring exactly $1$ unit. By Pythagoras\' theorem, the length of the diagonal hypotenuse $c$ is given by $c^2 = 1^2 + 1^2 = 2$, which means $c = \\sqrt{2}$. Where does this length live on our rational number line? <strong>Nowhere!</strong> Exactly where $\\sqrt{2}$ belongs, there is an invisible pinprick hole.\n'
        '            </p>\n\n'
        '            <!-- INTERACTIVE RATIONAL GAP STEPPER -->\n'
        '            <div style="background: #f8fafc; border: 1px solid var(--border); border-radius: 8px; padding: 1.5rem; margin: 1.75rem 0; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">\n'
        '                <div style="display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; gap: 0.5rem; border-bottom: 1px solid #f1f5f9; padding-bottom: 0.75rem; margin-bottom: 1rem;">\n'
        '                    <h3 style="margin: 0; color: #0f172a; font-size: 1.1rem;">Interactive Walkthrough: Approaching the Void ($\\sqrt{2}$)</h3>\n'
        '                    <span id="gap-telemetry" style="font-weight: 600; color: #047857; font-size: 0.88rem; background: #f0fdf4; padding: 0.2rem 0.6rem; border-radius: 4px; border: 1px solid #bbf7d0;">Phase: Initial Decimal Bounds</span>\n'
        '                </div>\n\n'
        '                <!-- SVG GAP VISUAL CANVAS -->\n'
        '                <div style="background: #ffffff; border: 1px solid var(--border); border-radius: 6px; padding: 1rem; text-align: center; margin-bottom: 1.25rem;">\n'
        '                    <svg id="gap-svg" viewBox="0 0 700 130" style="width: 100%; max-width: 660px; height: auto; display: inline-block;">\n'
        '                        <!-- Main Number Line Axis -->\n'
        '                        <line x1="50" y1="75" x2="650" y2="75" stroke="#0f172a" stroke-width="2.5"/>\n'
        '                        <!-- Ticks for 1.4 and 1.5 -->\n'
        '                        <line x1="150" y1="65" x2="150" y2="85" stroke="#0f172a" stroke-width="2"/>\n'
        '                        <line x1="550" y1="65" x2="550" y2="85" stroke="#0f172a" stroke-width="2"/>\n'
        '                        <text x="150" y="105" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">1.4</text>\n'
        '                        <text x="550" y="105" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">1.5</text>\n\n'
        '                        <!-- Target √2 Hole Marker (Always visible as a dashed target) -->\n'
        '                        <line x1="350" y1="40" x2="350" y2="110" stroke="#ef4444" stroke-width="2" stroke-dasharray="4"/>\n'
        '                        <text x="350" y="28" font-family="sans-serif" font-size="11" font-weight="bold" fill="#dc2626" text-anchor="middle">Missing Hole (√2)</text>\n\n'
        '                        <!-- Dynamic Approximation Markers -->\n'
        '                        <g id="gap-m1" style="display: none;">\n'
        '                            <circle cx="340" cy="75" r="5.5" fill="#10b981"/>\n'
        '                            <text x="340" y="58" font-family="sans-serif" font-size="10.5" font-weight="bold" fill="#047857" text-anchor="middle">1.41</text>\n'
        '                        </g>\n'
        '                        <g id="gap-m2" style="display: none;">\n'
        '                            <circle cx="348" cy="75" r="5.5" fill="#10b981"/>\n'
        '                            <text x="355" y="58" font-family="sans-serif" font-size="10.5" font-weight="bold" fill="#047857" text-anchor="start">1.414</text>\n'
        '                        </g>\n'
        '                        <g id="gap-m3" style="display: none;">\n'
        '                            <circle cx="349.5" cy="75" r="5.5" fill="#10b981"/>\n'
        '                            <text x="358" y="92" font-family="sans-serif" font-size="10.5" font-weight="bold" fill="#047857" text-anchor="start">1.41421...</text>\n'
        '                        </g>\n'
        '                    </svg>\n'
        '                </div>\n\n'
        '                <!-- NAVIGATION CONTROLS -->\n'
        '                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.25rem; flex-wrap: wrap; gap: 0.75rem;">\n'
        '                    <div style="display: flex; gap: 0.5rem;">\n'
        '                        <button onclick="gapPrev()" id="gap-prev-btn" style="background: #e2e8f0; color: #475569; border: none; padding: 0.45rem 1rem; border-radius: 4px; font-weight: 600; cursor: pointer; font-size: 0.9rem;" disabled>&larr; Previous</button>\n'
        '                        <button onclick="gapNext()" id="gap-next-btn" style="background: #10b981; color: white; border: none; padding: 0.45rem 1rem; border-radius: 4px; font-weight: 600; cursor: pointer; font-size: 0.9rem;">Zoom Closer &rarr;</button>\n'
        '                    </div>\n'
        '                    <button onclick="gapReset()" style="background: transparent; color: #64748b; border: 1px solid var(--border); padding: 0.45rem 0.85rem; border-radius: 4px; font-weight: 500; cursor: pointer; font-size: 0.85rem;">Reset View</button>\n'
        '                </div>\n\n'
        '                <!-- PAIRED ANALYTICAL PANES -->\n'
        '                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem;">\n'
        '                    <div style="background: #ffffff; border: 1px solid var(--border); border-radius: 6px; padding: 1rem; border-left: 3px solid #10b981;">\n'
        '                        <h4 style="margin: 0 0 0.4rem 0; color: #047857; font-size: 0.95rem;">1. What Is Happening</h4>\n'
        '                        <p id="gap-pane-what" style="margin: 0; font-size: 0.9rem; color: #334155; line-height: 1.5;">\n'
        '                            We know $\\sqrt{2}$ sits between $1.4$ and $1.5$. Fractions can get arbitrarily close to the target hole without ever hitting it.\n'
        '                        </p>\n'
        '                    </div>\n'
        '                    <div style="background: #ffffff; border: 1px solid var(--border); border-radius: 6px; padding: 1rem; border-left: 3px solid #d97706;">\n'
        '                        <h4 style="margin: 0 0 0.4rem 0; color: #92400e; font-size: 0.95rem;">2. Why The System Does This</h4>\n'
        '                        <p id="gap-pane-why" style="margin: 0; font-size: 0.9rem; color: #334155; line-height: 1.5;">\n'
        '                            Demonstrating the limit defect of $\\mathbb{Q}$: infinite rational approximations converge on a point that doesn\'t actually exist within the rational universe.\n'
        '                        </p>\n'
        '                    </div>\n'
        '                </div>\n'
        '            </div>\n\n'
        '            <!-- STEPPER JAVASCRIPT -->\n'
        '            <script>\n'
        '                let gapStep = 0;\n'
        '                function updateGapWidget() {\n'
        '                    const markerM1 = document.getElementById("gap-m1");\n'
        '                    const markerM2 = document.getElementById("gap-m2");\n'
        '                    const markerM3 = document.getElementById("gap-m3");\n'
        '                    const prevBtn = document.getElementById("gap-prev-btn");\n'
        '                    const nextBtn = document.getElementById("gap-next-btn");\n'
        '                    const telemetry = document.getElementById("gap-telemetry");\n'
        '                    const paneWhat = document.getElementById("gap-pane-what");\n'
        '                    const paneWhy = document.getElementById("gap-pane-why");\n\n'
        '                    markerM1.style.display = gapStep >= 1 ? "block" : "none";\n'
        '                    markerM2.style.display = gapStep >= 2 ? "block" : "none";\n'
        '                    markerM3.style.display = gapStep >= 3 ? "block" : "none";\n'
        '                    prevBtn.disabled = gapStep === 0;\n'
        '                    nextBtn.disabled = gapStep === 3;\n'
        '                    nextBtn.style.opacity = gapStep === 3 ? "0.5" : "1";\n\n'
        '                    if (gapStep === 0) {\n'
        '                        telemetry.innerText = "Phase: Initial Decimal Bounds";\n'
        '                        paneWhat.innerText = "We know √2 sits between 1.4 and 1.5. Fractions can get arbitrarily close to the target hole without ever hitting it.";\n'
        '                        paneWhy.innerText = "Demonstrating the limit defect of Q: infinite rational approximations converge on a point that doesn\'t actually exist within the rational universe.";\n'
        '                    } else if (gapStep === 1) {\n'
        '                        telemetry.innerText = "Phase: Approximation 1.41";\n'
        '                        paneWhat.innerText = "We test 1.41 (or 141/100). Since 1.41² = 1.9881 < 2, we are just under the target hole.";\n'
        '                        paneWhy.innerText = "Rational fractions can creep infinitely close from below, but squaring any fraction will never yield exactly 2.";\n'
        '                    } else if (gapStep === 2) {\n'
        '                        telemetry.innerText = "Phase: Approximation 1.414";\n'
        '                        paneWhat.innerText = "We refine further to 1.414 (1414/1000). 1.414² = 1.999396. We are practically touching the hole, yet still strictly rational.";\n'
        '                        paneWhy.innerText = "This infinite sequence of decimals proves that Q has no 'plug' for this hole. We need a larger number system (R) to fill it.";\n'
        '                    } else if (gapStep === 3) {\n'
        '                        telemetry.innerText = "Phase: The Missing Limit";\n'
        '                        paneWhat.innerText = "The sequence 1.4, 1.41, 1.414, 1.41421... marches endlessly toward the red dashed line without ever landing on a valid fraction.";\n'
        '                        paneWhy.innerText = "This foundational gap is precisely why real analysis requires the Axiom of Completeness!";\n'
        '                    }\n'
        '                }\n'
        '                function gapNext() { if (gapStep < 3) { gapStep++; updateGapWidget(); } }\n'
        '                function gapPrev() { if (gapStep > 0) { gapStep--; updateGapWidget(); } }\n'
        '                function gapReset() { gapStep = 0; updateGapWidget(); }\n'
        '            </script>\n\n'
        '            <div class="worked-example-box">\n'
        '                <h4>🎯 Why $\\sqrt{2}$ isn\'t a fraction (Proof by Contradiction)</h4>\n'
        '                <p style="margin-bottom: 0.5rem;">To prove mathematically that no fraction can ever plug this hole, we use a classic <strong>proof by contradiction</strong>. We start by assuming the exact opposite of what we want to prove:</p>\n'
        '                <p style="margin-bottom: 0.5rem;">\n'
        '                    Assume $\\sqrt{2}$ <em>could</em> be written as a simplified fraction $\\frac{p}{q}$ for integers $p$ and $q$ (with $q \\neq 0$ and no common factors). Squaring both sides gives:\n'
        '                </p>\n'
        '                <div style="text-align: center; margin: 0.5rem 0;">\n'
        '                    $$\\frac{p^2}{q^2} = 2 \\implies p^2 = 2q^2$$\n'
        '                </div>\n'
        '                <p style="margin-bottom: 0.5rem;">\n'
        '                    Think about prime factorizations. When you square any whole number, all its prime factors double in count, meaning <strong>every perfect square must contain an even number of prime factors</strong> (counting multiplicities).\n'
        '                </p>\n'
        '                <p style="margin-bottom: 0;">\n'
        '                    Therefore, $p^2$ has an <strong>even</strong> number of prime factors. But look at $2q^2$: $q^2$ has an even number, and multiplying by one extra $2$ makes it an <strong>odd</strong> number! An even number can never equal an odd number ($2n \neq 2k+1$). This inescapable contradiction proves that our starting assumption was false: $\\sqrt{2}$ <strong>cannot</strong> be a fraction ($\\sqrt{2} \\notin \\mathbb{Q}$). Rounds out the hole permanently!\n'
        '                </p>\n'
        '            </div>'
    )

    if old_section_2 in content:
        content = content.replace(old_section_2, new_section_2, 1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully updated Section 2 in week1-lecture2.html with beginner-friendly narrative and gap widget.")
        return True

    print("Error: Could not locate exact Section 2 match in week1-lecture2.html.")
    return False

def synchronize_git_changes():
    commit_message = """Enhance Section 2 with gap visualization widget in week1-lecture2.html

Rewrote Section 2 of week1-lecture2.html to feature an interactive SVG step-through
widget illustrating how rational decimal approximations approach the 'missing hole'
of sqrt(2), paired with an intuitive prime-factorization proof by contradiction."""
    commands = [
        ['git', 'add', 'week1-lecture2.html', 'update.py'],
        ['git', 'commit', '-m', commit_message],
        ['git', 'push', 'origin', 'main']
    ]
    for cmd in commands:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(f"> {' '.join(cmd)}\n{result.stdout}{result.stderr}")

if __name__ == '__main__':
    if update_rational_gaps_section():
        synchronize_git_changes()
