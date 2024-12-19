import hashlib
import hmac
import argparse
from Cryptodome.Cipher import ARC4

# Function to generate the encrypted session key
def generateEncryptedSessionKey(keyExchangeKey, exportedSessionKey):
    cipher = ARC4.new(keyExchangeKey)
    sessionKey = cipher.encrypt(exportedSessionKey)
    return sessionKey

# Set up command-line argument parser
parser = argparse.ArgumentParser(description="Calculate the Random Session Key based on data from a PCAP (maybe).")
parser.add_argument("-u", "--user", required=True, help="Username (e.g., george)")
parser.add_argument("-d", "--domain", required=True, help="Domain name (e.g., DOMAIN)")
parser.add_argument("-p", "--password", required=True, help="Password or NTLM hash (e.g., password)")
parser.add_argument("-n", "--ntproofstr", required=True, help="NTProofStr in hex format (e.g., 0ca6227a4f00b9654a48908c4801a0ac)")
parser.add_argument("-k", "--key", required=True, help="Encrypted session key in hex (e.g., c24f5102a22d286336aac2dfa4dc2e04)")
parser.add_argument("-v", "--verbose", action="store_true", help="Increase output verbosity")

# Parse the command-line arguments
args = parser.parse_args()

# Convert user and domain to uppercase and encode to utf-16le
user = str(args.user).upper().encode('utf-16le')
domain = str(args.domain).upper().encode('utf-16le')

# Create 'NTLM' hash of the password
passw = args.password.encode('utf-16le')
hash1 = hashlib.new('md4', passw)
password = hash1.digest()

# Calculate the ResponseNTKey using HMAC-MD5
h = hmac.new(password, digestmod=hashlib.md5)
h.update(user + domain)
respNTKey = h.digest()

# Use NTProofStr and ResponseNTKey to calculate the Key Exchange Key
NTproofStr = bytes.fromhex(args.ntproofstr)
h = hmac.new(respNTKey, digestmod=hashlib.md5)
h.update(NTproofStr)
KeyExchKey = h.digest()

# Calculate the Random Session Key by decrypting Encrypted Session Key with Key Exchange Key via RC4
RsessKey = generateEncryptedSessionKey(KeyExchKey, bytes.fromhex(args.key))

# If verbose mode is enabled, display detailed output
if args.verbose:
    print("USER WORK: " + user.decode('utf-16le') + "\\" + domain.decode('utf-16le'))
    print("PASS HASH: " + password.hex())
    print("RESP NT:   " + respNTKey.hex())
    print("NT PROOF:  " + NTproofStr.hex())
    print("KeyExKey:  " + KeyExchKey.hex())

# Output the final Random Session Key
print("Random SK: " + RsessKey.hex())
