
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile, askopenfile

# Dictionary to store library information
# Key = ISBN
# Value = [Title, Author, Status]
library = {}


# ---------------------------------------------------------
# Add a new book
# ---------------------------------------------------------
def add_book():
    title = title_entry.get().strip()
    author = author_entry.get().strip()
    isbn = isbn_entry.get().strip()
    shelf = shelf_entry.get().strip()

    if not title or not author or not isbn or not shelf:
        messagebox.showerror("Error", "Please fill in all fields")
        return

    if isbn in library:
        messagebox.showerror("Error", "Book with this ISBN already exists")
        return

    # Store book in dictionary
    library[isbn] = [title, author, "Available"]

    # Update Listbox
    update_listbox()

    # Clear Entry boxes
    clear_entries()

    messagebox.showinfo("Success", "Book added successfully.")


# ---------------------------------------------------------
# Issue a book
# ---------------------------------------------------------
def issue_book():
    selected = listbox.curselection()

    if selected:
        # Get selected line from Listbox
        book = listbox.get(selected[0])

        # Get ISBN from the selected line
        isbn = book.split(" | ")[0]

        # Get book details from dictionary
        details = library[isbn]

        if details[2] == "Available":
            # Change status
            details[2] = "Issued"

            # Update Listbox
            update_listbox()

            messagebox.showinfo("Success", "Book issued successfully.")

        else:
            messagebox.showerror("Error", "Book already out!")

    else:
        messagebox.showerror("Error", "Please select a book.")


# ---------------------------------------------------------
# Return a book
# ---------------------------------------------------------
def return_book():
    selected = listbox.curselection()

    if selected:
        # Get selected line from Listbox
        book = listbox.get(selected[0])

        # Get ISBN from the selected line
        isbn = book.split(" | ")[0]

        # Get book details
        details = library[isbn]

        # Change status back to Available
        details[2] = "Available"

        # Update Listbox
        update_listbox()

        messagebox.showinfo("Success", "Book returned successfully.")

    else:
        messagebox.showerror("Error", "Please select a book.")


# ---------------------------------------------------------
# Update the Listbox
# ---------------------------------------------------------
def update_listbox():
    # Delete old contents
    listbox.delete(0, tk.END)

    # Get search text
    search_author = search_entry.get().strip().lower()

    # Add books to Listbox
    for isbn in library:
        details = library[isbn]

        title = details[0]
        author = details[1]
        status = details[2]

        # Show only matching author
        if search_author == "" or search_author in author.lower():
            book_text = isbn + " | " + title + " | " + author + " | " + status
            listbox.insert(tk.END, book_text)


# ---------------------------------------------------------
# Search books by author
# ---------------------------------------------------------
def search_book():
    update_listbox()


# ---------------------------------------------------------
# Clear Entry boxes
# ---------------------------------------------------------
def clear_entries():
    title_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)
    isbn_entry.delete(0, tk.END)
    shelf_entry.delete(0, tk.END)


# ---------------------------------------------------------
# Save dictionary to a text file
# ---------------------------------------------------------
def save_catalog():
    # Ask user where to save the file
    fout = asksaveasfile(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt")]
    )

    if fout:
        # Save dictionary as text
        print(library, file=fout)

        # Close the file
        fout.close()

        messagebox.showinfo(
            "Success",
            "Library catalog saved successfully."
        )
    else:
        messagebox.showinfo(
            "Warning",
            "Library catalog not saved."
        )


# ---------------------------------------------------------
# Open dictionary from a text file
# ---------------------------------------------------------
def load_catalog():
    global library

    # Ask user which file to open
    fin = askopenfile(
        title="Open Library Catalog",
        filetypes=[("Text files", "*.txt")]
    )

    if fin:
        try:
            # Read the dictionary from the file
            library = eval(fin.read())

            # Update Listbox
            update_listbox()

            # Close file
            fin.close()

            messagebox.showinfo(
                "Success",
                "Library catalog loaded successfully."
            )

        except Exception as e:
            messagebox.showerror(
                "Error",
                f"Failed to load file: {e}"
            )
    else:
        messagebox.showinfo(
            "Warning",
            "No catalog opened."
        )


