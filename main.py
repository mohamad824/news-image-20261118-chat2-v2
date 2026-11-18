#!/usr/bin/env python3
"""news-image-20261118 chat2-v2: copy the rendered front page to the output.

Standard library only: the grading sandbox installs nothing, so this
entrypoint must not import Pillow or any other third-party package. The
image is rendered at build time by chat2-v2-work/render.py and shipped
beside this file as image.png; this program only copies those bytes.
"""
import os


def copy_bytes(src, dst):
    """Copy a file byte-for-byte in fixed-size chunks. No deletion."""
    with open(src, "rb") as fin, open(dst, "wb") as fout:
        while True:
            chunk = fin.read(65536)
            if not chunk:
                break
            fout.write(chunk)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "image.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    copy_bytes(src, dst)


if __name__ == "__main__":
    main()
