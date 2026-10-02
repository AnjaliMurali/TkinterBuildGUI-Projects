from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.filedialog import *
import ast

root=Tk()
root.title("paint")
oldx=None
oldy=None
widthpen=1
colour="black"
multiplier=1
eraser=False
drawing = []

def draw(event):
    global oldx,oldy,colour,widthpen,multiplier
    if oldx is not None and oldy is not None:
        if eraser:
            canvas1.create_line(oldx,oldy,event.x,event.y,width=widthpen*slider.get(),fill="white",capstyle=ROUND)
        else:
            canvas1.create_line(oldx,oldy,event.x,event.y,width=widthpen*slider.get(),fill=colour,capstyle=ROUND)
        drawing.append([
                    oldx,
                    oldy,
                    event.x,
                    event.y,
                    widthpen*slider.get(),
                    colour,
                    #capstyle=ROUND, #smooth=TRUE, #splinesteps=36
                ])
    oldx,oldy=event.x,event.y

def drawreset(event):
    global oldx,oldy
    oldx=None
    oldy=None

def brush():
    global widthpen,eraser
    widthpen=5
    eraser=False

def pen():
    global widthpen,eraser
    widthpen=3
    eraser=False

def colourfunc():
    global colour
    colour=askcolor(color=colour)[1]

def eraserfunc():
    global eraser
    eraser=True

def clear():
    canvas1.delete("all")
    drawing.clear()

def save():
    file = asksaveasfile(defaultextension=".txt")
    #if file is not None:
    for line in drawing:
        print(line, file=file)

def openfunc():
    file = askopenfile(title='Open File')
    #if file is not None:
    canvas1.delete("all")
    drawing.clear()

    for line in file:
        #line = line.strip()
        # Convert saved text back into a Python list
        data = ast.literal_eval(line)

        x1 = data[0]
        y1 = data[1]
        x2 = data[2]
        y2 = data[3]
        width = data[4]
        colour = data[5]
        
        print(x1,y1,x2,y2,width,colour)

        canvas1.create_line(
            x1, y1, x2, y2,
            width=width,
            fill=colour,
            #capstyle=ROUND,
            #smooth=TRUE,
            #splinesteps=36
        )
        
        #if you open a file and then draw more lines, the loaded lines need to be in drawing so that Save saves both the old loaded drawing and your new lines.
        # This helps synchronisation : Open → modify → Save
        drawing.append(data) 

penbutton=Button(root,text="Pen",width=6,command=pen)
penbutton.grid(row=0,column=0,padx=(2,20),pady=10)
brushbutton=Button(root,text="Brush",width=6,command=brush)
brushbutton.grid(row=0,column=1,pady=10)
eraserbutton=Button(root,text="Eraser",width=6,command=eraserfunc)
eraserbutton.grid(row=0,column=2,padx=20,pady=10)
colourbutton=Button(root,text="Colour",width=6,command=colourfunc)
colourbutton.grid(row=0,column=3,pady=10)
clearbutton=Button(root,text="Clear",width=6,command=clear)
clearbutton.grid(row=0,column=5,pady=10)

slider=Scale(root,from_=1,to_=10,orient=HORIZONTAL)
slider.grid(row=0,column=4,padx=20)

canvas1=Canvas(root,bg="white",width=500,height=500)
canvas1.grid(row=1,column=0,columnspan=6)

canvas1.bind('<B1-Motion>',draw)
canvas1.bind('<ButtonRelease-1>',drawreset)

openbutton=Button(root,text="Open",width=6,command=openfunc)
openbutton.grid(row=2,column=0,pady=10)
savebutton=Button(root,text="Save",width=6,command=save)
savebutton.grid(row=2,column=1,pady=10)

root.mainloop()