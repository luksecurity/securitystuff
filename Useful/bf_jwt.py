#!/usr/bin/env python3

import jwt
import sys
from colorama import Fore, Style

def main():
    token = input("Enter JWT token : ")

    with open('wordlist.txt', "r", encoding="ISO-8859-1") as f:
        l = f.readlines()

    for x in l:
        enc = jwt.encode({"role": "guest"}, x.strip(), algorithm='HS512')
        if enc == token:
            print(Fore.GREEN + '[+] The secret has been found! :)' + Style.RESET_ALL)
            print(Fore.GREEN + '[+] Secret : ' + x.strip() + Style.RESET_ALL)
            sys.exit(0)

    print(Fore.RED + '[-] Secret not found! :(' + Style.RESET_ALL)

if __name__ == '__main__':
    main()
