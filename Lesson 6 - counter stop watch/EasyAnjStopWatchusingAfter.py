#import time
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x250")
root.title("Time Counter")

temp=0
def submit():
    global temp
    btn.config(state="disabled")
    hourEntry.config(state="disabled")
    minuteEntry.config(state="disabled")
    secondEntry.config(state="disabled")
    temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())

    def update_timer():
        global temp
        mins, secs = divmod(temp, 60)
        hours, mins = divmod(mins, 60)

        hour.set(f"{hours:02d}")
        minute.set(f"{mins:02d}")
        second.set(f"{secs:02d}")

        if temp == 0:
            messagebox.showinfo("Time Countdown", "Time's up!")
            # Re-enable widgets
            btn.config(state="normal")
            hourEntry.config(state="normal")
            minuteEntry.config(state="normal")
            secondEntry.config(state="normal")
            return

        temp -= 1
        root.after(1000, update_timer)

    update_timer()  

# Declaration of variables
#StringVar() are special tkinter variables for values that 
#change frequently or need to stay synchronized with widgets.
hour = StringVar()
minute = StringVar()
second = StringVar()

# setting the default value as 0
hour.set("00")
minute.set("00")
second.set("00")

# Use of Entry class to take input from the user
#width=3 means the entry is approximately wide enough to display 3 average-width characters using the current font.
hourEntry = Entry(root, width=3, font=("Arial", 18, "bold"),
                  textvariable=hour)
hourEntry.place(x=80, y=20)

minuteEntry = Entry(root, width=3, font=("Arial", 18, "bold"),
                    textvariable=minute)
minuteEntry.place(x=130, y=20)

secondEntry = Entry(root, width=3, font=("Arial", 18, "bold"),
                    textvariable=second)
secondEntry.place(x=180, y=20)
btn = Button(root, text='Set Time Countdown', bd='5',
             command=submit)
btn.place(x=70, y=120)




root.mainloop()