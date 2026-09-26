import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Side Buttons Color Changer")
root.geometry("400x300")

# Functions to change background color
def set_red():
    root.configure(bg="red")

def set_green():
    root.configure(bg="green")

def set_blue():
    root.configure(bg="blue")

def set_yellow():
    root.configure(bg="yellow")

# Create buttons
top_btn = tk.Button(root, text="Top (Red)", command=set_red)
bottom_btn = tk.Button(root, text="Bottom (Green)", command=set_green)
left_btn = tk.Button(root, text="Left (Blue)", command=set_blue)
right_btn = tk.Button(root, text="Right (Yellow)", command=set_yellow)

# Place buttons on sides
top_btn.pack(side=tk.TOP, fill=tk.X)
bottom_btn.pack(side=tk.BOTTOM, fill=tk.X)
left_btn.pack(side=tk.LEFT, fill=tk.Y)
right_btn.pack(side=tk.RIGHT, fill=tk.Y)

# Start the GUI loop
root.mainloop()
