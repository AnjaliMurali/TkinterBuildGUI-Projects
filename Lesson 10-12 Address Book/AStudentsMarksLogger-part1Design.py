import tkinter as tk
from tkinter import ttk

def create_gui():
    # Create the main window
    root = tk.Tk()
    root.title("STUDENT INFORMATION AND MARKS LOGGER")
    root.geometry("600x300")
    root.resizable(False, False)

    # Set the background color of the window
    root.configure(bg="lightgreen")

    # Create a frame for the form fields
    frame = tk.Frame(root, bg="white", padx=5, pady=5)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Add the title label
    title_label = tk.Label(frame, text="STUDENT REPORT LOG", font=("Arial", 12, "bold"), bg="white")
    title_label.grid(row=0, column=0, columnspan=4, pady=(0, 10))

    # Add form fields
    tk.Label(frame, text="Name:", bg="white", font=("Arial", 10)).grid(row=1, column=0, sticky="w", padx=(0, 5))
    name_entry = tk.Entry(frame, width=20)
    name_entry.grid(row=1, column=1, padx=(0, 10), pady=(0, 5))

    tk.Label(frame, text="RollNumber:", bg="white", font=("Arial", 10)).grid(row=2, column=0, sticky="w", padx=(0, 5))
    roll_entry = tk.Entry(frame, width=20)
    roll_entry.grid(row=2, column=1, padx=(0, 10), pady=(0, 5))

    tk.Label(frame, text="Science_Marks:", bg="white", font=("Arial", 10)).grid(row=1, column=2, sticky="w", padx=(10, 5))
    science_entry = tk.Entry(frame, width=20)
    science_entry.grid(row=1, column=3, padx=(0, 10), pady=(0, 5))

    tk.Label(frame, text="Maths_Marks:", bg="white", font=("Arial", 10)).grid(row=2, column=2, sticky="w", padx=(10, 5))
    maths_entry = tk.Entry(frame, width=20)
    maths_entry.grid(row=2, column=3, padx=(0, 10), pady=(0, 5))

    tk.Label(frame, text="Percentage:", bg="white", font=("Arial", 10)).grid(row=3, column=2, sticky="w", padx=(10, 5))
    percentage_entry = tk.Entry(frame, width=20)
    percentage_entry.grid(row=3, column=3, padx=(0, 10), pady=(0, 5))

    # Add a large text area (blue background)
    text_area = tk.Text(frame, width=60, height=5, bg="lightblue", font=("Arial", 10))
    text_area.grid(row=4, column=0, columnspan=4, pady=(10, 10))

    # Add buttons
    button_frame = tk.Frame(frame, bg="white")
    button_frame.grid(row=5, column=0, columnspan=4, pady=(10, 0))

    tk.Button(button_frame, text="Edit", width=10).grid(row=0, column=0, padx=5)
    tk.Button(button_frame, text="Delete", width=10).grid(row=0, column=1, padx=5)
    tk.Button(button_frame, text="Open", width=10).grid(row=0, column=2, padx=5)
    tk.Button(button_frame, text="Update/Add", width=10).grid(row=0, column=3, padx=5)
    tk.Button(button_frame, text="Save", width=10).grid(row=0, column=4, padx=5)

    # Start the Tkinter main loop
    root.mainloop()

if __name__ == "__main__":
    create_gui()
