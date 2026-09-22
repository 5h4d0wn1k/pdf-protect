> **⚠️ EDUCATIONAL USE ONLY — AUTHORIZED TESTING ONLY.**
> This project exists for education, research, and **defense of systems you own
> or hold explicit written authorization to assess**. Unauthorized use is
> prohibited and may be illegal. Read [ETHICS.md](ETHICS.md) and
> [SCOPE.md](SCOPE.md) before use. Use at your own risk; **AS IS**, no warranty.

# PDF Protect — PDF Password Protection & Encryption Tool

PDF Protect is a small command-line utility that encrypts PDF files with a
user password using **PyPDF2**. It is built for educational learning about
**PDF security**, document **encryption**, and authorized security testing of
your own PDF workflows.

[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Stars](https://img.shields.io/github/stars/5h4d0wn1k/pdf-protect)](https://github.com/5h4d0wn1k/pdf-protect/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/5h4d0wn1k/pdf-protect)](https://github.com/5h4d0wn1k/pdf-protect/commits)
[![Issues](https://img.shields.io/github/issues/5h4d0wn1k/pdf-protect)](https://github.com/5h4d0wn1k/pdf-protect/issues)

Password-protect a PDF in one command: point it at an input file, a destination
file, and a password, and it writes an encrypted PDF ready for safe sharing.

## Why PDF Protect

Password protection is one of the simplest and most widely used access controls
for documents. PDF Protect demos the underlying mechanism — reading a PDF,
walking its pages, and encrypting the output via PyPDF2 — so you learn exactly
what "protecting a PDF" means under the hood. Used responsibly on documents you
own, it's a practical building block for handling sensitive PDFs (contracts,
invoices, reports) and for understanding what attackers might or might not be
able to do with an unprotected file.

## Features

- **Password encryption** — encrypts a PDF so a user password is required to
  open it (`writer.encrypt(password)` via PyPDF2).
- **Page preservation** — every page of the input document is copied to the
  output before encryption.
- **Simple CLI** — three required flags: `--input`, `--output`, `--password`.
- **Verified dependency** — requires `PyPDF2>=3.0.0` (`requirements.txt`).
- **Clear output** — prints `[+] Protected PDF written to <path>` on success
  and exits non-zero with a hint if PyPDF2 is missing.

## Quickstart

Prerequisites: Python 3.8+ and PyPDF2.

```bash
# Install dependencies
pip install -r requirements.txt

# Check the CLI
python pdf_protect.py --help

# Protect a PDF
python pdf_protect.py \
  --input document.pdf \
  --output protected.pdf \
  --password "SecurePassword123!"
```

### Batch protect several PDFs

```bash
for pdf in *.pdf; do
  python pdf_protect.py \
    --input "$pdf" \
    --output "protected_$pdf" \
    --password "SecurePassword123!"
done
```

## Project structure

```
pdf_protect.py    the CLI/encryption entry point
requirements.txt  Python dependencies (PyPDF2)
LICENSE           MIT license
ETHICS.md         intended use and authorization rules
SCOPE.md          the four-question authorized-testing checklist
SECURITY.md       vulnerability reporting
```

## Documentation

- [ETHICS.md](ETHICS.md) — educational and authorized-use policy.
- [SCOPE.md](SCOPE.md) — when you are allowed to run this tool.
- [SECURITY.md](SECURITY.md) — reporting vulnerabilities.
- [CONTRIBUTING.md](CONTRIBUTING.md) — how to contribute safely.
- [CHANGELOG.md](CHANGELOG.md) — release history.

## Security notes

Use strong passwords (12+ characters, mixed case, numbers, symbols), store them
in a secrets manager rather than hardcoding them, and keep output permissions
restricted. This tool only protects files **you own** or are authorized to
handle.

## License

[MIT](LICENSE). Educational and authorized-use software — use at your own risk.
By using it you accept full responsibility for lawful use in your jurisdiction.