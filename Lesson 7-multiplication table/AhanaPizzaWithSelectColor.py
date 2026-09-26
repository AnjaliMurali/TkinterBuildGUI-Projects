from tkinter import *
from tkinter.ttk import Combobox

def order_placed():
    pizza = opts.get()
    amount = num.get()
    psize = size.get()
    if pizza and amount and psize:
        finalo.config(text="You ordered "+amount+" "+psize+" "+pizza+" pizza(s)")
    else:
        finalo.config(text="Please select all options")

root = Tk()
root.geometry("600x700")
root.config(background="red")
root.title="Dominos"

title = Label(root,text="Welcome to Domino's!",font=("Arial",30,"bold"),bg="blue",fg="white")
title.grid(row=0,column=0,padx=40)

poL = Label(root,text="Pizza options:",font=("Arial",20),bg="white",fg="blue")
poL.grid(row=1,column=0,pady=30)

opts = StringVar()

po = Combobox(root,state="readonly",textvariable=opts)
po["values"]=["pepperoni","margharita","chicken"]
po.grid(row=2, column=0)

quanL = Label(root,text="Enter quantity:",font=("Arial",20),bg="white",fg="blue")
quanL.grid(row=3,column=0,pady=30)

num = StringVar()

quan = Combobox(root,textvariable=num)
quan["values"]=tuple(range(0,11))
quan.grid(row=4,column=0)

sizeL = Label(root,text="Select size:", font=("Arial",20),bg="white",fg="blue")
sizeL.grid(row=5,column=0,pady=30)

size = StringVar()
size.set("small") # to have small selected by default 
#Combining the above 2 lines - we can also write
#size = StringVar(value="small")
sizes = Frame(root,bg="red")
sizes.grid(row=6,column=0)
small = Radiobutton(sizes,text="S",variable=size,value="small",bg="blue",fg="white",selectcolor="red")
small.grid(row=0,column=0)
medium = Radiobutton(sizes,text="M",variable=size,value="medium",bg="blue",fg="white",selectcolor="red")
medium.grid(row=0,column=1,padx=25)
large = Radiobutton(sizes,text="L",variable=size,value="large",bg="blue",fg="white",selectcolor="red")
large.grid(row=0,column=2)

order = Button(root,text="place order",font=("Arial",10),bg="white",fg="black",command=order_placed)
order.grid(row=7,column=0,pady=50)

finalo = Label(root,text=" ",font=("Arial",25),bg="red",fg="blue")
finalo.grid(row=8,column=0)

root.mainloop()