#!/usr/bin/env python3
# Author - luks (@luksecurity_)

import cryptocode

def bruteforce(enc_file, wordlist):
    with open(enc_file, "r") as enc_file:
        encc_text = enc_file.read().strip()

    with open(wordlist, "r") as wordlist:
        for password in wordlist:
            password = password.strip()
            decrypt_text = cryptocode.decrypt(encc_text, password)

            if decrypt_text:
                print(f"[+] Password found: {password}")
                print(f"[+] Decrypted content:")
                print(decrypt_text)
                return

    print(f"[-] No password found :(")

if __name__ == "__main__":
    enc_file = "master_passwd.txt"
    wordlist = "rockyou.txt"

    bruteforce(enc_file, wordlist)
