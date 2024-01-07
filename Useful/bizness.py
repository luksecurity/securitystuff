#!/usr/bin/env python3

import hashlib
import base64
import os

hash_type = "SHA1"
salt = "d"
search = "$SHA1$d$uP0_QaVBpDWFeo8-dRzDqRwXQ2I="
wordlist = './rockyou.txt'

def hash_password(hash_type, salt, password):
    hash_obj = hashlib.new(hash_type)
    hash_obj.update(salt.encode('utf-8'))
    hash_obj.update(password)
    hashed_bytes = hash_obj.digest()
    return f"${hash_type}${salt}${base64.urlsafe_b64encode(hashed_bytes).decode('utf-8').replace('+', '.')}"

def search_password(search, wordlist):
    with open(wordlist, 'r', encoding='latin-1') as password_list:
        for password in password_list:
            hashed_password = hash_password("SHA1", "d", password.strip().encode('utf-8'))
            if hashed_password == search:
                print(f'Found Password: {password.strip()}, hash: {hashed_password}')

search_password(search, wordlist)
