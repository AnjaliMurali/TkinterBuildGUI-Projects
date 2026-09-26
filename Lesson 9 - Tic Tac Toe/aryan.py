"""
corrections:
1.Add if in line 15 and 18
2. line 51, change == to =
3. global gamemode in line mode()
"""

from tkinter import *
from tkinter import messagebox
import random

root=Tk()
root.config(bg="#A3F2CB")
root.title("Tic Tac Toe")

def win():
    global gameover, count, currentplayer, winner
    for row in range(3):
        if board[row][0]["text"]==board[row][1]["text"]==board[row][2]["text"]!="":
            return board[row][0]["text"]
    for column in range(3):
        if board[0][column]["text"]==board[1][column]["text"]==board[2][column]["text"]!="":
            return board[0][column]["text"]
    if board[0][0]["text"]==board[1][1]["text"]==board[2][2]["text"]!="":
        return board[0][0]["text"]
    if board[0][2]["text"]==board[1][1]["text"]==board[2][0]["text"]!="":
        return board[0][2]["text"]
    return None


def mode(gm):
    global gameover, count, currentplayer, winner,gamemode
    gamemode=gm
    reset()

def reset():
    global gameover, count, currentplayer, winner
    for row in range (3):
        for column in range (3):
            board[row][column]["text"]=""
    currentplayer="X"
    gameover=False
    count=0     

def tttbot():
    global gameover, count, currentplayer, winner
    emptybtn=[]
    for row in range(3):
        for column in range(3):
            if board[row][column]["text"]=="":
                emptybtn.append((row,column))
    if emptybtn:
        botchoice_row, botchoice_column=random.choice(emptybtn)
        board[botchoice_row][botchoice_column]["text"]=currentplayer
        winner=win()
        count+=1
        if winner:
            gameover=True
            messagebox.showinfo("Result", winner + " won!")
            reset()
        elif count==9:
            gameover=True
            messagebox.showinfo("Result", "It's a draw!")
            reset()
        else:
            currentplayer="X"

def onclick(row,column):
    global gameover, count, currentplayer, winner
    if gameover==False and board[row][column]["text"]=="":
        board[row][column]["text"]=currentplayer
        winner=win()
        print(winner)
        count+=1
        if winner:
            gameover=True
            messagebox.showinfo("Result", winner + " won!")
            reset()
        elif count==9:
            gameover=True
            messagebox.showinfo("Result", "It's a draw!")
            reset()
        else:
            if currentplayer=="X":
                currentplayer="O"
            else:
                currentplayer="X"
            if gamemode=="Single" and currentplayer=="O":
                tttbot()

board=[[None for _ in range(3)] for _ in range (3)]

for row in range(3):
    for column in range(3):
        board[row][column]=Button(root,width="10",height="3",command=lambda r=row, c=column:onclick(r,c))
        board[row][column].grid(row=row,column=column)

gamemode="Single"
currentplayer="X"
gameover=False
count=0

gameframe=Frame(root,bg="#A3F2CB")
gameframe.grid(row=3,column=0,columnspan=3)

singleplayermode=Button(gameframe,text="Singleplayer",font=("Arial", 13),command=lambda:mode("Single"))
singleplayermode.grid(row=0,column=0,pady=(10,0))

multiplayermode=Button(gameframe,text="Multiplayer mode",font=("Arial", 13),command=lambda:mode("Multiplayer"))
multiplayermode.grid(row=0,column=1,pady=(10,0))

resetbtn=Button(root,text="Reset",font=("Arial", 13),command=reset)
resetbtn.grid(row=4,column=1)

root.mainloop()