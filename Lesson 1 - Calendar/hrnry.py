from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("show calendar")
root.config(background="red")

titleLabel = Label(root,text="CALENDAR",font=("Arial",50,"bold"),bg="green",fg="orange")
titleLabel.grid(row=0,column=0,padx=10)

root.mainloop()