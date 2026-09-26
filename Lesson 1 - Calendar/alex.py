from tkinter import * 

root = Tk()
root.geometry("500x500")
root.config(background="blue")
root.title("calendar Display")

calendarLabel = Label(root,text="CALENDAR",font=("Arial",30),bg="blue",fg="red")
calendarLabel.grid(row=0,column=0,padx=50)



root.mainloop()