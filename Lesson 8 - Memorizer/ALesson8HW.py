import tkinter as tk
from tkinter import messagebox, simpledialog

class ColorChangerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Changer")
        self.root.geometry("400x300")
        
        # Initial colors
        self.colors = ["Red", "Green", "Blue", "Yellow", "Cyan", "Magenta", "White", "Black"]
        
        # Listbox
        self.listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=10)
        self.listbox.pack(pady=10, fill=tk.X, padx=20)
        self.populate_listbox()
        
        # Buttons
        self.add_button = tk.Button(root, text="Add Color", command=self.add_color)
        self.add_button.pack(side=tk.LEFT, padx=20)
        
        self.remove_button = tk.Button(root, text="Remove Color", command=self.remove_color)
        self.remove_button.pack(side=tk.LEFT)
        
        self.apply_button = tk.Button(root, text="Apply Color", command=self.apply_color)
        self.apply_button.pack(side=tk.RIGHT, padx=20)
        
    def populate_listbox(self):
        self.listbox.delete(0, tk.END)
        for color in self.colors:
            self.listbox.insert(tk.END, color)
    
    def add_color(self):
        new_color = simpledialog.askstring("Add Color", "Enter the name of the color:")
        if new_color:
            if new_color not in self.colors:
                self.colors.append(new_color)
                self.populate_listbox()
            else:
                messagebox.showerror("Error", "Color already exists in the list.")
    
    def remove_color(self):
        selected = self.listbox.curselection()
        if selected:
            color_to_remove = self.listbox.get(selected[0])
            self.colors.remove(color_to_remove)
            self.populate_listbox()
        else:
            messagebox.showwarning("Warning", "No color selected to remove.")
    
    def apply_color(self):
        selected = self.listbox.curselection()
        if selected:
            color = self.listbox.get(selected[0])
            try:
                self.root.configure(bg=color.lower())
            except tk.TclError:
                messagebox.showerror("Error", f"Invalid color: {color}")
        else:
            messagebox.showwarning("Warning", "No color selected.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ColorChangerApp(root)
    root.mainloop()
