#!/usr/bin/env python3
r"""
update_index_podcast.py

Appends the audio podcast link indicator to the Week 1 card heading in
index.html.
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
    target = Path("index.html")
    if not target.exists():
        print("Error: index.html not found.", file=sys.stderr)
        sys.exit(1)

    content = target.read_text(encoding="utf-8")

    if 'href="week1.html#podcast"' in content:
        print("Podcast link icon already exists in index.html")
        return

    old_heading = '<h4>Week 1 <span class="week-badge active">'
    new_heading = (
        '<h4>Week 1 <a href="week1.html#podcast" title="Audio Podcast Available" '
        'style="text-decoration: none; font-size: 0.95rem;" '
        'aria-label="Audio podcast available">🎧</a> '
        '<span class="week-badge active">'
    )

    if old_heading not in content:
        print("Error: Target heading pattern not found in index.html", file=sys.stderr)
        sys.exit(1)

    updated_content = content.replace(old_heading, new_heading, 1)
    target.write_text(updated_content, encoding="utf-8")
    print("Injected podcast icon into index.html")

    execute_git(["git", "add", str(target), str(Path(__file__).resolve())])
    commit_subject = "Add audio podcast indicator to Week 1 card in index"
    commit_body = (
        "Append a headphone link to the Week 1 heading in index.html that jumps\n"
        "directly to the new audio player component in week1.html."
    )
    execute_git(["git", "commit", "-m", f"{commit_subject}\n\n{commit_body}"])
    execute_git(["git", "push"])
    print("Successfully committed and pushed index.html changes.")

if __name__ == '__main__':
    main()
