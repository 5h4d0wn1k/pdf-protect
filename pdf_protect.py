"""
PDF protection helper (lab use).
Wraps PyPDF2 (needs to be installed) to set an owner/user password and basic permissions.
"""

from __future__ import annotations

import argparse
import sys


def protect_pdf(input_path: str, output_path: str, password: str) -> None:
    """
    Protect a PDF file with a password.
    
    Reads the input PDF, encrypts it with the provided password,
    and writes the protected PDF to the output path.
    
    Args:
        input_path: Path to the source PDF file.
        output_path: Path where the protected PDF will be written.
        password: Password to encrypt the PDF with.
        
    Raises:
        ImportError: If PyPDF2 is not installed.
        FileNotFoundError: If the input PDF does not exist.
        Exception: If PDF processing fails.
    """
    try:
        from PyPDF2 import PdfReader, PdfWriter  # type: ignore
    except Exception:
        print("PyPDF2 not installed. pip install PyPDF2", file=sys.stderr)
        sys.exit(1)

    reader = PdfReader(input_path)
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    writer.encrypt(password)
    with open(output_path, "wb") as f:
        writer.write(f)
    print(f"[+] Protected PDF written to {output_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Protect a PDF with a password (requires PyPDF2).")
    parser.add_argument("--input", required=True, help="Source PDF.")
    parser.add_argument("--output", required=True, help="Destination protected PDF.")
    parser.add_argument("--password", required=True, help="Password to set.")
    args = parser.parse_args()

    protect_pdf(args.input, args.output, args.password)


if __name__ == "__main__":
    main()
