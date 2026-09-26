from tkinter import *
import tkinter.font as font

def calc():
    c = tempE.get()
    if(c.replace('.','',1).isdigit() or (c.startswith('-') and c[1:].replace('.', '', 1).isdigit())):
        eL.grid_forget()
        f = ((9/5)*float(c))+32
        aL.config(text=str(f)+" F")
    else:
        aL.config(text="") 
        eL.grid(row=0,column=0,padx=20)
    
root = Tk()

root.rowconfigure(0, weight=1)  # Row 0 will expand
root.rowconfigure(1, weight=1)  # Row 1 will expand
root.rowconfigure(2, weight=1)  # Row 1 will expand
root.rowconfigure(3, weight=1)  # Row 1 will expand
root.columnconfigure(0, weight=1)  # Column 0 will expand
root.columnconfigure(1, weight=1)  # Column 0 will expand

Tl = Label(root,text="Celcius -> Farenheit",fg="red", font = font.Font(size = 20))
Tl.grid(row=0,column=1)

tempL = Label(root,text="Enter the degree Celcius here") 
tempL.grid(row=1,column=0)

tempE = Entry(root)
tempE.grid(row=1,column=1,padx=10)

tB = Button(root,text="Convert",command=calc)
tB.grid(row=2,column=1)

aL = Label(root, bg="green",fg="red")
aL.grid(row=3,column=1,padx=20)

frame = Frame(root)
frame.grid()

eL = Label(frame,text="Enter valid input", fg="Red", font=font.Font(size=10),bg="gray")


root.mainloop()
