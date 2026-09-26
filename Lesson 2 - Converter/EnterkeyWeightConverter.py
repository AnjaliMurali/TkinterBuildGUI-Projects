from tkinter import *

root = Tk()
root.geometry("700x300")

# Conversion functions
def convert(unit):
    try:
        if unit == "kg":
            kg = float(kgentry.get())

        elif unit == "g":
            kg = float(gramentry.get()) / 1000

        elif unit == "lb":
            kg = float(poundentry.get()) / 2.20462

        elif unit == "oz":
            kg = float(ounceentry.get()) / 35.274

        # Update all boxes
        kgentry.delete(0, END)
        kgentry.insert(0, f"{kg:.4f}")

        gramentry.delete(0, END)
        gramentry.insert(0, f"{kg * 1000:.2f}")

        poundentry.delete(0, END)
        poundentry.insert(0, f"{kg * 2.20462:.4f}")

        ounceentry.delete(0, END)
        ounceentry.insert(0, f"{kg * 35.274:.4f}")

    except ValueError:
        pass


Label(root, text="Kilogram").grid(row=0, column=0)
kgentry = Entry(root)
kgentry.grid(row=1, column=0)

Label(root, text="Gram").grid(row=0, column=1)
gramentry = Entry(root)
gramentry.grid(row=1, column=1)

Label(root, text="Pound").grid(row=0, column=2)
poundentry = Entry(root)
poundentry.grid(row=1, column=2)

Label(root, text="Ounce").grid(row=0, column=3)
ounceentry = Entry(root)
ounceentry.grid(row=1, column=3)

# Press Enter in any box to convert
kgentry.bind("<Return>", lambda e: convert("kg"))
gramentry.bind("<Return>", lambda e: convert("g"))
poundentry.bind("<Return>", lambda e: convert("lb"))
ounceentry.bind("<Return>", lambda e: convert("oz"))

root.mainloop()