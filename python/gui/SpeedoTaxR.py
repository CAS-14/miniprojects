from tkinter import *
from random import randint

root = Tk()
root.title("SpeedoTax")

lb = Label(root, text="Taxes:")
taxBx = Entry(root)

def getTax():
    amtOwed = randint(1000000000,999999999999999)
    lb.configure(text=str(amtOwed))

btn = Button(root, text="Calculate Taxes", command = getTax)

lb.grid(row=1,column=1, padx=(20,10), pady=(20, 10))
taxBx.grid(row=1,column=2,columnspan = 2, padx=(10,20))
btn.grid(row=2,column=2,columnspan=2, pady=(10,20))

root.mainloop()
