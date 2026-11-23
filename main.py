"""The One-Line Laugh: write one funny line to /output/entry.txt.

Deterministic, standard library only. No network, no subprocess, no
randomness: the same line comes out on every run.
"""

import os

# The line is built in two parts so the punchline lands last, exactly
# where the judge's brief wants the surprise: a real turn at the end
# that still makes sense, naming an everyday truth.
SETUP = "My password manager forgot my master password, "
PUNCH = "so now we are both locked out of my life together."


def build_line():
    line = SETUP + PUNCH
    if not 1 <= len(line) <= 200:
        raise ValueError("line must be 1 to 200 characters, got %d" % len(line))
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    return line


def main():
    line = build_line()
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    # Files under /output must be readable by the grader (another uid),
    # so the file gets 0644. The /output directory itself is never
    # chmodded and never removed: it is the grader's bind mount.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
