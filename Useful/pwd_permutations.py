#!/usr/bin/env python3
# Author - luks (@luksecurity_)

from itertools import permutations, product

with open("passwords.txt", "r") as f:
    w = [line.strip() for line in f]

def case_permutations(w1, w2):
    c1 = [w1.lower(), w1.capitalize(), w1.upper()]
    c2 = [w2.lower(), w2.capitalize(), w2.upper()]

    return [w1+w2 for w1,w2 in product(c1,c2)]

seen = set()
with open("passwords_permuts.txt", "w") as f:
    for p in permutations(w, 2):
        if p not in seen:
            for v in case_permutations(p[0],p[1]):
                f.write(v+"\n")
