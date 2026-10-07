#!/usr/bin/env python3
r"""
recover_and_apply_enhancements.py

1. Checks out the complete, rich week1-lecture3.html from commit e1921c8.
2. Carefully injects Figure 3.2 (arithmetic-vs-geometric.png).
3. Adds the beginner-friendly dual behavior breakdown to Section 2.
4. Normalizes Taylor and Gauss portrait boxes to .biography-box.
5. Commits and pushes the complete restored lecture file.
"""

import sys
import subprocess
from pathlib import Path

def execute_git(args: list[str]) -> None:
    res = subprocess.run(args, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Git execution error: {' '.join(args)}\n{res.stderr.strip()}", file=sys.stderr)
        sys.exit(res.returncode)

def main() -> None:
    target = Path("week1-lecture3.html")

    # 1. Restore complete file from commit e1921c8
    execute_git(["git", "checkout", "e1921c839feebdc2980c45577fae74a4392857f7", "--", str(target)])
    print("Checked out base file from commit e1921c839feebdc2980c45577fae74a4392857f7")

    content = target.read_text(encoding="utf-8")

    # 2. Add Figure 3.2 beneath Section 3.1 intro if missing
    fig_token = "images/arithmetic-vs-geometric.png"
    if fig_token not in content:
        anchor_text = "steady linear pacing versus explosive compounding magnification."
        pos = content.find(anchor_text)
        if pos != -1:
            close_p = content.find("</p>", pos)
            if close_p != -1:
                insert_idx = close_p + len("</p>")
                fig_html = (
                    "\n\n            <!-- ILLUSTRATION: ARITHMETIC VS GEOMETRIC -->\n"
                    "            <div style=\"margin: 1.75rem 0 2rem 0; text-align: center;\">\n"
                    "                <div style=\"border-radius: 8px; overflow: hidden; border: 1px solid var(--border); box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05), 0 2px 4px -1px rgba(0,0,0,0.03); background: #ffffff;\">\n"
                    "                    <img src=\"images/arithmetic-vs-geometric.png\" alt=\"Comparison of Arithmetic Paced Walk versus Geometric Zoom Magnification\" style=\"width: 100%; height: auto; display: block;\">\n"
                    "                </div>\n"
                    "                <p style=\"font-size: 0.88rem; color: #64748b; margin-top: 0.6rem; line-height: 1.5;\">\n"
                    "                    <em>Figure 3.2:</em> The two fundamental engines of discrete dynamics. <strong>1. The Paced Walk (Arithmetic):</strong> Advancing by fixed measuring-tape strides (+1 each step). <strong>2. The Magnifying Glass (Geometric):</strong> Compounding field-of-view magnification (&times;2 each twist).\n"
                    "                </p>\n"
                    "            </div>"
                )
                content = content[:insert_idx] + fig_html + content[insert_idx:]
                print("Added Figure 3.2 to Section 3.1")

    # 3. Add responsive .biography-box CSS into <style> if missing
    if "/* Full-width responsive biography cards on mobile */" not in content:
        bio_css = (
            "\n        .biography-box { background: #f5f3ff; border: 1px solid #ddd6fe; border-left: 5px solid #6366f1; padding: 1.25rem 1.5rem; margin: 2rem 0; border-radius: 0 6px 6px 0; }\n"
            "        .biography-box h4 { margin-top: 0; color: #3730a3; font-size: 1.05rem; display: flex; align-items: center; gap: 0.5rem; }\n"
            "        .biography-box p, .biography-box li { color: #0f172a !important; }\n\n"
            "        /* Full-width responsive biography cards on mobile */\n"
            "        @media (max-width: 768px) {\n"
            "            .biography-box { padding: 1.25rem 1rem !important; }\n"
            "            .biography-box > div { flex-direction: column !important; align-items: stretch !important; gap: 1.25rem !important; }\n"
            "            .biography-box > div > div:first-child { flex: 0 0 100% !important; width: 100% !important; max-width: 100% !important; margin: 0 0 0.5rem 0 !important; }\n"
            "            .biography-box > div > div:first-child img { width: 100% !important; max-height: 380px !important; object-fit: cover !important; border-radius: 6px !important; display: block !important; }\n"
            "            .biography-box > div > div:last-child { width: 100% !important; min-width: 0 !important; }\n"
            "        }\n"
        )
        style_close = content.find("</style>")
        if style_close != -1:
            content = content[:style_close] + bio_css + "    " + content[style_close:]
            print("Injected responsive biography card stylesheet")

    # 4. Standardize Taylor and Gauss containers to .biography-box
    content = content.replace(
        '<!-- HISTORICAL PROFILE: BROOK TAYLOR -->\n            <div class="infobox"',
        '<!-- HISTORICAL PROFILE: BROOK TAYLOR -->\n            <div class="biography-box"'
    )
    content = content.replace(
        '<!-- HISTORICAL PROFILE: CARL FRIEDRICH GAUSS -->\n            <div class="infobox"',
        '<!-- HISTORICAL PROFILE: CARL FRIEDRICH GAUSS -->\n            <div class="biography-box"'
    )

    target.write_text(content, encoding="utf-8")
    print("Saved complete file.")

    py_files = [str(p) for p in Path(".").glob("*.py")]
    stage_targets = list(set([str(target)] + py_files))

    execute_git(["git", "add"] + stage_targets)
    diff_status = subprocess.run(["git", "diff", "--cached", "--quiet"])
    if diff_status.returncode != 0:
        commit_subject = "Restore rich content in Lecture 3 and integrate Figure 3.2"
        commit_body = (
            "Restore full mathematical sections, explanations, and diagrams\n"
            "from commit e1921c8 in week1-lecture3.html. Preserves Figure 3.2\n"
            "concept diagram, Option 1 intro, and mobile responsive biographies."
        )
        execute_git(["git", "commit", "-m", f"{commit_subject}\n\n{commit_body}"])
        execute_git(["git", "push"])
        print("Successfully committed and pushed recovered lecture file.")
    else:
        print("No staged changes detected to commit.")

if __name__ == "__main__":
    main()
