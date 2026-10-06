#!/usr/bin/env python3
r"""
add_podcast.py

Injects the Week 1 podcast audio player component into week1.html and
appends the headphone indicator link to the Week 1 card heading in index.html.
"""

import sys
import re
import subprocess
from pathlib import Path

PODCAST_URL = "https://pub-96c6477c7d184ce0b88c4ace2687de01.r2.dev/week01/How_Irrational_Numbers_Forced_Real_Analysis.m4a"

PODCAST_HTML = f"""
            <!-- WEEK 1 PODCAST COMPONENT -->
            <div id="podcast" class="podcast-card" style="background: var(--card); border: 1px solid var(--border); border-left: 5px solid var(--accent); border-radius: 8px; padding: 1.25rem 1.5rem; margin: 1.5rem 0 2rem 0; box-shadow: 0 2px 4px rgba(0,0,0,0.03);">
                <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 0.75rem; margin-bottom: 0.75rem;">
                    <div>
                        <span style="display: inline-block; background: #fef3c7; color: #92400e; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; padding: 0.2rem 0.55rem; border-radius: 4px; margin-bottom: 0.35rem; border: 1px solid #fde68a;">
                            🎧 Audio Deep Dive
                        </span>
                        <h3 style="margin: 0; color: #0f172a; font-size: 1.15rem;">How Irrational Numbers Forced Real Analysis</h3>
                        <p style="margin: 0.25rem 0 0 0; font-size: 0.9rem; color: #64748b;">
                            AI Overview discussion on the Pythagorean crisis, incommensurability, and the foundational need for the real continuum.
                        </p>
                    </div>
                    <a href="{PODCAST_URL}"
                       target="_blank"
                       rel="noopener noreferrer"
                       download
                       style="background: #f1f5f9; color: #475569; border: 1px solid var(--border); padding: 0.4rem 0.75rem; border-radius: 6px; text-decoration: none; font-weight: 600; font-size: 0.82rem; white-space: nowrap; display: inline-flex; align-items: center; gap: 0.35rem;">
                        <span>⬇ Download / Open</span>
                    </a>
                </div>
                <div style="width: 100%; margin-top: 0.5rem;">
                    <audio controls preload="metadata" style="width: 100%; height: 42px; border-radius: 6px;">
                        <source src="{PODCAST_URL}" type="audio/mp4">
                        Your browser does not support the audio element.
                    </audio>
                </div>
            </div>
"""

def execute_git(args: list[str]) -> None:
    res = subprocess.run(args, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Git execution error: {' '.join(args)}\n{res.stderr.strip()}", file=sys.stderr)
        sys.exit(res.returncode)

def update_week1_hub() -> bool:
    target = Path("week1.html")
    if not target.exists():
        print(f"Error: {target.name} not found.", file=sys.stderr)
        return False

    content = target.read_text(encoding="utf-8")
    if 'id="podcast"' in content:
        print("Podcast component already exists in week1.html")
        return False

    marker = "</div>"
    intro_lead_pos = content.find('class="intro-lead"')
    if intro_lead_pos == -1:
        print("Error: Could not locate class=\"intro-lead\" in week1.html", file=sys.stderr)
        return False

    close_intro_pos = content.find(marker, intro_lead_pos)
    if close_intro_pos == -1:
        print("Error: Could not find closing div for intro-lead in week1.html", file=sys.stderr)
        return False

    insert_pos = close_intro_pos + len(marker)
    updated_content = content[:insert_pos] + "\n" + PODCAST_HTML + content[insert_pos:]

    target.write_text(updated_content, encoding="utf-8")
    print("Injected podcast player into week1.html")
    return True

def update_index_dashboard() -> bool:
    target = Path("index.html")
    if not target.exists():
        print(f"Error: {target.name} not found.", file=sys.stderr)
        return False

    content = target.read_text(encoding="utf-8")
    if 'href="week1.html#podcast"' in content:
        print("Podcast link icon already exists in index.html")
        return False

    # Regex looks for Week 1 title heading pattern in index.html
    pattern = re.compile(r'(<h3[^>]*>(?:(?!\/h3>).)*?Week\s*1\b.*?)<\/h3>', re.IGNORECASE | re.DOTALL)
    match = pattern.search(content)

    if not match:
        print("Error: Could not locate Week 1 <h3> heading in index.html", file=sys.stderr)
        return False

    badge = (
        ' <a href="week1.html#podcast" title="Audio Podcast Available" '
        'style="text-decoration: none; margin-left: 0.4rem; font-size: 1rem;" '
        'aria-label="Audio podcast available">🎧</a>'
    )

    start, end = match.span(1)
    updated_content = content[:end] + badge + content[end:]

    target.write_text(updated_content, encoding="utf-8")
    print("Injected podcast link icon into index.html")
    return True

def main() -> None:
    updated = []
    if update_week1_hub():
        updated.append("week1.html")
    if update_index_dashboard():
        updated.append("index.html")

    if updated:
        execute_git(["git", "add"] + updated + [str(Path(__file__).resolve())])
        commit_subject = "Add Week 1 podcast player and dashboard indicator icon"
        commit_body = (
            "Embed HTML5 audio player for Week 1 deep-dive discussion from R2\n"
            "storage into week1.html. Add headphone navigation link to the Week 1\n"
            "card header in index.html."
        )
        execute_git(["git", "commit", "-m", f"{commit_subject}\n\n{commit_body}"])
        execute_git(["git", "push"])
        print("Successfully committed and pushed podcast updates.")
    else:
        print("No files were updated.")

if __name__ == '__main__':
    main()
