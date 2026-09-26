from tkinter import *
from time import strftime

def time():
    if mode=="24":
        t24=strftime('%H:%M:%S')
        timelbl.config(text=t24)
        timelbl.after(1000,time)
        d=strftime('%A  %d / %m(%B) / %Y')
        datelbl.config(text=d)
    else:
        t12=strftime('%I:%M:%S %p')
        timelbl.config(text=t12)
        timelbl.after(1000,time)
        d=strftime('%A  %d / %m(%B) / %Y')
        datelbl.config(text=d)

mode="24"

def set12():
    global mode
    mode="12"

def set24():
    global mode
    mode="24"
    

root = Tk()
root.config(background="#4fe3c8")
root.title("Time")

timelbl=Label(root,font=("Arial",40),background="#4fe3c8",foreground="White")
timelbl.grid(row=0,column=0)

datelbl=Label(root,font=("Arial",40),background="#4fe3c8",foreground="White")
datelbl.grid(row=1,column=0)

twentyfour=Button(root,text="click here for 24 hour clock",font=("Arial",30),bg="#4fe3c8",fg="White",command=set24)
twentyfour.grid(row=2,column=0)

twelve=Button(root,text="click here for 12 hour clock",font=("Arial",30),bg="#4fe3c8",fg="White",command=set12)
twelve.grid(row=2,column=1)

time()

root.mainloop()