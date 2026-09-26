from tkinter import *
from tkinter.ttk import Combobox

def generateMulTable():
    # note we need to get the values from the IntVar varibales.
    # we can get the value from the combobox widget, but then you need to convert it to the int. 
    #but we can only get the value of the radio button from the intvar because there are 3 radio buttons 
    number = num.get()
    end = num2.get()

    tables = ""
    for i in range(end + 1):
        tables += f"{number} X {i} = {number * i}\n"
        #tables += str(number) + " x " + str(i) + " = " + str(number*i) + "\n"

    resultlbl.configure(text=tables)


root = Tk()
#root.geometry("270x1000")
root.config(bg="#7DCB9F")
root.title("Mathematical table generator")

titlelbl=Label(root,text="Mathematical table",bg="#7DCB9F",font=("Arial", 13))
titlelbl.grid(row=0,column=0,columnspan=2,pady=(20, 25),padx=20)

number_range=Label(root,text="Number and Range:",bg="#7DCB9F",font=("Arial", 10))
number_range.grid(row=1,column=0,padx=(20, 5),pady=5)

num=IntVar()
numrange=Combobox(root,textvariable=num,width=5)
numrange['values']=tuple(range(1,101))
#numrange['values'] = list(range(1, 101))
#numrange['values']=tuple(range(1,101))
numrange['values']=tuple(range(1,101))
#numrange.current(0)  # to default to the 1st item in values - here 0 is the index and it refers to 1. 
numrange.grid(row=2,column=0,padx=(20, 0),pady=(0, 15),sticky=W) #padx=(left, right)

num2=IntVar()
radbtn1=Radiobutton(root,text="10",variable=num2,value=10,bg="#7DCB9F")
radbtn1.grid(row=1,column=1,padx=(0, 20),sticky=W)

radbtn2=Radiobutton(root,text="20",variable=num2,value=20,bg="#7DCB9F")
radbtn2.grid(row=2,column=1, padx=(0, 20), sticky=W)

radbtn3=Radiobutton(root,text="30",variable=num2,value=30,bg="#7DCB9F")
radbtn3.grid(row=3,column=1,padx=(0, 20),sticky=W)

generatebtn=Button(root,text="Generate",width=12,command=generateMulTable)
generatebtn.grid(row=4,column=0,columnspan=2,pady=25)

resultlbl=Label(root,bg="#7DCB9F",font=("Arial", 10))
resultlbl.grid(row=5,column=0,columnspan=2)

root.mainloop()