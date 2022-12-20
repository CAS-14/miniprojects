import string
import itertools
from time import sleep

print("This will simulate monkeys on typewriters.")
input("Press enter to begin")

sleep(3)
print("\n\n\n\n\n\n\n\n\n\n")

index = 1
while index < 7:
    for word in itertools.product(string.ascii_lowercase, repeat=index):
        print(''.join(word))
    index += 1
