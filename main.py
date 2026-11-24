"""Angry Judge: The Short Rant Contest — entry program.

Writes one short, funny rant about an everyday annoyance to
``<MAKEFUN_OUTPUT_DIR>/entry.txt`` (default ``/output``).

The gate (RULES.txt): the file must be UTF-8 text of 1 to 400 characters,
not only whitespace. ``validate()`` enforces exactly that before the file
is written, so an invalid rant can never reach the judge.

Pure standard library only (``os``).
"""

import os

RANT = (
    "One person replied-all to a company-wide email, and now four hundred "
    "strangers are debating a meeting that ended yesterday. Someone "
    "replied-all to say 'please stop replying-all.' Then someone else "
    "replied-all to agree. We are in hour three. I have muted nothing, "
    "because at this point I need to see how it ends."
)

MAX_CHARS = 400


def validate(text):
    """Return the text if it passes the RULES.txt gate, else raise."""
    if not isinstance(text, str):
        raise TypeError("rant must be str")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(
            "rant must be 1-%d characters, got %d" % (MAX_CHARS, len(text))
        )
    if not text.strip():
        raise ValueError("rant must not be only whitespace")
    if "\n" in text or "\r" in text:
        # One unbroken block: a line break would split the punch.
        raise ValueError("rant must be a single paragraph, no line breaks")
    text.encode("utf-8")  # must be valid UTF-8
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = validate(RANT)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print("wrote %s (%d chars)" % (path, len(text)))


if __name__ == "__main__":
    main()
