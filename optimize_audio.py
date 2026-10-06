#!/usr/bin/env python3
r"""
optimize_audio.py

Compresses spoken-word podcast audio files for web distribution:
- Downmixes stereo to mono
- Resamples to 32 kHz
- Encodes with AAC at 56 kbps
- Moves moov atom to the front for instant HTML5 web playback (+faststart)
"""

import sys
import subprocess
from pathlib import Path


def format_bytes(size: int) -> str:
    for unit in ["B", "KB", "MB", "GB"]:
        if size < 1024.0:
            return f"{size:.2f} {unit}"
        size /= 1024.0
    return f"{size:.2f} TB"


def optimize_file(input_path: Path, output_path: Path) -> None:
    if not input_path.exists():
        print(f"Error: {input_path} not found.", file=sys.stderr)
        sys.exit(1)

    cmd = [
        "ffmpeg",
        "-y",
        "-i", str(input_path),
        "-c:a", "aac",
        "-b:a", "56k",
        "-ac", "1",
        "-ar", "32000",
        "-movflags", "+faststart",
        str(output_path),
    ]

    print(f"Running compression on {input_path.name}...")
    res = subprocess.run(cmd, capture_output=True, text=True)

    if res.returncode != 0:
        print(f"FFmpeg error:\n{res.stderr}", file=sys.stderr)
        sys.exit(res.returncode)

    initial_size = input_path.stat().st_size
    final_size = output_path.stat().st_size
    saved = 100.0 * (1.0 - (final_size / initial_size))

    print(f"\nOptimization complete:")
    print(f"  Original:  {format_bytes(initial_size)}")
    print(f"  Optimized: {format_bytes(final_size)}")
    print(f"  Reduction: {saved:.1f}% space saved")


def main() -> None:
    target = Path("How_Irrational_Numbers_Forced_Real_Analysis.m4a")
    output = Path("How_Irrational_Numbers_Forced_Real_Analysis_optimized.m4a")

    if len(sys.argv) > 1:
        target = Path(sys.argv[1])
        output = target.with_stem(target.stem + "_optimized")

    optimize_file(target, output)


if __name__ == "__main__":
    main()
