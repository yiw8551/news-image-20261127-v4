#!/usr/bin/env python3
"""news-image-20261127-v4: 27 November 2026 world news in one image.

The entry image is pre-rendered and shipped as entry.png. This program
only copies it to the output path the grader requests (argv[1], or the
MAKEFUN_OUTPUT_DIR environment variable, or ./output). Standard library
only; no image libraries, no network, fully deterministic.
"""

import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out = None
    if len(sys.argv) > 1:
        out = sys.argv[1]
    elif os.environ.get("MAKEFUN_OUTPUT_DIR"):
        out = os.environ["MAKEFUN_OUTPUT_DIR"]
    else:
        out = "output"
    if not os.path.isfile(src):
        raise FileNotFoundError(f"entry image not found: {src}")
    if os.path.isdir(out):
        out = os.path.join(out, "entry.png")
    parent = os.path.dirname(os.path.abspath(out))
    if parent:
        os.makedirs(parent, exist_ok=True)
    shutil.copyfile(src, out)
    if os.path.getsize(out) != os.path.getsize(src):
        raise IOError(f"incomplete copy: {out} is not the same size as {src}")


if __name__ == "__main__":
    main()
