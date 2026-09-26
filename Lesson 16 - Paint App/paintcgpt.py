from tkinter import *
from tkinter import filedialog
from tkinter.colorchooser import askcolor
from PIL import Image, ImageDraw
import random

# Functions
def use_pen():
    global eraser_on, spray_mode
    eraser_on = False
    spray_mode = False

def use_brush():
    global eraser_on, spray_mode
    eraser_on = False
    spray_mode = False

def choose_color():
    global color, eraser_on, spray_mode

    eraser_on = False
    spray_mode = False

    chosen_color = askcolor(color=color)[1]

    if chosen_color:
        color = chosen_color

def use_eraser():
    global eraser_on, spray_mode
    eraser_on = True
    spray_mode = False

def use_spray():
    global eraser_on, spray_mode
    eraser_on = False
    spray_mode = not spray_mode

def save_drawing():
    # Save the canvas as an EPS file
    c.postscript(file="my_art.eps")
    print("Drawing saved as my_art.eps")

def open_image():
    global opened_image, image_on_canvas

    # Ask the user to choose an image
    filename = filedialog.askopenfilename(
        title="Open Image",
        filetypes=[
            ("Image files", "*.png *.jpg *.jpeg *.eps"),
            ("PNG files", "*.png"),
            ("JPEG files", "*.jpg *.jpeg"),
            ("EPS files", "*.eps"),
            ("All files", "*.*")
        ]
    )

    if not filename:
        return

    try:
        # Open the image using Pillow
        opened_image = Image.open(filename)

        # Convert image to RGB so all image types work
        if opened_image.mode != "RGB":
            opened_image = opened_image.convert("RGB")

        # Resize image to fit the canvas
        max_width = 600
        max_height = 600

        opened_image.thumbnail((max_width, max_height))

        # Convert Pillow image into a Tkinter image
        image_on_canvas = ImageTk.PhotoImage(opened_image)

        # Clear the canvas
        c.delete("all")

        # Put the image in the center of the canvas
        c.create_image(
            300,
            300,
            image=image_on_canvas,
            anchor=CENTER
        )

        print("Image opened successfully.")

    except Exception as e:
        print("Could not open image:", e)


def paint(event):
    global old_x, old_y, line_width

    line_width = size_scale.get()
    paint_color = 'white' if eraser_on else color

    # Spray Can mode
    if spray_mode:

        # Create 5-10 random dots
        for _ in range(random.randint(5, 10)):

            offset_x = random.randint(-10, 10)
            offset_y = random.randint(-10, 10)

            x = event.x + offset_x
            y = event.y + offset_y

            c.create_oval(
                x,
                y,
                x + 2,
                y + 2,
                fill=paint_color,
                outline=paint_color
            )

        old_x, old_y = event.x, event.y
        return

    # Normal drawing
    if old_x is not None and old_y is not None:
        c.create_line(
            old_x,
            old_y,
            event.x,
            event.y,
            width=line_width,
            fill=paint_color,
            capstyle=ROUND,
            smooth=TRUE,
            splinesteps=36
        )

    old_x, old_y = event.x, event.y


def reset(event):
    global old_x, old_y
    old_x, old_y = None, None


# -----------------------------
# Main window
# -----------------------------

root = Tk()
root.title("My Paint App")

# Global variables
color = "black"
line_width = 5.0
eraser_on = False
spray_mode = False

old_x = None
old_y = None

# Keep references to opened images
opened_image = None
image_on_canvas = None


# -----------------------------
# Canvas
# -----------------------------

c = Canvas(
    root,
    bg="white",
    width=600,
    height=600
)


# -----------------------------
# Size scale
# -----------------------------

size_scale = Scale(
    root,
    from_=1,
    to=10,
    orient=HORIZONTAL
)

size_scale.set(5)


# -----------------------------
# Buttons
# -----------------------------

pen_button = Button(
    root,
    text="Pen",
    command=use_pen
)
pen_button.grid(row=0, column=0)

brush_button = Button(
    root,
    text="Brush",
    command=use_brush
)
brush_button.grid(row=0, column=1)

color_button = Button(
    root,
    text="Color",
    command=choose_color
)
color_button.grid(row=0, column=2)

eraser_button = Button(
    root,
    text="Eraser",
    command=use_eraser
)
eraser_button.grid(row=0, column=3)

spray_button = Button(
    root,
    text="Spray Can",
    command=use_spray
)
spray_button.grid(row=0, column=4)

save_button = Button(
    root,
    text="Save Image",
    command=save_drawing
)
save_button.grid(row=0, column=5)

open_button = Button(
    root,
    text="Open Image",
    command=open_image
)
open_button.grid(row=0, column=6)

size_scale.grid(row=0, column=7)


# -----------------------------
# Canvas placement
# -----------------------------

c.grid(row=1, columnspan=8)


# -----------------------------
# Mouse events
# -----------------------------

c.bind("<B1-Motion>", paint)
c.bind("<ButtonRelease-1>", reset)


# -----------------------------
# Start application
# -----------------------------

root.mainloop()

