import tkinter as tk
from tkinter import messagebox
import random

# Create main window
root = tk.Tk()
root.title("Lucky Slots")

def spin():
    # Generate three random numbers (0–9)
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    num3 = random.randint(0, 9)

    # Update labels
    slot1.config(text=str(num1))
    slot2.config(text=str(num2))
    slot3.config(text=str(num3))

    # Winning conditions
    if num1 == num2 == num3:
        messagebox.showinfo("Result", "JACKPOT! You win $1000!")
    elif num1 == num2 or num1 == num3 or num2 == num3:
        messagebox.showinfo("Result", "Mini Prize! You win $10!")
    else:
        messagebox.showwarning("Result", "Bad Luck! Try Again.")

# Create slot labels
slot1 = tk.Label(root, text="0", font=("Arial", 30), width=4)
slot2 = tk.Label(root, text="0", font=("Arial", 30), width=4)
slot3 = tk.Label(root, text="0", font=("Arial", 30), width=4)

slot1.grid(row=0, column=0, padx=5, pady=10)
slot2.grid(row=0, column=1, padx=5, pady=10)
slot3.grid(row=0, column=2, padx=5, pady=10)

# Create SPIN button
spin_button = tk.Button(root, text="SPIN", font=("Arial", 16), command=spin)
spin_button.grid(row=1, column=0, columnspan=3, pady=10)




# Run the application
root.mainloop()