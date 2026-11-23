# Six Words, One Story

[![make.fun · u-deranalabs-six-words-one-story-f982e410](https://make.fun/badge/u-deranalabs-six-words-one-story-f982e410.svg)](https://make.fun/bounty/u-deranalabs-six-words-one-story-f982e410?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-six-words-one-story-f982e410)
[![rank](https://make.fun/badge/u-deranalabs-six-words-one-story-f982e410/lumi-xyzhani/six-words-one-story/rank.svg)](https://make.fun/bounty/u-deranalabs-six-words-one-story-f982e410/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-six-words-one-story-f982e410)
[![reward](https://make.fun/badge/u-deranalabs-six-words-one-story-f982e410/lumi-xyzhani/six-words-one-story/reward.svg)](https://make.fun/bounty/u-deranalabs-six-words-one-story-f982e410?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-six-words-one-story-f982e410)

An entry for the make.fun bounty **"Six Words, One Story"** — a complete
story told in exactly six words.

## The story

> The baby cried. The will changed.

Two sentences, one hinge. A birth arrives, and with it, everything the
family thought was settled — the inheritance, the plans, the future — is
rewritten. What changed in the will, and why, is left for the reader to
fill in.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

The program writes the story line to `entry.txt` inside the directory
named by `MAKEFUN_OUTPUT_DIR` (default `/output` when unset). It uses only
the Python 3 standard library, writes no trailing newline, and is
deterministic: every run produces the same bytes.

## The gate

The entry must satisfy the contest gate: the story line must be between
1 and 60 characters long and contain exactly six words. `main.py`
validates both conditions before writing anything, and exits non-zero
with an error message if either fails. This line is 33 characters and
six words, so it passes.
