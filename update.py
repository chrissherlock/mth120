#!/usr/bin/env python3
import os
import re
import subprocess

def add_epsilon_labels_and_arrows():
    filepath = 'week2.html'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The updated renderGameSVG function containing the new labels and arrows
    new_function = r'''function renderGameSVG(eps, reqN, curN) {
            const svg = document.getElementById('game-plot');
            const originX = 90, originY = 130, maxXScale = 610;
            let svgContent = `<line x1="${originX}" y1="${originY}" x2="${originX + maxXScale}" y2="${originY}" stroke="#64748b" stroke-width="1.0"/><text x="${originX - 35}" y="${originY + 5}" font-family="sans-serif" font-size="12" font-weight="700" fill="#64748b">L=0</text><line x1="${originX}" y1="240" x2="${originX}" y2="25" stroke="#64748b" stroke-width="1.0"/><line x1="${originX}" y1="${originY}" x2="715" y2="${originY}" stroke="#64748b" stroke-width="1.0"/>`;
            if (eps === null) {
                svg.innerHTML = svgContent + `<text x="260" y="130" font-family="sans-serif" font-size="14" fill="#64748b">Select an &epsilon; budget above to illustrate the sample.</text>`;
                return;
            }
            const maxN = Math.max(14, reqN + 4);
            const scaleFactor = eps <= 0.05 ? 900 : (eps <= 0.1 ? 550 : 220);
            const topY = originY - (eps * scaleFactor), bottomY = originY + (eps * scaleFactor);
            svgContent += `<rect x="${originX}" y="${topY}" width="${maxXScale}" height="${bottomY - topY}" fill="#fef3c7" opacity="0.8"/><line x1="${originX}" y1="${topY}" x2="${originX + maxXScale}" y2="${topY}" stroke="#d97706" stroke-dasharray="4"/><line x1="${originX}" y1="${bottomY}" x2="${originX + maxXScale}" y2="${bottomY}" stroke="#d97706" stroke-dasharray="4"/>`;

            // --- NEW: L+eps and L-eps Labels with Arrows ---
            svgContent += `
                <!-- Top Arrow and Label -->
                <line x1="${originX - 15}" y1="${originY}" x2="${originX - 15}" y2="${topY + 2}" stroke="#d97706" stroke-width="1.5"/>
                <polygon points="${originX - 15},${topY} ${originX - 19},${topY + 6} ${originX - 11},${topY + 6}" fill="#d97706"/>
                <text x="${originX - 52}" y="${topY + 4}" font-family="sans-serif" font-size="11" font-weight="bold" fill="#d97706">L+&epsilon;</text>

                <!-- Bottom Arrow and Label -->
                <line x1="${originX - 15}" y1="${originY}" x2="${originX - 15}" y2="${bottomY - 2}" stroke="#d97706" stroke-width="1.5"/>
                <polygon points="${originX - 15},${bottomY} ${originX - 19},${bottomY - 6} ${originX - 11},${bottomY - 6}" fill="#d97706"/>
                <text x="${originX - 48}" y="${bottomY + 4}" font-family="sans-serif" font-size="11" font-weight="bold" fill="#d97706">L-&epsilon;</text>
            `;
            // -----------------------------------------------

            for (let n = 1; n <= curN; n++) {
                const val = 1 / n, cx = originX + (n * (maxXScale / maxN)), cy = originY - (val * scaleFactor);
                const inside = n > reqN;
                svgContent += `<circle cx="${cx}" cy="${cy}" r="${inside ? 7 : 5}" fill="${inside ? '#10b981' : '#d97706'}"/>`;
            }
            const thresholdX = originX + (reqN * (maxXScale / maxN));
            svgContent += `<line x1="${thresholdX}" y1="20" x2="${thresholdX}" y2="240" stroke="#ef4444" stroke-width="1.2" stroke-dasharray="4"/><text x="${thresholdX + 6}" y="32" font-family="sans-serif" font-size="11" font-weight="bold" fill="#ef4444">N = ${reqN}</text>`;
            svg.innerHTML = svgContent;
        }'''

    # Identify the old renderGameSVG function block to replace
    pattern = r'function renderGameSVG\(eps, reqN, curN\) \{[\s\S]*?svg\.innerHTML = svgContent;\n\s*\}'

    if re.search(pattern, content):
        # We pass lambda _: new_function to safely inject without regex evaluating backslashes or variables
        content = re.sub(pattern, lambda _: new_function, content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully added L+eps and L-eps labels and arrows to week2.html.")
    else:
        print("Could not locate renderGameSVG function in week2.html.")

def execute_git_sync():
    commit_message = (
        "Add L±ε region labels and arrows to Epsilon widget\n\n"
        "Updated the JavaScript SVG generation in week2.html to dynamically render\n"
        "L+ε and L-ε text labels alongside outward-pointing arrows, explicitly marking\n"
        "the upper and lower boundaries of the tolerance band."
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
    add_epsilon_labels_and_arrows()
    execute_git_sync()
