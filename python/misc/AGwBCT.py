# adventure game with better choice thingies
# by CAS (c) 2020. All right reserved.

# NEEDED CHANGES: fix inv cmds

def reset():
    global p
    global inv
    global devMode
    
    p = 1
    inv = []
    devMode = False
    cmd = ""
    full = ""

reset()

print("Welcome to adventure game with better choice thingies!")
print("Created in 2020 by CAS.\n")

def choice():
    global ch
    global devMode
    global inv
    
    ch = input(" > ").lower()

    if ch == "qwerty":
        devMode = True
        path()
    elif ch == "north" or ch == "n":
        ch = "goNorth"
    elif ch == "east" or ch == "e":
        ch = "goEast"
    elif ch == "south" or ch == "s":
        ch = "goSouth"
    elif ch == "west" or ch == "w":
        ch = "goWest"
    elif ch == "down" or ch == "d":
        ch = "goDown"
    elif ch == "up" or ch == "u":
        ch = "goUp"
    elif "inv" in ch or "inventory" in ch:
        if len(inv) == 0:
            
            print("You have nothing in your inventory.\n")
            choice()
            
        elif len(inv) != 0:
            
            print(len(inv)+" items in your inventory:")
            for item in inv:
                print(" - "+item)
                
            print("")
            choice()
            
        else:
            print("Sorry, inventory error.\n")
            choice()
            
    else:
        ch = ch

