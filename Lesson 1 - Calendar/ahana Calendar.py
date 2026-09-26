from tkinter import *
import calendar

def showcal():
    yearCal = Tk()
    yearCal.geometry("800x800")
    y = int(year.get())
    calcon = calendar.calendar(y)
    yearLab = Label(yearCal,text = calcon,font=("Consolas",10),justify=LEFT)
    yearLab.grid(row=0,column=0)
    yearCal.mainloop()

root = Tk()
root.geometry("300x300")
root.config(background="red")
root.title("calendar")

calLabel = Label(root,text = "Calendar",font=("Arial",52,"bold"),bg="blue",fg="white")
calLabel.grid(row=0,column=0)

yearLabel = Label(root,text = "Enter year",font=("Arial",20),bg="yellow",fg="blue")
yearLabel.grid(row=1,column=0,sticky="w")

year = Entry(root)
year.grid(row=1,column=0,sticky="e",padx=20)

calbutton = Button(root,text = "show calendar",font=("Arial",15),bg="white",fg="red",command=showcal)
calbutton.grid(row=2,column=0,pady=10)

root.mainloop()