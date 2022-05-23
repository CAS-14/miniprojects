from tkinter import *
from random import choice
import webbrowser

root = Tk()
root.title("DinnerPicker 1.0")
root.config(bg="lightblue")
root.resizable(0,0)

bxAdd = Entry(root)
lbMain = Label(root, text="Pick a dinner!")

def pick():
    with open("dinners.txt", "r") as reader:
        chosen = choice(reader.readlines())
    lbMain.config(text="Picked \""+chosen+".\"")

def add():
    new = bxAdd.get()
    if new != "":
        with open("dinners.txt", "a") as writer:
            writer.write("\n"+new)
        lbMain.config(text="Added \""+new+".\"")

def show():
    wList = Tk()
    wList.title("All Dinners")
    wList.config(bg="lightblue")
    wList.resizable(0,0)

    with open("dinners.txt", "r") as reader:
        list = reader.read()

    lbList = Label(wList, text=list)

    lbList.grid(row=1, column=1, padx=100, pady=100)

def access():
    webbrowser.open("dinners.txt")

btPick = Button(root, text="Pick Dinner", command=pick)
btAdd = Button(root, text="Add", command=add)
btShow = Button(root, text="All", command=show)
btHelp = Button(root, text="Help")
btAccess = Button(root, text="Access File", command=access)

btPick.grid(row=1, column=1, columnspan=2)
bxAdd.grid(row=2, column=1)
btAdd.grid(row=2, column=2)
btShow.grid(row=3, column=1)
btHelp.grid(row=3, column=2)
btAccess.grid(row=10, column=10)
lbMain.grid(row=4, column=1, columnspan=2)

root.mainloop()
