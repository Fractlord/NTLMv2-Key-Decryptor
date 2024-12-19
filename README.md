# NTLMv2 Key Decryptor

This project provides a Python script for decrypting the session key in NTLMv2 authentication. It uses the NTLMv2 authentication process and cryptographic elements like the NTLM hash, NTProofStr, and the encrypted session key to calculate the random session key used in SMB traffic.

## Features
- Calculates the NTLMv2 session key based on the user's credentials and NTProofStr.
- Supports verbose mode for detailed output.
- Can be used with packet capture (PCAP) files to decrypt SMB traffic.

## Requirements
- Python 3.x
- `pycryptodome` library (install with `pip install pycryptodome`)

## Installation

To use the script, clone this repository:

```bash
git clone https://github.com/Fractlord/NTLMv2-Key-Decryptor.git
cd NTLMv2-Key-Decryptor
```

## Usage

### Command-Line Arguments

| Argument       | Description                                   | Example                                      |
|----------------|-----------------------------------------------|----------------------------------------------|
| `-u, --user`    | Username (uppercase)                          | `username`                                   |
| `-d, --domain`  | Domain name (uppercase)                       | `domain`                                  |
| `-p, --password`| Password or NTLM hash                         | `somepassword`                               |
| `-n, --ntproofstr` | NTProofStr in hex format                    | `0ca6227a4f00b9654a48908c4801a0ac`          |
| `-k, --key`     | Encrypted session key (hex)                   | `c24f5102a22d286336aac2dfa4dc2e04`          |
| `-v, --verbose` | Optional, verbose output                      | `--verbose`                                  |

### Example Usage

```bash
python ntlmv2_decryptor.py -u USERNAME -d DOMAIN -p SOMEPASSWORD -n 0ca6227a4f00b9654a48908c4801a0ac -k c24f5102a22d286336aac2dfa4dc2e04 --verbose
```

### Example Output

#### Verbose Mode

When verbose mode is enabled (`--verbose`), the script provides detailed output:

```
USER WORK: username\domain
PASS HASH: 8846f7eaee8fb117ad06bdd830b7586c
RESP NT:   9e107d9d372bb6826bd81d3542a419d6
NT PROOF:  0ca6227a4f00b9654a48908c4801a0ac
KeyExKey:  c24f5102a22d286336aac2dfa4dc2e04
Random SK: 0123456789abcdef0123456789abcdef
```

#### Without Verbose Mode

Without verbose mode, the script only outputs the decrypted session key:

```
Random SK: 0123456789abcdef0123456789abcdef
```

## How It Works

1. **NTLM Hash:** The script first generates an MD4 hash of the password.
2. **ResponseNTKey:** Using the password hash, the username, and the domain, it calculates the ResponseNTKey.
3. **Key Exchange Key:** The script then uses the NTProofStr and ResponseNTKey to calculate the Key Exchange Key.
4. **Session Key Decryption:** Finally, the encrypted session key is decrypted using the Key Exchange Key with the RC4 cipher.


