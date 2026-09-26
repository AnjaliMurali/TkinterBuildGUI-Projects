from tkinter import *
from tkinter.colorchooser import askcolor
def use_pen():
    global eraser_on
    eraser_on = False

def use_brush():
    global eraser_on
    eraser_on = False  # In this implementation, pen and brush are equivalent

def choose_color():
    global color, eraser_on
    eraser_on = False
    chosen_color = askcolor(color=color)[1]
    if chosen_color:  # Avoid setting color to None if user cancels
        color = chosen_color

def use_eraser():
    global eraser_on
    eraser_on = True

def paint(event):
    global old_x, old_y, line_width
    line_width = size_scale.get()
    paint_color = 'white' if eraser_on else color
    if old_x and old_y:
        c.create_line(old_x, old_y, event.x, event.y, width=line_width, fill=paint_color, capstyle=ROUND, smooth=TRUE, splinesteps=36)
    old_x, old_y = event.x, event.y

def reset(event):
    global old_x, old_y
    old_x, old_y = None, None
root = Tk()
color = "black"
line_width = 5.0
eraser_on = False
old_x, old_y = None, None

c = Canvas(root, bg='white', width=600, height=600)
c.grid(row=1, columnspan=5)

size_scale = Scale(root, from_=1, to=10, orient=HORIZONTAL)
size_scale.grid(row=0, column=4)

pen_button = Button(root, text='pen', command=use_pen)
pen_button.grid(row=0, column=0)

brush_button = Button(root, text='brush', command=use_brush)
brush_button.grid(row=0, column=1)

color_button = Button(root, text='color', command=choose_color)
color_button.grid(row=0, column=2)

eraser_button = Button(root, text='eraser', command=use_eraser)
eraser_button.grid(row=0, column=3)

c.bind('<B1-Motion>', paint)
c.bind('<ButtonRelease-1>', reset)
root.mainloop()
