import time
from tkinter import *
from tkinter import messagebox

# creating Tk window
root = Tk()

# setting geometry of tk window
root.geometry("300x250")

# Using title() to display a message in
# the dialogue box of the message in the
# title bar.
root.title("Time Counter")

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
hourEntry = Entry(root, width=3, font=("Arial", 18, "bold"),
                  textvariable=hour)
hourEntry.place(x=80, y=20)

minuteEntry = Entry(root, width=3, font=("Arial", 18, "bold"),
                    textvariable=minute)
minuteEntry.place(x=130, y=20)

secondEntry = Entry(root, width=3, font=("Arial", 18, "bold"),
                    textvariable=second)
secondEntry.place(x=180, y=20)


def submit():
    #disabled state could be added later so button/ entries are not editted or clicked again. 
    btn.config(state="disabled")
    hourEntry.config(state="disabled")
    minuteEntry.config(state="disabled")
    secondEntry.config(state="disabled")
    #can add try and except to avoid typing incorrect values. 
    try:
        h = int(hour.get())
        m = int(minute.get())
        s = int(second.get())
     
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter numbers only")
        btn.config(state="normal")
        hourEntry.config(state="normal")
        minuteEntry.config(state="normal")
        secondEntry.config(state="normal")
        return
    
    if h < 0 or m < 0 or s < 0:
            messagebox.showerror("Invalid input", "Please enter positive numbers only")
            btn.config(state="normal")
            hourEntry.config(state="normal")
            minuteEntry.config(state="normal")
            secondEntry.config(state="normal")
            return

    temp = h * 3600 + m * 60 + s
    #temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
    while temp > -1:

        # divmod(firstvalue = temp//60, secondvalue = temp%60)
        mins, secs = divmod(temp, 60)

        # Converting the input entered in mins or secs to hours,
        # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
        # 50min: 0sec)
        #hours = 00
        if mins > 60:
            # divmod(firstvalue = temp//60, secondvalue
            # = temp%60)
            hours, mins = divmod(mins, 60)
        else:
            hours = 0

        # using format () method to store the value with 2 digits. 
        #example: 5 will be printed as 05. 
       
        #hour.set(hours) #0-9 only 1 digit will be displayed, instead of 09, it displays just 9
        hour.set("{:02d}".format(hours))
        minute.set("{:02d}".format(mins))
        #second.set("{:02d}".format(secs))
        second.set(f"{secs:02d}")
       

        # updating the GUI window after decrementing the
        # temp value every time
        root.update()
        time.sleep(1)

        # when temp value = 0; then a messagebox pop's up
        # with a message:"Time's up"
        if (temp == 00):
            messagebox.showinfo("Time Countdown", "Time's up ")

        # after every one sec the value of temp will be decremented
        # by one
        temp -= 1


# button widget
btn = Button(root, text='Set Time Countdown', bd='5',
             command=submit)
btn.place(x=70, y=120)

# infinite loop which is required to
# run tkinter program infinitely
# until an interrupt occurs
root.mainloop()