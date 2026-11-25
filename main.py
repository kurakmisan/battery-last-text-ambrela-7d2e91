"""The Battery's Last Text to Its Charger.

Writes the phone battery's final one-line text message to the charger
it waited for all day to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR
when set, for local testing).

Gate: the file must be UTF-8, 1-200 characters, one line, not only
whitespace. This program validates its own output before writing.
"""

import os

TEXT = (
    "You had 14 hours, three outlets, and a power bank. You chose "
    "TikTok. I'm at 1% now, and I'm taking your unsent drafts with me."
)


def main() -> None:
    text = TEXT
    if not text.strip():
        raise ValueError("entry text must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry text must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry text must be 1-200 characters, got {len(text)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Re-read and re-validate what was actually written: the gate
    # judges the file on disk, not the in-memory string.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != text:
        raise ValueError("written entry differs from validated text")
    if not written.strip() or "\n" in written or "\r" in written:
        raise ValueError("written entry failed the gate re-check")
    if not 1 <= len(written) <= 200:
        raise ValueError("written entry failed the length re-check")


if __name__ == "__main__":
    main()
