from tkinter import *

def use_brush():
    global eraser_on,brush_on
    eraser_on = False 
    brush_on = True

def use_pen():
    global eraser_on, brush_on
    eraser_on = False
    brush_on = False

def use_eraser():
    global eraser_on, brush_on
    eraser_on = True
    brush_on = False

root = Tk()
color = "black"
#line_width = 5
eraser_on = False
brush_on = False
old_x = None
old_y = None
# This list stores the drawing
drawing = []

def paint(event):
    global old_x, old_y
    # Choose the line width
    if brush_on:
        line_width = size_scale.get() + 5
    else:
        line_width = size_scale.get()
    # Choose the colour
    if eraser_on:
        pen_color = "white"
    else:
        pen_color = color
    # Draw the line
    if old_x is not None and old_y is not None:
        c.create_line(
            old_x,
            old_y,
            event.x,
            event.y,
            width=line_width,
            fill=pen_color,
            capstyle=ROUND #(capstyle → What do the ends look like? give as HW - #other capstyle values are BUTT, PROJECTING)
        )
        
        # IMPORTANT:
        # Store the line so that we can save it later
        drawing.append([
            old_x,
            old_y,
            event.x,
            event.y,
            line_width,
            pen_color
        ])
    old_x = event.x
    old_y = event.y

def reset(event):
    global old_x, old_y
    old_x = None
    old_y = None

c = Canvas(root, bg='white', width=600, height=600)
c.grid(row=1, columnspan=6)
c.bind('<B1-Motion>', paint)
c.bind('<ButtonRelease-1>', reset)

size_scale = Scale(root, from_=1, to_=10, orient=HORIZONTAL)
size_scale.grid(row=0, column=4)

pen_button = Button(root, text='pen')
pen_button.grid(row=0, column=0)

brush_button = Button(root, text='brush',command=use_brush)
brush_button.grid(row=0, column=1)

color_button = Button(root, text='color')
color_button.grid(row=0, column=2)

eraser_button = Button(root, text='eraser')
eraser_button.grid(row=0, column=3)

clear_button = Button(root,text="Clear Canvas")
clear_button.grid(row=0, column=5)

save_button = Button( root, text="Save") 
save_button.grid(row=0, column=6) 

open_button = Button( root, text="Open") 
open_button.grid(row=0, column=7)

root.mainloop()