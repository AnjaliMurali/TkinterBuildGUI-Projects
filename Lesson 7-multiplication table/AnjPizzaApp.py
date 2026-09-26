import tkinter as tk
from tkinter import ttk

# Function to display the order
def place_order():
    pizza = pizza_var.get()
    quantity = quantity_var.get()
    size = size_var.get()
    if pizza and quantity and size:
        result_label.config(text=f"You ordered {quantity} {pizza} {size} Size Pizza(s)")
    else:
        result_label.config(text="Please complete all fields.")

# Main application window
root = tk.Tk()
root.title("Pizza App")

# App title label
title_label = tk.Label(root, text="Welcome to Pizza Hut", font=("Arial", 14))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Pizza selection label and dropdown
pizza_label = tk.Label(root, text="Select Your Fav Pizza:")
pizza_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

pizza_var = tk.StringVar()
pizza_dropdown = ttk.Combobox(root, textvariable=pizza_var, state="readonly") #3 different states - normal,readonly and disabled. 
#Normal is default. Normal allows the user to either select from dropdown or also type. 
pizza_dropdown["values"] = ["Veg Extravaganza", "Margherita", "Pepperoni", "Farmhouse"]
pizza_dropdown.grid(row=1, column=1, padx=10, pady=5)

# Quantity label and dropdown
quantity_label = tk.Label(root, text="Enter Quantity:")
quantity_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")

#quantity_var = tk.StringVar()
quantity_var = tk.IntVar()
quantity_dropdown = ttk.Combobox(root, textvariable=quantity_var, state="readonly")
quantity_dropdown["values"] = [str(i) for i in range(1, 11)]
#quantity_dropdown["values"] = [i for i in range(1, 11)]
#quantity_dropdown["values"] = list(range(1, 11))
quantity_dropdown.grid(row=2, column=1, padx=10, pady=5)

# Pizza size label and radio buttons
size_label = tk.Label(root, text="Select Size:")
size_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")

size_var = tk.StringVar()
small_radio = tk.Radiobutton(root, text="S", variable=size_var, value="Small")
small_radio.grid(row=3, column=1, sticky="w")

medium_radio = tk.Radiobutton(root, text="M", variable=size_var, value="Medium")
medium_radio.grid(row=3, column=1)

large_radio = tk.Radiobutton(root, text="L", variable=size_var, value="Large")
large_radio.grid(row=3, column=1, sticky="e")

size_var.set("Small")

# Order button
order_button = tk.Button(root, text="Order", command=place_order)
order_button.grid(row=4, column=0, columnspan=2, pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12), fg="red")
result_label.grid(row=5, column=0, columnspan=2, pady=5)

# Start the application
root.mainloop()