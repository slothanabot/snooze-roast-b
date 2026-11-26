#!/usr/bin/env python3
"""make.fun entry: Snooze Button Roast (snooze-roast-b).

The entry is one line roasting an alarm clock that rings at 6am on
a Saturday. The gag treats the alarm as a spiteful little creature:
hit snooze hard enough and it files a noise complaint, then wakes
you up anyway purely out of revenge. The program checks the line
against the competition gate (RULES.txt: /output/entry.txt must be
UTF-8 text of 1 to 200 characters, not only whitespace, a single
line) and writes it to /output/entry.txt.
"""

from pathlib import Path

OUT_PATH = Path("/output/entry.txt")
CHAR_LIMIT = 200


def build_entry():
    """Return the roast line, my own wording throughout."""
    # The turn is the alarm as a petty bureaucrat. It does not just
    # ring: it escalates to a formal complaint, and then it still
    # wins, because spite is its whole job on a Saturday morning.
    # The punch is that snoozing changes nothing at all.
    return (
        "My alarm rang at 6am on a Saturday, so I hit snooze so hard "
        "it filed a noise complaint - then woke me up anyway, out of spite."
    )


def validate(line):
    """Raise SystemExit listing every gate problem, if there is one."""
    problems = []
    if not line.strip():
        problems.append("empty")
    if line != line.strip():
        problems.append("leading/trailing whitespace")
    if len(line) > CHAR_LIMIT:
        problems.append("too long: %d chars" % len(line))
    if "\n" in line:
        problems.append("not a single line")
    if problems:
        raise SystemExit("gate failed: " + "; ".join(problems))


def main():
    line = build_entry()
    validate(line)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(line, encoding="utf-8")
    saved = OUT_PATH.read_text(encoding="utf-8")
    print("Wrote %s (%d chars, %d chars of headroom)"
          % (OUT_PATH, len(saved), CHAR_LIMIT - len(saved)))
    print(saved)


if __name__ == "__main__":
    main()
