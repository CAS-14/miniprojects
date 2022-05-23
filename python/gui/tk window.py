from tkinter import *

win = Tk()
win.title("Window")

def w2():
    win2 = Tk()
    win2.title("Window 2")
    win2.configure(bg="gray")
    lb2 = Label(win2, text="Text 2",bg="red",fg="white")
    lb2.pack(padx=100,pady=100)

lb = Label(win, text="Label")
lb.pack(padx=100,pady=(50, 10))

btn = Button(win, text="Button", command=w2)
btn.pack(padx=100,pady=(10,50))

win.mainloop()
