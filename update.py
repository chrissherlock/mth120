#!/usr/bin/env python3
import re
import sys

def inject_step1_svg(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: '{filepath}' not found.")
        sys.exit(1)

    # --- SVG 1: Making the Picks (Fixed Clipping with 2px downward shift & increased viewBox) ---
    svg1 = r"""
                <!-- VISUALIZATION: STEP 1 -->
                <div style="margin: 1.5rem 0 2.5rem 0; text-align: center; background:#ffffff; border-radius: 8px; border: 1px solid #cbd5e1; padding: 1.5rem; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 185" width="100%" style="font-family:system-ui, -apple-system, sans-serif;">
                        <style>
                            .box-text { font-size: 20px; font-weight: bold; fill: #0f172a; }
                            .small-text { font-size: 14px; fill: #64748b; }
                            .math { font-size: 22px; font-family: 'Times New Roman', Times, serif; fill: #0f172a; }
                        </style>
                        <!-- Pushed down 2px to prevent clipping the top stroke -->
                        <g transform="translate(160, 2)">
                            <rect x="0" y="0" width="60" height="60" rx="8" fill="#e0f2fe" stroke="#38bdf8" stroke-width="2"/>
                            <text x="30" y="36" text-anchor="middle" class="box-text">A</text>
                            <rect x="80" y="0" width="60" height="60" rx="8" fill="#e0f2fe" stroke="#38bdf8" stroke-width="2"/>
                            <text x="110" y="36" text-anchor="middle" class="box-text">B</text>
                            <rect x="160" y="0" width="60" height="60" rx="8" fill="#e0f2fe" stroke="#38bdf8" stroke-width="2"/>
                            <text x="190" y="36" text-anchor="middle" class="box-text">C</text>
                            <rect x="240" y="0" width="60" height="60" rx="8" fill="#e0f2fe" stroke="#38bdf8" stroke-width="2"/>
                            <text x="270" y="36" text-anchor="middle" class="box-text">D</text>
                            <rect x="320" y="0" width="60" height="60" rx="8" fill="#e0f2fe" stroke="#38bdf8" stroke-width="2"/>
                            <text x="350" y="36" text-anchor="middle" class="box-text">E</text>
                        </g>
                        <!-- Pushed down 2px to keep relative spacing -->
                        <g transform="translate(140, 102)">
                            <rect x="0" y="0" width="80" height="80" rx="8" fill="none" stroke="#cbd5e1" stroke-width="2" stroke-dasharray="4"/>
                            <text x="40" y="-10" text-anchor="middle" class="small-text">1st Pick</text>
                            <text x="40" y="45" text-anchor="middle" class="box-text" fill="#0369a1">5</text>
                            <text x="110" y="45" text-anchor="middle" class="math">×</text>

                            <rect x="140" y="0" width="80" height="80" rx="8" fill="none" stroke="#cbd5e1" stroke-width="2" stroke-dasharray="4"/>
                            <text x="180" y="-10" text-anchor="middle" class="small-text">2nd Pick</text>
                            <text x="180" y="45" text-anchor="middle" class="box-text" fill="#0369a1">4</text>
                            <text x="250" y="45" text-anchor="middle" class="math">×</text>

                            <rect x="280" y="0" width="80" height="80" rx="8" fill="none" stroke="#cbd5e1" stroke-width="2" stroke-dasharray="4"/>
                            <text x="320" y="-10" text-anchor="middle" class="small-text">3rd Pick</text>
                            <text x="320" y="45" text-anchor="middle" class="box-text" fill="#0369a1">3</text>

                            <text x="430" y="45" text-anchor="middle" class="math">= 60 ways</text>
                        </g>
                    </svg>
                </div>"""

    # Inject strictly after the Step 1 text paragraph
    content = re.sub(
        r'(Multiply those together: \$5 \\times 4 \\times 3 = 60\$ possible ways to pick 3 letters\.\s*</p>)',
        lambda m: m.group(1) + "\n" + svg1,
        content,
        count=1
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Successfully injected the Step 1 inline SVG into {filepath}.")

if __name__ == "__main__":
    inject_step1_svg("week2-lecture5.html")
