#!/usr/bin/env python3
import sys

def fix_svg_box_widths(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: '{filepath}' not found.")
        sys.exit(1)

    # 1. Widen the Shirt boxes from 110px to 135px to fit "Green Shirt"
    content = content.replace(
        '<rect width="110" height="44" rx="8" fill="#fee2e2" stroke="#ef4444" stroke-width="2" />',
        '<rect width="135" height="44" rx="8" fill="#fee2e2" stroke="#ef4444" stroke-width="2" />'
    )
    content = content.replace(
        '<rect width="110" height="44" rx="8" fill="#dbeafe" stroke="#3b82f6" stroke-width="2" />',
        '<rect width="135" height="44" rx="8" fill="#dbeafe" stroke="#3b82f6" stroke-width="2" />'
    )
    content = content.replace(
        '<rect width="110" height="44" rx="8" fill="#dcfce7" stroke="#22c55e" stroke-width="2" />',
        '<rect width="135" height="44" rx="8" fill="#dcfce7" stroke="#22c55e" stroke-width="2" />'
    )

    # 2. Adjust the connecting curves to start at 265px instead of 240px
    # (since the shirt boxes were just widened by 25px)
    content = content.replace('M 240 90 C 300 90, 300 65, 360 65', 'M 265 90 C 310 90, 310 65, 360 65')
    content = content.replace('M 240 90 C 300 90, 300 115, 360 115', 'M 265 90 C 310 90, 310 115, 360 115')

    content = content.replace('M 240 190 C 300 190, 300 165, 360 165', 'M 265 190 C 310 190, 310 165, 360 165')
    content = content.replace('M 240 190 C 300 190, 300 215, 360 215', 'M 265 190 C 310 190, 310 215, 360 215')

    content = content.replace('M 240 290 C 300 290, 300 265, 360 265', 'M 265 290 C 310 290, 310 265, 360 265')
    content = content.replace('M 240 290 C 300 290, 300 315, 360 315', 'M 265 290 C 310 290, 310 315, 360 315')

    # 3. Widen the final Outcome boxes from 190px to 215px to fit "Green & Khakis"
    content = content.replace(
        '<rect width="190" height="44" rx="22" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2" />',
        '<rect width="215" height="44" rx="22" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2" />'
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Successfully fixed the SVG rectangle widths in {filepath}.")

if __name__ == "__main__":
    fix_svg_box_widths("week2-lecture5.html")
