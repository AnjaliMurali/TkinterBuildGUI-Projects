from tkinter import *
import calendar

# Function to display the selected month's calendar
def show_month():
    year = int(year_entry.get())
    month = int(month_entry.get())

    # Get the calendar as a string
    cal = calendar.month(year, month)

    # Display it in the label
    calendar_label.config(text=cal)

# Create the main window
root = Tk()
root.title("Monthly Calendar")

# Year input
Label(root, text="Year:").grid(row=0, column=0, padx=5, pady=5)
year_entry = Entry(root)
year_entry.grid(row=0, column=1, padx=5, pady=5)

# Month input
Label(root, text="Month Number:").grid(row=1, column=0, padx=5, pady=5)
month_entry = Entry(root)
month_entry.grid(row=1, column=1, padx=5, pady=5)

# Show Month button
Button(root, text="Show Month", command=show_month).grid(row=2, column=0, columnspan=2, pady=10)

# Label to display the calendar
calendar_label = Label(root, font=("Consolas", 12), justify=LEFT)
calendar_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()