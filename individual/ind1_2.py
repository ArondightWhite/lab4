import sys

word = input("Write some word: ")

if ' ' in word:
    print("You write sentence, not word", file=sys.stderr)
    exit(1)

print(word[::-1])
