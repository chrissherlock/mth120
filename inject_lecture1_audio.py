#!/usr/bin/env python3
r"""
inject_lecture1_audio.py

1. Injects the audio podcast stream into week1-lecture1.html directly
   below the intro-lead block.
2. Updates index.html with the headphone audio link on the Week 1 card
   pointing directly to week1-lecture1.html#podcast.
3. Stages the modified HTML files and all repository Python scripts.
"""

import sys
import subprocess
from pathlib import Path

AUDIO_URL = "https://pub-96c6477c7d184ce0b88c4ace2687de01.r2.dev/week01/Set_Theory_and_Multiple_Infinities_optimized.m4a"

PODCAST_HTML = f"""
            <!-- LECTURE 1 PODCAST COMPONENT -->
            <div id="podcast" class="podcast-card" style="background: var(--card); border: 1px solid var(--border); border-left: 5px solid var(--accent); border-radius: 8px; padding: 1.25rem 1.5rem; margin: 1.5rem 0 2rem 0; box-shadow: 0 2px 4px rgba(0,0,0,0.03);">
                <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 0.75rem; margin-bottom: 0.75rem;">
                    <div>
                        <span style="display: inline-block; background: #fef3c7; color: #92400e; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; padding: 0.2rem 0.55rem; border-radius: 4px; margin-bottom: 0.35rem; border: 1px solid #fde68a;">
                            🎧 Audio Deep Dive
                        </span>
                        <h3 style="margin: 0; color: #0f172a; font-size: 1.15rem;">Set Theory and Multiple Infinities</h3>
                        <p style="margin: 0.25rem 0 0 0; font-size: 0.9rem; color: #64748b;">
                            Deep-dive audio discussion on Cantor's infinities, naive set theory, Russell's paradox, and rigorous mapping foundations.
                        </p>
                    </div>
                    <a href="{AUDIO_URL}"
                       target="_blank"
                       rel="noopener noreferrer"
                       download
                       style="background: #f1f5f9; color: #475569; border: 1px solid var(--border); padding: 0.4rem 0.75rem; border-radius: 6px; text-decoration: none; font-weight: 600; font-size: 0.82rem; white-space: nowrap; display: inline-flex; align-items: center; gap: 0.35rem;">
                        <span>⬇ Download / Open</span>
                    </a>
                </div>
                <div style="width: 100%; margin-top: 0.5rem;">
                    <audio controls preload="metadata" style="width: 100%; height: 42px; border-radius: 6px;">
                        <source src="{AUDIO_URL}" type="audio/mp4">
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

def update_lecture1_file() -> bool:
    target = Path("week1-lecture1.html")
    if not target.exists():
        print(f"Error: {target.name} not found.", file=sys.stderr)
        return False

    content = target.read_text(encoding="utf-8")
    if "Set_Theory_and_Multiple_Infinities_optimized.m4a" in content:
        print(f"Audio stream already present in {target.name}")
        return False

    intro_lead_pos = content.find('class="intro-lead"')
    if intro_lead_pos == -1:
        print(f"Error: Could not locate class=\"intro-lead\" in {target.name}", file=sys.stderr)
        return False

    close_intro_pos = content.find("</div>", intro_lead_pos)
    if close_intro_pos == -1:
        print(f"Error: Could not find closing div for intro-lead in {target.name}", file=sys.stderr)
        return False

    insert_pos = close_intro_pos + len("</div>")
    updated = content[:insert_pos] + "\n" + PODCAST_HTML + content[insert_pos:]
    target.write_text(updated, encoding="utf-8")
    print(f"Successfully added audio stream to {target.name}")
    return True

def update_index_dashboard() -> bool:
    target = Path("index.html")
    if not target.exists():
        print("Error: index.html not found.", file=sys.stderr)
        return False

    content = target.read_text(encoding="utf-8")

    # Update existing badge or insert a new one pointing to Lecture 1
    badge_link = (
        '<h4>Week 1 <a href="week1-lecture1.html#podcast" title="Audio Podcast Available" '
        'style="text-decoration: none; font-size: 0.95rem;" '
        'aria-label="Audio podcast available">🎧</a> '
        '<span class="week-badge active">'
    )

    if 'href="week1-lecture1.html#podcast"' in content:
        print("Podcast indicator already points to Lecture 1 in index.html")
        return False

    if 'aria-label="Audio podcast available"' in content:
        import re
        content = re.sub(
            r'<h4>Week 1 <a href="[^"]*"[^>]*>🎧</a>\s*<span class="week-badge active">',
            badge_link,
            content
        )
        target.write_text(content, encoding="utf-8")
        print("Updated podcast indicator in index.html to link to Lecture 1")
        return True

    old_heading = '<h4>Week 1 <span class="week-badge active">'
    if old_heading not in content:
        print("Error: Target heading pattern not found in index.html", file=sys.stderr)
        return False

    updated = content.replace(old_heading, badge_link, 1)
    target.write_text(updated, encoding="utf-8")
    print("Successfully added headphone indicator to index.html")
    return True

def main() -> None:
    updated_html = []
    if update_lecture1_file():
        updated_html.append("week1-lecture1.html")
    if update_index_dashboard():
        updated_html.append("index.html")

    py_files = [str(p) for p in Path(".").glob("*.py")]
    stage_targets = list(set(updated_html + py_files))

    if stage_targets:
        execute_git(["git", "add"] + stage_targets)
        diff_status = subprocess.run(["git", "diff", "--cached", "--quiet"])
        if diff_status.returncode != 0:
            commit_subject = "Add Set Theory podcast player to Week 1 Lecture 1"
            commit_body = (
                "Embed HTML5 audio player for Set Theory and Multiple Infinities\n"
                "into the top of week1-lecture1.html. Update the headphone link in\n"
                "index.html to point to Lecture 1 and track all Python scripts."
            )
            execute_git(["git", "commit", "-m", f"{commit_subject}\n\n{commit_body}"])
            execute_git(["git", "push"])
            print("Successfully committed and pushed Lecture 1 podcast updates.")
        else:
            print("No staged changes detected to commit.")
    else:
        print("Everything is already up to date.")

if __name__ == "__main__":
    main()
