import tkinter as tk
from tkinter import messagebox

# -----------------------------
# Exam Timer
# -----------------------------

def start_exam():
    """Starts the countdown."""
    try:
        minutes = int(min_entry.get() or 0)
        seconds = int(sec_entry.get() or 0)

        if minutes < 0 or seconds < 0:
            raise ValueError

        total = minutes * 60 + seconds

        if total <= 0:
            messagebox.showerror("Invalid Time", "Please enter a time greater than 0.")
            return

        start_button.config(state=tk.DISABLED)
        countdown(total)

    except ValueError:
        messagebox.showerror("Invalid Input", "Enter valid integer values for minutes and seconds.")


def countdown(total_seconds):
    """Updates the timer every second."""
    mins = total_seconds // 60
    secs = total_seconds % 60

    # Change color based on remaining time
    if total_seconds > 10:
        timer_label.config(fg="black")
    else:
        timer_label.config(fg="red")

    timer_label.config(text=f"{mins:02}:{secs:02}")

    if total_seconds > 0:
        root.after(1000, countdown, total_seconds - 1)
    else:
        timer_label.config(text="Time's Up", fg="red")
        start_button.config(state=tk.NORMAL)


# -----------------------------
# GUI
# -----------------------------

root = tk.Tk()
root.title("Exam Timer")
root.geometry("300x220")

tk.Label(root, text="Minutes:").pack(pady=(10, 0))
min_entry = tk.Entry(root, width=10)
min_entry.pack()

tk.Label(root, text="Seconds:").pack(pady=(10, 0))
sec_entry = tk.Entry(root, width=10)
sec_entry.pack()

start_button = tk.Button(root, text="Start Exam", command=start_exam)
start_button.pack(pady=15)

timer_label = tk.Label(
    root,
    text="00:00",
    font=("Arial", 24),
    fg="black"
)
timer_label.pack(pady=10)

root.mainloop()