# ---------------------------------------------------------
# Create main GUI
# ---------------------------------------------------------
def create_gui():
    global title_entry
    global author_entry
    global isbn_entry
    global shelf_entry
    global search_entry
    global listbox

    # Main window
    root = tk.Tk()
    root.title("City Library System")
    root.geometry("750x450")
    root.resizable(False, False)
    root.configure(bg="lightgreen")

    # -----------------------------------------------------
    # Menu Bar
    # -----------------------------------------------------
    menu_bar = tk.Menu(root)

    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(
        label="Save Catalog",
        command=save_catalog
    )
    file_menu.add_command(
        label="Load Catalog",
        command=load_catalog
    )

    menu_bar.add_cascade(
        label="File",
        menu=file_menu
    )

    root.config(menu=menu_bar)

    # -----------------------------------------------------
    # Title
    # -----------------------------------------------------
    title_label = tk.Label(
        root,
        text="CITY LIBRARY SYSTEM",
        font=("Arial", 16, "bold"),
        bg="lightgreen"
    )
    title_label.pack(pady=10)

    # -----------------------------------------------------
    # Main frame
    # -----------------------------------------------------
    main_frame = tk.Frame(
        root,
        bg="lightgreen"
    )
    main_frame.pack(pady=10)

    # -----------------------------------------------------
    # Left side - Book information
    # -----------------------------------------------------
    input_frame = tk.Frame(
        main_frame,
        bg="lightgreen"
    )
    input_frame.grid(row=0, column=0, padx=20)

    tk.Label(
        input_frame,
        text="Book Title:",
        bg="lightgreen",
        font=("Arial", 10)
    ).grid(row=0, column=0, sticky="w", pady=5)

    title_entry = tk.Entry(
        input_frame,
        width=25
    )
    title_entry.grid(row=0, column=1, pady=5)

    tk.Label(
        input_frame,
        text="Author:",
        bg="lightgreen",
        font=("Arial", 10)
    ).grid(row=1, column=0, sticky="w", pady=5)

    author_entry = tk.Entry(
        input_frame,
        width=25
    )
    author_entry.grid(row=1, column=1, pady=5)

    tk.Label(
        input_frame,
        text="ISBN Code:",
        bg="lightgreen",
        font=("Arial", 10)
    ).grid(row=2, column=0, sticky="w", pady=5)

    isbn_entry = tk.Entry(
        input_frame,
        width=25
    )
    isbn_entry.grid(row=2, column=1, pady=5)

    tk.Label(
        input_frame,
        text="Shelf Number:",
        bg="lightgreen",
        font=("Arial", 10)
    ).grid(row=3, column=0, sticky="w", pady=5)

    shelf_entry = tk.Entry(
        input_frame,
        width=25
    )
    shelf_entry.grid(row=3, column=1, pady=5)

    # -----------------------------------------------------
    # Right side - Search and Listbox
    # -----------------------------------------------------
    display_frame = tk.Frame(
        main_frame,
        bg="lightgreen"
    )
    display_frame.grid(row=0, column=1, padx=20)

    tk.Label(
        display_frame,
        text="Search by Author:",
        bg="lightgreen",
        font=("Arial", 10)
    ).pack()

    search_entry = tk.Entry(
        display_frame,
        width=35
    )
    search_entry.pack(pady=5)

    tk.Button(
        display_frame,
        text="Search",
        width=10,
        command=search_book
    ).pack(pady=5)

    listbox = tk.Listbox(
        display_frame,
        width=50,
        height=10,
        font=("Arial", 10)
    )
    listbox.pack(pady=5)

    # -----------------------------------------------------
    # Bottom buttons
    # -----------------------------------------------------
    button_frame = tk.Frame(
        root,
        bg="lightgreen"
    )
    button_frame.pack(pady=15)

    tk.Button(
        button_frame,
        text="Add New Book",
        width=15,
        command=add_book
    ).grid(row=0, column=0, padx=5)

    tk.Button(
        button_frame,
        text="Issue Book",
        width=15,
        command=issue_book
    ).grid(row=0, column=1, padx=5)

    tk.Button(
        button_frame,
        text="Return Book",
        width=15,
        command=return_book
    ).grid(row=0, column=2, padx=5)

    # Start the program
    root.mainloop()


# ---------------------------------------------------------
# Start program
# ---------------------------------------------------------
if __name__ == "__main__":
    create_gui()
