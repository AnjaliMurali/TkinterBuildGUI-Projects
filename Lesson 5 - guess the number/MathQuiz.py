from tkinter import *
from tkinter import messagebox
import random

# Create window
root = Tk()
root.title("Guess the Product")

"""
# Width = 400, Height = 300
# Position = 200 pixels from left, 100 pixels from top
root.geometry("400x300+200+100")
"""

window_width = 400
window_height = 300

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)


root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Variables to store numbers and answer
num1 = 0
num2 = 0
correct_answer = 0

def show_question():
    global num1, num2, correct_answer

    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    correct_answer = num1 * num2
    messagebox.showinfo("question","What is " + str(num1)+ "X" + str(num2))
"""
    messagebox.showinfo(
        "Question",
        f"What is the product of {num1} × {num2}?"
    )
"""
    

def check_answer():
    try:
        user_answer = int(answer_entry.get())

        if user_answer == correct_answer:
            messagebox.showinfo("Feedback", "Correct Answer!")
        else:
            messagebox.showinfo(
                "Feedback",
                f"Wrong Answer!\nThe correct answer is {correct_answer}"
            )

        answer_entry.delete(0, END)

    except ValueError:
        messagebox.showinfo(
            "Input Error",
            "Please enter a number."
        )

# Widgets
quiz_button = Button(root, text="Quiz", command=show_question)
quiz_button.pack(pady=10)

Label(root, text="Enter your answer:").pack()

answer_entry = Entry(root)
answer_entry.pack(pady=5)

submit_button = Button(root, text="Submit", command=check_answer)
submit_button.pack(pady=10)

root.mainloop()