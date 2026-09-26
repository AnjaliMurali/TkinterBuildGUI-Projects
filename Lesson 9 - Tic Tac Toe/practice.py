from tkinter import *
from tkinter import messagebox
import random

def onclick(row,col):
    global gameover,gamemode,count,cp
    if board[row][col]["text"] =="" and gameover == False:
        board[row][col]["text"] = cp
        count+=1
        winner = checkwin()
        if winner:
            gameover=True
            messagebox.showinfo("Result",f"Player {winner} wins!")
            reset()
        
        elif count==9:
            gameover=True
            messagebox.showinfo("Result","It's a Tie! ")
            reset()

        else:
            cp="O" if cp=="X" else "X"
            if gamemode=="Single" and cp=="O":
                comp()


def comp():
    global count,cp,gameover
    emptycells = [(r,c) for r in range(3) for c in range(3) if board[r][c]["text"] == ""]
    if emptycells: 
        row,col = random.choice(emptycells)
        board[row][col]["text"] = cp
        count +=1
        winner = checkwin()
    if winner:
            gameover=True
            messagebox.showinfo("Result",f"Player {winner} wins!")
            reset()
        
    elif count==9:
        gameover=True
        messagebox.showinfo("Result","It's a Tie! ")
        reset()

    else:
        cp="X"


   


def checkwin():
    for row in range(3):
        if(board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"] != ""):
            return board[row][0]["text"]
    
    for col in range(3):
        if(board[0][col]["text"] == board[1][col]["text"] == board[2][col]["text"] != ""):
            return board[0][col]["text"]
        
    if board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]:
        return board[0][0]["text"]
    
    if board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]:
        return board[0][2]["text"]

    return None
         
def reset():
    global gameover,count,cp
    for row in range(3):
        for col in range(3):
            board[row][col]["text"] = ""
    gameover=False
    cp="X"
    count=0

def gm(mode):
    global gamemode
    gamemode=mode
    reset()
       
gamemode="Single"
cp = "X"
gameover=False
count=0

root = Tk()
root.title("Tic Tac Toe")
board = [[None for _ in range(3)] for _ in range(3)]
for row in range(3):
    for col in range(3):
        board[row][col]= Button(root,text="",font="Ariial 24",width=3,height=1,command=lambda r=row, c=col: onclick(r,c))
        board[row][col].grid(row=row,column=col)

frame = Frame(root)
frame.grid(row=3,column=0,columnspan=3)

singlebtn = Button(frame,text="Single Player", command=lambda:gm("Single"))
singlebtn.pack(side="left")

multibtn = Button(frame,text="Multi Player",command=lambda:gm("Multi"))
multibtn.pack(side="right")

resetbtn = Button(root,text="Reset",command=reset)
resetbtn.grid(row=4,column=0,columnspan=3)
root.mainloop()