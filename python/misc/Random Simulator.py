# RANDOM SIMULATOR created by CAS,
# copyright (c) 2020. All rights reserved.

from time import sleep
import datetime
import random

def err():
    print(random.choice(["\nSorry, that's an error.\n\nTHE END\nError Ending (0)",
                         "\nYOU DIRTY HACKER YOU!\n\nTHE END\nError Ending (0)",
                         "\nOopsie oopsie, you did a floopsie.\n\nNOW FACE THE CONSEQUENCES!\n\nTHE END\nError Ending (0)"]))

# choice system
def ch():
    chStr = input("> ")
    print("")
    if chStr == "1":
        return 1
    elif chStr == "2":
        return 2
    elif chStr == "3":
        return 3

def findWeekday():
    weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday",
                "Sunday"]
    return weekdays[datetime.date(datetime.date.today().year,
                                  datetime.date.today().month,
                                  datetime.date.today().day).weekday()]

def intro():
# "title" screen
    print("----------------------------\nWelcome to RANDOM SIMULATOR\npress",
          "[enter] to start\n----------------------------")
    input("")

    if input("Do you need to know how to play? [y/n] > ") == "y":
        print("\nHOW TO PLAY:\nRandom Simulator is a game about making choices",
              "and doing random stuff. In the\ngame, you are often given choices",
              "in this format:\n\nEXAMPLE: What do you want to do?\n[1] Read the",
              "example\n[2] Skim the example\n[3] Eat the example\n>\n\nIn the",
              "game, you would simply type the number of the choice",
              "and press [enter]. I hope you understand these instructions, and",
              "enjoy!\n")
        input("Press [enter] to begin the game!")

    print("\nYou are in your house on this nice "+findWeekday()+".\n[1] order a",
          "pizza\n[2] play some video games\n[3] phone a friend")
    chn = ch()
    if chn == 1:
        chPizza()
    else:
        print("It's a work in progress, ok?\n\nTHE END\nWIP Ending (-1)")
        playAgain()

def playAgain():
    if input("Play again? [y/n]\n> ") == "y":
        print("\n\n")
        intro()
    else:
        print("\n\nHave a nice day!")

def chPizza():
    print("You call the pizza place. What toppings would you like?\n[1]",
          "Extra Spicy Super Chile Peppers\n[2] No Extra Spicy Super Chile",
          "Peppers")
    ch()
    delivery()

def delivery():
    print("The "+random.choice(["man","woman"])+" on the phone says \"Okay\"",
          "and the pizza is on its way\n")
    sleep(1)
    print("You wait...\n")
    sleep(1)
    print("Ah! Finally the pizza is here. At the door, you see the Extra Spicy",
          "Super Chile Pepper pizza in the pizza guy's hands.\n[1] Pay for the pizza.\n[2] \"This isn't",
          "what I ordered!\"")
    chn = ch()
    if chn == 1:
        print("You sit down at the table. You take a bite of the pizza.",
              "It is too spicy and you die.\n\nTHE END\nPizza Death Ending (1)")
        playAgain()
    elif chn == 2:
        print("Pizza Guy: It's not?")
        sleep(0.5)
        print("\nYou: No! I didn't order these peppers!")
        sleep(0.5)
        print("\nRetaliate?\n[1] Grab the pizza and slam the door without",
              "paying\n[2] Say that you understand, pay, and take the pizza")
        chn = ch()
        if chn == 1:
            print("You take the pizza without paying. The pizza man smashes",
                  "down your door and kills you, then eats you whole.\n\n",
                  "THE END\nPizza Man Kills You Ending (2)")
            playAgain()
        elif chn == 2:
            print("You sit down at the table. You take a bite of the pizza.",
              "It is too spicy and you die.\n\nTHE END\nPizza Death Ending (3)")
        else:
            err()
    else:
        err()

intro()
