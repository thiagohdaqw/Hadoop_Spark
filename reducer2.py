#!/bin/python3
import sys

current_word = None
current_count = 0


def print_word_info():
    if not current_word:
        return

    print(current_word, current_count)


for line in sys.stdin:
    if not line.strip():
        continue

    word, count = line.split()

    try:
        count = int(count)
    except ValueError:
        continue
    
    if word == current_word:
        current_count += count
        continue
    
    print_word_info()
    current_word = word
    current_count = count


print_word_info()
