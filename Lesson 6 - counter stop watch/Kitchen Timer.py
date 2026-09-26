import tkinter as tk
from tkinter import messagebox

# Create window
root = tk.Tk()
root.title("Kitchen Timer")
root.geometry("300x200")

# Label to display time
time_label = tk.Label(root, text="00:00", font=("Arial", 30))
time_label.pack(pady=20)


# Countdown function
def countdown(seconds):
    mins, secs = divmod(seconds, 60)
    time_label.config(text=f"{mins:02d}:{secs:02d}")
    # or instead of above line it can also be written as: 
            # formatted_time = "{:02d}:{:02d}".format(mins, secs)
            # time_label.config(text=formatted_time)
    for btn in (btn1, btn2, btn3):
        btn.config(state="disabled")
    if seconds > 0:
        root.after(1000, countdown, seconds - 1)
    else:
        messagebox.showinfo("Timer", "Time's up!")
        for btn in (btn1, btn2, btn3):
            btn.config(state="normal")





# Buttons
btn1 = tk.Button(root, text="Soft Boiled (3 min)", width=20,
                 command=lambda: countdown(180))
btn1.pack(pady=5)

btn2 = tk.Button(root, text="Medium (5 min)", width=20,
                 command=lambda: countdown(300))
btn2.pack(pady=5)

btn3 = tk.Button(root, text="Hard Boiled (10 min)", width=20,
                 command=lambda: countdown(600))
btn3.pack(pady=5)


# Run app
root.mainloop()