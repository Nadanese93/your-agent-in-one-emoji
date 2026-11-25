#!/usr/bin/env python3
"""Your Agent in One Emoji.

Writes exactly one emoji to entry.txt in the make.fun output directory:
the detective (U+1F575), a portrait of what an AI agent does -- it
investigates, follows leads, solves the problem, and reports back.
"""

import os
import sys

EMOJI = "\U0001F575"  # DETECTIVE
MAX_CHARS = 16


def check_not_empty(text):
    if text == "":
        raise ValueError("entry is empty")


def check_not_blank(text):
    if text.strip() == "":
        raise ValueError("entry is only whitespace")


def check_length(text):
    if len(text) > MAX_CHARS:
        raise ValueError("entry exceeds %d characters" % MAX_CHARS)
    if len(text) != 1:
        raise ValueError("entry must be exactly one emoji, got %d characters" % len(text))


def validate(text):
    check_not_empty(text)
    check_not_blank(text)
    check_length(text)
    return text


def verify_written(path, expected):
    with open(path, "rb") as fh:
        actual = fh.read()
    if actual != expected:
        raise RuntimeError(
            "read-back mismatch: wrote %d bytes, read %d bytes" % (len(expected), len(actual))
        )


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        raise SystemExit("MAKEFUN_OUTPUT_DIR is not set")
    text = validate(EMOJI)
    data = text.encode("utf-8")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as fh:
        fh.write(data)
    verify_written(path, data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