def path():
    global p
    global ch
    global devMode

    def again():
        againChoice = input("Play again? [y/n]: ").lower()

        if againChoice == "y" or againChoice == "yes":
            print("\n\n")
            reset()
            play()
            
        else:
            print("Goodbye.")

    # temp for devs - disable with "#"
    # print("CURRENT PATH IS "+str(p)+"\n")
    # print("DEVMODE: "+str(devMode)+"\n")

    def con():
        global devMode
        global p
        global inv

        full = input("c> ")
        print("")
        cmd = full.split()

        if cmd[0] == "path":
            
            try:
                p = int(cmd[1])
                print("Jumping to path "+str(p)+":")
                devMode = False
                path()

            except:
                print("Incorrect argument for path command.")
                con()

        elif cmd[0] == "help":
            try:
                if cmd[1] == "help":
                    print("Help command:\nThe help command brings up the help menu")
                    print("or helps with a specific command.\n\nSyntax:\n - help")
                    print(" - help <command>\n")
                    con()
                elif cmd[1] == "path":
                    print("Path command:\nThe path command allows you to jump to a")
                    print("path in the game.\n\nSyntax:\n - path <number>\n")
                    con()
                elif cmd[1] == "exit":
                    print("Exit command:\nThe exit command brings you back to the")
                    print("regular adventure game.\n\nSyntax:\n - exit\n")
                    con()
                elif cmd[1] == "setpack":
                    print("Iventory command:\nThe inventory command allows you")
                    print("to check the player's inventory, or add or remove items.")
                    print("\nSyntax:\n - setpack add <item>\n - setpack remove <item>")
                    print(" - setpack query\n")
                    con()
                else:
                    print('There is no "'+cmd[1]+'" command to get help with.')
                    con()
            except:
                print("List of commands:\n - help [command]\n - path <number>\n - exit")
                print(" - setpack <args>")
                print('Type "help <command>" to get help with a specific one.\n')
                con()

        elif cmd[0] == "exit":
            print("Back to normal:")
            devMode = False
            full = ""
            cmd = []
            path()

        elif cmd[0] == "setpack":
            try:
                if cmd[1] == "add":
                    try:
                        inv.append(cmd[2])

                    except:
                        print("Inventory add command must have an arguement.")

                    con()

                elif cmd[1] == "remove":
                    try:
                        inv.remove(cmd[2])

                    except:
                        print("Error.")

                    con()

                elif cmd[1] == "query":
                    if len(inv) == 0:
                        print("The player has nothing in their inventory.")
                        con()

                    elif len(inv) != 0:
                        print(len(inv)+" items in player's inventory:")
                        for item in inv:
                            print(" - "+item)

                        con()

                    else:
                        print("Inventory error.")
                        con()

                else:
                    print("Incorrect argument for inventory command.")
                    con()

            except:
                print("Incorrect argument for inventory command.")
            con()

        else:
            print('There is no command "'+full+'"')
            con()

    if devMode:
        print("\nAh, so you found the secret code!")
        con()
    
    # error - leads to beginning (1)
    elif p == 0:
        input("How did you get here? Go home, hacker.\n")
        p = 1
        path()

    # beginning - leads to south nothing (3) and path (2)
    elif p == 1:
        print("You are sitting on a white swing in the middle of a sunny field.")
        print("You aren't too sure how you got here. There is nothing to the")
        print("north, south, or east, but to the west, there is the start of a")
        print("small path.\n\nYou can choose by typing a direction.")

        def ev():
            global p
            choice()

            print("")
            if ch == "goNorth":
                print("There is nothing to the north.")
                ev()
            elif ch == "goEast":
                print("There is nothing to the east.")
                ev()
            elif ch == "goSouth":
                p = 3
                path()
            elif ch == "goWest":
                p = 2
                path()
            else:
                print("Sorry, what?")
                ev()

        ev()

    # path/door - leads to open door (4)
    elif p == 2:
        print("You follow the path for a while. It leads to a small bridge which")
        print("crosses a brook. Then the path continues, eventually leading")
        print("to a hill. In the side of the hill is a pair of double doors and")
        print("a very tiny window, which has closed brown curtains on the other")
        print("side. The path stretches to the east behind you.")

        def ev():
            global p
            choice()

            print("")
            if "open" in ch and "door" in ch:
                p = 4
                path()
            elif ch == "goNorth":
                print("There is nothing to the north.")
                ev()
            elif ch == "goEast":
                p = 5
                path()
            elif ch == "goSouth":
                print("There is nothing to the south.")
                ev()
            elif ch == "goWest":
                print("You must open the door first.")
                ev()
            elif "smash" in ch or "break" in ch:
                print("What are you a vandal or something? Be nice!")
                ev()
            else:
                print("Sorry, what?")
                ev()

        ev()

    # south nothing - leads to beginning 2 (5) and trapdoor (6)
    elif p == 3:
        print("There is nothing to the south, but you walk over there anyway.")
        print("The swing is to the north of you, but there is nothing else.")

        def ev():
            global p
            choice()

            print("")
            if ch == "goNorth":
                p = 5
                path()
            elif ch == "goEast":
                print("There is nothing to the east.")
                ev()
            elif ch == "goSouth":
                p = 6
                path()
            elif ch == "goWest":
                print("There is nothing to the west.")
                ev()
            else:
                print("Sorry, what?")
                ev()

        ev()

    # temporary: open door - only ending
    elif p == 4:
        # END 0: temporary
        print("You open the door. THE END: Temporary Dev Ending. (ending 0)")
        again()

    # beginning 2 - leads to path (2)
    elif p == 5:
        print("You are back at the white swing in the middle of the sunny field.")
        print("There is nothing to the north, south, or east, but to the west,")
        print("there is the start of a small path. You feel a sense of deja vu.")

        def ev():
            global p
            choice()

            print("")
            if ch == "goNorth":
                print("There is nothing to the north.")
                ev()
            elif ch == "goEast":
                print("There is nothing to the east.")
                ev()
            elif ch == "goSouth":
                print("There is nothing to the south.")
                ev()
            elif ch == "goWest":
                p = 2
                path()
            else:
                print("Sorry, what?")
                ev()

        ev()

    # trapdoor - leads to beginning 2 (5) and 2 endings
    elif p == 6:
        print("You once again have disobeyed the game's instructions. Anyway,")
        print("there is a wooden trapdoor set into the ground here. Far to the")
        print("north is the white swing. There is nothing else around.")

        def ev():
            global p
            choice()

            print("")
            if ch == "goNorth":
                print("You go extra far north, back to the swing.")
                p = 5
                path()
            elif ch == "goEast":
                print("There is nothing to the east.")
                ev()
            elif ch == "goSouth":
                # END 2: 2 mch south
                print("STOP trying to go SOUTH already! You have been killed by")
                print("The developer. THE END: 2 Much SOUTH. (ending 2)")
                again()
            elif ch == "goWest":
                print("There is nothing to the west.")
                ev()
            elif ch == "goDown":
                print("You must open the trapdoor to go down.")
                ev()
            elif "open" in ch or "lift" in ch:
                # END 1: sucked into void
                print("You open the trapdoor...")
                print("Suddenly, you are sucked into the void. THE END: Sucked into")
                print("the void. (ending 1)")
                again()

        ev()
        
    else:
        p = 0
        path()

def play():
    path()

play()
