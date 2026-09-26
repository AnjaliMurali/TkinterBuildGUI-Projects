from tkinter import *

def calc():
    errorL.grid_forget()
    try:
        c_value = tempE.get()
        c_value = float(c_value)  # Try converting input to a float
        f_value = (9/5) * c_value + 32
        ansL.config(text=str(f_value)+" F")
        ansL.grid(row=3,column=0,columnspan=2,padx=30,pady=20)
    except ValueError:
        ansL.config(text=" ")
        ansL.grid_forget()
        print("Please enter a valid number!")
        errorL.grid(row=4,column=0,padx=10)
        


root = Tk()
root.geometry('300x300')
root.config(background="pink")
root.title("Converter")

#when weight is 0, it does not allow the column to expand, if its 1 it(tkinter) allows to expand the column proportionally.
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2,weight=1)

titleLabel = Label(root,text = "Celcius --> Farenheit",bg="pink", font=("Playbill", 28, 'italic'),anchor="w") 
#ew is east west - stretch horizontally east to west. 
titleLabel.grid(row=0,column=0,columnspan=2,sticky="ew",padx=50) 

tempL = Label(root,text="Enter the degree Celcius here") 
tempL.grid(row=1,column=0,sticky="w",padx=10,pady=20)

tempE = Entry(root,width=10,font=("Arial", 12)) 
#there is no height to increase the entry height.We use the fontsize to increase its height
tempE.grid(row=1,column=1,sticky="w")

tB = Button(root,text="Convert",command=calc)
tB.grid(row=2,column=0,columnspan=2,padx=30)

ansL = Label(root, bg="green",fg="red")


errorL = Label(root,text="Enter valid input", fg="Red", font=("Comic Sans MS", 15),bg="pink")


root.mainloop()