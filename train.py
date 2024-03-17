from tkinter import *
import os
from PIL import Image, ImageTk
import cv2
from tkinter import messagebox
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face-Recognition Attendance System")

        # background image
        img1 = Image.open("assets/background_iist.jpg")
        img1 = img1.resize((1920, 1080), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        # background label
        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1920, height=1080)

        frame = Frame(self.root, bg="black")
        frame.place(x=450, y=30, width=1000, height=950)

        title_lbl = Label(frame, text="Train Data Set", font=("Open Sans", 40, "bold"), bg="black", fg="blue")
        title_lbl.place(x=0, y=4, width=1000, height=100)

        # background image
        img_top = Image.open("assets/traindata_img.png")
        img_top = img_top.resize((600, 700), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img_top)

        # background label
        top_img = Label(frame, image=self.photoimg2)
        top_img.place(x=200, y=100, width=600, height=700)

        b1_1 = Button(frame, text="Click here to Train", cursor="hand2", command=self.train_classifier,
                      font=("Times new roman", 20, "bold"), bg="blue", fg="White", relief=RIDGE,
                      activeforeground="white", activebackground="blue")
        b1_1.place(x=290, y=850, width=420, height=50)

    # *************************Create Function of Training***********************

    def train_classifier(self):
        data_dir = "Img_data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []  # images and id should be same
        ids = []

        for image in path:
            img = Image.open(image).convert('L')  # convert to gray scale
            image_np = np.array(img, 'uint8')  # convert into grid with the help of numpy
            # in any particular file path there is file path and then file name
            # so file path is 0 and file name is 1 but there name is 1.1
            # so we are splitting because first 1 is user id and second 1 is image count
            user_id_str = int(os.path.split(image)[1].split('.')[2])  # Change index to 2

            faces.append(image_np)
            ids.append(user_id_str)

            cv2.imshow("Training",image_np)
            cv2.waitKey(1)==13 #after enter window should be close

        ids = np.array(ids)



        # ****************** Train Classifier*******************
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")  # train data will store in this file

        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Dataset Completed!", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
