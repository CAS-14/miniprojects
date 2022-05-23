# lisp

def lisp():
    par = input("Lisp: ")

    par = par.replace("s", "th")
    par = par.replace("S", "Th")
    par = par.replace("z", "th")
    par = par.replace("Z", "Th")
    par = par.replace("r", "w")
    par = par.replace("R", "W")

    print("\nHere it is:\n"+par+"\n")
    lisp()

lisp()
