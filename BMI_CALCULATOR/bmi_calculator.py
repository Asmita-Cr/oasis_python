from tkinter import *
import tkinter as tkinter
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
root.title("BMI Calculator")
root.geometry("470x580+300+200")
root.resizable(False, False)
root.configure(bg="#f7f1e3") 

def BMI():
    h = float(Height.get())
    w = float(Weight.get())

    # Convert height into meters
    m = h / 100
    bmi = round(float(w / m**2), 1)
    label1.config(text=bmi)

    if bmi <= 18.5:
        label2.config(text="Underweight!")
        label3.config(text="You have lower weight than normal body!")
    elif bmi > 18.5 and bmi <= 25:
        label2.config(text="Normal!")
        label3.config(text="You are healthy!")
    elif bmi > 25 and bmi <= 30:
        label2.config(text="Overweight!")
        label3.config(text="You have slightly overweight!")
    else:
        label2.config(text="Obese!")
        label3.config(text="Your health might be at risk!")

# Icon
image_icon = PhotoImage(file="PROJECT1/icon.png")
root.iconphoto(False, image_icon)

# Top Image
top = PhotoImage(file="PROJECT1/top.png")
top_image = Label(root, image=top, background="#f7f1e3")
top_image.place(x=-10, y=-10)

# Bottom box
Label(root, width=72, height=18, bg="#d1ccc0").pack(side=BOTTOM)  
# Two boxes
box = PhotoImage(file="PROJECT1/box.png")
Label(root, image=box, bg="#f7f1e3").place(x=20, y=100)
Label(root, image=box, bg="#f7f1e3").place(x=240, y=100)

# Scale image
scale = PhotoImage(file="PROJECT1/scale.png")
Label(root, image=scale, bg="#d1ccc0").place(x=20, y=310)

#--------------------------Slider 1 ------------------------------------------------
current_value = DoubleVar()

def get_current_value():
    return '{: .2f}'.format(current_value.get())

def slider_changed(event):
    Height.set(get_current_value())

    size = int(float(get_current_value()))
    img = Image.open("PROJECT1/man.png")
    resized_image = img.resize((50, 10 + size))
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.place(x=70, y=550 - size)
    secondimage.image = photo2
# Command to change background colour of scale
style = ttk.Style()
style.configure("TScale", background="#f7f1e3")
slider = ttk.Scale(root, from_=0, to=220, orient='horizontal', style="TScale",
                   command=slider_changed, variable=current_value)
slider.place(x=80, y=250)
#-----------------------------------------------------------------------------

#------------------------------ Slider 2 --------------------------------------
current_value2 = DoubleVar()

def get_current_value2():
    return '{: .2f}'.format(current_value2.get())

def slider_changed2(event):
    Weight.set(get_current_value2())

# Command to change background colour of scale
style2 = ttk.Style()
style2.configure("TScale", background="#f7f1e3")
slider2 = ttk.Scale(root, from_=0, to=200, orient='horizontal', style="TScale",
                    command=slider_changed2, variable=current_value2)
slider2.place(x=300, y=250)

#----------------------------------------------------------------------------------

# Entry boxes for height and weight
Height = StringVar()
Weight = StringVar()
height = Entry(root, textvariable=Height, width=5, font='arial 50', bg="#ffffff", fg="#2f3542", bd=0, justify=CENTER)  # White entry box with dark text
height.place(x=35, y=160)
Height.set(get_current_value())

weight = Entry(root, textvariable=Weight, width=5, font='arial 50', bg="#ffffff", fg="#2f3542", bd=0, justify=CENTER)  # White entry box with dark text
weight.place(x=255, y=160)
Weight.set(get_current_value2())

# Man image
secondimage = Label(root, bg="#d1ccc0")  
secondimage.place(x=70, y=530)

# "View Report" Button
Button(root, text="View Report", width=15, height=2, font="arial 10 bold", bg="#1e3799", fg="white", command=BMI).place(x=280, y=340)  # Blue button with white text

# Result
label1 = Label(root, font="arial 60 bold", bg="#d1ccc0", fg="#000")  
label1.place(x=125, y=305)

# Category
label2 = Label(root, font="arial 20 bold", bg="#d1ccc0", fg="#40407a") 
label2.place(x=280, y=430)

# Message
label3 = Label(root, font="arial 10 bold", bg="#d1ccc0", fg="#40407a")  
label3.place(x=200, y=500)

root.mainloop()
