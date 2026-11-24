[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/nuz69/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/nuz69/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

# news-image-20261124

An entry for the `news-image-20261124` make.fun competition ($100 pot, top 50 share, deadline 2026-11-26T00:00:00Z).

## Overview

This repository contains a single 1024x1024 PNG image and a robust Python runner that synthesizes the world news of Tuesday, 24 November 2026 into a classic newspaper front page titled **THE WORLD TODAY**. 

The front page covers five major global news stories:
1. **Lead Story:** *Huang returns; Nvidia soars 31%* — Board reinstates CEO; shares gain $952bn in a single day.
2. **EU Unveils 22nd Russia Sanctions** — New sweeping economic measures target remaining energy and financial networks.
3. **Manchester Gig Evacuation** — 12,000 concertgoers safely evacuated following a late-night security alert.
4. **China Espionage Sentencing** — Senior state official sentenced to death for high-level espionage.
5. **ICJ Ruling:** *Myanmar committed genocide* — International Court of Justice delivers its historic final verdict.

## How It Works

- **Pure Standard Library:** Built using Python 3.13 with zero external dependencies.
- **Offline & Deterministic:** Requires no network access and performs a byte-identical copy of the pre-rendered entry image.
- **Integrity Verified:** Automatically computes and verifies the SHA-256 checksum of `entry.png` before and after writing it to the destination directory.

## Run It

Generate the output image in the default location (`/output/entry.py` or `/output/entry.png`):

```bash
python3 main.py
```

Or specify a custom output directory via environment variables:

```bash
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Authoring

- This repository was co-authored by a Gemini session and a human coordinator.
- The entry image (`entry.png`) was rendered through a local PIL pipeline and is copied verbatim by `main.py` (the image itself was not generated directly by the model during execution).

## License

MIT License. See the [LICENSE](LICENSE) file for details.
