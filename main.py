#!/usr/bin/env python3
"""Six Words, One Story — make.fun entry.

Writes the six-word story to entry.txt inside the directory named by the
MAKEFUN_OUTPUT_DIR environment variable (default /output when unset).

The story line is validated before anything is written: it must be exactly
six words and between 1 and 60 characters long. The output is written with
no trailing newline, and the program is fully deterministic — the same input
always produces the same bytes.
"""

import os
import sys

STORY = "The baby cried. The will changed."
MIN_LENGTH = 1
MAX_LENGTH = 60
EXPECTED_WORDS = 6


def validate_story(story):
    """Check the story against the rules; return an error message or None."""
    if not (MIN_LENGTH <= len(story) <= MAX_LENGTH):
        return "error: story must be {}-{} characters, got {}".format(
            MIN_LENGTH, MAX_LENGTH, len(story)
        )
    words = story.split()
    if len(words) != EXPECTED_WORDS:
        return "error: story must be exactly {} words, got {}".format(
            EXPECTED_WORDS, len(words)
        )
    return None


def write_story(story, output_dir):
    """Write the story to entry.txt inside output_dir, no trailing newline."""
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(story)


def main():
    error = validate_story(STORY)
    if error is not None:
        print(error, file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    write_story(STORY, output_dir)
    return 0


if __name__ == "__main__":
    sys.exit(main())
