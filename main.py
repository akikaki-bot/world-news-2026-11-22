"""Entry for make.fun bounty 'Sum up 22 November's world news in one image'.

Writes the bundled newspaper-style summary image to /output/entry.png.
Pure file copy: no network, fully deterministic (same bytes every run).
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"


def main() -> None:
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
