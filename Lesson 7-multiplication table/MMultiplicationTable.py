from tkinter import *
#combobox is defined inside ttk
from tkinter.ttk import *
  
# Creating tkinter window 
window = Tk() 
window.title('Mathematical table generator')
  
# label text for title 
title=Label(window, text = "Mathematical table")
title.grid(row = 0, column = 0,columnspan = 3, pady=25)
# label 
caption=Label(window, text = "Number and Range:")
caption.grid(column = 0,row = 1,padx=10)
  
# Combobox creation 
#A Combobox in Tkinter is a widget that combines an Entry box and a drop-down list.
#In Tkinter, the Combobox is provided by the ttk module.
theNum = IntVar() 
numbers=Combobox(window,textvariable = theNum,width=5)   
# Adding combobox drop down list 
#range(start, stop, step)
#list/tuple can be used to list down the values (you can write as in line 24 or 25)
numbers['values'] = tuple(range(101))
#numbers['values'] = list(range(1, 101))

numbers.grid(column = 1, row = 1)
# IntVar() is a special Tkinter variable class 
# used to store integer values that can automatically connect to GUI widgets.

#radio buttons
endVal = IntVar()
r10=Radiobutton(window,text="10",variable=endVal,value=10)
r20=Radiobutton(window,text="20",variable=endVal,value=20)
r30=Radiobutton(window,text="30",variable=endVal,value=30)
#set the default value
endVal.set(10)


#place radiobuttons and combobox

r10.grid(column = 2, row = 1)
r20.grid(column = 2, row = 2,padx=30)
r30.grid(column = 2, row = 3,padx=30)

#use any function - whichever is easy for the learner. 
"""
def generateMulTable():
    tables=""
    #for i in range(1,endVal.get()+1,1):
    for i in range(endVal.get()+1):
        #tables+="{:^10d} X {:^10d} = {:^10d}\n".format(theNum.get(),i,theNum.get()*i)
        tables+=str(theNum.get())+"   X   "+str(i)+"   =   "+str(theNum.get()*i)+"\n" 
    table.configure(text=tables)
"""

def generateMulTable():
    num = theNum.get()
    end = endVal.get()

    tables = ""
    for i in range(end + 1):
        tables += f"{num} X {i} = {num * i}\n"

    table.configure(text=tables)

#create button and result table
generateButton=Button(window,text="Generate",command=generateMulTable)
generateButton.grid(row=4,column=1)

table=Label(window,anchor="center")
table.grid(row=5,column=1, pady = 25)


window.mainloop() 