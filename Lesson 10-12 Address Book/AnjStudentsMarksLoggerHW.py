
import tkinter as tk
from tkinter import messagebox, filedialog
import os

# Global dictionary to store student information
addressbook = {}


def handle_add_update():

    name = name_entry.get().strip()
    roll_number = roll_entry.get().strip()
    science_marks = science_entry.get().strip()
    maths_marks = maths_entry.get().strip()
    percentage = percentage_entry.get().strip()

    if not name:
        messagebox.showerror("Error", "Name cannot be blank")
        return

    # Check if the student already exists
    if name in addressbook:
        message = "Updated"
    else:
        message = "Added"

    # Add or update the entry in the dictionary
    addressbook[name] = (
        roll_number,
        science_marks,
        maths_marks,
        percentage
    )

    update_listbox()
    clear_entries()

    messagebox.showinfo(
        "Success",
        f"{message} {name}'s information successfully."
    )


def handle_edit():

    selected = listbox.curselection()

    if selected:

        # Get the selected student's name
        selected_name = listbox.get(selected[0])

        # Get student's details from dictionary
        details = addressbook[selected_name]

        # Put the name into the Entry
        name_entry.delete(0, tk.END)
        name_entry.insert(0, selected_name)

        # Put the roll number into the Entry
        roll_entry.delete(0, tk.END)
        roll_entry.insert(0, details[0])

        # Put science marks into the Entry
        science_entry.delete(0, tk.END)
        science_entry.insert(0, details[1])

        # Put maths marks into the Entry
        maths_entry.delete(0, tk.END)
        maths_entry.insert(0, details[2])

        # Put percentage into the Entry
        percentage_entry.delete(0, tk.END)
        percentage_entry.insert(0, details[3])

    else:
        messagebox.showerror(
            "Error",
            "Please select a student to edit"
        )


def handle_delete():

    selected = listbox.curselection()

    if selected:

        # Get the selected student's name
        selected_name = listbox.get(selected[0])

        # Delete student from dictionary
        del addressbook[selected_name]

        # Update Listbox
        update_listbox()

        # Clear Entry fields
        clear_entries()

        messagebox.showinfo(
            "Success",
            f"Deleted {selected_name}'s information successfully."
        )

    else:
        messagebox.showerror(
            "Error",
            "Please select a student to delete"
        )


def handle_save():

    # Ask user where to save the file
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt")]
    )

    if file_path:

        # Open the file for writing
        with open(file_path, "w") as file:

            # Save the dictionary as text
            print(addressbook, file=file)

        messagebox.showinfo(
            "Success",
            "Student marks saved successfully."
        )


def handle_open():

    global addressbook

    # Ask user which file to open
    file_path = filedialog.askopenfilename(
        filetypes=[("Text files", "*.txt")]
    )

    if file_path:

        try:

            # Open the text file
            with open(file_path, "r") as file:

                # Read the dictionary from the text file
                addressbook = eval(file.read())

            # Update Listbox
            update_listbox()

            messagebox.showinfo(
                "Success",
                "Student marks loaded successfully."
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                f"Failed to load file: {e}"
            )


def update_listbox():

    # Remove existing names
    listbox.delete(0, tk.END)

    # Add all names from dictionary
    for name in addressbook.keys():
        listbox.insert(tk.END, name)


def clear_entries():

    name_entry.delete(0, tk.END)
    roll_entry.delete(0, tk.END)
    science_entry.delete(0, tk.END)
    maths_entry.delete(0, tk.END)
    percentage_entry.delete(0, tk.END)


