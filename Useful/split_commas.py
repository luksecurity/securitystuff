#!/usr/bin/env python3

with open('file.txt', 'r') as f:

    for i in f:
        new_line = i.replace(',', '\n')
        print(new_line, end="")
