from tkinter import *
from tkinter import messagebox
import random

def namenext():
    myname=nameentry.get()
    okbuttonname.config(state="disabled")
    messagebox.showinfo("game explain","Hi " + myname +", I am thinking of a number between 1-20. Can you guess it?")
    guessbutton.config(state="normal")

randomnumber=random.randint(1,20)

attempts=0

def guess():
    global attempts
    attempts+=1
    inputnumber=int(guessentry.get())
    if (inputnumber>0 and inputnumber<21):
        if inputnumber==randomnumber:
            messagebox.showinfo("Correct", "Your answer is correct!")
            guessbutton.config(state="disabled")
            attemptstxt.config(text="You took "+ str(attempts) + " attempts in total to guess the right number")
        elif inputnumber<randomnumber:
            messagebox.showinfo("Incorrect", "Your answer is too low!")
        elif inputnumber>randomnumber:
            messagebox.showinfo("Incorrect", "Your answer is too high!")
    else:
        messagebox.showinfo("Warning", "enter only number netween 1 and 20")

root = Tk()
root.config(background="#8bfab4")
root.geometry("800x800")
root.title("GTN")

title=Label(root,text="Welcome to GTN",font=("Arial",30,"bold"),bg="#8bfab4",fg="white")
title.grid(column=0,row=0,padx=250,pady=50)

nameget=Frame(root,bg="#8bfab4")
nameget.grid(column=0,row=1,padx=30,pady=200)

name=Label(nameget,text="What is your name?",font=("Arial",20),bg="#8bfab4",fg="white")
name.grid(column=0,row=0)

nameentry=Entry(nameget)
nameentry.grid(column=0,row=1)

okbuttonname=Button(nameget,text="Next",font=("Arial",10),command=namenext)
okbuttonname.grid(column=1,row=1)

guesstxt=Label(nameget,text="Guess the number",font=("Arial",20),bg="#8bfab4",fg="white")
guesstxt.grid(column=0,row=2,pady=15)

guessentry=Entry(nameget)
guessentry.grid(column=0,row=3)

guessbutton=Button(nameget,text="Guess",font=("Arial",10),command=guess,state="disabled")
guessbutton.grid(column=1,row=3)

attemptstxt=Label(root,font=("Arial",20),bg="#8bfab4",fg="white")
attemptstxt.grid(column=0,row=2)

mainloop()