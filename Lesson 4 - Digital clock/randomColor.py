from tkinter import *
import random


def changecolour():
    colorList = ["red","green","yellow","blue","brown"]
    randomcolour=random.choice(colorList)
    root.config(bg=randomcolour)
    """
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)

    randomcolour=f'#{r:02x}{g:02x}{b:02x}'
    root.config(bg=randomcolour)
    """

    #To dorectly pick from hex code. 
    """
    hex_code = f"#{random.randint(0, 0xFFFFFF):06X}"
    print(hex_code)
    """


root = Tk()
root.config(background="#a5f5b2")
root.title("Colour changer bg")
root.geometry("800x800")

changecolour=Button(root,text="Click to change colour",font=("Arial",40),bg="#ffffff",fg="black",command=changecolour)
changecolour.grid(column=0,row=0,padx=125,pady=325)

mainloop()