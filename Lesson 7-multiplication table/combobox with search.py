from tkinter import *
from tkinter.ttk import Combobox

def autocomplete(event):
    value = numrange.get()

    for item in numrange["values"]:
        if str(item).startswith(value):
            numrange.set(item)
            numrange.icursor(len(value))       # cursor position
            numrange.select_range(len(value), END)  # highlight remaining text
            break

root = Tk()

numrange = Combobox(root)
numrange["values"] = tuple(range(1, 101))
numrange.pack()

numrange.bind("<KeyRelease>", autocomplete)

root.mainloop()