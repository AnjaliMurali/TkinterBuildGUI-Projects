from tkinter import*
from tkinter import messagebox

root=Tk()
root.geometry("700x700")
root.title("Kitchen Timer")

totals=0

def softboiled():
    global totals
    totals=180
    setpreset()

def medium():
    global totals
    totals=300
    setpreset()

def hardboiled():
    global totals
    totals=600
    setpreset()

def setpreset():
    global totals
    softbutton.config(state=DISABLED)
    medbutton.config(state=DISABLED)
    hardbutton.config(state=DISABLED)
    countdown()

def countdown():
    global totals
    mi,se=divmod(totals,60)
    timelabel.config(text= f"{mi:02d}:{se:02d}" )

    if totals==0:
        messagebox.showinfo("Time's Up","Time's Up" )
        softbutton.config(state=NORMAL)
        medbutton.config(state=NORMAL)
        hardbutton.config(state=NORMAL)
        return

    totals=totals-1
    root.after(1000,countdown)


timelabel=Label(root, text="00:00", font=("times new roman", 60))
timelabel.pack(pady=100)

softbutton=Button(root, text="Soft Boiled (3 min)", font=("times new roman", 20), command=softboiled)
softbutton.pack(pady=10)

medbutton=Button(root, text="Medium (5 min)", font=("times new roman", 20), command=medium)
medbutton.pack(pady=10)

hardbutton=Button(root, text="Hard Boiled (10 min)", font=("times new roman", 20), command=hardboiled)
hardbutton.pack(pady=10)


root.mainloop()