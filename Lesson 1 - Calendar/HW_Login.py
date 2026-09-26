from tkinter import *

gui = Tk()
gui.geometry("300x300")
gui.title("Login")
gui.config(background="grey")
label_title = Label(gui,text="Login",bg="grey")
label_title.grid(row=0,column=0,columnspan=2,pady=20)
label_un = Label(gui,text="Username : ",bg="red",fg="yellow")
label_un.grid(row=1,column=0,padx=30,sticky="w")
entry_un = Entry(gui)
entry_un.grid(row=1,column=1,padx=0,pady= 20, sticky="w")
label_pw = Label(gui,text="Password : ",bg="red",fg="yellow")
label_pw.grid(row=2,column=0,padx=30,sticky="w")
entry_pw = Entry(gui,show="*")
entry_pw.grid(row=2,column=1,padx=0,pady= 2, sticky="w")

gui.mainloop()