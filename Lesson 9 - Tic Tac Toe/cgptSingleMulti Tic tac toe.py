#import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random

def check_winner():
    for row in board:
        if row[0]['text'] == row[1]['text'] == row[2]['text'] != "":
            highlight_buttons(row)
            return row[0]['text']

    for col in range(3):
        if board[0][col]['text'] == board[1][col]['text'] == board[2][col]['text'] != "":
            highlight_buttons([board[0][col], board[1][col], board[2][col]])
            return board[0][col]['text']

    if board[0][0]['text'] == board[1][1]['text'] == board[2][2]['text'] != "":
        highlight_buttons([board[0][0], board[1][1], board[2][2]])
        return board[0][0]['text']

    if board[0][2]['text'] == board[1][1]['text'] == board[2][0]['text'] != "":
        highlight_buttons([board[0][2], board[1][1], board[2][0]])
        return board[0][2]['text']

    return None

def highlight_buttons(buttons):
    for button in buttons:
        button.config(bg="lightgreen")

def on_click(row, col):
    global current_player, game_mode

    if board[row][col]['text'] == "" and not game_over:
        board[row][col]['text'] = current_player
        winner = check_winner()

        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset_game()
        elif all(board[i][j]['text'] != "" for i in range(3) for j in range(3)):
            messagebox.showinfo("Game Over", "It's a tie!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"
            if game_mode == "Single Player" and current_player == "O":
                computer_move()

def computer_move():
    global current_player

    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c]['text'] == ""]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col]['text'] = current_player
        winner = check_winner()

        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset_game()
        elif all(board[i][j]['text'] != "" for i in range(3) for j in range(3)):
            messagebox.showinfo("Game Over", "It's a tie!")
            reset_game()
        else:
            current_player = "X"
            

def reset_game():
    global current_player, game_over
    current_player = "X"
    game_over = False
    for row in range(3):
        for col in range(3):
            board[row][col].config(text="", bg="SystemButtonFace")

def set_game_mode(mode):
    global game_mode
    game_mode = mode
    reset_game()

# Initialize the main application window
root = Tk()
root.title("Tic Tac Toe")

current_player = "X"
game_over = False
board = [[None for _ in range(3)] for _ in range(3)]
game_mode = "Two Player"

# Create a 3x3 board
for row in range(3):
    for col in range(3):
        board[row][col] = Button(root, text="", font=("Arial", 24), width=5, height=2, command=lambda r=row, c=col: on_click(r, c))
        board[row][col].grid(row=row, column=col)

# Add buttons for selecting game mode
game_mode_frame = Frame(root)
game_mode_frame.grid(row=3, column=0, columnspan=3)

single_player_button = Button(game_mode_frame, text="Single Player", font=("Arial", 14), command=lambda: set_game_mode("Single Player"))
single_player_button.pack(side="left", padx=5)

multi_player_button =Button(game_mode_frame, text="Two Player", font=("Arial", 14), command=lambda: set_game_mode("Two Player"))
multi_player_button.pack(side="right", padx=5)

# Add reset button
reset_button = Button(root, text="Reset", font=("Arial", 14), command=reset_game)
reset_button.grid(row=4, column=0, columnspan=3, sticky="nsew")

# Start the main event loop
root.mainloop()
