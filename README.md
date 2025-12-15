# PDF Protection Tool

⚠️ **EDUCATIONAL PURPOSE ONLY** - This tool is designed for authorized security testing and educational purposes.

## Overview

A simple PDF password protection tool that adds encryption and password protection to PDF files. Useful for learning about PDF security and protecting sensitive documents.

## Features

- **Password Protection**: Add password protection to PDF files
- **Encryption**: Encrypt PDF files with user password
- **Simple Interface**: Easy-to-use command-line tool
- **Educational**: Learn about PDF security

## Installation

### Requirements

- Python 3.8+
- PyPDF2 library

### Setup

```bash
# Clone the repository
git clone https://github.com/5h4d0wn1k/pdf-protect.git
cd pdf-protect

# Install dependencies
pip install PyPDF2

# Verify installation
python pdf_protect.py --help
```

## Usage

### Basic Usage

```bash
# Protect a PDF with password
python pdf_protect.py \
  --input document.pdf \
  --output protected.pdf \
  --password "SecurePassword123!"
```

## Command-Line Options

| Option | Description |
|--------|-------------|
| `--input` | Source PDF file (required) |
| `--output` | Destination protected PDF file (required) |
| `--password` | Password to protect PDF (required) |

## Examples

### Example 1: Protect a Document

```bash
# Add password protection
python pdf_protect.py \
  --input sensitive_document.pdf \
  --output protected_document.pdf \
  --password "MySecurePassword123!"
```

### Example 2: Batch Protection

```bash
# Protect multiple PDFs
for pdf in *.pdf; do
  python pdf_protect.py \
    --input "$pdf" \
    --output "protected_$pdf" \
    --password "SecurePassword123!"
done
```

## Output

```
[+] Protected PDF written to protected.pdf
```

## Security Notes

- **Password Strength**: Use strong passwords (12+ characters, mixed case, numbers, symbols)
- **Password Storage**: Store passwords securely, don't hardcode
- **File Permissions**: Ensure protected PDFs have appropriate file permissions

## Use Cases

- **Document Security**: Protect sensitive PDF documents
- **Educational Purposes**: Learn about PDF encryption
- **Security Testing**: Test PDF protection mechanisms

## Legal Disclaimer

⚠️ **IMPORTANT**: This tool is for authorized security testing and educational purposes only.

- Only protect PDFs you own or have explicit written authorization to protect
- Follow responsible disclosure practices
- Comply with all applicable laws and regulations

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is for educational purposes only. Use responsibly and ethically.

---

**Remember**: Always use strong passwords when protecting PDFs!
