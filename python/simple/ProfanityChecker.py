def main():
    bad = ["fudge", "poop"]

    par = input("Enter a paragraph: ")

    for word in bad:

        poss = [word.upper(), word.capitalize(), word]
        for word in poss:

            if word in par:

                cen = word[0]
                for i in range(len(word)-1):
                    cen = cen+"*"
                
                par = par.replace(word, cen)

    print(par)
    main()

main()
        
