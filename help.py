from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import webbrowser


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title(" Face-Recognition Attendance System ")

        img3=Image.open(r"assets\background_iist.jpg")
        img3=img3.resize((1920,1080),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1920,height=1080)
        
        title_lbl=Label(self.root,text="Help Desk",font=("Open Sans",40,"bold"),bg="black",fg="blue")
        title_lbl.place(x=800,y=150,width=300,height=60)

        title_lbl2=Label(self.root,text="Contact Us",font=("Open Sans",20,"bold"),bg="black",fg="blue")
        title_lbl2.place(x=850,y=310,width=150,height=60)

        title_lbl2=Label(self.root,text="mail us at - rudrajain2003@gmail.com",font=("Open Sans",20,"bold"),bg="black",fg="blue")
        title_lbl2.place(x=490,y=680,width=550,height=60)


        main_frame=Frame(bg_img,bd=4,bg="black")
        main_frame.place(x=450,y=100,width=1000,height=700)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # Linkedin button 1
        std_img_btn=Image.open(r"assets\linkedin.png")
        std_img_btn=std_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(main_frame,command=self.Linkedin,image=self.std_img1,cursor="hand2")
        std_b1.place(x=60,y=300,width=180,height=180)

        std_b1_1 = Button(main_frame,command=self.Linkedin,text="Linkedin",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=60,y=480,width=180,height=45)

        # Github Face  button 2
        det_img_btn=Image.open(r"assets\github.jpeg")
        det_img_btn=det_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(main_frame,command=self.Github,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=400,y=300,width=180,height=180)

        det_b1_1 = Button(main_frame,command=self.Github,text="Github",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        det_b1_1.place(x=400,y=480,width=180,height=45)


         # Help  Support  button 4
        hlp_img_btn=Image.open(r"assets\email.png")
        hlp_img_btn=hlp_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(main_frame,command=self.gmail,image=self.hlp_img1,cursor="hand2",)
        hlp_b1.place(x=740,y=300,width=180,height=180)

        hlp_b1_1 = Button(main_frame,command=self.gmail,text="Gmail",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        hlp_b1_1.place(x=740,y=480,width=180,height=45)


        # create function for button 
    
    
    def Linkedin(self):
         self.new = 1
         self.url = "https://www.linkedin.com/in/rudra-jain-468633226"
         webbrowser.open(self.url,new=self.new)
    
    def Github(self):
        self.new = 1
        self.url = "https://github.com/R-J003"
        webbrowser.open(self.url,new=self.new)
    
    def Instagram(self):
        self.new = 1
        self.url = "https://mail.google.com/mail/u/0/#inbox"
        webbrowser.open(self.url,new=self.new)
    
    def gmail(self):
        self.new = 1
        self.url = "https://mail.google.com/mail/u/0/#inbox?compose=CllgCJfmrDVKPKcFfvKCKPVxZCmTGHKkFKlVTckdzCSCWpSbxzXRShxkvDdNCzJTlMkSzHMvJwg"
        webbrowser.open(self.url,new=self.new)

if __name__ =="__main__":
    root=Tk()
    obj=Help(root) 
    root.mainloop()        