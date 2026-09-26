from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.filedialog import *
import ast

def use_pen():
    global eraser_on, brush_on
    eraser_on = False
    brush_on = False

def use_brush():
    global eraser_on, brush_on
    eraser_on = False
    brush_on = True

def choose_color():
    global color, eraser_on
    eraser_on = False
    chosen_color = askcolor(color=color)[1] #askcolor returns 2 values - 1.RGB and 2.Hex code for the chosen color. We need hex and so we put index 1. 
    if chosen_color: # Avoid setting color to None if user cancels
        color = chosen_color

def use_eraser():
    global eraser_on, brush_on
    eraser_on = True
    brush_on = False

def paint(event):
    global old_x, old_y, line_width
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
            #capstyle=ROUND,
            #smooth=TRUE,
            #splinesteps=36
        )
        # IMPORTANT:
        # Store the line so that we can save it later
        drawing.append([
            old_x,
            old_y,
            event.x,
            event.y,
            line_width,
            pen_color,
             #capstyle=ROUND, #smooth=TRUE, #splinesteps=36
        ])

    old_x = event.x
    old_y = event.y
    #other capstyle values are BUTT, PROJECTING
            #give capstyle as Hw
    """
    These 3 are optional
    capstyle     → What do the ends look like?
    smooth       → Should the stroke be curved/smoothed?
    splinesteps → How finely should that curve be approximated? (bigger the splinesteps, more natural the strokes are.)     
    """

# Mouse button released
def reset(event):
    global old_x, old_y
    old_x = None
    old_y = None

def clear_canvas():
    c.delete("all")
    # Remove saved drawing information
    drawing.clear()
"""
def save_drawing():
   # Ask where to save the file
    #file = asksaveasfilename(
     #   defaultextension=".txt",filetypes=[("Text files", "*.txt")])
    file=asksaveasfile(defaultextension=".txt")
    if file:
        # Open the file
        saved_file = open(file, "w")
        # Save every line
        for line in drawing:
            # Convert the line into text
            saved_file.write(",".join(map(str, line)) + "\n")
        # Close the file
        saved_file.close()

def open_drawing():
    # Ask the user to choose a file
    file = askopenfilename(filetypes=[("Text files", "*.txt")])
    if file:
        # Clear the canvas
        c.delete("all")
        # Clear the old drawing
        drawing.clear()
        # Open the file
        saved_file = open(file, "r")
        # Read every line
        for line in saved_file:
            # Remove the newline
            line = line.strip()
            # Split the information
            parts = line.split(",")
            # Get the information
            x1 = float(parts[0])
            y1 = float(parts[1])
            x2 = float(parts[2])
            y2 = float(parts[3])
            width = float(parts[4])
            colour = parts[5]
            # Draw the line again
            c.create_line(
                x1,
                y1,
                x2,
                y2,
                width=width,
                fill=colour,
                capstyle=ROUND,
                smooth=TRUE,
                splinesteps=36
            )
            # Store the line again
            drawing.append([
                x1,
                y1,
                x2,
                y2,
                width,
                colour
            ])
        # Close the file
        saved_file.close()
"""
def save_drawing():
    file = asksaveasfile(defaultextension=".txt")
    if file is not None:
        for line in drawing:
            print(line, file=file)
        #file.close()


def open_drawing():
    file = askopenfile(title='Open File')
    if file is not None:
        c.delete("all")
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

            c.create_line(
                x1, y1, x2, y2,
                width=width,
                fill=colour,
                #capstyle=ROUND,
                #smooth=TRUE,
                #splinesteps=36
            )

            drawing.append(data)

        #file.close()

root = Tk()
color = "black"
#line_width = 5
eraser_on = False
brush_on = False
old_x = None
old_y = None
# This list stores the drawing
drawing = []

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

save_button = Button( root, text="Save", command=save_drawing ) 
save_button.grid(row=0, column=6) 

open_button = Button( root, text="Open", command=open_drawing ) 
open_button.grid(row=0, column=7)

root.mainloop()