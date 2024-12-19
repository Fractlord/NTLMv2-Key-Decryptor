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

Command-Line Arguments
Argument	Description	Example
-u, --user	Username (uppercase)	mrealman
-d, --domain	Domain name (uppercase)	WORKGROUP
-p, --password	Password or NTLM hash	Blockbuster1
-n, --ntproofstr	NTProofStr in hex format	0ca6227a4f00b9654a48908c4801a0ac
-k, --key	Encrypted session key (hex)	c24f5102a22d286336aac2dfa4dc2e04
-v, --verbose	Optional, verbose output	--verbose


## Running the script

 ```bash
python ntlm_key_decryptor.py -u <USERNAME> -d <DOMAIN> -p <PASSWORD> -n <NTPROOFSTR> -k <ENCRYPTED_SESSION_KEY>




