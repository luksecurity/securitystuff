#!/usr/bin/env python3
# Author - Luks (@luksecurity_)

import argparse
import hashlib
from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import unpad
from binascii import unhexlify

def decrypt_openfirepass(ciphertext, key):
    cypher = Blowfish.new(hashlib.sha1(key.encode()).digest(), Blowfish.MODE_CBC, iv=ciphertext[:8])
    decrypted_data = cypher.decrypt(ciphertext[8:])
    return unpad(decrypted_data, Blowfish.block_size)

def main():
    parser = argparse.ArgumentParser(description="Decrypt Openfire password")
    parser.add_argument("-e", "--enc", help="The ciphertext in hexadecimal format", required=True)
    parser.add_argument("-k", "--key", help="The key used for decryption", required=True)
    args = parser.parse_args()

    try:
        ciphertext = unhexlify(args.enc)
    except ValueError:
        print("Invalid hex string provided for ciphertext.")
        return

    try:
        plaintext = decrypt_openfirepass(ciphertext, args.key)
        print("Decrypted password:", plaintext.decode())
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
