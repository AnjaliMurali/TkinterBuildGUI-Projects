from tkinter import *
from tkinter import messagebox
import random

def clicked(row,column):
    global current_player,gameover,count
    if gameboard[row][column]["text"]=="":
        gameboard[row][column]["text"]=current_player
        count +=1
        if current_player=="x":
            current_player="o"
        else:
            current_player="x"
        winner = checkwin()
        if winner:
            gameover=True
            messagebox.showinfo("Result", f"Player {winner} wins")
            Reset()
        elif count == 9:
            gameover=True
            messagebox.showinfo("Result", "It's a Tie")
            Reset()
        if gamemode == "Single" and current_player=="o":
            compmove()

def checkwin():
    for row in range(3):
        if gameboard[row][0]["text"] == gameboard[row][1]["text"] == gameboard[row][2]["text"] != "":
            return gameboard[row][0]["text"]
        
    for col in range(3):
        if gameboard[0][col]["text"] == gameboard[1][col]["text"] == gameboard[2][col]["text"] != "":
            return gameboard[0][col]["text"]
    
    if gameboard[0][0]["text"] == gameboard[1][1]["text"] == gameboard[2][2]["text"] != "":
        return gameboard[0][0]["text"]
    
    if gameboard[0][2]["text"] == gameboard[1][1]["text"] == gameboard[2][0]["text"] != "":
        return gameboard[0][2]["text"]
    
    return None

def Reset():
    global count,gameover,current_player
    for row in range(3):
        for col in range(3):
            gameboard[row][col]["text"] = ""

    count=0
    gameover = False  # Allow the game to continue
    current_player = "x"

def setGamemode(mode):
    global gamemode
    gamemode = mode
    Reset() 

def compmove():
    global count,current_player,gameover
    #emptycells= [(r,c) for r in range(3) for c in range(3) if board[r][c]["text"] == ""]
    #The above line is called list comprehension. It is equivalent to the below commented lines.
    emptycells = []

    for r in range(3):
        for c in range(3):
            if gameboard[r][c]["text"] == "":
                emptycells.append((r, c))
    
    if emptycells:
        row,col = random.choice(emptycells)
        gameboard[row][col]["text"] = current_player
        count += 1
        winner = checkwin()

        if winner:
            gameover=True
            messagebox.showinfo("Result", f"Player {winner} wins")
            Reset()
        elif count == 9:
             gameover=True
             messagebox.showinfo("Result", "It's a Tie")
             Reset()
        else:
            current_player="x" 

root = Tk()
root.geometry("400x600")
root.config(background="pink")
root.title("Tic tac toe game")

current_player="x"

gameboard = []
count = 0
gameover = False
gamemode = "Single"

for i in range(3):
    new_row=[]
    for c in range(3):
        new_row.append(None)
    gameboard.append(new_row)

for row in range(3):
    for column in range(3):
        gameboard[row][column]=Button(root,text="",font=("Arial",50),bg="light blue",fg="white",width="3",height="1",command=lambda r=row,c=column:clicked(r,c))
        gameboard[row][column].grid(row=row,column=column)

players = Frame(root,bg="pink")
players.grid(row=3,column=0,columnspan=3,pady=10)

splayer = Button(players,text="single player",font=("Arial",20),bg="white",fg="pink",command=lambda:setGamemode("Single"))
splayer.grid(row=0,column=0)

mplayer = Button(players,text="muliplayer",font=("Arial",20),bg="white",fg="pink",command=lambda:setGamemode("Multi"))
mplayer.grid(row=0,column=1)

reset = Button(players,text="reset",font=("Arial",20),bg="white",fg="light blue",command = Reset)
reset.grid(row=1,column=0,columnspan=2)

root.mainloop()