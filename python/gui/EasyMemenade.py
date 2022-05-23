from os import system
from tkinter import *

root = Tk()
root.title("EasyMemenade")
root.resizable(0,0)

clr = IntVar(root)

box = Entry(root)
delCh = Checkbutton(root, text="Clear box after reading.", variable=clr)

def Meme():
    text = box.get()
    system("say -v daniel \""+text+"\"")

    if clr == 1:
        box.delete(0, END)

def Help():
    system("say -v daniel Welcome to Easy Meme nade, an app created by CAS to easily make the daniel meme nade voice.")
    system("say -v daniel Simply enter your text below to become meme nade and amaze your friends and family")

btnMeme = Button(root, text="Meme Time", command=Meme)
btnHelp = Button(root, text="Help2Meme", command=Help)

box.grid(row=1, column=1, columnspan=2, padx=10, pady=10)
btnMeme.grid(row=2, column=1, padx=10, pady=(0, 10))
btnHelp.grid(row=2, column=2, padx=(0, 10), pady=(0, 10))
delCh.grid(row=3, column=1, columnspan=1, padx=10, pady=(0, 10))

root.mainloop()
