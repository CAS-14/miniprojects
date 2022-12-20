from random import randint
from math import floor

filename = input("Path to text file: ")

f = open(filename, "r")
text = f.read()
f.close()

times = floor(len(text) / 100)

for i in range(times):
    length = randint(10, 100)
    start = randint(0, len(text) - 1)

    snippet = text[start : start + length]

    text = text.replace(snippet, "", 1)
    place = randint(0, len(text))
    text = text[0 : place] + snippet + text[place+1 : len(text) - 1]

with open("output.txt", "w+") as f:
    f.write(text)

print(text)