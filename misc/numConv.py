def main():

    # setup
    ones = {"0":"", "1":"one", "2":"two", "3":"three", "4":"four", "5":"five", "6":"six", "7":"seven", "8":"eight", "9":"nine"}
    tens = {"0":"", "2":"twenty", "3":"thirty", "4":"forty", "5":"fifty", "6":"sixty", "7":"seventy", "8":"eighty", "9":"ninety"}
    weirds = {"10":"ten", "11":"eleven", "12":"twelve", "13":"thirteen", "14":"fourteen", "15":"fifteen", "16":"sixteen", "17":"seventeen", "18":"eighteen",
        "19":"nineteen"}
    pers = ["hundred","thousand","million","billion","trillion","quadrillion","quintillion","sextillion","septillion","octillion","nonillion","decillion"]

    De = input("Please input numerals to be converted to written format: ")
    Str = str(De)
    Len = len(Str)

    # account for string typed by user
    try:
        Int = int(Str)
    except:
        print("Sorry, that number is not supported.")
        main()

    # run main code
    else:
        #0-9
        if Len == 1:
            if Int == 0:
                Fin = "zero"

            else:
                Fin = ones[Str]

        #10-99
        elif Len == 2:
            # the weird numbers
            if Str[0] == "1":
                Fin = weirds[Str]

            else:
                Fin = tens[Str[0]]+"-"+ones[Str[1]]

        #100-999
        elif Len == 3:
            Fin = ones[Str[0]]+" hundred "+tens[Str[1]]+"-"+ones[Str[2]]

        else:
            Per = Len-2


        print("The final number is "+"\""+Fin+"\".")
        main()

main()
