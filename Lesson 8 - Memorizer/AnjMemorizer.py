from tkinter import *
from tkinter.filedialog import * #Imports file dialog functions such as askopenfile() asksaveasfile() askdirectory() askopenfilename()


#create the window
master = Tk()
#title of window
master.title("Memorizer")

#callback function to open file
def openFile():
    #opens file using dialog
    fin=askopenfile(title='Open File')
    #if filename selected
    #if fin is not None:
    #delete items in listbox
    listbox.delete(0, END)
    #read from file
    items = fin.readlines()
    #print (items)
    #insert to listbox
    for item in items:
        listbox.insert(END, item)
        #listbox.insert(END, item.strip())

#callback function to save file                
def saveFile():
    #get file using dialog
    # default extension is optional, here will add .txt if missing
    fout=asksaveasfile(defaultextension=".txt")
    #if filename selected
    #if fout is not None:
        #get items in listbox and add to file
    for item in listbox.get(0,END):
        print(item.strip(),file=fout) #here instead of usual print in console, it prints into the file
    #delete items in listbox
    listbox.delete(0, END)

#Function to add item to listbox
def addItem():
    listbox.insert(END,item.get())
    #delete from textbox
    item.delete(0,END)

#Function to delete item from listbox
def deleteItem():
    # get selected line index
    index = listbox.curselection()
    if index:        
        listbox.delete(index)

def clearList():
    listbox.delete(0, END)
        

#create all buttons and place them on screen
fOpen=Button(master,text="OPEN",command=openFile,width=15)
lDelete=Button(master,text="DELETE",command=deleteItem,width=15)
fSave=Button(master,text="SAVE",command=saveFile,width=15)
fOpen.pack(side = LEFT, padx=5,pady=5)
lDelete.pack(side = RIGHT , padx=5,pady=5)
fSave.pack(padx=5,pady=5)

#create add button and input, place them on screen
lAdd=Button(master,text="ADD",command=addItem,width=15)
lClear=Button(master,text="CLEAR",command=clearList,width=15)
item=Entry(master,width=35)
item.pack(padx=5,pady=5)
lAdd.pack(padx=5,pady=5)
lClear.pack(padx=5,pady=5)

#create listbox and place on screen

#frame = Frame(master)
scrollbar = Scrollbar(master, orient = "vertical")
scrollbar.pack(side = RIGHT, fill = Y)

listbox = Listbox(master,width=70,height=5, yscrollcommand=scrollbar.set, bg = 'red')
#listbox = Listbox(master,width=70,height=5,  bg = 'red')
for i in range(1,100):
    listbox.insert(END, "LIST "+ str(i))

listbox.pack(side = LEFT, padx = 5)    
scrollbar.config(command=listbox.yview)


#frame.pack(side = RIGHT)
#listbox.grid(row=2,column=0,columnspan=3,pady=20,padx=5)
#scrollbar.grid(row=2,column=2,columnspan=3, sticky='NS')


mainloop()