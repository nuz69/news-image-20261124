[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/nuz69/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/nuz69/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

# news-image-20261124

An entry for the [make.fun](https://make.fun) `news-image-20261124` competition. This repository provides a program that outputs a single 1024x1024 PNG image summarizing the world news for Tuesday, 24 November 2026.

## News Stories Featured

The image presents a classic newspaper front page titled **THE WORLD TODAY** for Tuesday, 24 November 2026, featuring five major global headlines:

1. **Lead Story:** Huang returns; Nvidia soars 31% (board reinstates CEO; shares gain $952bn in a day).
2. EU unveils 22nd Russia sanctions.
3. 12,000 evacuated at Manchester gig.
4. China sentences official to death for spying.
5. ICJ: Myanmar committed genocide.

## How It Works

- Written in **Python 3.13** using **only the standard library**.
- Operates entirely offline with **no network access**.
- Performs a robust, byte-identical copy of `entry.png` to the output destination (`/output/entry.png` by default, or `$MAKEFUN_OUTPUT_DIR/entry.png`).
- Verifies the integrity of the copied file using **SHA-256** checksum verification.

## Run It

To execute the entry script using default output directories:

```bash
python3 main.py
```

To specify a custom output directory via environment variables:

```bash
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Authoring

This repository was authored collaboratively by a Gemini session and a human coordinator. The entry image (`entry.png`) was rendered by a local PIL pipeline and is copied verbatim by `main.py` (it is not generated dynamically at runtime by the model).

## License

MIT, see [LICENSE](LICENSE).
