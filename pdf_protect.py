"""
PDF protection helper (lab use).
Wraps PyPDF2 (needs to be installed) to set an owner/user password and basic permissions.
"""

from __future__ import annotations

import argparse
import sys


def main() -> None:
    parser = argparse.ArgumentParser(description="Protect a PDF with a password (requires PyPDF2).")
    parser.add_argument("--input", required=True, help="Source PDF.")
    parser.add_argument("--output", required=True, help="Destination protected PDF.")
    parser.add_argument("--password", required=True, help="Password to set.")
    args = parser.parse_args()

    try:
        from PyPDF2 import PdfReader, PdfWriter  # type: ignore
    except Exception:
        print("PyPDF2 not installed. pip install PyPDF2", file=sys.stderr)
        sys.exit(1)

    reader = PdfReader(args.input)
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    writer.encrypt(args.password)
    with open(args.output, "wb") as f:
        writer.write(f)
    print(f"[+] Protected PDF written to {args.output}")


if __name__ == "__main__":
    main()
