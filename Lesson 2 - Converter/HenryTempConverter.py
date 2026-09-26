from tkinter import *

root=Tk()
root.geometry("500x500")
root.config(background="grey")
root.title("Celcius to Farenheit")

def ConvertFunc():
    global resultFa
    try:
        inputCel=float(entryBox.get())
        resultFa=str((inputCel*9/5)+32)
        print(resultFa)
        resultLabel.config(text=resultFa+"f")
        resultLabel.grid(row=3,column=0,columnspan=2)
    except ValueError:
        resultLabel.config(text="You can only input numbers for the conversion. Please try again")
        resultLabel.grid(row=3,column=0,columnspan=2)

headingLabel=Label(root,bg="grey",fg="white",text="Celcius to Farenheit",font=("Ariel",20,"bold"))
headingLabel.grid(row=0,column=0,columnspan=2)
entryNoteLabel=Label(root,bg="grey",fg="white",text="Enter Degrees (in celcius)",font=("Ariel",15))
entryNoteLabel.grid(row=1,column=0,sticky="w",pady=40,padx=10)
entryBox=Entry(root,font=("Arial",15),width=20)
entryBox.grid(row=1,column=1)
buttonButton=Button(root,bg="black",fg="white",text="CONVERT",font=("Arial",15,"bold"),command=ConvertFunc)
buttonButton.grid(row=2,column=0,columnspan=2)
resultLabel=Label(root,bg="grey",fg="white",font=("Arial",10))

root.mainloop()