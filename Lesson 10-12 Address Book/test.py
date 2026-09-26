from tkinter import Tk, Label as TkL
from tkinter.ttk import *

# Create the main window
root = Tk()
root.title("tkinter vs ttk")

# Create a label using tk
tk_label = TkL(root, text="This is a tk.Label", fg="red", bg="yellow")
tk_label.pack(pady=10)

# Create a label using ttk
ttk_label = Label(root, text="This is a ttk.Label")
ttk_label.pack(pady=10)

# Start the main loop
root.mainloop()