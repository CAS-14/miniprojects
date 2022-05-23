# chisp

def chisp():
    par = input("Chisp: ")

    par = par.replace("ps", "sp")
    par = par.replace("PS", "SP")
    par = par.replace("pS", "sP")
    par = par.replace("Ps", "Sp")

    print("\nFinal paragraph:\n"+par+"\n")

    chisp()

chisp()
