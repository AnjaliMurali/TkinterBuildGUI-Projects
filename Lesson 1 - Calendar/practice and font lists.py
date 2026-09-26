from tkinter import *
import calendar
#from tkinter import font

def calender():
    c = Tk()
    c.geometry("550x600")
    fetch_year = int(yi.get())
    cal_content = calendar.calendar(fetch_year)
    cal_year = Label(c, text=cal_content,padx = 20,pady = 20, font="Consolas 10 bold",justify="left")
    cal_year.grid(row=0, column=0, columnspan=3, pady=20, sticky="n")
    c.mainloop()

root = Tk()
root.geometry('300x300')
root.config(background="pink")
root.title("CALENDER")
#root.mainloop()

#To List down the different fonts available in system. Tkinter uses the font available in the system. 
# fonts = list(font.families())
# fonts.sort()

# for f in fonts:
#     print(f)

cal = Label(root, text="CALENDAR", bg="gray",font=("Sitka Small Semibold", 28, 'bold'))
cal.grid(row=0, column=0,columnspan=10,pady=10, padx=15)
y = Label(root,bg = "yellow" ,text="Enter Year")
y.grid(row=1,column=0,pady=10,padx=20)
#yi = Entry(root) # we can only increase the width of input box. 
yi = Entry(root,width=25)
#yi.grid(row=1,column=1,padx=30,ipady = 5) to increase the height of Entry, use internal padding ipady.
yi.grid(row=1,column=1,padx=30)
b = Button(root, text="Show Calendar", fg="Black", bg="Red",command=calender)
b.grid(row=2,column=0,columnspan=2) #Grid columns don’t exist visually until something gives them width
root.mainloop()

