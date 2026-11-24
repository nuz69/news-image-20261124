[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/nuz69/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/nuz69/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

# news-image-20261124

A program that outputs a single 1024x1024 PNG image summarizing the world news for Tuesday, 24 November 2026.

## News Stories Featured

1. **Lead story: Huang returns; Nvidia soars 31%** — Board reinstates CEO; shares gain $952bn in a day.
2. **EU unveils 22nd Russia sanctions.**
3. **12,000 evacuated at Manchester gig.**
4. **China sentences official to death for spying.**
5. **ICJ: Myanmar committed genocide.**

## How It Works

- **Python 3.13** compatible, using the standard library only.
- **Fully offline** execution with no external dependencies or network calls.
- Performs a byte-identical copy of `entry.png` to the output destination (`/output/entry.png` by default, or `$MAKEFUN_OUTPUT_DIR/entry.png`).
- **SHA-256 verification** validates source and destination file integrity against expected hash `8c2e620df7c282a0ecc9a19a673b9c9670cc8f1fb8fcd2f7c1996f45320d4d9a`.

## Run It

Run with the default output destination (`/output`):
```bash
python3 main.py
```

Run with a custom output directory via environment variable:
```bash
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Or via command-line argument:
```bash
python3 main.py --output-dir out
```

## Authoring

The entry image was rendered by a local pipeline and is copied verbatim by `main.py`.

## License

Licensed under the [MIT License](LICENSE).
