from tkinter import *

def conversioncalc():
    c=celentry.get()
    errormessage.grid_forget()
    try:
        c=float(c)
        f=(c * (9/5)) + 32
        #f=round((c * (9/5)) + 32, 2)
        answer.config(text=str(f)+"F")
        answer.grid(row=3,column=0,columnspan=2)
    except ValueError:
        answer.config(text="")
        print("Wrong input")
        errormessage.grid(row=4,column=0,columnspan=2)

root = Tk()
root.geometry("800x800")
root.config(background="#f886eb")
root.title("Celcius-->Fahrenheit")

cf=Label(root,text="Celcius-->Fahrenheit",font=("Arial",30),bg="#f886eb",fg="white")
cf.grid(row=0,column=0,columnspan=2,padx=225,pady=50)

entercel=Label(root,text="Enter temperature in degree Celcius",font=("Arial",15),bg="#f591e9",fg="white",anchor="nw")
entercel.grid(row=1,column=0,padx=50,pady=100,sticky="e")

celentry=Entry(root)
celentry.grid(row=1,column=1,sticky="w")

convertbutton=Button(root,text="Click here to convert",command=conversioncalc)
convertbutton.grid(row=2, column=0,columnspan=2)

answer=Label(root,font=("Arial",20),bg="#f886eb",fg="white")

errormessage=Label(root,text="Wrong input",font=("Arial",20),bg="#f886eb",fg="white")

root.mainloop()