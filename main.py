#!/usr/bin/env python3
"""Competition entry script for news-image-20261124.

Writes the pre-rendered entry.png to the designated output directory,
verifying the SHA-256 hash.
"""

import argparse
from hashlib import sha256
import os
from pathlib import Path

# Expected SHA-256 hash of the pre-rendered entry.png
EXPECTED_HASH = "8c2e620df7c282a0ecc9a19a673b9c9670cc8f1fb8fcd2f7c1996f45320d4d9a"


def compute_sha256(path: Path) -> str:
    """Compute the SHA-256 hex digest of a file."""
    hasher = sha256()
    with open(path, "rb") as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Write the pre-rendered entry.png to the output directory."
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="Override the output directory (takes precedence over MAKEFUN_OUTPUT_DIR and /output).",
    )
    args = parser.parse_args()

    # 1. Resolve path of entry.png relative to this script's location
    script_dir = Path(__file__).resolve().parent
    source_path = script_dir / "entry.png"

    # 2. Raise FileNotFoundError with a clear message if entry.png is missing
    if not source_path.is_file():
        raise FileNotFoundError(
            f"Required entry image not found at expected location: {source_path}"
        )

    # Determine output directory
    if args.output_dir is not None:
        output_dir = args.output_dir
    else:
        output_dir_env = os.environ.get("MAKEFUN_OUTPUT_DIR")
        if output_dir_env:
            output_dir = Path(output_dir_env)
        else:
            output_dir = Path("/output")

    output_path = output_dir / "entry.png"

    # 3. Create the output directory if needed, and copy bytes verbatim
    output_dir.mkdir(parents=True, exist_ok=True)

    source_bytes = source_path.read_bytes()
    output_path.write_bytes(source_bytes)

    # 4. Verify the copy by comparing SHA-256 hashes
    source_hash = compute_sha256(source_path)
    dest_hash = compute_sha256(output_path)

    if source_hash != dest_hash:
        raise RuntimeError(
            f"Hash verification failed! Source hash ({source_hash}) "
            f"does not match destination hash ({dest_hash})."
        )

    if source_hash != EXPECTED_HASH:
        raise RuntimeError(
            f"Source file hash ({source_hash}) does not match expected "
            f"competition hash ({EXPECTED_HASH})."
        )

    print(f"Successfully wrote entry.png to {output_path} [SHA-256: {dest_hash}]")


if __name__ == "__main__":
    main()
