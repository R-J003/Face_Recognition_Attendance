from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title(" Face-Recognition Attendance System ")

        img3=Image.open(r"assets\background_iist.jpg")
        img3=img3.resize((1920,1080),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1920,height=1080)

# ***********************title***************************
        title_lbl=Label(self.root,text="Developer Information",font=("Open Sans",40,"bold"),bg="black",fg="blue")
        title_lbl.place(x=600,y=100,width=800,height=100)

        # ***********************main frame***************************
        main_frame=Frame(bg_img,bd=4,bg="black")
        main_frame.place(x=300,y=100,width=1350,height=700)

        img4=Image.open(r"assets\logo_bg.png")
        img4=img4.resize((300,250),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        bg_img=Label(main_frame,image=self.photoimg4)
        bg_img.place(x=500,y=150,width=300,height=250)

        #developer info
        dev_label=Label(main_frame,text="""
TypeFace, a Python Tkinter desktop app, employs facial recognition technology for 
efficient user authentication. Its intuitive interface facilitates easy interaction, allowing users 
to initiate recognition with few clicks. Leveraging OpenCV and machine learning algorithms LBPH for 
face detection and Haar Cascade for object detection, the app accurately detects and matches facial 
features. TypeFace extends beyond recognition, incorporating features like attendance tracking and 
student management. Built with Python libraries such as openCV PIL and MySQL connector and many more, 
the application ensures robust data seamless flow.""",font=("times new roman",20,"bold"),bg="black",fg="yellow",justify="center")
        dev_label.place(x=10,y=400)




if __name__ =="__main__":
    root=Tk()
    obj=Developer(root) 
    root.mainloop()