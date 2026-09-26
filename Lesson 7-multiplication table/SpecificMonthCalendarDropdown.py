from tkinter import *
#from tkinter.ttk import *
from tkinter.ttk import Combobox
import calendar

# Function to display the selected month's calendar
def show_month():
    year = int(year_entry.get())
    #month = int(month_combo.get())
    month = month_number.get()
    cal = calendar.month(year, month)
    calendar_label.config(text=cal)

# Create the main window
root = Tk()
root.title("Monthly Calendar")

# Year
Label(root, text="Enter Year:").grid(row=0, column=0, padx=5, pady=5)

year_entry = Entry(root)
year_entry.grid(row=0, column=1, padx=5, pady=5)

# Month Combobox
Label(root, text="Select Month:").grid(row=1, column=0, padx=5, pady=5)

"""
month_combo = Combobox(root, values=[
    1, 2, 3, 4, 5, 6,
    7, 8, 9, 10, 11, 12
], width=10)
"""

month_number = IntVar()
month_combo = Combobox(root,width=10,textvariable = month_number)
month_combo["values"] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#month_combo.current(0)      # Default to January
month_combo.grid(row=1, column=1, padx=5, pady=5)

# Button
Button(root, text="Show Month", command=show_month).grid(row=2, column=0, columnspan=2, pady=10)

# Calendar Label
calendar_label = Label(root, font=("Courier", 12), justify=LEFT)
calendar_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()