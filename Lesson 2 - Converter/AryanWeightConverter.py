from tkinter import *

def kgconversion():
    kg=kgentry.get()
    try:
        kg=float(kg)
        g=kg*1000
        gramentry.delete(0,END)
        gramentry.insert(0,g)
        Lbs=kg*2.20462
        poundentry.delete(0,END)
        poundentry.insert(0,Lbs)
        Ounce=kg*35.274
        ounceentry.delete(0,END)
        ounceentry.insert(0,Ounce)
    except ValueError:
        print("Wrong input")



root = Tk()
root.geometry("700x300")
root.config(background="#86bff8")
root.title("Kg-->gram,pound & ounce")

kglbl=Label(root,text="Enter kg:",font=("Arial",30),bg="#86bff8",fg="White")
kglbl.grid(row=0,column=0,pady=70,padx=20)

kgentry=Entry(root)
kgentry.grid(row=0,column=1,pady=70,padx=60)

kgbutton=Button(root,text="Click to convert",font=("Arial",20),bg="White",fg="#86bff8",command=kgconversion)
kgbutton.grid(row=0,column=2)

gramlbl=Label(root,text="Gram",font=("Arial",20),bg="#86bff8",fg="White")
gramlbl.grid(row=1,column=0)

gramentry=Entry(root)
gramentry.grid(row=2,column=0)

poundlbl=Label(root,text="Pound",font=("Arial",20),bg="#86bff8",fg="White")
poundlbl.grid(row=1,column=1)

poundentry=Entry(root)
poundentry.grid(row=2,column=1)

ouncelbl=Label(root,text="Ounce",font=("Arial",20),bg="#86bff8",fg="White")
ouncelbl.grid(row=1,column=2)

ounceentry=Entry(root)
ounceentry.grid(row=2,column=2)


root.mainloop()