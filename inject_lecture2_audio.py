#!/usr/bin/env python3
r"""
inject_lecture2_audio.py

Injects the audio podcast stream into week1-lecture2.html directly
below the intro-lead block and stages all modified files and Python scripts.
"""

import sys
import subprocess
from pathlib import Path

AUDIO_URL = "https://pub-96c6477c7d184ce0b88c4ace2687de01.r2.dev/week01/Set_Theory_and_Multiple_Infinities_optimized.m4a"

PODCAST_HTML = f"""
            <!-- LECTURE 2 PODCAST COMPONENT -->
            <div id="podcast" class="podcast-card" style="background: var(--card); border: 1px solid var(--border); border-left: 5px solid var(--accent); border-radius: 8px; padding: 1.25rem 1.5rem; margin: 1.5rem 0 2rem 0; box-shadow: 0 2px 4px rgba(0,0,0,0.03);">
                <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 0.75rem; margin-bottom: 0.75rem;">
                    <div>
                        <span style="display: inline-block; background: #fef3c7; color: #92400e; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; padding: 0.2rem 0.55rem; border-radius: 4px; margin-bottom: 0.35rem; border: 1px solid #fde68a;">
                            🎧 Audio Deep Dive
                        </span>
                        <h3 style="margin: 0; color: #0f172a; font-size: 1.15rem;">Set Theory and Multiple Infinities</h3>
                        <p style="margin: 0.25rem 0 0 0; font-size: 0.9rem; color: #64748b;">
                            Deep-dive audio discussion on Cantor's infinities, number structures, and foundational continuum concepts.
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

def main() -> None:
    target = Path("week1-lecture2.html")
    if not target.exists():
        print(f"Error: {target.name} not found.", file=sys.stderr)
        sys.exit(1)

    content = target.read_text(encoding="utf-8")
    if "Set_Theory_and_Multiple_Infinities_optimized.m4a" in content:
        print(f"Audio stream already present in {target.name}")
        return

    intro_lead_pos = content.find('class="intro-lead"')
    if intro_lead_pos == -1:
        print(f"Error: Could not locate class=\"intro-lead\" in {target.name}", file=sys.stderr)
        sys.exit(1)

    close_intro_pos = content.find("</div>", intro_lead_pos)
    if close_intro_pos == -1:
        print(f"Error: Could not find closing div for intro-lead in {target.name}", file=sys.stderr)
        sys.exit(1)

    insert_pos = close_intro_pos + len("</div>")
    updated = content[:insert_pos] + "\n" + PODCAST_HTML + content[insert_pos:]
    target.write_text(updated, encoding="utf-8")
    print(f"Successfully added audio stream to {target.name}")

    py_files = [str(p) for p in Path(".").glob("*.py")]
    stage_targets = list(set([str(target)] + py_files))

    execute_git(["git", "add"] + stage_targets)
    diff_status = subprocess.run(["git", "diff", "--cached", "--quiet"])
    if diff_status.returncode != 0:
        commit_subject = "Add Set Theory podcast player to Week 1 Lecture 2"
        commit_body = (
            "Embed HTML5 audio player for Set Theory and Multiple Infinities into\n"
            "the top of week1-lecture2.html. Stages modified lecture notes and\n"
            "all repository Python automation scripts."
        )
        execute_git(["git", "commit", "-m", f"{commit_subject}\n\n{commit_body}"])
        execute_git(["git", "push"])
        print("Successfully committed and pushed Lecture 2 podcast updates.")
    else:
        print("No staged changes detected to commit.")

if __name__ == "__main__":
    main()
