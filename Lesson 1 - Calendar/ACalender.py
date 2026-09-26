from tkinter import *
import calendar
#Note: If the calendar module is not found. It could be the name conflict with file name and folder name. 
# Make sure file name and folder name are not calendar.py

def showCal():
    gui= Tk()
    gui.geometry("1000x600")
    fetch_year = int(yi.get())
    cal_content = calendar.calendar(fetch_year)
    cal_year = Label(gui, text=cal_content,padx = 20,pady = 20, font="Consolas 10",justify=LEFT,
    anchor="nw") 
    cal_year.grid(row=5, column=1, padx=20)
    gui.mainloop()

root = Tk()
root.geometry('200x300')
root.config(background="pink")
root.title("CALENDER")

cal = Label(root, text="CALENDAR", bg="gray",font=("Playbill", 28, 'bold'))
cal.grid(row=0, column=1)
y = Label(root,text="Enter Year")
y.grid(row=1,column=0,sticky="e")
yi = Entry(root)
yi.grid(row=1,column=1)
b = Button(root, text="Show Calendar", fg="Black", bg="Red", command=showCal)
b.grid(row=3,column=1)
#Exit = Button(root, text="Exit", fg="Black", bg="Red", command=exit)
#Exit.grid(row=4, column=1)

# Configure the grid columns to center the label
#root.grid_columnconfigure(0, weight=1)  # Left empty column
#root.grid_columnconfigure(1, weight=1)  # Center column
#root.grid_columnconfigure(2, weight=1)  # Right empty column
#cal.pack(side="top", anchor="n")


root.mainloop()