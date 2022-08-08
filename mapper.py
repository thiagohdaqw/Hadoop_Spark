#!/bin/python3
import sys

for line in sys.stdin:
    if not line.strip():
        continue
    words = line.split()
    words_mapped = map(lambda w: f'{w.lower()} 1\n', words)
    print("".join(words_mapped), end='')
