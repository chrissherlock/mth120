#!/usr/bin/env python3
import re
import sys

def build_full_network_svg():
    items = ['A', 'B', 'C', 'D', 'E']
    colors = ['#0284c7', '#16a34a', '#d97706', '#9333ea', '#e11d48']

    y_offset = 120
    y_spacing = 22

    x_start = 60
    x_L1 = 200
    x_L2 = 450
    x_L3 = 700
    x_L4 = 820

    paths = []
    nodes = []

    # Start node calculation
    y_start = y_offset + (59 / 2.0) * y_spacing

    nodes.append(f'<circle cx="{x_start}" cy="{y_start}" r="8" fill="#0f172a" />')
    nodes.append(f'<text x="{x_start-15}" y="{y_start+5}" text-anchor="end" font-size="16" font-weight="bold" fill="#0f172a">Start</text>')

    l3_idx = 0
    # Level 1: 5 choices
    for i, a in enumerate(items):
        color = colors[i]
        y_L1 = y_offset + (i * 12 + 5.5) * y_spacing

        paths.append(f'<path d="M {x_start+8} {y_start} C {(x_start+x_L1)//2} {y_start}, {(x_start+x_L1)//2} {y_L1}, {x_L1-15} {y_L1}" fill="none" stroke="{color}" stroke-width="3" opacity="0.8" />')

        nodes.append(f'<circle cx="{x_L1}" cy="{y_L1}" r="16" fill="{color}" />')
        nodes.append(f'<text x="{x_L1}" y="{y_L1+5}" text-anchor="middle" font-size="16" font-weight="bold" fill="#ffffff">{a}</text>')

        rem_L2 = [x for x in items if x != a]
        # Level 2: 4 branches each
        for j, b in enumerate(rem_L2):
            l2_idx = i * 4 + j
            y_L2 = y_offset + (l2_idx * 3 + 1) * y_spacing

            paths.append(f'<path d="M {x_L1+16} {y_L1} C {(x_L1+x_L2)//2} {y_L1}, {(x_L1+x_L2)//2} {y_L2}, {x_L2-14} {y_L2}" fill="none" stroke="{color}" stroke-width="2" opacity="0.6" />')

            nodes.append(f'<circle cx="{x_L2}" cy="{y_L2}" r="14" fill="#ffffff" stroke="{color}" stroke-width="2" />')
            nodes.append(f'<text x="{x_L2}" y="{y_L2+5}" text-anchor="middle" font-size="14" font-weight="bold" fill="#334155">{b}</text>')

            rem_L3 = [x for x in rem_L2 if x != b]
            # Level 3: 3 branches each
            for k, c in enumerate(rem_L3):
                y_L3 = y_offset + l3_idx * y_spacing

                paths.append(f'<path d="M {x_L2+14} {y_L2} C {(x_L2+x_L3)//2} {y_L2}, {(x_L2+x_L3)//2} {y_L3}, {x_L3-12} {y_L3}" fill="none" stroke="{color}" stroke-width="1.5" opacity="0.4" />')

                nodes.append(f'<circle cx="{x_L3}" cy="{y_L3}" r="12" fill="#f8fafc" stroke="{color}" stroke-width="1.5" />')
                nodes.append(f'<text x="{x_L3}" y="{y_L3+4}" text-anchor="middle" font-size="12" font-weight="bold" fill="#475569">{c}</text>')

                # Terminal Result Block
                nodes.append(f'<rect x="{x_L4}" y="{y_L3-10}" width="40" height="20" rx="4" fill="{color}" opacity="0.1" />')
                nodes.append(f'<text x="{x_L4+20}" y="{y_L3+4}" text-anchor="middle" font-size="13" font-family="monospace" font-weight="bold" fill="{color}">{a}{b}{c}</text>')

                l3_idx += 1

    # Headers
    header_y = 60
    nodes.append(f'<text x="{x_L1}" y="{header_y}" text-anchor="middle" font-size="18" font-weight="bold" fill="#0f172a">1st Pick (5 options)</text>')
    nodes.append(f'<text x="{x_L2}" y="{header_y}" text-anchor="middle" font-size="18" font-weight="bold" fill="#0f172a">2nd Pick (4 options)</text>')
    nodes.append(f'<text x="{x_L3}" y="{header_y}" text-anchor="middle" font-size="18" font-weight="bold" fill="#0f172a">3rd Pick (3 options)</text>')
    nodes.append(f'<text x="{x_L4+20}" y="{header_y}" text-anchor="middle" font-size="18" font-weight="bold" fill="#0f172a">60 Endings</text>')

    # Assemble complete SVG
    svg = f'''
                <!-- VISUALIZATION: STEP 1 (Full 60-Branch Network) -->
                <div style="margin: 1.5rem 0 2.5rem 0; text-align: center; background:#ffffff; border-radius: 8px; border: 1px solid #cbd5e1; padding: 2rem 1rem; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1); overflow-x: auto;">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 1480" width="100%" style="font-family:system-ui, -apple-system, sans-serif; min-width: 800px;">
                        <text x="460" y="25" text-anchor="middle" font-size="22" font-weight="bold" fill="#0f172a">The Branching Network: 5 &times; 4 &times; 3 = 60 Outcomes</text>
                        <line x1="50" y1="80" x2="870" y2="80" stroke="#e2e8f0" stroke-width="2" />
                        {''.join(paths)}
                        {''.join(nodes)}
                    </svg>
                </div>'''
    return svg

def inject_full_tree_svg(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: '{filepath}' not found.")
        sys.exit(1)

    full_svg_block = build_full_network_svg()

    # Search for the target paragraph to inject below
    target_pattern = r'(Multiply those together: \$5 \\times 4 \\times 3 = 60\$ possible ways to pick 3 letters\.\s*</p>)'

    if not re.search(target_pattern, content):
        print("Error: Target injection string not found in the HTML file.")
        sys.exit(1)

    # Inject the generated SVG
    updated_content = re.sub(
        target_pattern,
        lambda m: m.group(1) + "\n" + full_svg_block,
        content,
        count=1
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(updated_content)

    print(f"Successfully generated and injected the full 60-branch SVG network into {filepath}.")

if __name__ == "__main__":
    inject_full_tree_svg("week2-lecture5.html")
