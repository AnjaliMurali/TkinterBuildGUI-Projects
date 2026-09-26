from tkinter import *
from tkinter import messagebox


# Create the window
master = Tk()

# Title of window
master.title("Color Changer")


# Initial colors
colors = ["Red", "Green", "Blue", "Yellow",
          "Cyan", "Magenta", "White", "Black"]


# Function to add color to listbox
def addColor():
    color = item.get()

    if color != "":
        # Check if color already exists
        if color in listbox.get(0, END):
            messagebox.showerror("Error", "Color already exists!")
        else:
            # Add color to listbox
            listbox.insert(END, color)

        # Clear Entry box
        item.delete(0, END)


# Function to delete selected color
def deleteColor():
    # Get selected line index
    index = listbox.curselection()
    if index:
        listbox.delete(index)


# Function to clear listbox
def clearList():
    listbox.delete(0, END)


# Function to apply selected color
def applyColor():
    # Get selected line index
    index = listbox.curselection()

    if index:
        # Get selected color
        color = listbox.get(index)

        # Change window background
        try:
            master.configure(bg=color.lower())
        except TclError:
            messagebox.showerror("Error", "Invalid color!")


# Create Entry box for adding colors
item = Entry(master, width=35)
item.pack(padx=5, pady=5)


# Create buttons
lAdd = Button(master, text="ADD", command=addColor, width=15)
lDelete = Button(master, text="DELETE", command=deleteColor, width=15)
lApply = Button(master, text="APPLY", command=applyColor, width=15)
lClear = Button(master, text="CLEAR", command=clearList, width=15)


# Place buttons on screen
lAdd.pack(padx=5, pady=5)
lDelete.pack(padx=5, pady=5)
lApply.pack(padx=5, pady=5)
lClear.pack(padx=5, pady=5)


# Create frame for listbox and scrollbar
frame = Frame(master)

scrollbar = Scrollbar(frame, orient="vertical")
scrollbar.pack(side=RIGHT, fill=Y)


# Create listbox
listbox = Listbox(
    frame,
    width=40,
    height=8,
    yscrollcommand=scrollbar.set
)


# Insert initial colors into listbox
for color in colors:
    listbox.insert(END, color)


# Place listbox
listbox.pack(side=LEFT, padx=5)


# Connect scrollbar to listbox
scrollbar.config(command=listbox.yview)


# Place frame
frame.pack(pady=10)


# Run the program
mainloop()