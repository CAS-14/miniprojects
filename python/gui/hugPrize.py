from tkinter import *

root = Tk()
root.title("Prize Time!")

def prize():
    hugs = 10
    lb = Label(root,text="PRIZE: 20 hugs!")
    lb.pack(padx=20,pady=(5,20))
    while True:
        hugs += 1
        lb = Label(root,text="PRIZE:"+str(hugs)+"hugs!")
        lb.pack(padx=20,pady=(5,20))

btn = Button(root,text="\nIt's Prize Time!\n",command=prize,fg="red")
btn.pack(padx=20,pady=(20,5))

root.mainloop()
