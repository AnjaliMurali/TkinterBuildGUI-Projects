from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
import os as os

adrsbk = {}

def clear_all():
    NameE.delete(0,END)
    AdrsE.delete(0,END)
    MobE.delete(0,END)
    EmailE.delete(0,END)
    BDE.delete(0,END)

def add():
    n = NameE.get()
    if n=="":
        messagebox.showinfo("Error","Name cannot be empty")
    else:
        if n not in adrsbk.keys():
            LB.insert(END,n)
        adrsbk[n] = (AdrsE.get(),MobE.get(),EmailE.get(),BDE.get())
        clear_all()


def edit():
    i = LB.curselection()
    if i :
        NameE.insert(0,LB.get(i))
        details = adrsbk[LB.get(i)]
        AdrsE.insert(0,details[0])
        MobE.insert(0,details[1])
        EmailE.insert(0,details[2])
        BDE.insert(0,details[3])
    else:
        messagebox.showinfo("Error","Insertion error")

def delete():
    i = LB.curselection()
    if i:
        del adrsbk[LB.get(i)]
        LB.delete(i)
        clear_all()
    else:
        messagebox.showinfo("Error","Select a name")

def reset():
    clear_all()
    LB.delete(0,END)
    adrsbk.clear()
    AddBookL.configure(text='My Address Book')

def save():
    fout=asksaveasfile(defaultextension=".txt") #if filename selected
    if fout:
        print(adrsbk,file=fout)
        reset()          
    else:
        messagebox.showinfo("Warning", "Address Book not saved")


def openFile():
    global adrsbk
    reset()
    fin=askopenfile(title='Open File')
    if fin:
        adrsbk=eval(fin.read())
        #populate listbox
        for key in adrsbk.keys():
            LB.insert(END,key)
        #dispaly filename on screen
        AddBookL.configure(text=os.path.basename(fin.name))
    else:
        messagebox.showinfo("Warning", "No address book opened.")

root = Tk()
root.title("Address Book")

AddBookL = Label(root,text="My AddressBook")
AddBookL.grid(row=0,column=1,padx=20)

OpenB = Button(root,text="Open",width=10,command=openFile)
OpenB.grid(row=0,column=2)

LB = Listbox(root,width=35,height=15)
LB.grid(row=1,column=0,rowspan=5,columnspan=2,padx=10)

NameL = Label(root,text="Name :")
NameL.grid(row=1,column=2) 

NameE = Entry(root)
NameE.grid(row=1,column=3,padx=(0,10)) #creates the space at the left and right of the widget. 

AdrsL = Label(root,text="Address :")
AdrsL.grid(row=2,column=2) 

AdrsE = Entry(root)
AdrsE.grid(row=2,column=3)

MobL = Label(root,text="Mobile :")
MobL.grid(row=3,column=2) 

MobE = Entry(root)
MobE.grid(row=3,column=3)

EmailL = Label(root,text="Email :")
EmailL.grid(row=4,column=2) 

EmailE = Entry(root)
EmailE.grid(row=4,column=3)

BDL = Label(root,text="Birthday :")
BDL.grid(row=5,column=2) 

BDE = Entry(root)
BDE.grid(row=5,column=3)

EditB = Button(root,text="Edit",command=edit)
EditB.grid(row=6,column=0,pady=20)

DelB = Button(root,text="Delete",command=delete)
DelB.grid(row=6,column=1,pady=20)

UpdateB = Button(root,text="Update/Add", command=add)
UpdateB.grid(row=6,column=3,pady=20)

SaveB = Button(root,text="Save",width=30, command=save)
SaveB.grid(row=7,column=2,columnspan=1,pady=10)

root.mainloop()

