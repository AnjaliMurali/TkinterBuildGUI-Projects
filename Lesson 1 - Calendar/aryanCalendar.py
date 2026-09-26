from tkinter import *
import calendar

def Calendarwin():
    C = Tk()
    C.geometry("800x800")
    #C.config(background="")
    C.title("Calendar")
    fy=int(iy.get())
    calcontent=calendar.calendar(fy)
    fc=Label(C,text=calcontent,font=("Arial",10),fg="green")
    fc.grid(row=0,column=0)

    C.mainloop()

root = Tk()
root.geometry("800x800")
root.config(background="#03adfc")
root.title("Calendar set up")

calendartxt=Label(root,text="CALENDAR",font=("Arial",50,"bold"),bg="#03adfc",fg="white")
calendartxt.grid(row=0,column=0,columnspan=3,padx=200,pady=50)

enter=Label(root,text="Enter year",font=("Arial",20),bg="#03adfc",fg="white")
enter.grid(row=1,column=0)

iy=Entry(root)
iy.grid(row=1,column=1)

yb=Button(root,text="Show calendar",font=("Arial",20),fg="white",bg="light grey",command=Calendarwin)
yb.grid(row=2,column=1,pady=10)


root.mainloop()