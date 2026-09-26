import tkinter as tk
from tkinter import messagebox

# Functionality for the listbox
class ListboxHandler:
    def __init__(self, listbox):
        self.listbox = listbox

    def add_item(self):
        new_item = f"Item {self.listbox.size() + 1}"
        self.listbox.insert(tk.END, new_item)

    def delete_selected(self):
        selected_items = self.listbox.curselection()
        if selected_items:
            for index in reversed(selected_items):
                self.listbox.delete(index)
        else:
            messagebox.showwarning("Delete", "No item selected to delete!")

    def select_item(self):
        selected_items = self.listbox.curselection()
        if selected_items:
            items = [self.listbox.get(i) for i in selected_items]
            messagebox.showinfo("Selected Items", f"You selected: {', '.join(items)}")
        else:
            messagebox.showinfo("Select", "No item selected!")

# Main application window
root = tk.Tk()
root.title("Tkinter Frames Demo")
root.geometry("500x400")

# Frame 1 for Listbox
frame1 = tk.Frame(root, padx=10, pady=10, bg="lightblue")
frame1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

listbox = tk.Listbox(frame1, selectmode=tk.MULTIPLE, height=15, width=25)
listbox.pack(pady=10)

listbox_handler = ListboxHandler(listbox)

add_button = tk.Button(frame1, text="Add Item", command=listbox_handler.add_item)
add_button.pack(pady=5)

delete_button = tk.Button(frame1, text="Delete Selected", command=listbox_handler.delete_selected)
delete_button.pack(pady=5)

select_button = tk.Button(frame1, text="Select Item(s)", command=listbox_handler.select_item)
select_button.pack(pady=5)

# Frame 2 for Spinbox
frame2 = tk.Frame(root, padx=10, pady=10, bg="lightgreen")
frame2.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Spinbox for text data
text_label = tk.Label(frame2, text="Text Spinbox:", bg="lightgreen")
text_label.pack(pady=(20, 5))
text_spinbox = tk.Spinbox(frame2, values=("Option A", "Option B", "Option C", "Option D"), wrap=True)
text_spinbox.pack(pady=5)

# Spinbox for float data
float_label = tk.Label(frame2, text="Float Spinbox:", bg="lightgreen")
float_label.pack(pady=(20, 5))
float_spinbox = tk.Spinbox(frame2, from_=0.0, to=10.0, increment=0.5, format="%0.2f")
float_spinbox.pack(pady=5)

# Spinbox for integer data
int_label = tk.Label(frame2, text="Integer Spinbox:", bg="lightgreen")
int_label.pack(pady=(20, 5))
int_spinbox = tk.Spinbox(frame2, from_=0, to=100, increment=1)
int_spinbox.pack(pady=5)

root.mainloop()
