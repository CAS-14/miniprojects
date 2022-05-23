# ColorWindow by CAS copyright (c) 2020. All Rights Reserved.

from tkinter import *

root = Tk()
root.title("ColorWindow")

def Red():
    root.configure(bg="red")
def Blu():
    root.configure(bg="blue")
def Grn():
    root.configure(bg="lime")
def Yel():
    root.configure(bg="yellow")
def Blk():
    root.configure(bg="black")
def Whi():
    root.configure(bg="white")

btnRed = Button(root,text="Red",fg="red",command=Red)
btnBlu = Button(root,text="Blue",fg="blue",command=Blu)
btnGrn = Button(root,text="Green",fg="green",command=Grn)
btnYel = Button(root,text="Yellow",fg="yellow",command=Yel)
btnBlk = Button(root,text="Black",fg="black",command=Blk)
btnWhi = Button(root,text="White",fg="black",command=Whi)

btnRed.pack(padx=50,pady=(50,10))
btnBlu.pack(padx=50,pady=(10,10))
btnGrn.pack(padx=50,pady=(10,10))
btnYel.pack(padx=50,pady=(10,10))
btnBlk.pack(padx=50,pady=(10,10))
btnWhi.pack(padx=50,pady=(10,50))

root.mainloop()
