#!/usr/bin/env python3
"""Competition entry copier for news-image-20261124.

Reads entry.png relative to this script, copies it to the designated
output directory, verifies its SHA-256 hash, and exits.
"""

from hashlib import sha256
import os
from pathlib import Path


def main() -> None:
    # 1. Resolve path relative to script's own location
    script_dir = Path(__file__).resolve().parent
    source_path = script_dir / "entry.png"

    # 2. Raise FileNotFoundError if missing
    if not source_path.is_file():
        raise FileNotFoundError(f"Required source image not found: {source_path}")

    # 3. Determine output directory
    output_dir_env = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if output_dir_env:
        output_dir = Path(output_dir_env)
    else:
        output_dir = Path("/output")

    output_path = output_dir / "entry.png"

    # Create output directory if needed
    output_dir.mkdir(parents=True, exist_ok=True)

    # Read source bytes
    source_bytes = source_path.read_bytes()

    # Write to destination
    output_path.write_bytes(source_bytes)

    # 4. Verify copy by comparing SHA-256 hashes
    source_hash = sha256(source_bytes).digest()
    dest_bytes = output_path.read_bytes()
    dest_hash = sha256(dest_bytes).digest()

    if source_hash != dest_hash:
        raise RuntimeError(
            f"SHA-256 mismatch! Source: {source_hash.hex()}, Destination: {dest_hash.hex()}"
        )


if __name__ == "__main__":
    main()
