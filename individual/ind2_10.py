import sys

string = input("Write some words with 'жи' и 'ши': ")

words = string.split(' ')

for word in words:
    if 'жы' in word.lower():
        print(f"You have a mistake in: {word}\n"
              f"Write was {word.lower().replace('жы', 'жи')}")
    elif 'шы' in word.lower():
        print(f"You have a mistake in: {word}\n"
              f"Write was {word.lower().replace('шы', 'ши')}")
    else:
        print(f"You wrote {word} correctly")
