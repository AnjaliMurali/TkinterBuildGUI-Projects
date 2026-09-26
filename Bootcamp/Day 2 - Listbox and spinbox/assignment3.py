import tkinter as tk

root = tk.Tk()
root.title("Tkinter Frames Demo")
root.geometry("500x400")

frame1 = tk.Frame(root, padx=10, pady=10, bg="lightblue")
frame1.pack(side=tk.LEFT, expand=True)

frame2 = tk.Frame(root, padx=10, pady=10, bg="lightgreen")
frame2.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

listbox = tk.Listbox(frame1, selectmode=tk.MULTIPLE, height=15, width=25)
listbox.pack(pady=10)

root.mainloop()