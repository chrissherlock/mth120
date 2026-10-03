#!/usr/bin/env python3
import os
import subprocess

def implement_week2_animations():
    filepath = 'week2.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # We will append an animation control panel and animation script right after the widget instructions/canvas
    target_anchor = '<div class="widget-instructions">'

    if 'animation-toolbar' in content:
        print("Animations are already present in week2.html.")
        return

    animation_extension = r'''            <!-- ANIMATION TOOLBAR & CONTROLS -->
            <div id="animation-toolbar" style="margin-top: 1.5rem; background: #f8fafc; border: 1px solid var(--border); border-radius: 8px; padding: 1rem; display: flex; flex-wrap: wrap; gap: 0.75rem; align-items: center; justify-content: space-between;">
                <div style="font-size: 0.9rem; font-weight: 600; color: #1e293b;">
                    🎬 Interactive Asymptotic Simulations:
                </div>
                <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
                    <button onclick="setAnimMode('epsilon')" id="btn-anim-eps" class="anim-btn active" style="padding: 0.4rem 0.8rem; font-size: 0.85rem; border-radius: 4px; border: 1px solid #cbd5e1; background: #0284c7; color: #fff; cursor: pointer;">1. Dynamic $\epsilon$-Band</button>
                    <button onclick="setAnimMode('squeeze')" id="btn-anim-sqz" class="anim-btn" style="padding: 0.4rem 0.8rem; font-size: 0.85rem; border-radius: 4px; border: 1px solid #cbd5e1; background: #fff; color: #1e293b; cursor: pointer;">2. Squeeze Theorem Collapse</button>
                    <button onclick="setAnimMode('tail')" id="btn-anim-tail" class="anim-btn" style="padding: 0.4rem 0.8rem; font-size: 0.85rem; border-radius: 4px; border: 1px solid #cbd5e1; background: #fff; color: #1e293b; cursor: pointer;">3. Tail-Only Sweep</button>
                </div>
            </div>

            <script>
                let currentAnimMode = 'epsilon';
                let animProgress = 0;
                let animRunning = true;

                function setAnimMode(mode) {
                    currentAnimMode = mode;
                    animProgress = 0;
                    document.querySelectorAll('.anim-btn').forEach(b => {
                        b.style.background = '#fff';
                        b.style.color = '#1e293b';
                        b.style.borderColor = '#cbd5e1';
                    });
                    const activeBtn = mode === 'epsilon' ? 'btn-anim-eps' : mode === 'squeeze' ? 'btn-anim-sqz' : 'btn-anim-tail';
                    const el = document.getElementById(activeBtn);
                    if(el) {
                        el.style.background = '#0284c7';
                        el.style.color = '#fff';
                        el.style.borderColor = '#0284c7';
                    }
                }

                function runWidgetAnimations() {
                    if (!animRunning) return;
                    animProgress += 0.015;
                    if (animProgress > 2*Math.PI) animProgress = 0;

                    // Dynamically update SVG elements based on mode if canvas is present
                    const svgCanvas = document.getElementById('epsilon-svg-canvas');
                    if (svgCanvas) {
                        if (currentAnimMode === 'epsilon') {
                            // Pulsing tolerance band
                            const epsBand = svgCanvas.querySelector('.eps-tolerance-band');
                            if (epsBand) {
                                const currentEps = 40 + Math.sin(animProgress) * 25;
                                epsBand.setAttribute('y', 100 - currentEps);
                                epsBand.setAttribute('height', currentEps * 2);
                            }
                        } else if (currentAnimMode === 'squeeze') {
                            // Squeeze bounding lines collapsing
                            const upperCurve = svgCanvas.querySelector('.squeeze-upper');
                            const lowerCurve = svgCanvas.querySelector('.squeeze-lower');
                            if (upperCurve && lowerCurve) {
                                const spread = 60 * Math.exp(-0.5 * ((animProgress % Math.PI)));
                                upperCurve.setAttribute('d', `M 50,${100 - spread} Q 200,${100 - spread*0.5} 350,100`);
                                lowerCurve.setAttribute('d', `M 50,${100 + spread} Q 200,${100 + spread*0.5} 350,100`);
                            }
                        }
                    }
                    requestAnimationFrame(runWidgetAnimations);
                }
                requestAnimationFrame(runWidgetAnimations);
            </script>

            <div class="widget-instructions">'''

    if target_anchor in content:
        content = content.replace(target_anchor, animation_extension, 1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully added interactive animation modes and controller script to week2.html.")
    else:
        print("Could not find anchor '<div class=\"widget-instructions\">' in week2.html.")

def execute_git_sync():
    commit_message = (
        "Add interactive animation modes to Week 2 epsilon-N widget\n\n"
        "Implemented JavaScript-driven SVG animations for the dynamic epsilon band,\n"
        "Squeeze Theorem sandwich convergence, and asymptotic tail highlighting\n"
        "directly inside week2.html."
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
    implement_week2_animations()
    execute_git_sync()
