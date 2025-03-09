#!/usr/bin/env python3
# Author - luks (@luksecurity_)

import itertools

base = "Motdepasse"

def generate_case_permutations(word):
    return set("".join(p) for p in itertools.product(*[(c.lower(), c.upper()) for c in word]))

years = [str(y) for y in range(2017, 2026)]

special_chars = "!@#$%^&*()-_=+<>?/"

with open("password.txt", "w") as f:
    for perm in generate_case_permutations(base):
        for year, char in itertools.product(years, special_chars):
            f.write(f"{perm}{year}{char}\n")

print("Wordlist générée : password.txt")
