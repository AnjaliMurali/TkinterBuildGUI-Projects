import tkinter as tk
from tkinter import messagebox, simpledialog

# Create window
root = tk.Tk()
root.title("Color Changer")
root.geometry("400x300")

# Initial colors
colors = ["Red", "Green", "Blue", "Yellow", "Cyan", "Magenta", "White", "Black"]

# Function to fill the listbox
def populate_listbox():
    listbox.delete(0, tk.END)
    for color in colors:
        listbox.insert(tk.END, color)

# Function to add a new color
def add_color():
    new_color = simpledialog.askstring("Add Color", "Enter the name of the color:")

    if new_color:
        if new_color not in colors:
            colors.append(new_color)
            populate_listbox()
        else:
            messagebox.showerror("Error", "Color already exists in the list.")

# Function to remove selected color
def remove_color():
    selected = listbox.curselection()

    if selected:
        color = listbox.get(selected[0])
        colors.remove(color)
        populate_listbox()
    else:
        messagebox.showwarning("Warning", "No color selected to remove.")

# Function to apply selected color
def apply_color():
    selected = listbox.curselection()

    if selected:
        color = listbox.get(selected[0])

        try:
            root.configure(bg=color.lower())
        except tk.TclError:
            messagebox.showerror("Error", f"Invalid color: {color}")
    else:
        messagebox.showwarning("Warning", "No color selected.")

# Listbox
listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=10)
listbox.pack(pady=10, fill=tk.X, padx=20)

populate_listbox()

# Buttons
add_button = tk.Button(root, text="Add Color", command=add_color)
add_button.pack(side=tk.LEFT, padx=20)

remove_button = tk.Button(root, text="Remove Color", command=remove_color)
remove_button.pack(side=tk.LEFT)

apply_button = tk.Button(root, text="Apply Color", command=apply_color)
apply_button.pack(side=tk.RIGHT, padx=20)

# Run the application
root.mainloop()