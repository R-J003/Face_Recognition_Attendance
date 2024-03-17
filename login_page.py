from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
from main import Face_Recognition_System
import os



def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1920x1080+0+0")

        # background image
        bg_img = Image.open(r"assets\background_iist.jpg")
        bg_img = bg_img.resize((1920, 1080), Image.Resampling.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(bg_img)

        lbl_bg = Label(self.root, image=self.bg_img)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="black")
        frame.place(x=750, y=270, width=440, height=550)

        img1 = Image.open(r"assets\login_icon.png")
        img1 = img1.resize((100, 100), Image.Resampling.LANCZOS)
        self.PhotoImage1 = ImageTk.PhotoImage(img1)
        lbl1 = Label(image=self.PhotoImage1, bg="black", borderwidth=0)
        lbl1.place(x=930, y=285, width=100, height=100)

        get_str = Label(frame, text="Get Started", font=("times new roman", 25, "bold"), fg="white", bg="black")
        get_str.place(x=140, y=120)

        username = Label(frame, text="Username", font=("times new roman", 20, "bold"), fg="white", bg="black")
        username.place(x=140, y=195)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 20, "bold"))
        self.txtuser.place(x=80, y=245, width=290)

        password = Label(frame, text="Password", font=("times new roman", 20, "bold"), fg="white", bg="black")
        password.place(x=140, y=305)

        self.txtpass = ttk.Entry(frame, show='*', font=("times new roman", 20, "bold"))
        self.txtpass.place(x=80, y=355, width=290)

        img2 = Image.open(r"assets\login_icon.png")
        img2 = img2.resize((40, 40), Image.Resampling.LANCZOS)
        self.PhotoImage2 = ImageTk.PhotoImage(img2)
        lblimg1 = Label(image=self.PhotoImage2, bg="black", borderwidth=0)
        lblimg1.place(x=845, y=460, width=40, height=40)

        img3 = Image.open(r"assets\lock_icon.png")
        img3 = img3.resize((40, 40), Image.Resampling.LANCZOS)
        self.PhotoImage3 = ImageTk.PhotoImage(img3)
        lblimg2 = Label(image=self.PhotoImage3, bg="black", borderwidth=0)
        lblimg2.place(x=845, y=575, width=40, height=40)

        loginbtn = Button(frame, command=self.login, text="login", font=("times new roman", 20, "bold"),
                          bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=155, y=420, width=120, height=40)

        registerbtn = Button(text="New User Register", command=self.register_window,
                             font=("times new roman", 15, "bold"), borderwidth=0, fg="white", bg="black",
                             activeforeground="white", activebackground="black")
        registerbtn.place(x=780, y=750, width=200)

        forgetbtn = Button(text="Forget Password", command=self.forgot_password_window,
                            font=("times new roman", 15, "bold"), borderwidth=0, fg="white", bg="black",
                            activeforeground="white", activebackground="black")
        forgetbtn.place(x=770, y=780, width=200)

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.txtuser.get() == "rudra" and self.txtpass.get() == "rudra":
            messagebox.showinfo("Success", "Logging in...")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_recognizer")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where user_name = %s and password = %s", (
                self.txtuser.get(),
                self.txtpass.get()
            ))

            row = my_cursor.fetchone()
            if row is None:
                messagebox.showerror("Error", "Invalid Username & password")
            else:
                try:
                    open_main = messagebox.askyesno("YesNo", "Access only Admin")
                
                    if open_main > 0:
                        self.root.withdraw()
                        os.system("python main.py")

                    else:
                        if not open_main:
                            return
                except Exception as es:
                    print(f"Error due to: {str(es)}")
            conn.commit()
            conn.close()

    def forgot_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Please Enter the User Name Address to Reset the Password")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_recognizer")
            my_cursor = conn.cursor()

            query = ("select * from register where user_name = %s")
            value = (self.txtuser.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row is None:
                messagebox.showerror("Error", "Please Enter the Valid Username")
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("450x550+750+300")
                self.root2.configure(bg="black")

                l = Label(self.root2, text="Forget Password", font=("times new roman", 30, "bold"), bg="black",
                          fg="white")
                l.place(x=0, y=20, relwidth=1)

                security_Q = Label(self.root2, text="Security Question", font=("times new roman", 20, "bold",),
                                   bg="black", fg="white")
                security_Q.place(x=50, y=100)

                self.combo_security_Q = ttk.Combobox(self.root2, font=("times new roman", 20, "bold",), state="readonly")
                self.combo_security_Q["value"] = ("Select", "Your Birth Place", "Your favourite city",
                                                  "Your favourite food", "Your Pet's Name")
                self.combo_security_Q.place(x=50, y=150, width=250)
                self.combo_security_Q.current(0)

                security_A = Label(self.root2, text="Security Answer", font=("times new roman", 20, "bold",),
                                   bg="black", fg="white")
                security_A.place(x=50, y=220)

                self.txt_security = ttk.Entry(self.root2, font=("times new roman", 20, "bold",))
                self.txt_security.place(x=50, y=270, width=250)

                new_password = Label(self.root2, text=" New Password", font=("times new roman", 20, "bold",),
                                     bg="black", fg="white")
                new_password.place(x=50, y=330)

                self.txt_newpass = ttk.Entry(self.root2, show='*', font=("times new roman", 20, "bold",))
                self.txt_newpass.place(x=50, y=380, width=250)

                btn = Button(self.root2, text="Reset", command=self.reset_pass,
                             font=("times new roman", 25, "bold"), fg="white", bg="red")
                btn.place(x=150, y=450)

    def reset_pass(self):
        if self.combo_security_Q.get() == "Select":
            messagebox.showerror("Error", "Select the Security Question", parent=self.root2)
        elif self.txt_security.get() == "Select":
            messagebox.showerror("Error", "Please enter the Answer", parent=self.root2)
        elif self.txt_newpass.get() == "":
            messagebox.showerror("Error", "Please enter the New Password", parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="root",
                                           database="face_recognizer")
            my_cursor = conn.cursor()

            qury = ("select * from register where email = %s and securityQ = %s and securityA = %s")
            value = (self.txtuser.get(), self.combo_security_Q.get(), self.txt_security.get(),)
            my_cursor.execute(qury, value)
            row = my_cursor.fetchone()
            if row is None:
                messagebox.showerror("Error", "Please enter correct Answer", parent=self.root2)
            else:
                query = ("update register set password = %s where email = %s")
                value1 = (self.txt_newpass.get(), self.txtuser.get())
                my_cursor.execute(query, value1)
                conn.commit()
                conn.close()
                messagebox.showinfo("Info", "Your password has been reset, please login using new password",
                                    parent=self.root2)
                self.root2.destroy()


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration")
        self.root.geometry("1920x1080+0+0")

        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        bg = Image.open(r"assets\background_iist.jpg")
        bg = bg.resize((1920, 1080), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(bg)

        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="white")
        frame.place(x=525, y=175, width=850, height=700)

        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 30, "bold",), fg="darkgreen",
                             bg="white")
        register_lbl.place(x=270, y=50)

        fname = Label(frame, text="First Name", font=("times new roman", 20, "bold",), bg="white")
        fname.place(x=100, y=160)

        fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 20, "bold",))
        fname_entry.place(x=100, y=200, width=250)

        lname = Label(frame, text="Last Name", font=("times new roman", 20, "bold",), bg="white")
        lname.place(x=490, y=160)

        self.lname_entry = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 20, "bold",))
        self.lname_entry.place(x=490, y=200, width=250)

        contact = Label(frame, text="Contact No.", font=("times new roman", 20, "bold",), bg="white")
        contact.place(x=100, y=260)

        self.contact_entry = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 20, "bold",))
        self.contact_entry.place(x=100, y=300, width=250)

        email = Label(frame, text="Username", font=("times new roman", 20, "bold",), bg="white")
        email.place(x=490, y=260)

        self.email_entry = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 20, "bold",))
        self.email_entry.place(x=490, y=300, width=250)

        security_Q = Label(frame, text="Security Question", font=("times new roman", 20, "bold",), bg="white")
        security_Q.place(x=100, y=370)

        self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ, font=("times new roman", 20, "bold",),
                                             state="readonly")
        self.combo_security_Q["value"] = ("Select", "Your Birth Place", "Your favourite city", "Your favourite food",
                                          "Your Pet's Name")
        self.combo_security_Q.place(x=100, y=410, width=250)
        self.combo_security_Q.current(0)

        security_A = Label(frame, text="Security Answer", font=("times new roman", 20, "bold",), bg="white")
        security_A.place(x=490, y=370)

        self.security_A_entry = ttk.Entry(frame, textvariable=self.var_securityA, font=("times new roman", 20, "bold",))
        self.security_A_entry.place(x=490, y=410, width=250)

        passwo = Label(frame, text="Password", font=("times new roman", 20, "bold",), bg="white")
        passwo.place(x=100, y=470)

        self.pass_entry = ttk.Entry(frame, textvariable=self.var_pass, font=("times new roman", 20, "bold",))
        self.pass_entry.place(x=100, y=510, width=250)

        confirm_pass = Label(frame, text="Confirm Password", font=("times new roman", 20, "bold",), bg="white")
        confirm_pass.place(x=490, y=470)

        self.confirmpass_entry = ttk.Entry(frame, textvariable=self.var_confpass, font=("times new roman", 20, "bold",))
        self.confirmpass_entry.place(x=490, y=510, width=250)

        registernowbtn = Button(frame, text="Register Now", command=self.register_data, cursor="hand2",
                                font=("times new roman", 25, "bold"), borderwidth=0, fg="white", bg="red",
                                activeforeground="white", activebackground="red")
        registernowbtn.place(x=90, y=600, width=300)

        loginnowbtn = Button(frame, text="Login Now", command=self.return_login, cursor="hand2",
                             font=("times new roman", 25, "bold"), borderwidth=0, fg="white", bg="darkblue",
                             activeforeground="white", activebackground="darkblue")
        loginnowbtn.place(x=470, y=600, width=300)

    def return_login(self):
        self.root.destroy()

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password & Confirm Password must be same")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_recognizer")
            my_cursor = conn.cursor()
            query = ("select * from register where email = %s")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row is not None:
                messagebox.showerror("Error", "User already exists, please try another email")
            else:
                my_cursor.execute("insert into register values(%s, %s, %s, %s, %s, %s, %s)", (
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_confpass.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get()
                ))

            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Registered Successfully")


if __name__ == "__main__":
    main()
