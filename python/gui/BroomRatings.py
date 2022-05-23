# This program is a ratings system for Broom AKA Pantheraleo
from tkinter import *
from time import sleep

root = Tk()
root.title("Ratings System")
root.resizable(0,0)

textBroom = Label(root, text="Broom")
textStars = Label(root, text="★★★★★")
textRate = Label(root, text="Rate")
textRespond = Label(root, text="Please leave a rating for Broom.", fg="black")

textBroom.grid(row=1,column=1,pady=(10,0),padx=(50,0))
textStars.grid(row=1,column=2,columnspan=2)
textRate.grid(row=2,column=1)
textRespond.grid(padx=10,pady=(0,10),column=1,columnspan=6)

def error():
    textRespond.config(text="Sorry, ratings cannot be less than 5 stars.", fg="red")
    
def success():
    textRespond.config(text="Thanks for your 5-star rating!", fg="green")

btn1 = Button(root, text="☆",command=error)
btn2 = Button(root, text="☆",command=error)
btn3 = Button(root, text="☆",command=error)
btn4 = Button(root, text="☆",command=error)
btn5 = Button(root, text="☆",command=success)

btn1.grid(row=2, column=2)
btn2.grid(row=2, column=3)
btn3.grid(row=2, column=4)
btn4.grid(row=2, column=5)
btn5.grid(row=2, column=6, padx=(0,50))

root.mainloop()
