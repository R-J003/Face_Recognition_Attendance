from tkinter import *
import os
from tkinter import ttk
from PIL import Image, ImageTk
from time import strftime
from datetime import datetime
from tkinter import messagebox
import tkinter
from Student import Student
from train import Train
from face_recognition import Face_recognition
from attendance import Attendance
from developer import Developer
from help import Help

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title(" Face-Recognition Attendance System ")
        self.img_label = None  # Store the label as an attribute


    def overlay_images(self, background_path, overlay_path1, overlay_path2, x1=50, y1=100, x2=210, y2=370):
        # Open background and overlay images
        background = Image.open(background_path)
        overlay1 = Image.open(overlay_path1)
        overlay2 = Image.open(overlay_path2)

        # Resize background image to 1920x1080
        background = background.resize((1920, 1080), Image.Resampling.LANCZOS)

        # Resize overlay images to the desired size
        overlay1 = overlay1.resize((200, 200), Image.Resampling.LANCZOS)
        overlay2 = overlay2.resize((500, 300), Image.Resampling.LANCZOS)

        # Convert images to RGBA mode (if not already in that mode)
        background = background.convert("RGBA")
        overlay1 = overlay1.convert("RGBA")
        overlay2 = overlay2.convert("RGBA")

        # Create a blank RGBA image for blending
        blended_image = Image.new("RGBA", background.size)

        # Use the paste method for overlaying
        blended_image.paste(background, (0, 0))
        blended_image.paste(overlay1, (x1, y1), overlay1)
        blended_image.paste(overlay2, (x2, y2), overlay2)

        # Convert the blended image to a PhotoImage object
        img = ImageTk.PhotoImage(blended_image, master=self.root)

        # Display the result using Tkinter
        if self.img_label is not None:
            self.img_label.destroy()  # Destroy previous label if it exists

        self.img_label = Label(self.root, image=img)
        self.img_label.image = img  # Store the image reference
        self.img_label.place(x=0, y=0)




    def start(self):
        # Specify the file paths
        background_path = r'assets\background_iist.jpg'  # Replace with your background image
        overlay_path1 = r'assets\iist_logo.png'  # Replace with your first overlay image
        overlay_path2 = r'assets\logo.png'  # Replace with your second overlay image

        # Overlay images and display the result
        self.overlay_images(background_path, overlay_path1, overlay_path2)



        # first image
        img = Image.open(r"assets\iist_image.png")
        img = img.resize((550, 95), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        # label
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=350, y=150, width=550, height=95)


        #title
        title_label = Label(self.root, text="Face Recognition Attendance\n system", font=("times new roman", 50, "bold"), bg="black", fg="yellow")
        title_label.place(x=50, y=750, width=850, height=200)

        frame = Frame(self.root, bg = "black")
        frame.place(x = 950, y = 30, width = 950, height = 950 )



        # Student Button
        img4 = Image.open(r"assets\student.png")
        img4 = img4.resize((130, 150), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(self.root, image=self.photoimg4, command = self.student_details, cursor="hand2")
        b1.place(x=1050, y=100, width=130, height=150)

        b1_1 = Button(self.root, text="Student Details", command = self.student_details, cursor="hand2",font=("Times new roman", 15, "bold"), bg="red", fg="yellow", relief = RIDGE, activeforeground="yellow", activebackground="red")
        b1_1.place(x=1050, y=250, width=130, height=40)

        # Attendance button
        img6 = Image.open(r"assets\report.png")
        img6 = img6.resize((130, 150), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        # button
        b3 = Button(self.root, image=self.photoimg6, cursor="hand2")
        b3.place(x=1350, y=100, width=130, height=150)

        b3_1 = Button(self.root, text="Attendance", cursor="hand2", command = self.attendance_data, font=("times new roman", 15, "bold"), bg="red", fg="yellow", relief = RIDGE, activeforeground="yellow", activebackground="red")
        b3_1.place(x=1350, y=250, width=130, height=40)


        # Face Detection button5
        img5 = Image.open(r"assets\face_detector1.png")
        img5 = img5.resize((130, 150), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        # button
        b2 = Button(self.root, image=self.photoimg5, cursor="hand2", command = self.face_data)
        b2.place(x=1650, y=100, width=130, height=150)

        b2_1 = Button(self.root, text="Face Detection", cursor="hand2", command = self.face_data, font=("times new roman", 15, "bold"), bg="red", fg="yellow", relief = RIDGE, activeforeground="yellow", activebackground="red")
        b2_1.place(x=1650, y=250, width=130, height=40)


        # Train Data button
        img8 = Image.open(r"assets\Train.png")
        img8 = img8.resize((130, 150), Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        # button
        b3 = Button(self.root, image=self.photoimg8, cursor="hand2", command = self.Train_data)
        b3.place(x=1050, y=400, width=130, height=150)

        b3_1 = Button(self.root, text="Train Data", cursor="hand2", command = self.Train_data, font=("times new roman", 15, "bold"), bg="red", fg="yellow", relief = RIDGE, activeforeground="yellow", activebackground="red")
        b3_1.place(x=1050, y=550, width=130, height=40)

        # Photo button
        img9 = Image.open(r"assets\teaser.png")
        img9 = img9.resize((130, 150), Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        # button
        b3 = Button(self.root, image=self.photoimg9, cursor="hand2", command = self.open_img)
        b3.place(x=1350, y=400, width=130, height=150)

        b3_1 = Button(self.root, text="Photos", cursor="hand2", command = self.open_img, font=("times new roman", 15, "bold"), bg="red", fg="yellow", relief = RIDGE, activeforeground="yellow", activebackground="red")
        b3_1.place(x=1350, y=550, width=130, height=40)

        # Developer face button
        img10 = Image.open(r"assets\developer.png")
        img10 = img10.resize((130, 150), Image.Resampling.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        # button
        b3 = Button(self.root, image=self.photoimg10, cursor="hand2", command = self.Developer) 
        b3.place(x=1650, y=400, width=130, height=150)

        b3_1 = Button(self.root, text="Developer", cursor="hand2", command = self.Developer, font=("times new roman", 15, "bold"), bg="red", fg="yellow", relief = RIDGE, activeforeground="yellow", activebackground="red")
        b3_1.place(x=1650, y=550, width=130, height=40)


        # Help button
        img7 = Image.open(r"assets\help.png")
        img7 = img7.resize((130, 150), Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        # button
        b3 = Button(self.root, image=self.photoimg7, cursor="hand2", command = self.Help)
        b3.place(x=1050, y=700, width=130, height=150)

        b3_1 = Button(self.root, text="Help Desk", cursor="hand2", command = self.Help, font=("times new roman", 15, "bold"), bg="red", fg="yellow", relief = RIDGE, activeforeground="yellow", activebackground="red")
        b3_1.place(x=1050, y=850, width=130, height=40)

        # Exit button
        img11 = Image.open(r"assets\exit.png")
        img11 = img11.resize((130, 150), Image.Resampling.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        # button
        b3 = Button(self.root, image=self.photoimg11, cursor="hand2", command = self.iExit)
        b3.place(x=1350, y=700, width=130, height=150)

        b3_1 = Button(self.root, text="Exit", cursor="hand2", command = self.iExit, font=("times new roman", 15, "bold"), bg="red", fg="yellow", relief = RIDGE, activeforeground="yellow", activebackground="red")
        b3_1.place(x=1350, y=850, width=130, height=40)


        #----------time-----
        def time():
            string = strftime("%m/%d/%Y, %I:%M:%S %p")
            lbl.config(text = string)
            lbl.after(1000, time)
            now = datetime.now()

        lbl = Label(self.root,font=("Times new roman",20,"bold"),bg="black",fg="yellow")
        lbl.place(x=1320,y=30,width=300,height=50)
        time()


    def open_img(self):
                os.startfile("Img_data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","are you sure to exit ?",parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return


    #*****************Function Button***********************
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def Train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def Developer(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window) 

    def Help(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)  



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    obj.start()  # Call the start method after initializing the object
    root.mainloop()

