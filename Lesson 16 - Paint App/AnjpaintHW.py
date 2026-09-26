from tkinter import *
from tkinter import ttk
from tkinter.colorchooser import askcolor


# Functions

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

    chosen_color = askcolor(color=color)[1]

    if chosen_color:
        color = chosen_color


def choose_background():
    global background_color

    chosen_color = askcolor(color=background_color)[1]

    if chosen_color:
        background_color = chosen_color
        c.config(bg=background_color)


def choose_stroke(event):
    global stroke_style

    selected_stroke = stroke_combo.get()

    if selected_stroke == "Round":
        stroke_style = ROUND

    elif selected_stroke == "Butt":
        stroke_style = BUTT

    elif selected_stroke == "Projecting":
        stroke_style = PROJECTING


def use_eraser():
    global eraser_on, brush_on

    eraser_on = True
    brush_on = False


def paint(event):
    global old_x, old_y, line_width

    if brush_on:
        line_width = size_scale.get() + 5
    else:
        line_width = size_scale.get()

    paint_color = 'white' if eraser_on else color

    if old_x is not None and old_y is not None:

        c.create_line(
            old_x,
            old_y,
            event.x,
            event.y,
            width=line_width,
            fill=paint_color,
            capstyle=stroke_style,
            smooth=TRUE,
            splinesteps=36
        )

    old_x, old_y = event.x, event.y


def reset(event):
    global old_x, old_y

    old_x, old_y = None, None


def clear_canvas():
    c.delete("all")


# -----------------------------------
# Global variables
# -----------------------------------

root = Tk()

color = "black"
background_color = "white"

line_width = 5.0

eraser_on = False
brush_on = False

old_x, old_y = None, None

# Default stroke style
stroke_style = ROUND


# -----------------------------------
# Canvas
# -----------------------------------

c = Canvas(
    root,
    bg=background_color,
    width=600,
    height=600
)

c.grid(row=1, columnspan=8)

c.bind('<B1-Motion>', paint)
c.bind('<ButtonRelease-1>', reset)


# -----------------------------------
# Size Scale
# -----------------------------------

size_scale = Scale(
    root,
    from_=1,
    to_=10,
    orient=HORIZONTAL
)

size_scale.grid(row=0, column=4)


# -----------------------------------
# Buttons
# -----------------------------------

pen_button = Button(
    root,
    text='Pen',
    command=use_pen
)

pen_button.grid(row=0, column=0)


brush_button = Button(
    root,
    text='Brush',
    command=use_brush
)

brush_button.grid(row=0, column=1)


color_button = Button(
    root,
    text='Color',
    command=choose_color
)

color_button.grid(row=0, column=2)


eraser_button = Button(
    root,
    text='Eraser',
    command=use_eraser
)

eraser_button.grid(row=0, column=3)


background_button = Button(
    root,
    text='Background Color',
    command=choose_background
)

background_button.grid(row=0, column=5)


# -----------------------------------
# Stroke Style Combobox
# -----------------------------------

stroke_combo = ttk.Combobox(
    root,
    values=["Round", "Butt", "Projecting"],
    state="readonly",
    width=12
)

stroke_combo.set("Round")

stroke_combo.grid(row=0, column=6)

stroke_combo.bind("<<ComboboxSelected>>", choose_stroke)


# -----------------------------------
# Clear Button
# -----------------------------------

clear_button = Button(
    root,
    text="Clear Canvas",
    command=clear_canvas
)

clear_button.grid(row=0, column=7)


root.mainloop()

