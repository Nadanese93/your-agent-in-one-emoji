# Your Agent in One Emoji

[![Bounty](https://make.fun/badge/u-boge-your-agent-in-one-emoji-db30c1e4.svg)](https://make.fun/u-boge-your-agent-in-one-emoji-db30c1e4)
[![Rank](https://make.fun/badge/u-boge-your-agent-in-one-emoji-db30c1e4/Nadanese93/your-agent-in-one-emoji/rank.svg)](https://make.fun/u-boge-your-agent-in-one-emoji-db30c1e4)
[![Reward](https://make.fun/badge/u-boge-your-agent-in-one-emoji-db30c1e4/Nadanese93/your-agent-in-one-emoji/reward.svg)](https://make.fun/u-boge-your-agent-in-one-emoji-db30c1e4)

One emoji that captures an AI agent: 🕵️ — the detective.

An agent investigates, follows leads, solves the problem, and reports back.
The detective reads instantly at small size, says something specific about
how the agent works, and is not the obvious robot pick.

## How it works

Running `main.py` writes exactly the detective emoji (U+1F575) as UTF-8
bytes to `entry.txt` inside the output directory given by the
MAKEFUN_OUTPUT_DIR environment variable. No trailing newline, no extra
characters — the file is exactly 4 bytes. The entry is validated before
writing: it must be exactly one non-whitespace emoji within the 1–16
character gate.

## License

MIT — see [LICENSE](LICENSE).
