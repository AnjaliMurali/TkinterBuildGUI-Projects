# importing whole module
from tkinter import *
#the tkinter.ttk module provides access to the Tk themed widget set 
from tkinter.ttk import *

# importing strftime function to
# retrieve system's time
#The `strftime` function in Python stands for “string format time” and is part of the `datetime` module. 
#It converts a `datetime` object into a string based on a specified format representing the date and time.
from time import strftime

# creating tkinter window
root = Tk()
root.title('Clock')


# This function is used to
# display time on the label
def time():
    string = strftime("%H:%M:%S %p")
    lbl.config(text=string)
    lbl.after(1000, time)


# Styling the label widget so that clock
# will look more attractive
lbl = Label(root, font=('calibri', 40, 'bold'),
            background='orange',
            foreground='white')

# Placing clock at the centre
# of the tkinter window
lbl.pack(anchor='center')
time()

mainloop()