import random
import string

WORDS_PER_LINE = 1_000
TOTAL_LINES = int(1e8 / WORDS_PER_LINE)
MAX_CHAR_PER_WORD = 12
MIN_CHAR_PER_WORD = 1

def gen_random_word():
    len = random.randint(MIN_CHAR_PER_WORD, MAX_CHAR_PER_WORD)
    return "".join(random.choices(string.ascii_letters, k=len))

for _ in range(TOTAL_LINES):
    words = (gen_random_word() for _ in range(WORDS_PER_LINE))
    print(" ".join(words))