def create_gui():

    global name_entry
    global roll_entry
    global science_entry
    global maths_entry
    global percentage_entry
    global listbox

    # Create the main window
    root = tk.Tk()

    root.title("STUDENT INFORMATION AND MARKS LOGGER")
    root.geometry("600x450")
    root.resizable(False, False)
    root.configure(bg="lightgreen")


    # ---------------------------------------------------------
    # Title
    # ---------------------------------------------------------

    title_label = tk.Label(
        root,
        text="STUDENT REPORT LOG",
        font=("Arial", 16, "bold"),
        bg="lightgreen"
    )

    title_label.pack(pady=10)


    # ---------------------------------------------------------
    # Form frame
    # ---------------------------------------------------------

    form_frame = tk.Frame(
        root,
        bg="lightgreen"
    )

    form_frame.pack(pady=10)


    # Name
    tk.Label(
        form_frame,
        text="Name:",
        bg="lightgreen",
        font=("Arial", 10)
    ).grid(
        row=0,
        column=0,
        sticky="w",
        padx=10,
        pady=5
    )

    name_entry = tk.Entry(
        form_frame,
        width=20
    )

    name_entry.grid(
        row=0,
        column=1,
        padx=10,
        pady=5
    )


    # Roll Number
    tk.Label(
        form_frame,
        text="RollNumber:",
        bg="lightgreen",
        font=("Arial", 10)
    ).grid(
        row=1,
        column=0,
        sticky="w",
        padx=10,
        pady=5
    )

    roll_entry = tk.Entry(
        form_frame,
        width=20
    )

    roll_entry.grid(
        row=1,
        column=1,
        padx=10,
        pady=5
    )


    # Science Marks
    tk.Label(
        form_frame,
        text="Science_Marks:",
        bg="lightgreen",
        font=("Arial", 10)
    ).grid(
        row=0,
        column=2,
        sticky="w",
        padx=10,
        pady=5
    )

    science_entry = tk.Entry(
        form_frame,
        width=20
    )

    science_entry.grid(
        row=0,
        column=3,
        padx=10,
        pady=5
    )


    # Maths Marks
    tk.Label(
        form_frame,
        text="Maths_Marks:",
        bg="lightgreen",
        font=("Arial", 10)
    ).grid(
        row=1,
        column=2,
        sticky="w",
        padx=10,
        pady=5
    )

    maths_entry = tk.Entry(
        form_frame,
        width=20
    )

    maths_entry.grid(
        row=1,
        column=3,
        padx=10,
        pady=5
    )


    # Percentage
    tk.Label(
        form_frame,
        text="Percentage:",
        bg="lightgreen",
        font=("Arial", 10)
    ).grid(
        row=2,
        column=2,
        sticky="w",
        padx=10,
        pady=5
    )

    percentage_entry = tk.Entry(
        form_frame,
        width=20
    )

    percentage_entry.grid(
        row=2,
        column=3,
        padx=10,
        pady=5
    )


    # ---------------------------------------------------------
    # Listbox
    # ---------------------------------------------------------

    listbox = tk.Listbox(
        root,
        width=50,
        height=8,
        font=("Arial", 10)
    )

    listbox.pack(pady=10)


    # ---------------------------------------------------------
    # Buttons
    # ---------------------------------------------------------

    button_frame = tk.Frame(
        root,
        bg="lightgreen"
    )

    button_frame.pack(pady=10)


    # Edit button
    tk.Button(
        button_frame,
        text="Edit",
        width=10,
        command=handle_edit
    ).grid(
        row=0,
        column=0,
        padx=5
    )


    # Delete button
    tk.Button(
        button_frame,
        text="Delete",
        width=10,
        command=handle_delete
    ).grid(
        row=0,
        column=1,
        padx=5
    )


    # Update/Add button
    tk.Button(
        button_frame,
        text="Update/Add",
        width=10,
        command=handle_add_update
    ).grid(
        row=0,
        column=2,
        padx=5
    )


    # Open button
    tk.Button(
        button_frame,
        text="Open",
        width=10,
        command=handle_open
    ).grid(
        row=0,
        column=3,
        padx=5
    )


    # Save button
    tk.Button(
        button_frame,
        text="Save",
        width=10,
        command=handle_save
    ).grid(
        row=0,
        column=4,
        padx=5
    )


    # Start the Tkinter program
    root.mainloop()


if __name__ == "__main__":
    create_gui()

