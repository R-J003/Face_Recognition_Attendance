from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk, ImageDraw  # Import ImageDraw for drawing
import os

root = Tk()

# Load and resize the image
original_image = Image.open("assets/logo.png")
resized_image = original_image.resize((300, 250), Image.Resampling.LANCZOS)  # Use LANCZOS for resampling
image = ImageTk.PhotoImage(resized_image)


height = 430
width = 530
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
root.overrideredirect(True)

root.config(background="black")
canvas = Canvas(root, width=width, height=height, highlightthickness=0, bg = "black")
canvas.pack()

rounded_image = Image.new("RGBA", (width, height), (0, 0, 0, 0))  # Use RGBA mode and add an alpha channel
draw = ImageDraw.Draw(rounded_image)

# Draw the rounded rectangle with a black fill
draw.rounded_rectangle([(0, 0), (width, height)], radius=20, fill=(0, 0, 0, 255))  # RGBA values, 255 for full opacity

# Convert to "L" mode before creating ImageTk.PhotoImage
rounded_image = rounded_image.convert("L")

rounded_mask = ImageTk.PhotoImage(rounded_image)
canvas.create_image(0, 0, anchor=NW, image=rounded_mask)

canvas.create_image(120, 65, anchor=NW, image=image)



welcome_label = Label(text="Face Recognition System", bg="black", font=("Trebuchet Ms", 15, "bold"), fg="white")
welcome_label.place(x=150, y=25)

progress_label = Label(root, text="Loading...", font=("Trebuchet Ms", 13, "bold"), fg="white", bg="black")
progress_label.place(x=210, y=330)

# Fix progressbar style and object naming
progress_style = ttk.Style()
progress_style.theme_use('clam')
progress_style.configure("red.Horizontal.TProgressbar", background="#108cff")

progressbar = Progressbar(root, orient=HORIZONTAL, length=400, mode='determinate', style="red.Horizontal.TProgressbar")
progressbar.place(x=60, y=370)

def top():
    root.withdraw()
    os.system("Python login_page.py")  # used to access other pages
    root.destroy()

i = 0

# loading animation
def load():
    global i
    if i <= 10:
        txt = 'Loading...' + (str(10 * i) + '%')
        progress_label.config(text=txt)
        progress_label.after(600, load)
        progressbar['value'] = 10 * i
        i += 1
    else:
        top()

load()
root.resizable(False, False)
root.mainloop()
