#!/usr/bin/env python3
import argparse
import hashlib
import os
import shutil
from pathlib import Path

EXPECTED_HASH = "8c2e620df7c282a0ecc9a19a673b9c9670cc8f1fb8fcd2f7c1996f45320d4d9a"

def compute_sha256(file_path: Path) -> str:
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(65536), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", help="Override output directory")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    entry_path = script_dir / "entry.png"

    if not entry_path.is_file():
        raise FileNotFoundError(f"entry.png not found at expected location: {entry_path}")

    # Verify source hash
    source_hash = compute_sha256(entry_path)
    if source_hash != EXPECTED_HASH:
        raise RuntimeError(f"Source entry.png hash mismatch! Expected {EXPECTED_HASH}, got {source_hash}")

    # Determine output destination
    output_dir = args.output_dir if args.output_dir is not None else os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_path = Path(output_dir) / "entry.png"

    # Ensure output parent directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Copy bytes verbatim
    shutil.copyfile(entry_path, output_path)

    # Verify destination hash
    dest_hash = compute_sha256(output_path)
    if dest_hash != EXPECTED_HASH:
        raise RuntimeError(f"Destination entry.png hash mismatch! Expected {EXPECTED_HASH}, got {dest_hash}")

    print(f"Successfully copied to {output_path} with SHA-256 {dest_hash}")


if __name__ == "__main__":
    main()
