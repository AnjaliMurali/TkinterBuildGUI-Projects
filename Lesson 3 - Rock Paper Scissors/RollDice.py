from tkinter import *
import random

dicenumbers=["1","2","3","4","5","6"]

def outcome():
    do=random.choice(dicenumbers)
    diceoutcome.config(text="dice outcome: "+ str(do))

root = Tk()
root.geometry("800x800")
root.config(background="#a5f1d3")
root.title("Roll a dice")

header=Label(root,text="Roll a dice",font=("Arial",30),bg="#a5f1d3",fg="white")
header.grid(row=0,column=0, padx=325,pady=25)

diceoutcome=Label(root,text="dice outcome: ",font=("Arial",25),bg="#a5f1d3",fg="white")
diceoutcome.grid(row=2,column=0, pady=100)

rolladice=Button(root,text="Click here to roll the dice",font=("Arial",20),bg="#baeed9",fg="white",command=lambda:outcome())
rolladice.grid(row=1,column=0, pady=150)

root.mainloop()