#!/usr/bin/env python3
# Author - luks (@luksecurity_)

import argparse
import cryptocode
import sys

def bruteforce(enc_file, wordlist):
    with open(enc_file, "r") as enc_file:
        encc_text = enc_file.read().strip()

    with open(wordlist, "r") as wordlist_file:
        for password in wordlist_file:
            password = password.strip()
            decrypt_text = cryptocode.decrypt(encc_text, password)

            if decrypt_text:
                print(f"[+] Password found: {password}")
                print(f"[+] Decrypted content:")
                print(decrypt_text)
                return

    print(f"[-] No password found :(")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Decrypt pswm master password")
    parser.add_argument("-m", "--master", required=True, help="Path to the master password file")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to the wordlist file")

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()
    enc_file = args.master
    wordlist = args.wordlist

    bruteforce(enc_file, wordlist)
