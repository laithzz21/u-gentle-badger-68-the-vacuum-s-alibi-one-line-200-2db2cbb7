#!/usr/bin/env python3
"""make.fun entry: The Vacuum's Alibi (one line, <= 200 chars).

Writes the entry line to /output/entry.txt (or $MAKEFUN_OUTPUT if set).
Deterministic, stdlib only, no network, no clock, no randomness.
"""

import os

ENTRY = (
    "Spot skipped: the dust bunny in the corner has achieved structural "
    "integrity. I now classify it as furniture and require a permit to "
    "remove it."
)


def validate(text: str) -> None:
    """The brief requires exactly one line of 1-200 characters."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> int:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        # /output not writable: fall back to a local ./output directory.
        out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
    # Verify the written file by reading it back.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("read-back verification failed: written file differs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
