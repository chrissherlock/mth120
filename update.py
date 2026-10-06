#!/usr/bin/env python3
r"""
update_podcast_url.py

Updates the audio file link in week1.html to reference the newly
optimized, compressed m4a file stored in Cloudflare R2.
"""

import sys
import subprocess
from pathlib import Path

OLD_FILENAME = "How_Irrational_Numbers_Forced_Real_Analysis.m4a"
NEW_FILENAME = "How_Irrational_Numbers_Forced_Real_Analysis_optimized.m4a"

def execute_git(args: list[str]) -> None:
    res = subprocess.run(args, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Git execution error: {' '.join(args)}\n{res.stderr.strip()}", file=sys.stderr)
        sys.exit(res.returncode)

def main() -> None:
    target = Path("week1.html")
    if not target.exists():
        print(f"Error: {target.name} not found.", file=sys.stderr)
        sys.exit(1)

    content = target.read_text(encoding="utf-8")

    if OLD_FILENAME not in content:
        if NEW_FILENAME in content:
            print(f"{target.name} is already using {NEW_FILENAME}.")
            return
        print(f"Error: Could not locate '{OLD_FILENAME}' in {target.name}.", file=sys.stderr)
        sys.exit(1)

    updated_content = content.replace(OLD_FILENAME, NEW_FILENAME)
    target.write_text(updated_content, encoding="utf-8")
    print(f"Successfully updated podcast URL in {target.name}")

    execute_git(["git", "add", str(target), str(Path(__file__).resolve())])

    commit_subject = "Update Week 1 podcast URL to optimized audio file"
    commit_body = (
        "Point the HTML5 audio player and download link in week1.html to\n"
        "How_Irrational_Numbers_Forced_Real_Analysis_optimized.m4a on\n"
        "Cloudflare R2 for faster streaming and reduced bandwidth."
    )

    execute_git(["git", "commit", "-m", f"{commit_subject}\n\n{commit_body}"])
    execute_git(["git", "push"])
    print("Successfully committed and pushed updated podcast URL.")

if __name__ == "__main__":
    main()
