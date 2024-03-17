from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2


class Student:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

        # variables
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_Batch = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()



#for creating label and inserting image
        # background image
        img1 = Image.open(r"assets\background_iist.jpg")
        img1 = img1.resize((1920, 1080), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        # background label
        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1920, height=1080)

        # Footer Image
        img2 = Image.open(r"assets\student_management.png")
        img2 = img2.resize((1920, 180), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        # Footer label
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=0, y=0, width=1920, height=180)


        #title
        title_lbl = Label(bg_img, text = "Student Management System", font=("times new roman", 35, "bold"), bg="black", fg="yellow")
        title_lbl.place(x=0, y=175, width=1920, height=80)



        #frame
        main_frame=Frame(bg_img, bd=3, bg="white")
        main_frame.place(x=15, y=255, width=1890, height=1060)

        #left frame
        left_frame=LabelFrame(main_frame, bg="white", bd=4, relief=RIDGE, text="Student Details", font=("times new roman", 32, "bold"))
        left_frame.place(x=10, y=10, width=925, height=765)

        #current course label
        current_course_frame=LabelFrame(left_frame, bg="white", bd=3, relief=RIDGE, text="Current Course Information", font=("times new roman", 20, "bold"))
        current_course_frame.place(x=5, y=40, width=905, height=170)

        #Department
        dep_label=Label(current_course_frame, text="Department", font=("times new roman", 16, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=4, sticky=W)

        dep_combo=ttk.Combobox(current_course_frame, textvariable = self.var_dep, font=("times new roman", 14, "bold"), width=20, state="readonly")
        dep_combo["values"]=("    Select Department   ", "  CSE  ", "  IT  ", "  AIML  ", "  ECE  ", "  CIVIL  ", "  MECHANICAL  ", "  CHEMICAL  ")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=8, pady=20, sticky=W)


        # Course
        course_label = Label(current_course_frame, text="   Course  ", font=("times new roman", 16, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=8, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, textvariable =self.var_course, font=("times new roman", 14, "bold"), width=20, state="readonly")
        course_combo["values"] = ("     Select Course     ", "  B.Tech  ", "  B.E  ", "  Diploma  ")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=8, pady=15, sticky=W)


        # Year
        year_label = Label(current_course_frame, text=" Year    ", font=("times new roman", 16, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=4, sticky=W)

        year_combo = ttk.Combobox(current_course_frame, textvariable = self.var_year, font=("times new roman", 14, "bold"), width=20, state="readonly")
        year_combo["values"] = ("      Select Year      ", "   2019-20  ", "   2020-21  ", "   2021-22  ", "   2022-23   ", "   2023-24   ")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=8, pady=20, sticky=W)


        # Semester
        year_label = Label(current_course_frame, text="   Semester ", font=("times new roman", 16, "bold"), bg="white")
        year_label.grid(row=1, column=2, padx=8, sticky=W)

        year_combo = ttk.Combobox(current_course_frame, textvariable = self.var_semester, font=("times new roman", 14, "bold"), width=20,state="readonly")
        year_combo["values"] = ("     Select Semester     ", "   1st  ", "   2nd  ", "   3rd  ", "   4th  ", "   5th  ", "   6th  ", "   7th  ", "   8th  ")
        year_combo.current(0)
        year_combo.grid(row=1, column=3, padx=8, pady=15, sticky=W)




        # class Student label
        class_Student_frame = LabelFrame(left_frame, bg="white", bd=3, relief=RIDGE, text="Class Student Information",font=("times new roman", 20, "bold"))
        class_Student_frame.place(x=5, y=250, width=905, height=420)

        # Student id
        studentId_label = Label(class_Student_frame, text="Student ID:",font=("times new roman", 16, "bold"), bg="white")
        studentId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        studentId_entry = ttk.Entry(class_Student_frame, textvariable = self.var_id, width=20,font=("times new roman", 16, "bold"))
        studentId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Student name
        student_name_label = Label(class_Student_frame, text="Student Name:", font=("times new roman", 16, "bold"), bg="white")
        student_name_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        student_name_entry = ttk.Entry(class_Student_frame, textvariable = self.var_name, width=20, font=("times new roman", 16, "bold"))
        student_name_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Batch
        student_Batch_label = Label(class_Student_frame, text="Batch: ", font=("times new roman", 16, "bold"), bg="white")
        student_Batch_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        Batch_combo = ttk.Combobox(class_Student_frame, textvariable = self.var_Batch, font=("times new roman", 14, "bold"),  width=20, state="readonly")
        Batch_combo["values"] = ("Select Batch","Batch-1", "Batch-2")
        Batch_combo.current(0)
        Batch_combo.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        # Roll No
        student_roll_label = Label(class_Student_frame, text="Roll-No:", font=("times new roman", 16, "bold"), bg="white")
        student_roll_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        student_roll_entry = ttk.Entry(class_Student_frame, textvariable = self.var_roll, width=20, font=("times new roman", 16, "bold"))
        student_roll_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Gender
        student_gender_label = Label(class_Student_frame, text="Gender:", font=("times new roman", 16, "bold"), bg="white",)
        student_gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        # combo box
        gender_combo = ttk.Combobox(class_Student_frame, textvariable = self.var_gender, width=20,font=("times new roman", 16, "bold"), state="readonly")
        gender_combo["values"] = ("Select Gender","Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Date of Birth
        student_dob_label = Label(class_Student_frame, text="DOB :", font=("times new roman", 16, "bold"), bg="white")
        student_dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        student_dob_entry = ttk.Entry(class_Student_frame, textvariable = self.var_dob, width=20, font=("times new roman", 16, "bold"))
        student_dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Email
        student_email_label = Label(class_Student_frame, text="Email:", font=("times new roman", 16, "bold"), bg="white")
        student_email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        student_email_entry = ttk.Entry(class_Student_frame, textvariable = self.var_email, width=20, font=("times new roman", 16, "bold"))
        student_email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Phone Number
        student_mob_label = Label(class_Student_frame, text="Mob-No:", font=("times new roman", 16, "bold"), bg="white")
        student_mob_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        student_mob_entry = ttk.Entry(class_Student_frame, textvariable = self.var_phone, width=20, font=("times new roman", 16, "bold"))
        student_mob_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Address
        student_address_label = Label(class_Student_frame, text="Address:", font=("times new roman", 16, "bold"), bg="white")
        student_address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        student_address_entry = ttk.Entry(class_Student_frame, width=20, textvariable = self.var_address, font=("times new roman", 16, "bold"))
        student_address_entry.grid(row=4, column=1, padx=10, pady=10, sticky=W)

        # Teacher Name
        student_tutor_label = Label(class_Student_frame, text="Teacher Name:", font=("times new roman", 16, "bold"), bg="white")
        student_tutor_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        student_tutor_entry = ttk.Entry(class_Student_frame, textvariable = self.var_teacher, width=20, font=("times new roman", 16, "bold"))
        student_tutor_entry.grid(row=4, column=3, padx=5, pady=10, sticky=W)


        #Radio Buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=5,column=1,padx=10,pady=15,sticky=W)

        radiobtn2 = ttk.Radiobutton(class_Student_frame, variable=self.var_radio1, text="No Photo Sample", value="No",)
        radiobtn2.grid(row=5,column=2,padx=10,pady=15,sticky=W)

        #Button Frame 1
        btn_frame = Frame(left_frame,bd=2,bg="#DCDCDC",relief=RIDGE)
        btn_frame.place(x=10,y=560,width=890,height=90)

        #save button
        save_btn=Button(btn_frame,text="Save", command = self.add_data, width=14,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        save_btn.grid(row=0,column=0,padx=20,pady=8,sticky=W)

        #update button
        update_btn=Button(btn_frame,text="Update", command = self.update_data, width=14,font=("verdana",12,"bold"),fg="white",bg="green")
        update_btn.grid(row=0,column=1,padx=20,pady=8,sticky=W)

        #delete button
        del_btn=Button(btn_frame,text="Delete", command = self.delete_data, width=14,font=("verdana",12,"bold"),fg="white",bg="red")
        del_btn.grid(row=0,column=2,padx=20,pady=8,sticky=W)

        #reset button
        reset_btn=Button(btn_frame,text="Reset", command = self.reset_data, width=14,font=("verdana",12,"bold"),fg="white",bg="grey")
        reset_btn.grid(row=0,column=3,padx=20,pady=8,sticky=W)


        #take photo button
        take_photo_btn=Button(btn_frame,text="Take Photo", command = self.generate_dataset, width=20,font=("times new roman",12,"bold"),fg="white",bg="black")
        take_photo_btn.grid(row=1,column=1, padx=5)

        #update photo button
        update_photo_btn=Button(btn_frame,text="Update Photo",width=20,font=("times new roman",12,"bold"),fg="white",bg="black")
        update_photo_btn.grid(row=1,column=2,padx=5)


        # right frame
        right_frame = LabelFrame(main_frame, bg="white", bd=4, relief=RIDGE, text="Student Details", font=("times new roman", 32, "bold"))
        right_frame.place(x=945, y=10, width=930, height=765)


        #Searching System in Right Label Frame
        search_frame = LabelFrame(right_frame,bg="white", bd=3,relief=RIDGE,text="Search System",font=("times new roman",20,"bold"))
        search_frame.place(x=10,y=40,width=905,height=90)

        search_label = Label(search_frame,text="Search:",font=("times new roman",14,"bold"), bg="white")
        search_label.grid(row=0,column=0,padx=10,pady=20,sticky=W)

        #combo box
        search_combo=ttk.Combobox(search_frame,width=12,font=("times new roman",14,"bold"),state="readonly")
        search_combo["values"]=("    Select  ","Roll-No","Phone-no")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=10,pady=15,sticky=W)

        #search Entry button
        search_entry = ttk.Entry(search_frame,width=15,font=("times new roman",14,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=15,sticky=W)

        search_btn=Button(search_frame,text="Search",width=18,font=("times new roman",14,"bold"),fg="white",bg="red")
        search_btn.grid(row=0,column=3,padx=10,pady=10,sticky=W)

        showAll_btn=Button(search_frame,text="Show All",width=18,font=("times new roman",14,"bold"),fg="white",bg="green")
        showAll_btn.grid(row=0,column=4,padx=10,pady=10,sticky=W)

        #-----------------------------Table Frame-------------------------------------------------
        #Table Frame
        #Searching System in Right Label Frame
        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=150,width=905,height=520)

        #scroll bar
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #create table
        self.student_table = ttk.Treeview(table_frame,column=("Dep","Course","Year","Sem","ID","Name","Batch","Roll-No","Gender","DOB","Email","Mob-No","Address","Teacher","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Dep",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Sem",text="Semester")
        self.student_table.heading("ID",text="StudentID")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Batch",text="Batch")
        self.student_table.heading("Roll-No",text="Roll-No")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Mob-No",text="Mob-No")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Teacher",text="Teacher")
        self.student_table.heading("Photo",text="PhotoSample")
        self.student_table["show"]="headings"

        # Set Width of Colums
        self.student_table.column("Dep",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Sem",width=100)
        self.student_table.column("ID",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Batch",width=100)
        self.student_table.column("Roll-No",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Mob-No",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Teacher",width=100)
        self.student_table.column("Photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()


    #***************************Function declaration**************************
    def add_data(self):
        if self.var_dep.get()=="select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error", "All Fields are required", parent = self.root)
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='root', database='face_recognizer')
                mycursor = conn.cursor()
                mycursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_Batch.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                ))
    
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "All Records are Saved!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


#*********************Fetch data form database to table***************************

    def fetch_data(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='root', database='face_recognizer')
        mycursor = conn.cursor()
    
        mycursor.execute("select * from student")
        data=mycursor.fetchall()
    
        if len(data)!= 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()


#*********************get cursor function************************
    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        if data:

            self.var_dep.set(data[0]),
            self.var_course.set(data[1]),
            self.var_year.set(data[2]),
            self.var_semester.set(data[3]),
            self.var_id.set(data[4]),
            self.var_name.set(data[5]),
            self.var_Batch.set(data[6]),
            self.var_roll.set(data[7]),
            self.var_gender.set(data[8]),
            self.var_dob.set(data[9]),
            self.var_email.set(data[10]),
            self.var_phone.set(data[11]),
            self.var_address.set(data[12]),
            self.var_teacher.set(data[13]),
            self.var_radio1.set(data[14])


    # **********************Update Function*************************
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_id.get()=="" or self.var_name.get()=="" or self.var_Batch.get()=="" or self.var_roll.get()=="" or self.var_gender.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_address.get()=="" or self.var_teacher.get()=="":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to Update this Student Details!",parent=self.root)
                if Update>0:
                    conn = mysql.connector.connect(host='localhost', username='root', password='root', database='face_recognizer')
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Batch=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",( 
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_name.get(),
                    self.var_Batch.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_id.get()   
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Successfully Updated!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)


    # **********************Delete Function*************************
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student Id Must be Required!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to Delete?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host='localhost', username='root', password='root', database='face_recognizer')
                    mycursor = conn.cursor() 
                    sql="delete from student where Student_id=%s"
                    val=(self.var_id.get(),)
                    mycursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    # ********************Reset Function************************
    def reset_data(self):
        self.var_name.set(""),
        self.var_id.set(""),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_dep.set("Select Department"),
        self.var_semester.set("Select Semester"),
        self.var_Batch.set("Select Batch"),
        self.var_gender.set("Select Gender"),
        self.var_dob.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_roll.set(""),
        self.var_email.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("") 
   


