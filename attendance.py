from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import os
import csv
from tkinter import filedialog


mydata = [] # global variable for store xl list data
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title(" Face-Recognition Attendance System ")

        #-----------Variables-------------------
        self.var_id=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_dep=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attendance=StringVar()


        img=Image.open(r"assets\background_iist.jpg")
        img=img.resize((1920,1080),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1920,height=1080)

        title_lbl = Label(self.root, text="Attendance Management System", font=("Open Sans", 40, "bold"), bg="black", fg="blue")
        title_lbl.place(x=500, y=0, width=900, height=120)

        #Main Frame
        main_frame=Frame(root,bd=2,bg="white")
        main_frame.place(x=35,y=120,width=1850,height=900)


        # Left Label Frame 
        left_frame = LabelFrame(main_frame,bd=4, bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",32,"bold"))
        left_frame.place(x=20,y=10,width=850,height=850)

        # left inner frame        
        leftin_frame = LabelFrame(left_frame,bd=4,bg="white",relief=RIDGE,font=("times new roman",20,"bold"),fg="white")
        leftin_frame.place(x=15,y=40,width=815,height=600)

        # *******************************Text boxes and Combo Boxes**************************

        #Student id
        studentId_label = Label(leftin_frame,text="Student ID:",font=("times new roman",20,"bold"),fg="black", bg = "white")
        studentId_label.grid(row=0,column=0,padx=10,pady=20,sticky=W)

        studentId_entry = ttk.Entry(leftin_frame,width=15,textvariable=self.var_id,font=("times new roman",18,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=20,sticky=W)


        #Student Roll
        student_roll_label = Label(leftin_frame,text="Roll No:",font=("times new roman",20,"bold"),fg="black", bg = "white")
        student_roll_label.grid(row=0,column=2,padx=10,pady=20,sticky=W)

        student_roll_entry = ttk.Entry(leftin_frame,width=15,textvariable=self.var_roll,font=("times new roman",18,"bold"))
        student_roll_entry.grid(row=0,column=3,padx=10,pady=20,sticky=W)

        #Studnet Name
        student_name_label = Label(leftin_frame,text="Student-Name:",font=("times new roman",20,"bold"),fg="black", bg = "white")
        student_name_label.grid(row=1,column=0,padx=10,pady=20,sticky=W)


        student_name_entry = ttk.Entry(leftin_frame,width=15,textvariable=self.var_name,font=("times new roman",18,"bold"))
        student_name_entry.grid(row=1,column=1,padx=10,pady=20,sticky=W)

        #Department
        dep_label = Label(leftin_frame,text="Department:",font=("times new roman",20,"bold"),fg="black", bg = "white")
        dep_label.grid(row=1,column=2,padx=10,pady=20,sticky=W)

        dep_entry = ttk.Entry(leftin_frame,width=15,textvariable=self.var_dep,font=("times new roman",18,"bold"))
        dep_entry.grid(row=1,column=3,padx=10,pady=20,sticky=W)

        #time
        time_label = Label(leftin_frame,text="Time:",font=("times new roman",20,"bold"),fg="black", bg = "white")
        time_label.grid(row=2,column=0,padx=10,pady=20,sticky=W)

        time_entry = ttk.Entry(leftin_frame,width=15,textvariable=self.var_time,font=("times new roman",18,"bold"))
        time_entry.grid(row=2,column=1,padx=10,pady=20,sticky=W)

        #Date 
        date_label = Label(leftin_frame,text="Date:",font=("times new roman",20,"bold"),fg="black", bg = "white")
        date_label.grid(row=2,column=2,padx=10,pady=20,sticky=W)

        date_entry = ttk.Entry(leftin_frame,width=15,textvariable=self.var_date,font=("times new roman",18,"bold"))
        date_entry.grid(row=2,column=3,padx=10,pady=20,sticky=W)

        #Attendance
        student_attend_label = Label(leftin_frame,text="Attend-status:",font=("times new roman",20,"bold"),fg="black", bg = "white")
        student_attend_label.grid(row=3,column=0,padx=10,pady=20,sticky=W)

        attend_combo=ttk.Combobox(leftin_frame,width=13,textvariable=self.var_attendance,font=("times new roman",20),state="readonly")
        attend_combo["values"]=("Status","Present","Absent")
        attend_combo.current(0)
        attend_combo.grid(row=3,column=1,padx=10,pady=20,sticky=W)


        # *******************************button section***************************

        #Button Frame
        btn_frame = Frame(left_frame,bd=2,bg="#DCDCDC",relief=RIDGE)
        btn_frame.place(x=80,y=370,width=670,height=240)

        #Improt button
        save_btn=Button(btn_frame,text="Import CSV",command = self.importCsv, width=20,font=("times new roman",18,"bold"),fg="white",bg="red", borderwidth=0, activeforeground="white", activebackground="red")
        save_btn.grid(row=0,column=0,padx=20,pady=40,sticky=W)

        #Exprot button
        update_btn=Button(btn_frame,text="Export CSV",command = self.exportCsv,width=20,font=("times new roman",18,"bold"),fg="white",bg="green",borderwidth=0, activeforeground="white", activebackground="green")
        update_btn.grid(row=0,column=1,padx=20,pady=40,sticky=W)

        #Update button
        del_btn=Button(btn_frame,text="Update",width=20,font=("times new roman",18,"bold"),fg="white",bg="navyblue",borderwidth=0, activeforeground="white", activebackground="navyblue")
        del_btn.grid(row=1,column=0,padx=20,pady=20,sticky=W)

        #reset button
        reset_btn=Button(btn_frame,text="Reset", command = self.reset_data, width=20,font=("times new roman",18,"bold"),fg="white",bg="black",borderwidth=0, activeforeground="white", activebackground="black")
        reset_btn.grid(row=1,column=1,padx=20,pady=20,sticky=W)


        # right frame
        right_frame = LabelFrame(main_frame, bg="white", bd=4, relief=RIDGE, text="Attendance Details", font=("times new roman", 32, "bold"))
        right_frame.place(x=890, y=10, width=930, height=850)

    # *********************************Table Frame************************************

        #Table Frame 
        #Searching System in Right Label Frame 
        table_frame = Frame(right_frame,bd=3,bg="white",relief=RIDGE)
        table_frame.place(x=20,y=40,width=880,height=730)
        
        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #create table 
        self.attendanceReport = ttk.Treeview(table_frame,column=("ID","Roll_No","Name","Department","Time","Date","Attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.attendanceReport.xview)
        scroll_y.config(command=self.attendanceReport.yview)


        self.attendanceReport.heading("ID",text="Std-ID")
        self.attendanceReport.heading("Roll_No",text="Roll.No")
        self.attendanceReport.heading("Name",text="Std-Name")
        self.attendanceReport.heading("Department",text="Department")
        self.attendanceReport.heading("Time",text="Time")
        self.attendanceReport.heading("Date",text="Date")
        self.attendanceReport.heading("Attendance",text="Attend-status")
        self.attendanceReport["show"]="headings"


        # Set Width of Colums 
        self.attendanceReport.column("ID",width=100)
        self.attendanceReport.column("Roll_No",width=100)
        self.attendanceReport.column("Name",width=100)
        self.attendanceReport.column("Department",width=100)
        self.attendanceReport.column("Time",width=100)
        self.attendanceReport.column("Date",width=100)
        self.attendanceReport.column("Attendance",width=100)
        
        self.attendanceReport.pack(fill=BOTH,expand=1)
        self.attendanceReport.bind("<ButtonRelease>",self.get_cursor)



    def fetchData(self,rows):
        mydata = rows
        self.attendanceReport.delete(*self.attendanceReport.get_children())
        for i in rows:
                self.attendanceReport.insert("",END,values=i)
                print(i)
        

    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                    mydata.append(i)
                    self.fetchData(mydata)

    #==================Experot CSV=============
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No Data Found!",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Successfuly","Export Data Successfully!")
        except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    #=============Cursur Function for CSV========================

    def get_cursor(self,event=""):
        cursor_row = self.attendanceReport.focus()
        content = self.attendanceReport.item(cursor_row)
        rows = content["values"]

        self.var_id.set(rows[0]),
        self.var_roll.set(rows[1]),
        self.var_name.set(rows[2]),
        self.var_dep.set(rows[3]),
        self.var_time.set(rows[4]),
        self.var_date.set(rows[5]),
        self.var_attendance.set(rows[6]) 

    #============================Reset Data======================
    def reset_data(self):
        self.var_id.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_dep.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attendance.set("Status")   







if __name__ =="__main__":
    root=Tk()
    obj=Attendance(root) 
    root.mainloop()        
