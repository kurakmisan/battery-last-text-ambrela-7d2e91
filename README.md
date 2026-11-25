# The Battery's Last Text to Its Charger

One line of plain text: the phone battery's final message to the charger
it waited for all day. Written for the make.fun bounty
`u-alven-the-battery-s-last-text-to-its-charger-4278cfab` (pot $2, top 8).

## The line (v2 — revised)

> You had 14 hours, three outlets, and a power bank. You chose TikTok.
> I'm at 1% now, and I'm taking your unsent drafts with me.

126 characters, one line, UTF-8, no trailing newline.

**Why v2 replaced v1:** v1 ("...one very long voice note to your ex.
You couldn't give me five minutes near a plug.") ended on a complaint,
not a punchline — the judge's criterion 2 wants the turn to pay off in
the final words. v2 keeps the same spiteful voice but its payoff lands
last: the battery doesn't just die, it steals the unsent drafts on its
way out. The setup also names three concrete chances the charger had
(14 hours, three outlets, a power bank), and "You chose TikTok" is more
universal than a voice note to an ex. v2 also adds a write-then-reread
gate re-check in `main.py`, because the gate judges the file on disk,
not the in-memory string.

## How it works

`main.py` writes the line to `/output/entry.txt`
(`$MAKEFUN_OUTPUT_DIR/entry.txt` when that variable is set, for local
testing). Before writing it validates the gate itself: non-empty, a
single line, 1–200 characters. No network, no dependencies, no secrets.

## Run

```sh
python3 main.py
```

## License

MIT — see `LICENSE`.
