from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import * 

root=Tk()
root.title("template")

everyDictionary={}

def click(event):
    item=box.curselection()
    itemstr=box.get(item)
    details=everyDictionary[itemstr]
    #details2="Name: "+everyDictionary[itemstr]+"\n\n"
    #details2+=
    messagebox.showinfo("Entry","Name: "+itemstr+"\nE-mail: "+details[0]+"\nNumber: "+details[1]+"\nAddress: "+details[2]+"\nB-Day: "+details[3])

def clear_all():
    nameEnt.delete(0,END)
    emailEnt.delete(0,END)
    numberEnt.delete(0,END)
    addressEnt.delete(0,END)
    bdayEnt.delete(0,END)

def apply():
    key = nameEnt.get()
    if key not in everyDictionary:
        box.insert(END,nameEnt.get())
    everyDictionary[nameEnt.get()]=(emailEnt.get(),numberEnt.get(),addressEnt.get(),bdayEnt.get())
    clear_all()    

def edit():
    item=box.curselection()
    if item:
        nameEnt.insert(0,box.get(item))
        details=everyDictionary[box.get(item)]
        emailEnt.insert(0,details[0])
        numberEnt.insert(0,details[1])
        addressEnt.insert(0,details[2])
        bdayEnt.insert(0,details[3])
    else:
            messagebox.showinfo("Error", "Select a name.")

def delete():
    item=box.curselection()
    if item:
        #delete from dictionary
        del everyDictionary[box.get(item)]
        #delete from listbox
        box.delete(item)
        #clear the textboxes if any
        clear_all()
    else:
        messagebox.showinfo("Error", "Select a name.")

def save():
    fout=asksaveasfile(defaultextension=".txt")
    #if fout:
    print(everyDictionary,file=fout)
    box.delete(0, END)

def open():
    global everyDictionary
    fin=askopenfile(title='Open File')
    box.delete(0, END)
    clear_all()
    #Removes all existing entries
    everyDictionary.clear()
    #fin.read() jut reads the entire file as a string and not a dictionary. 
    #eval() converts the string into the dictionary.
    everyDictionary=eval(fin.read())
    #populate listbox
    for key in everyDictionary.keys():
        box.insert(END,key)


frameAdd=Frame(root)
frameAdd.pack(pady=(10,30))

addressText=Label(frameAdd,text="Address book")
addressText.grid(row=0,column=0)
addressOpen=Button(frameAdd,text="OPEN",command=open)
addressOpen.grid(row=0,column=1)

frameMid=Frame(root)
frameMid.pack()

box=Listbox(frameMid,height=12,width=20)
box.grid(row=0,column=0,rowspan=5,columnspan=2)
box.bind('<<ListboxSelect>>',click)
nameText=Label(frameMid,text="Name: ")
nameText.grid(row=0,column=2,padx=(10,0))
emailText=Label(frameMid,text="Email: ")
emailText.grid(row=1,column=2,padx=(10,0))
numberText=Label(frameMid,text="Number: ")
numberText.grid(row=2,column=2,padx=(10,0))
addressText=Label(frameMid,text="Address: ")
addressText.grid(row=3,column=2,padx=(10,0))
bdayText=Label(frameMid,text="B-Day: ")
bdayText.grid(row=4,column=2,padx=(10,0))

nameEnt=Entry(frameMid,width=10)
nameEnt.grid(row=0,column=3)
emailEnt=Entry(frameMid,width=10)
emailEnt.grid(row=1,column=3)
numberEnt=Entry(frameMid,width=10)
numberEnt.grid(row=2,column=3)
addressEnt=Entry(frameMid,width=10)
addressEnt.grid(row=3,column=3)
bdayEnt=Entry(frameMid,width=10)
bdayEnt.grid(row=4,column=3)

delButton=Button(frameMid,text="DELETE",command=delete)
delButton.grid(row=5,column=0,pady=10)
editButton=Button(frameMid,text="EDIT",command=edit)
editButton.grid(row=5,column=1,pady=10)
applyButton=Button(frameMid,text="APPLY",command=apply)
applyButton.grid(row=5,column=3,pady=10)
saveButton=Button(root,text="SAVE",width=15,command = save)
saveButton.pack()

root.mainloop()