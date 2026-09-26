from tkinter import *
from tkinter.colorchooser import askcolor
# Functions
def use_pen():
    global eraser_on,brush_on
    eraser_on = False
    brush_on = False
    #pen_button.config(bg="gray")

def use_brush():
    global eraser_on,brush_on
    eraser_on = False  
    brush_on = True

def choose_color():
    global color, eraser_on
    eraser_on = False
    chosen_color = askcolor(color=color)[1] #askcolor returns 2 values - 1.RGB and 2.Hex code for the chosen color. We need hex and so we put index 1. 
    if chosen_color:  # Avoid setting color to None if user cancels
        color = chosen_color

def use_eraser():
    global eraser_on,brush_on
    eraser_on = True
    brush_on = False

def paint(event):
    global old_x, old_y, line_width,color
    if brush_on:
        line_width = size_scale.get()+5
    else: 
        line_width = size_scale.get()
    pen_color = 'white' if eraser_on else color

    if old_x and old_y:
        c.create_line(old_x, old_y, event.x, event.y,
                      width=line_width, fill=pen_color,
                      capstyle=ROUND #smooth=TRUE, #splinesteps=36)
        )
        #other capstyle values are BUTT, PROJECTING
        #give capstyle as Hw
        """
        These 3 are optional
        capstyle     → What do the ends look like?
        smooth       → Should the stroke be curved/smoothed?
        splinesteps → How finely should that curve be approximated? (bigger the splinesteps, more natural the strokes are.)     
        """

    old_x, old_y = event.x, event.y

def reset(event):
    global old_x, old_y
    old_x, old_y = None, None

def clear_canvas():
    c.delete("all")

# Global variables to manage state
#DEFAULT_PEN_SIZE = 5.0
#DEFAULT_COLOR = 'black'

root = Tk()
color = "black"
#line_width = 5.0
eraser_on = False
brush_on = False
old_x, old_y = None, None
#root.config(background="black")
#root.geometry("1000x1000")

# Create the canvas and size scale as global variables
c = Canvas(root, bg='white', width=600, height=600)
c.grid(row=1, columnspan=6)
c.bind('<B1-Motion>', paint)
c.bind('<ButtonRelease-1>', reset)

size_scale = Scale(root, from_=1, to_=10, orient=HORIZONTAL)
size_scale.grid(row=0, column=4)

pen_button = Button(root, text='pen', command=use_pen)
pen_button.grid(row=0, column=0)

brush_button = Button(root, text='brush', command=use_brush)
brush_button.grid(row=0, column=1)

color_button = Button(root, text='color', command=choose_color)
color_button.grid(row=0, column=2)

eraser_button = Button(root, text='eraser', command=use_eraser)
eraser_button.grid(row=0, column=3)

clear_button = Button(root,text="Clear Canvas",command=clear_canvas)
clear_button.grid(row=0, column=5)


root.mainloop()

