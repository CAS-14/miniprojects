# better factorial

def fact():
    num = input("> ")

    if "." in num or "-" in num:
        print("Sorry, but that is not a valid integer.")

    elif num.isnumeric():
        num = int(num)
        mult = num-1
        org = num

        while mult != 0:
            num *= mult
            mult -= 1

        print("Calculation complete. "+str(org)+"! = "+str(num))

    else:
        print("Sorry, but that is not a valid integer.")

    fact()

fact()
