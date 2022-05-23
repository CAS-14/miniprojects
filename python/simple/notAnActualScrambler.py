# This program mangles words

from random import randint

norm = input("Enter a word to be scrambled: ")
chars = list(norm)
final = ""

for i in range(len(norm)):
    final = final+(chars[randint(0, (len(norm)-1))])

print("Your scrambled word is \""+final+"\".")
