from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
from datetime import datetime


class Face_recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition Attendance System")

        # Background image
        img1 = Image.open("assets/background_iist.jpg")
        img1 = img1.resize((1920, 1080), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        # Background label
        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1920, height=1080)

        frame = Frame(self.root, bg="black")
        frame.place(x=350, y=30, width=1200, height=940)

        title_lbl = Label(frame, text="Face Recognition", font=("Open Sans", 40, "bold"), bg="black", fg="blue")
        title_lbl.place(x=350, y=0, width=500, height=100)

        img3 = Image.open("assets/face_recognition.jpg")
        img3 = img3.resize((800, 700), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=550, y=150, width=800, height=700)

        # Face recognition Button
        b1_1 = Button(frame, text="Start Face Recognition", cursor="hand2", command=self.face_recog, font=("Times new roman", 20, "bold"), bg="blue", fg="White", relief=RIDGE, activeforeground="white", activebackground="blue")
        b1_1.place(x=400, y=870, width=380, height=45)

    def mark_attendance(self, i, r, n, d):
        with open("attendance.csv", "r+", newline="\n") as f:
            myDatalist = f.readlines()
            name_list = []
            for line in myDatalist:
                entry = line.split(",")
                name_list.append(entry[0])

            if (i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i}, {r}, {n},{d}, {dtString}, {d1}, Present")

    def face_recog(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])

                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host='localhost', username='root', password='root',
                                               database='face_recognizer')
                cursor = conn.cursor()

                cursor.execute("select Name from student where Student_id=" + str(id))
                n = cursor.fetchone()
                n = "+".join(n) if n else "Unknown"

                cursor.execute("select Roll from student where Student_id=" + str(id))
                r = cursor.fetchone()
                r = "+".join(r) if r else "Unknown"

                cursor.execute("select Dep from student where Student_id=" + str(id))
                d = cursor.fetchone()
                d = "+".join(d) if d else "Unknown"

                cursor.execute("select Student_id from student where Student_id=" + str(id))
                i = cursor.fetchone()
                i = "+".join(i) if i else "Unknown"

                if confidence > 77:
                    cv2.putText(img, f"id:{i}", (x, y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    cv2.putText(img, f"dep:{d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    cv2.putText(img, f"name:{n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    cv2.putText(img, f"roll:{r}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    self.mark_attendance(i, r, n, d)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)

                coord = [x, y, w, y]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("clf.xml")

        videoCap = cv2.VideoCapture(0)

        while True:
            ret, img = videoCap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Face Detector", img)

            if cv2.waitKey(1) == 13:
                break
        videoCap.release()
        cv2.destroyAllWindows()


# main class object
if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition(root)
    root.mainloop()
