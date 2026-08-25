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

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## ⚠️ Legal Disclaimer

### Educational Purpose Only
This tool is provided strictly for **educational purposes** and **authorized security testing** only. It is intended to help security professionals and students learn about security concepts in controlled environments.

### Authorized Use Only
- You must have **explicit written authorization** before testing any system you do not own
- Unauthorized access to computer systems is **illegal** and punishable under laws including but not limited to the Computer Fraud and Abuse Act (CFAA), Computer Misuse Act, and similar legislation worldwide
- Only use this tool on systems you own, have permission to test, or in isolated lab environments

### No Warranty
This software is provided "AS IS" without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. The author makes no representations or warranties regarding the accuracy, completeness, or reliability of this software.

### Limitation of Liability
**In no event shall the author (Nikhil Nagpure) be liable for any direct, indirect, incidental, special, exemplary, or consequential damages (including, but not limited to, procurement of substitute goods or services; loss of use, data, or profits; or business interruption) however caused and on any theory of liability, whether in contract, strict liability, or tort (including negligence or otherwise) arising in any way out of the use of this software, even if advised of the possibility of such damage.**

### User Responsibility
- The user assumes **full responsibility** for any consequences resulting from the use of this tool
- The author is **not responsible** for any misuse, damage, or illegal activities performed with this software
- Users are solely responsible for ensuring compliance with all applicable local, state, national, and international laws and regulations

### Indemnification
By using this software, you agree to **indemnify, defend, and hold harmless** the author from and against any and all claims, liabilities, damages, losses, costs, and expenses (including reasonable attorneys fees) arising from or related to your use of this software.

### Responsible Disclosure
If you discover vulnerabilities using this tool, please follow responsible disclosure practices and report them to the affected parties through appropriate channels.

---

**By using this software, you acknowledge that you have read, understood, and agree to be bound by this disclaimer.**
## License

This project is for educational purposes only. Use responsibly and ethically.

---

**Remember**: Always use strong passwords when protecting PDFs!