#**********************************This part is related to Opencv Camera part************************
#************************************Generate Data set take image*************************

    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_id.get()=="" or self.var_name.get()=="" or self.var_Batch.get()=="" or self.var_roll.get()=="" or self.var_gender.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_address.get()=="" or self.var_teacher.get()=="":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='root', database='face_recognizer')
                mycursor = conn.cursor()
                mycursor.execute("select * from student")
                myreslut = mycursor.fetchall()
                id=0
                for x in myreslut:
                    id+=1

                mycursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Batch=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",( 
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_name.get(),
                    self.var_Batch.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_id.get()==id+1   
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #***************part of opencv (load predefined data from opencv)********************

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_croped(img):
                    # conver gary sacle
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #Scaling factor 1.3
                    # Minimum neighbors 5
                    for (x,y,w,h) in faces:
                        face_croped=img[y:y+h,x:x+w] #this size face will be cropped
                        return face_croped
                cap=cv2.VideoCapture(0) #open the Camera #webcamera is always 0
                img_id=0
                while True:
                    ret,my_frame=cap.read() #read the image
                    if face_croped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_croped(my_frame),(400,400))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path = f"data/student."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)#--> size,color,thickness     
                        cv2.imshow("Capture Images",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:  #13 for automaticall3y close window
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset completed!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)


if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()

