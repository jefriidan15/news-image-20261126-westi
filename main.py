#!/usr/bin/env python3
"""Entry point for the make.fun news-image-20261126 bounty.

Copies the bundled front-page image (entry.png, shipped next to this file)
to the output directory as /output/entry.png.

Standard library only. No network access. Deterministic: the same input
file always produces the same output file, byte for byte.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, target)
    print(f"wrote {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
