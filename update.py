#!/usr/bin/env python3
"""
update_mobile_portraits.py

Updates mobile stylesheet rules across all coursework HTML files so that:
1. Biography portrait boxes stack vertically on mobile (<= 768px).
2. The portrait image takes up the full width of the box above the narrative text.
3. The biography text flows underneath at 100% width.
"""

from pathlib import Path
import re

# Comprehensive mobile rules for biography cards
MOBILE_BIO_CSS = """
            /* Full-width responsive biography cards on mobile */
            .biography-box {
                padding: 1.25rem 1rem !important;
            }
            .biography-box > div {
                flex-direction: column !important;
                align-items: stretch !important;
                gap: 1.25rem !important;
            }
            .biography-box > div > div:first-child {
                flex: 0 0 100% !important;
                width: 100% !important;
                max-width: 100% !important;
                margin: 0 0 0.5rem 0 !important;
            }
            .biography-box > div > div:first-child img {
                width: 100% !important;
                max-height: 380px !important;
                object-fit: cover !important;
                border-radius: 6px !important;
                display: block !important;
            }
            .biography-box > div > div:last-child {
                width: 100% !important;
                min-width: 0 !important;
            }
"""

def patch_file(file_path: Path) -> bool:
    content = file_path.read_text(encoding="utf-8")
    original = content

    # Check if a mobile media query already exists
    if "@media (max-width: 768px)" in content:
        # Check if biography rules are already defined in the media query
        if ".biography-box > div" in content:
            # Replace existing biography rules inside the media query
            pattern = re.compile(
                r'/\*.*?[Bb]iography.*?\*/\s*\.biography-box\s*>\s*div\s*\{.*?\.biography-box\s*>\s*div\s*>\s*div:last-child\s*\{[^}]*\}',
                re.DOTALL
            )
            if pattern.search(content):
                content = pattern.sub(MOBILE_BIO_CSS.strip(), content, count=1)
            else:
                # If specific selectors differed slightly, insert before the media query close
                mq_end = content.find("}", content.find("@media (max-width: 768px)"))
                if mq_end != -1:
                    content = content[:mq_end] + f"{MOBILE_BIO_CSS}\n        " + content[mq_end:]
        else:
            # Inject the rules before the closing brace of the existing media query
            pos = content.find("@media (max-width: 768px)")
            # Find the closing brace of the @media block
            brace_count = 0
            insert_pos = -1
            for idx in range(pos, len(content)):
                if content[idx] == '{':
                    brace_count += 1
                elif content[idx] == '}':
                    brace_count -= 1
                    if brace_count == 0:
                        insert_pos = idx
                        break

            if insert_pos != -1:
                content = content[:insert_pos] + f"{MOBILE_BIO_CSS}\n        " + content[insert_pos:]
    else:
        # If no media query exists at all, append a full block before </style>
        full_mq = f"""
        @media (max-width: 768px) {{{MOBILE_BIO_CSS}
        }}
"""
        if "</style>" in content:
            content = content.replace("</style>", f"{full_mq}    </style>", 1)

    if content != original:
        file_path.write_text(content, encoding="utf-8")
        return True
    return False

def main() -> None:
    directory = Path(".")
    html_files = sorted(directory.glob("*.html"))

    if not html_files:
        print("No HTML files found in current directory.")
        return

    count = 0
    for target in html_files:
        if patch_file(target):
            print(f"Updated portrait rules in: {target.name}")
            count += 1
        else:
            print(f"Skipped / No changes: {target.name}")

    print(f"\nDone. Successfully updated {count} file(s).")

if __name__ == "__main__":
    main()
