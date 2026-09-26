from tkinter import *
from tkinter import messagebox
import random

#Define the functions in this order - onclick(till test),checkwin,setgamemode,reset,onclick,compmove 

def onclick(row,col):
    global currentplayer,count,gameover
    if board[row][col]["text"]=="" and gameover==False:
        board[row][col]["text"] = currentplayer
        count += 1
        #testing time
        winner = checkwin()
        if winner:
            gameover=True
            messagebox.showinfo("Result", f"Player {winner} wins")
            reset()
        elif count == 9:
             gameover=True
             messagebox.showinfo("Result", "It's a Tie")
             reset()
        else:
            currentplayer="O" if currentplayer=="X" else "X"
            #testing time - with only multiplayer.
            if gamemode=="Single" and currentplayer =="O" :
                compmove()

def setGamemode(mode):
    global gamemode
    gamemode = mode
    reset()

def compmove():
    global count,currentplayer,gameover
    emptycells= [(r,c) for r in range(3) for c in range(3) if board[r][c]["text"] == ""]
    #The above line is called list comprehension. It is equivalent to the below commented lines.
    """
    emptycells = []

    for r in range(3):
        for c in range(3):
            if board[r][c]["text"] == "":
                emptycells.append((r, c))
    """
    if emptycells:
        row,col = random.choice(emptycells)
        board[row][col]["text"] = currentplayer
        count += 1
        winner = checkwin()

        if winner:
            gameover=True
            messagebox.showinfo("Result", f"Player {winner} wins")
            reset()
        elif count == 9:
             gameover=True
             messagebox.showinfo("Result", "It's a Tie")
             reset()
        else:
            currentplayer="X" 

def checkwin():
    for row in range(3):
        if board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"] != "":
            return board[row][0]["text"]
        
    for col in range(3):
        if board[0][col]["text"] == board[1][col]["text"] == board[2][col]["text"] != "":
            return board[0][col]["text"]
    
    if board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] != "":
        return board[0][0]["text"]
    
    if board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] != "":
        return board[0][2]["text"]
    
    return None

def reset():
    global count,gameover,currentplayer
    for row in range(3):
        for col in range(3):
            board[row][col]["text"] = ""
    count=0
    gameover = False  # Allow the game to continue
    currentplayer = "X"  # Set to the default starting player

root = Tk()
#root.geometry("200x250") #no need to specify, it will automatically take the width as per the widgets added. 
root.title("Tic Tac Toe")
gamemode = "Single"
gameover = False
currentplayer = "X"
count = 0
#board creates a 3 × 3 two-dimensional list, which your Tic-Tac-Toe game uses to store the 9 buttons.
board = [[None for _ in range(3)] for _ in range(3)]
#instead of the above line, the traditional approach: 
"""
board = []

for row in range(3):
    new_row = []

    for col in range(3):
        new_row.append(None)

    board.append(new_row)
"""
for row in range(3):
    for col in range(3):
        #Here, the current values of row and col are saved as default values for r and c when each lambda is created.
        #So each button remembers its own position. That's why r=row,c=col: onclick(r,c) is important. 
        board[row][col] = Button(root,text="",font=("Arial", 24),width="3",height="1",command= lambda r=row,c=col: onclick(r,c))
        board[row][col].grid(row=row,column=col)

btnfr = Frame(root)
btnfr.grid(row=3,column=0,columnspan=3)

sp = Button(btnfr,text="Single Player",command=lambda:setGamemode("Single"))
sp.pack(side="left")

mp = Button(btnfr,text="Multi Player",command=lambda:setGamemode("Multi"))
mp.pack(side="right")

resetbtn = Button(root,text="Reset",command=reset)
resetbtn.grid(row=4,column=0,columnspan=3)

root.mainloop()