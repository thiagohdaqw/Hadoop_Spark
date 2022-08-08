#!/bin/python3
import sys

current_word = None
current_count = 0
count_words = 0


def print_word_info():
    if not current_word:
        return

    print(current_word, current_count)

    if (fstLetter := current_word[0].upper()) in 'SPR':
        print(f'__TOTAL_{fstLetter}_WORDS__ {current_count}')

    if (ln := len(current_word)) in [6, 8, 11]:
        print(f'__TOTAL_{ln}_WORDS__ {current_count}')


for line in sys.stdin:
    if not line.strip():
        continue
    
    word, count = line.split()

    try:
        count = int(count)
    except ValueError:
        continue
    
    count_words += count

    if word == current_word:
        current_count += count
        continue
    
    print_word_info()
    current_word = word
    current_count = count


print_word_info()
print('__TOTAL_WORDS__', count_words)
