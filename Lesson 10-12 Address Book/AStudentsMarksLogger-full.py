import tkinter as tk
from tkinter import messagebox, filedialog
import json

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

    # Add or update the entry in the dictionary
    addressbook[name] = (roll_number, science_marks, maths_marks, percentage)
    #print(addressbook[name])
    update_listbox()
    clear_entries()
    messagebox.showinfo("Success", f"{'Updated' if name in addressbook else 'Added'} {name}'s information successfully.")

def handle_edit():
    selected_name = listbox.get(tk.ACTIVE) #directly gets the active item's text

    #selected_name = listbox.curselection() cannot be used directly as it returns a tuple 
    # why tuple like(0,) Because curselection() is designed to support multiple selections.
    # If indexes 0,2,3 are selected, curselection returns(0,2,3) 
    # If you want to use this only, # then write like this: 
    """
    selected = listbox.curselection()

    if selected:
        selected_name = listbox.get(selected[0])
        if not selected_name:
            messagebox.showerror("Error", "Please select a name to edit")
            return
    """

    # Populate the entry fields with the selected name's details
    details = addressbook[selected_name]
    name_entry.delete(0, tk.END)
    name_entry.insert(0, selected_name)
    roll_entry.delete(0, tk.END)
    roll_entry.insert(0, details[0])
    #roll_entry.insert(0, addressbook[selected_name][0])
    science_entry.delete(0, tk.END)
    science_entry.insert(0, details[1])
    maths_entry.delete(0, tk.END)
    maths_entry.insert(0, details[2])
    percentage_entry.delete(0, tk.END)
    percentage_entry.insert(0, details[3])

def handle_delete():
    selected_name = listbox.get(tk.ACTIVE)
    if not selected_name:
        messagebox.showerror("Error", "Please select a name to delete")
        return

    # Remove the selected name from the dictionary and update the listbox
    del addressbook[selected_name]
    update_listbox()
    clear_entries()
    messagebox.showinfo("Success", f"Deleted {selected_name}'s information successfully.")

def handle_save():
    #JSON is designed to store structured data like dictionaries. 
    #If txt is used, then when loading it, you'd have to convert that text back into a dictionary yourself.
    file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if file_path:
        with open(file_path, "w") as file:
            json.dump(addressbook, file)
        messagebox.showinfo("Success", "Address book saved successfully.")

def handle_open():
    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if file_path:
        try:
            with open(file_path, "r") as file:
                global addressbook
                addressbook = json.load(file)
            update_listbox()
            messagebox.showinfo("Success", "Address book loaded successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file: {e}")

def update_listbox():
    listbox.delete(0, tk.END)
    for name in addressbook.keys():
        listbox.insert(tk.END, name)

def clear_entries():
    name_entry.delete(0, tk.END)
    roll_entry.delete(0, tk.END)
    science_entry.delete(0, tk.END)
    maths_entry.delete(0, tk.END)
    percentage_entry.delete(0, tk.END)

def create_gui():
    global name_entry, roll_entry, science_entry, maths_entry, percentage_entry, listbox

    # Create the main window
    root = tk.Tk()
    root.title("STUDENT INFORMATION AND MARKS LOGGER")
    root.geometry("600x450")
    root.resizable(False, False)
    root.configure(bg="lightgreen")

    # Add the title label
    title_label = tk.Label(root, text="STUDENT REPORT LOG", font=("Arial", 16, "bold"), bg="lightgreen")
    title_label.pack(pady=10)

    # Create a frame for the form fields
    form_frame = tk.Frame(root, bg="lightgreen")
    form_frame.pack(pady=10)

    # Add form fields
    tk.Label(form_frame, text="Name:", bg="lightgreen", font=("Arial", 10)).grid(row=0, column=0, sticky="w", padx=10, pady=5)
    name_entry = tk.Entry(form_frame, width=20)
    name_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(form_frame, text="RollNumber:", bg="lightgreen", font=("Arial", 10)).grid(row=1, column=0, sticky="w", padx=10, pady=5)
    roll_entry = tk.Entry(form_frame, width=20)
    roll_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(form_frame, text="Science_Marks:", bg="lightgreen", font=("Arial", 10)).grid(row=0, column=2, sticky="w", padx=10, pady=5)
    science_entry = tk.Entry(form_frame, width=20)
    science_entry.grid(row=0, column=3, padx=10, pady=5)

    tk.Label(form_frame, text="Maths_Marks:", bg="lightgreen", font=("Arial", 10)).grid(row=1, column=2, sticky="w", padx=10, pady=5)
    maths_entry = tk.Entry(form_frame, width=20)
    maths_entry.grid(row=1, column=3, padx=10, pady=5)

    tk.Label(form_frame, text="Percentage:", bg="lightgreen", font=("Arial", 10)).grid(row=2, column=2, sticky="w", padx=10, pady=5)
    percentage_entry = tk.Entry(form_frame, width=20)
    percentage_entry.grid(row=2, column=3, padx=10, pady=5)

    # Add a Listbox
    listbox = tk.Listbox(root, width=50, height=8, font=("Arial", 10))
    listbox.pack(pady=10)

    # Add buttons
    button_frame = tk.Frame(root, bg="lightgreen")
    button_frame.pack(pady=10)

    tk.Button(button_frame, text="Edit", width=10, command=handle_edit).grid(row=0, column=0, padx=5)
    tk.Button(button_frame, text="Delete", width=10, command=handle_delete).grid(row=0, column=1, padx=5)
    tk.Button(button_frame, text="Update/Add", width=10, command=handle_add_update).grid(row=0, column=2, padx=5)
    tk.Button(button_frame, text="Open", width=10, command=handle_open).grid(row=0, column=3, padx=5)
    tk.Button(button_frame, text="Save", width=10, command=handle_save).grid(row=0, column=4, padx=5)

    # Start the Tkinter main loop
    root.mainloop()

if __name__ == "__main__":
    create_gui()
