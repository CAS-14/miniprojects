print("SentenceCapitalizer by CAS. You can input nothing to quit.")

def main():
    q = ["who", "what", "why", "when", "where", "how", "whos", "whom", "whose", "whats", "whys", "whens", "wheres", "hows", "whoms", "whom's", "what's", "who's", "why's", "when's", "where's", "how's"]
    wrQ = ["whos", "whats", "whys", "whens", "wheres", "hows", "whatevers", "thats", "hes"]
    isQ = False
    isComp = False
    end = False

    sen = input("Enter a sentence to be punctuated properly: ")
    sen = sen.lower()
    spl = sen.split()

    if sen == "":
        end = True

    if "!" in sen or "." in sen or "?" in sen:
        fin = sen
        isComp = True

    for word in q:
        if word in spl:
            isQ = True

    if isQ:
        if isComp:
            sen.replace(".", "?")

        elif "what a" in sen:
            isQ = False

            if isComp:
                fin = sen.replace(".", "!")

            else:
                fin = sen+"!"
        
        else:
            fin = sen+"?"

    elif isComp == False:
        fin = sen+"."

    for word in wrQ:
        if word in spl:
            fin = fin.replace(word, word.replace("s", "")+"'s")

    if "shes" in spl:
        fin = fin.replace("shes", "she's")

    if "im" in spl:
        fin = fin.replace("im", "i'm")

    fin = fin.replace("gonna", "going to")
    fin = fin.capitalize()

    if end:
        print("Goodbye.")

    else:
        print(fin+"\n")
        main()

main()
