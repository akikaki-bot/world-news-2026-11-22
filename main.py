"""Entry for make.fun bounty 'Sum up 22 November's world news in one image'.

Writes the bundled newspaper-style summary image to /output/entry.png.
Pure file copy: no network, fully deterministic (same bytes every run).
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
# The grader reads /output/entry.png; outside its container,
# MAKEFUN_OUTPUT_DIR stands in for /output (as in the kit's starter).
DST = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")


def main() -> None:
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)
    # Verify what the judge will read: a whole PNG within the 1 MiB cap.
    with open(DST, "rb") as f:
        head = f.read(8)
    size = os.path.getsize(DST)
    assert head == b"\x89PNG\r\n\x1a\n", "output is not a PNG"
    assert size <= 1_048_576, f"output too large: {size} bytes"


if __name__ == "__main__":
    main()
