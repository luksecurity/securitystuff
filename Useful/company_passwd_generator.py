#!/usr/bin/env python3
# Author - luks (@luksecurity_)

import itertools

company_variants = ["company", "Company", "etc"]

years = [str(y) for y in range(2018, 2026)]
special_chars = ["!", "@", "#", "$", "%", "&", "*", "-", "_", "."]
separators = ["", "_", "-"]
suffixes = ["", "01", "02", "123", "admin", "pass"]
leet_map = {"a": "4", "e": "3", "i": "1", "o": "0", "s": "5"}

def leet_transform(word):
    return "".join(leet_map.get(c.lower(), c) for c in word)

wordlist = set()

for company, sep, year, suffix in itertools.product(company_variants, separators, years, suffixes):
    base = f"{company}{sep}{year}{suffix}"
    wordlist.add(base)
    wordlist.add(leet_transform(base))

    for char in special_chars:
        special_base = f"{company}{sep}{year}{char}{suffix}"
        wordlist.add(special_base)
        wordlist.add(leet_transform(special_base))

for c1, c2, sep, year, suffix in itertools.product(company_variants, company_variants, separators, years, suffixes):
    if c1 != c2:
        base = f"{c1}{sep}{c2}{year}{suffix}"
        wordlist.add(base)
        wordlist.add(leet_transform(base))

        for char in special_chars:
            special_base = f"{c1}{sep}{c2}{year}{char}{suffix}"
            wordlist.add(special_base)
            wordlist.add(leet_transform(special_base))

with open("company_password.txt", "w") as f:
    f.write("\n".join(wordlist))

print(f"Wordlist generated with {len(wordlist)} passwords!")
