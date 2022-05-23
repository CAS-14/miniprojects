from tkinter import *
from time import sleep

amt = 1000
inc = 1
upgInc = 10
aut = 0
upgAut = 1000

wGame = Tk()
wGame.title("Thing Clicker")
wGame.resizable(0,0)
wGame.config(bg="lightblue")

lbAmt = Label(wGame, text=amt, font=("arial", 50), bg="lightblue")
lbUnits = Label(wGame, text="Thingies (+"+str(inc)+")", bg="lightblue")
lbUpg = Label(wGame, text="It costs "+str(upgInc)+" thingies to upgIncrade.", bg="lightblue")

def increase():
    global amt
    global inc

    amt = amt+inc
    lbAmt.config(text=amt)

def upgrade():
    global amt
    global inc
    global upgInc

    if amt-upgInc > -1:
        inc += 1
        amt -= upgInc
        upgInc *=2
        lbAmt.config(text=amt)
        lbUpg.config(text="It costs "+str(upgInc)+" thingies to upgrade.")
        lbUnits.config(text="Thingies (+"+str(inc)+")")

def help():
    wHelp = Tk()
    wHelp.title("Help Guide")
    wHelp.resizable(0,0)
    wHelp.config(bg="lightblue")

    helpTextVar = "Welcome to ThingClicker!, a simple clicker game where\nyou get thingies to do things.\n\nHow to Play:\n1. Click the \"Click Here!\" button to gain thingies.\n2. When you have enough thingies to upgIncrade, click the upgIncrade button.\n3. upgIncrade to gain more thingies. And that's it.\n4. Have fun!"
    lbHelp = Label(wHelp, bg="lightblue", text=helpTextVar)

    def close():
        wHelp.destroy()

    btnClose = Button(wHelp, text="Close", highlightbackground="lightblue", command=close)

    lbHelp.grid(row=1, column=1, padx=20, pady=(20,0))
    btnClose.grid(row=2, column=1, padx=20, pady=(5, 20))

def auto():
    global amt
    global aut
    global upgAut

    if amt-upgAut > -1:
        aut += 1
        amt -= upgAut
        upgAut *= 2
        lbAmt.config(text=amt)

btnInc = Button(wGame, text="Click me!", highlightbackground="lightblue", command=increase)
btnHelp = Button(wGame, text="Help/Info", highlightbackground="lightblue", command=help)
btnUpg = Button(wGame, text="Upgrade!", highlightbackground="lightblue", command=upgrade)
btnAuto = Button(wGame, text="AutoClick", highlightbackground="lightblue", command=auto)

lbAmt.grid(row=1, column=1, padx=20, pady=(20,5), rowspan=2)
lbUnits.grid(row=3, column=1, padx=20, pady=(0, 20))
btnInc.grid(row=1, column=2, padx=(0,20), pady=(20,0))
btnUpg.grid(row=2, column=2, padx=(0,20), pady=10)
btnHelp.grid(row=3, column=2, padx=(0, 20), pady=(0,20))
btnAuto.grid(row=1, column=3, padx=(0, 20), pady=(20,0))
lbUpg.grid(row=4, column=1, columnspan=3, padx=20, pady=(0,20))

wGame.mainloop()

while True:
    if aut > 0:
        sleep(5/aut)
        amt += inc
        wGame.update()
