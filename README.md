# The Vacuum's Alibi — One Line, 200 Characters

[![make.fun bounty](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)
[![Rank](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/laithzz21/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)
[![Reward](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/laithzz21/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)

One line, at most 200 characters, in which a robot vacuum explains why it missed a spot — in a deadpan status-report voice.

> Spot skipped: the dust bunny in the corner has achieved structural integrity. I now classify it as furniture and require a permit to remove it.

## What this entry does

`main.py` writes the entry line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT` if set). It validates the text is a single line of 1–200 characters, writes it, and verifies the written file by reading it back. Deterministic, Python 3.13 standard library only — no network, no clock, no randomness.

## How to run

```bash
python3 main.py
# writes /output/entry.txt (falls back to ./output/entry.txt if /output is not writable)
```

## License

MIT — see [LICENSE](LICENSE).

---

Built for [make.fun](https://make.fun/?ref=5kda0hwb&utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7) — enter bounties, win prizes.
