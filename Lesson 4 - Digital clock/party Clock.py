from tkinter import *
from time import strftime
import random

colours = ["red","orange","yellow","green","blue","purple","pink","light pink","light blue","light green", "dark blue"]
bgc="white"

def new_time():
    global bgc
    t = strftime("%H:%M:%S")
    time.config(text=t)
    bgc = colours[random.randint(0,10)]
    root.config(background=bgc)
    time.config(fg=bgc)
    time.after(1000,new_time)
    
    



root = Tk()
root.geometry("500x300")
root.config(background=bgc)
root.title("party clock")

time = Label(root,font=("Arial",50))
time.grid(row=0,column=0,padx=110,pady=80)

new_time()

root.mainloop()