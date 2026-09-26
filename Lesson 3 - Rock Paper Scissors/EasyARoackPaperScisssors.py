from tkinter import *
import random

playerchoice=["Rock","Paper","Scissors"]
pscore=0
cscore=0

def tie():
    Winner.config(text="It's a tie")
    computerscore.config(text="computer score: "+ str(cscore))
    playerscore.config(text="player score: "+ str(pscore))

def pwin():
    global pscore
    Winner.config(text="Player wins!")
    pscore+=1
    playerscore.config(text="player score: "+ str(pscore))
    computerscore.config(text="computer score: "+ str(cscore))

def cwin():
    global cscore
    Winner.config(text="Computer wins!")
    cscore+=1
    computerscore.config(text="computer score: "+ str(cscore))
    playerscore.config(text="player score: "+ str(pscore))

def pchoice(pc):
    cc=random.choice(playerchoice)
    playerinput.config(text="Your input: "+ pc)
    computerinput.config(text="Computers input: "+ cc)
    if pc==cc:
        tie()
    elif pc=="Rock":
        if cc=="Paper":
            cwin()
        elif cc=="Scissors":
            pwin()
    elif pc=="Paper":
        if cc=="Rock":
            pwin()
        elif cc=="Scissors":
            cwin()
    elif pc=="Scissors":
        if cc=="Rock":
            cwin()
        elif cc=="Paper":
            pwin()

root = Tk()
root.geometry("800x800")
root.config(background="#a5e7f1")
root.title("Rock Paper Scissors")

Rock_Paper_Scissors=Label(root,text="Rock Paper Scissors Shoot",font=("Arial",30),bg="#a5e7f1",fg="white")
Rock_Paper_Scissors.pack()

Winner=Label(root,text="Start game",font=("Arial",20),bg="#a5e7f1",fg="white")
Winner.pack()

choiceframe=Frame(root,bg="#a5e7f1")
choiceframe.pack(pady=100)

Playeropt=Label(choiceframe,text="Player Options",font=("Arial",20),bg="#a5e7f1",fg="white")
Playeropt.grid(row=0,column=0)

Rock=Button(choiceframe,text="Rock",font=("Arial",20),bg="#84b1b8",fg="white",command=lambda:pchoice(playerchoice[0]))
Rock.grid(row=0,column=1)

Paper=Button(choiceframe,text="Paper",font=("Arial",20),bg="#84b1b8",fg="white",command=lambda:pchoice(playerchoice[1]))
Paper.grid(row=0,column=2)

Scissors=Button(choiceframe,text="Scissors",font=("Arial",20),bg="#84b1b8",fg="white",command=lambda:pchoice(playerchoice[2]))
Scissors.grid(row=0,column=3)


outcomeframe=Frame(root,bg="#a5e7f1")
outcomeframe.pack(pady=50)

playerinput=Label(outcomeframe,text="Your input: --- ",font=("Arial",20),bg="#a5e7f1",fg="white")
playerinput.grid(row=0,column=0)

computerinput=Label(outcomeframe,text="Computers input: ---",font=("Arial",20),bg="#a5e7f1",fg="white")
computerinput.grid(row=1,column=0)

playerscore=Label(outcomeframe,text="player score: ",font=("Arial",20),bg="#a5e7f1",fg="white")
playerscore.grid(row=0,column=1)

computerscore=Label(outcomeframe,text="computer score: ",font=("Arial",20),bg="#a5e7f1",fg="white")
computerscore.grid(row=1,column=1,padx=20)

root.mainloop()