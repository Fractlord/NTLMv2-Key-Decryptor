# NTLMv2 Key Decryptor

A Python-based tool to simulate NTLMv2 authentication processes and decrypt session keys for SMB traffic decryption. This project provides insights into the cryptographic mechanisms of NTLMv2 and serves educational purposes in network security.

## Features
- Simulates NTLMv2 key exchange and session key derivation.
- Decrypts session keys using RC4.
- Outputs decrypted session keys for SMB traffic analysis (e.g., in Wireshark).


- Python 3.6+
- `pycryptodome`

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Fractlord/NTLMv2-Key-Decryptor.git

## Usage

### Command-Line Arguments

| Argument         | Description                              | Example                           |
|------------------|------------------------------------------|-----------------------------------|
| `-u`, `--user`   | Username (uppercase)                     | `mrealman`                        |
| `-d`, `--domain` | Domain name (uppercase)                  | `WORKGROUP`                       |
| `-p`, `--password` | Password or NTLM hash                  | `Blockbuster1`                    |
| `-n`, `--ntproofstr` | NTProofStr in hex format             | `0ca6227a4f00b9654a48908c4801a0ac`|
| `-k`, `--key`    | Encrypted session key (hex)              | `c24f5102a22d286336aac2dfa4dc2e04`|
| `-v`, `--verbose` | Optional, verbose output                | `--verbose`                       |

### Example Usage

Run the script with the required arguments:

```bash
python ntlmv2_key_decryptor.py -u mrealman -d WORKGROUP -p Blockbuster1 -n 0ca6227a4f00b9654a48908c4801a0ac -k c24f5102a22d286336aac2dfa4dc2e04 --verbose





