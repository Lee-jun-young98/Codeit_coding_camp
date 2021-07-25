import random

with open("vocabulary.txt", "r") as f:
    keys = list(f.keys())
    index = random.randint(0, len(keys) - 1)
    english_word = keys[index]
    korean_word = f[english_word]
    while True:
        a = input("{}: ".format(english_word))
