from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import re
import os
import glob

# Testing Connection
"""
conn = mysql.connector.connect(user='root', password='@omama1234',host='localhost',database='face_recognition',port=3307)
cursor = conn.cursor()
cursor.execute("show databases")
data = cursor.fetchall()
print(data)
conn.close()
"""


class Student:
    def _init_(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Student Pannel")

        # -----------Variables-------------------
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_mob = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

        self.entry_std_name = Entry(self.root, textvariable=self.var_std_name, validate="key",
                                    validatecommand=(self.root.register(self.validate_name), '%P'))
        self.entry_std_name.pack()
        # This is the part where image labels setting start
        # first header image
        img = Image.open(r"C:\Users\PMLS\Downloads\aa1.png")
        img = img.resize((1366, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        # set image as lable
        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1366, height=130)
        # backgorund image
        bg1 = Image.open(r"C:\Users\PMLS\Downloads\a1.png")
        bg1 = bg1.resize((1366, 768), Image.ANTIALIAS)
        self.photobg1 = ImageTk.PhotoImage(bg1)
        # set image as lable
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=130, width=1366, height=768)
        # title section
        title_lb1 = Label(bg_img, text="STUDENT INFORMATION", font=("Algerian", 30, "bold"), bg="white", fg="#003151")
        title_lb1.place(x=0, y=0, width=1366, height=45)
        # Creating Frame
        main_frame = Frame(bg_img, bd=2, bg="white")  # bd mean border
        main_frame.place(x=5, y=55, width=1355, height=510)
        # Left Label Frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details",
                                font=("verdana", 12, "bold"), fg="#003151")
        left_frame.place(x=10, y=10, width=660, height=480)
        # Current Course
        current_course_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course",
                                          font=("verdana", 12, "bold"), fg="#003151")
        current_course_frame.place(x=10, y=5, width=635, height=150)
        # label Department
        dep_label = Label(current_course_frame, text="Department", font=("verdana", 12, "bold"), bg="white",
                          fg="#003151")
        dep_label.grid(row=0, column=0, padx=5, pady=15)
        # combo box
        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, width=15,
                                 font=("verdana", 12, "bold"), state="readonly")
        dep_combo["values"] = ("Select Department", "BSCS", "BSIT", "BSE", "BCE", "BSAI")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=5, pady=15, sticky=W)

        # -----------------------------------------------------
        # label Course
        cou_label = Label(current_course_frame, text="Course", font=("verdana", 12, "bold"), bg="white", fg="#003151")
        cou_label.grid(row=0, column=2, padx=5, pady=15)
        # combo box
        cou_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, width=15,
                                 font=("verdana", 12, "bold"), state="readonly")
        cou_combo["values"] = ("Select Course", "ISE", "CC", "DSA", "SQE", "AI")
        cou_combo.current(0)
        cou_combo.grid(row=0, column=3, padx=5, pady=15, sticky=W)

        # -------------------------------------------------------------
        # label Year
        year_label = Label(current_course_frame, text="Year", font=("verdana", 12, "bold"), bg="white", fg="#003151")
        year_label.grid(row=1, column=0, padx=5, sticky=W)
        # combo box
        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, width=15,
                                  font=("verdana", 12, "bold"), state="readonly")
        year_combo["values"] = ("Select Year", "2020-2024", "2021-2025", "2022-2026", "2023-2027", "2024-2028")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=5, pady=15, sticky=W)

        # -----------------------------------------------------------------
        # label Semester
        year_label = Label(current_course_frame, text="Semester", font=("verdana", 12, "bold"), bg="white",
                           fg="#003151")
        year_label.grid(row=1, column=2, padx=5, sticky=W)
        # combo box
        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, width=15,
                                  font=("verdana", 12, "bold"), state="readonly")
        year_combo["values"] = (
        "Select Semester", "Semester-1", "Semester-2", "Semester-3", "Semester-4", "Semester-5", "Semester-6",
        "Semester-7", "Semester-8")
        year_combo.current(0)
        year_combo.grid(row=1, column=3, padx=5, pady=15, sticky=W)
        # Class Student Information
        class_Student_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information",
                                         font=("verdana", 12, "bold"), fg="#003151")
        class_Student_frame.place(x=10, y=160, width=635, height=230)
        # Student id
        studentId_label = Label(class_Student_frame, text="Std-ID:", font=("verdana", 12, "bold"), fg="#003151",
                                bg="white")
        studentId_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        studentId_entry = ttk.Entry(class_Student_frame, textvariable=self.var_std_id, width=15,
                                    font=("verdana", 12, "bold"))
        studentId_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        # Student name
        student_name_label = Label(class_Student_frame, text="Std-Name:", font=("verdana", 12, "bold"), fg="#003151",
                                   bg="white")
        student_name_label.grid(row=0, column=2, padx=5, pady=5, sticky=W)
        student_name_entry = ttk.Entry(class_Student_frame, textvariable=self.var_std_name, width=15,
                                       font=("verdana", 12, "bold"))
        student_name_entry.grid(row=0, column=3, padx=5, pady=5, sticky=W)
        # Class Didvision
        student_div_label = Label(class_Student_frame, text="Class Division:", font=("verdana", 12, "bold"),
                                  fg="#003151", bg="white")
        student_div_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        div_combo = ttk.Combobox(class_Student_frame, textvariable=self.var_div, width=13, font=("verdana", 12, "bold"),
                                 state="readonly")
        div_combo["values"] = ("Morning", "Evening")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=5, pady=5, sticky=W)
        # Roll No
        student_roll_label = Label(class_Student_frame, text="Roll-No:", font=("verdana", 12, "bold"), fg="#003151",
                                   bg="white")
        student_roll_label.grid(row=1, column=2, padx=5, pady=5, sticky=W)
        student_roll_entry = ttk.Entry(class_Student_frame, textvariable=self.var_roll, width=15,
                                       font=("verdana", 12, "bold"))
        student_roll_entry.grid(row=1, column=3, padx=5, pady=5, sticky=W)
        # Gender
        student_gender_label = Label(class_Student_frame, text="Gender:", font=("verdana", 12, "bold"), fg="#003151",
                                     bg="white")
        student_gender_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)
        # combo box
        gender_combo = ttk.Combobox(class_Student_frame, textvariable=self.var_gender, width=13,
                                    font=("verdana", 12, "bold"), state="readonly")
        gender_combo["values"] = ("Male", "Female", "Others")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=5, pady=5, sticky=W)
        # Date of Birth
        student_dob_label = Label(class_Student_frame, text="DOB:", font=("verdana", 12, "bold"), fg="#003151",
                                  bg="white")
        student_dob_label.grid(row=2, column=2, padx=5, pady=5, sticky=W)
        student_dob_entry = ttk.Entry(class_Student_frame, textvariable=self.var_dob, width=15,
                                      font=("verdana", 12, "bold"))
        student_dob_entry.grid(row=2, column=3, padx=5, pady=5, sticky=W)
        # Email
        student_email_label = Label(class_Student_frame, text="Email:", font=("verdana", 12, "bold"), fg="#003151",
                                    bg="white")
        student_email_label.grid(row=3, column=0, padx=5, pady=5, sticky=W)
        student_email_entry = ttk.Entry(class_Student_frame, textvariable=self.var_email, width=15,
                                        font=("verdana", 12, "bold"))
        student_email_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)
        # Phone Number
        student_mob_label = Label(class_Student_frame, text="Mob-No:", font=("verdana", 12, "bold"), fg="#003151",
                                  bg="white")
        student_mob_label.grid(row=3, column=2, padx=5, pady=5, sticky=W)
        student_mob_entry = ttk.Entry(class_Student_frame, textvariable=self.var_mob, width=15,
                                      font=("verdana", 12, "bold"))
        student_mob_entry.grid(row=3, column=3, padx=5, pady=5, sticky=W)
        # Address
        student_address_label = Label(class_Student_frame, text="Address:", font=("verdana", 12, "bold"), fg="#003151",
                                      bg="white")
        student_address_label.grid(row=4, column=0, padx=5, pady=5, sticky=W)
        student_address_entry = ttk.Entry(class_Student_frame, textvariable=self.var_address, width=15,
                                          font=("verdana", 12, "bold"))
        student_address_entry.grid(row=4, column=1, padx=5, pady=5, sticky=W)
        # Teacher Name
        student_tutor_label = Label(class_Student_frame, text="Tutor Name:", font=("verdana", 12, "bold"), fg="#003151",
                                    bg="white")
        student_tutor_label.grid(row=4, column=2, padx=5, pady=5, sticky=W)
        student_tutor_entry = ttk.Entry(class_Student_frame, textvariable=self.var_teacher, width=15,
                                        font=("verdana", 12, "bold"))
        student_tutor_entry.grid(row=4, column=3, padx=5, pady=5, sticky=W)
        # Radio Buttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_Student_frame, text="Take Photo Sample", variable=self.var_radio1,
                                    value="Yes")
        radiobtn1.grid(row=5, column=0, padx=5, pady=5, sticky=W)
        radiobtn1 = ttk.Radiobutton(class_Student_frame, text="No Photo Sample", variable=self.var_radio1, value="No")
        radiobtn1.grid(row=5, column=1, padx=5, pady=5, sticky=W)
        # Button Frame
        btn_frame = Frame(left_frame, bd=2, bg="white", relief=RIDGE)
        btn_frame.place(x=10, y=390, width=635, height=60)
        # save button
        save_btn = Button(btn_frame, command=self.add_data, text="Save", width=7, font=("verdana", 12, "bold"),
                          fg="white", bg="#003151")
        save_btn.grid(row=0, column=0, padx=5, pady=10, sticky=W)
        # update button
        update_btn = Button(btn_frame, command=self.update_data, text="Update", width=7, font=("verdana", 12, "bold"),
                            fg="white", bg="#003151")
        update_btn.grid(row=0, column=1, padx=5, pady=8, sticky=W)
        # delete button
        del_btn = Button(btn_frame, command=self.delete_data, text="Delete", width=7, font=("verdana", 12, "bold"),
                         fg="white", bg="#003151")
        del_btn.grid(row=0, column=2, padx=5, pady=10, sticky=W)
        # reset button
        reset_btn = Button(btn_frame, command=self.reset_data, text="Reset", width=7, font=("verdana", 12, "bold"),
                           fg="white", bg="#003151")
        reset_btn.grid(row=0, column=3, padx=5, pady=10, sticky=W)
        # take photo button
        take_photo_btn = Button(btn_frame, command=self.generate_dataset, text="Take Pic", width=9,
                                font=("verdana", 12, "bold"), fg="white", bg="#003151")
        take_photo_btn.grid(row=0, column=4, padx=5, pady=10, sticky=W)
        # update photo button
        update_photo_btn = Button(btn_frame, command=self.update_photo, text="Update Pic", width=9,
                                  font=("verdana", 12, "bold"), fg="white", bg="#003151")
        update_photo_btn.grid(row=0, column=5, padx=5, pady=10, sticky=W)

        # ----------------------------------------------------------------------
        # Right Label Frame
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details",
                                 font=("verdana", 12, "bold"), fg="#003151")
        right_frame.place(x=680, y=10, width=660, height=480)
        # Search System in Right Label Frame
        search_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE, text="Search System",
                                  font=("verdana", 12, "bold"), fg="#003151")
        search_frame.place(x=10, y=5, width=635, height=80)
        # Phone Number
        search_label = Label(search_frame, text="Search:", font=("verdana", 12, "bold"), fg="#003151", bg="white")
        search_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        self.var_searchTX = StringVar()
        # combo box
        search_combo = ttk.Combobox(search_frame, textvariable=self.var_searchTX, width=12,
                                    font=("verdana", 12, "bold"), state="readonly")
        search_combo["values"] = ("Select", "Roll-No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=5, pady=15, sticky=W)

        self.var_search = StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=self.var_search, width=12, font=("verdana", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        search_btn = Button(search_frame, command=self.search_data, text="Search", width=9,
                            font=("verdana", 12, "bold"), fg="white", bg="#003151")
        search_btn.grid(row=0, column=3, padx=5, pady=10, sticky=W)

        showAll_btn = Button(search_frame, command=self.fetch_data, text="Show All", width=8,
                             font=("verdana", 12, "bold"), fg="white", bg="#003151")
        showAll_btn.grid(row=0, column=4, padx=5, pady=10, sticky=W)

        # -----------------------------Table Frame-------------------------------------------------
        # Table Frame
        # Search System in Right Label Frame
        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=10, y=90, width=635, height=360)
        # scroll bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        # create table
        self.student_table = ttk.Treeview(table_frame, column=(
        "ID", "Name", "Dep", "Course", "Year", "Sem", "Div", "Gender", "DOB", "Mob-No", "Address", "Roll-No", "Email",
        "Teacher", "Photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("ID", text="StudentID")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Dep", text="Department")
        self.student_table.heading("Course", text="Course")
        self.student_table.heading("Year", text="Year")
        self.student_table.heading("Sem", text="Semester")
        self.student_table.heading("Div", text="Division")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("DOB", text="DOB")
        self.student_table.heading("Mob-No", text="Mob-No")
        self.student_table.heading("Address", text="Address")
        self.student_table.heading("Roll-No", text="Roll-No")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Teacher", text="Teacher")
        self.student_table.heading("Photo", text="PhotoSample")
        self.student_table["show"] = "headings"

        # Set Width of Colums
        self.student_table.column("ID", width=100)
        self.student_table.column("Name", width=100)
        self.student_table.column("Dep", width=100)
        self.student_table.column("Course", width=100)
        self.student_table.column("Year", width=100)
        self.student_table.column("Sem", width=100)
        self.student_table.column("Div", width=100)
        self.student_table.column("Gender", width=100)
        self.student_table.column("DOB", width=100)
        self.student_table.column("Mob-No", width=100)
        self.student_table.column("Address", width=100)
        self.student_table.column("Roll-No", width=100)
        self.student_table.column("Email", width=100)
        self.student_table.column("Teacher", width=100)
        self.student_table.column("Photo", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # ==================Function Decleration==============================
    def validate_name(self, value):
        if re.match("^[A-Za-z ]*$", value):
            return True
        else:
            return False

    def add_data(self):
        # Check if any of the required fields are empty
        if (self.var_dep.get() == "Select Department" or
                self.var_course.get() == "Select Course" or
                self.var_year.get() == "Select Year" or
                self.var_semester.get() == "Select Semester" or
                self.var_std_name.get() == "" or
                self.var_div.get() == "" or
                self.var_roll.get() == "" or
                self.var_gender.get() == "" or
                self.var_dob.get() == "" or
                self.var_email.get() == "" or
                self.var_mob.get() == "" or
                self.var_address.get() == "" or
                self.var_teacher.get() == ""):

            messagebox.showerror("Error", "Please Fill All Fields are Required!", parent=self.root)
        else:
            # Validate student's name (only alphabetic characters and spaces allowed)
            if not re.match("^[A-Za-z ]+$", self.var_std_name.get()):
                messagebox.showerror("Error", "Invalid Student Name! Name should only contain alphabets and spaces.",
                                     parent=self.root)
                return
            if not re.match("^[A-Za-z ]+$", self.var_teacher.get()):
                messagebox.showerror("Error", "Invalid Teacher Name! Name should only contain alphabets and spaces.",
                                     parent=self.root)
                return
            # Validate mobile number (must be exactly 11 digits)
            if not re.match("^\d{11}$", self.var_mob.get()):
                messagebox.showerror("Error", "Invalid Mobile Number! It should be exactly 11 digits.",
                                     parent=self.root)
                return
            # Validate email address (standard email format)
            if not re.match(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", self.var_email.get()):
                messagebox.showerror("Error", "Invalid Email Address! Please enter a valid email.", parent=self.root)
                return
            try:
                # Connect to the database
                conn = mysql.connector.connect(user='root', password='@omama1234', host='localhost',
                                               database='face_recognition', port=3307)
                mycursor = conn.cursor()
                # Check for duplicate roll number
                mycursor.execute("SELECT * FROM student WHERE Roll_No = %s", (self.var_roll.get(),))
                row = mycursor.fetchone()
                if row:
                    messagebox.showerror("Error", "Roll Number already exists!", parent=self.root)
                    conn.close()
                    return
                # Insert data into the student table
                mycursor.execute("""
                    INSERT INTO student (Name, Department, Course, Year, Semester, Division, Gender, DOB, Mobile_No, Address, Roll_No, Email, Teacher_Name, PhotoSample)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (
                    self.var_std_name.get(),
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_div.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_mob.get(),
                    self.var_address.get(),
                    self.var_roll.get(),
                    self.var_email.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()  # Assuming var_radio1 corresponds to PhotoSample
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "All Records are Saved!", parent=self.root)
            except Exception as es:
                # Show error message if any exception occurs
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    # ===========================Fetch data form database to table ================================

    def fetch_data(self):
        conn = mysql.connector.connect(user='root', password='@omama1234', host='localhost',
                                       database='face_recognition', port=3307)
        mycursor = conn.cursor()
        mycursor.execute("select * from student")
        data = mycursor.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # ================================get cursor function=======================

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_std_id.set(data[0]),
        self.var_std_name.set(data[1]),
        self.var_dep.set(data[2]),
        self.var_course.set(data[3]),
        self.var_year.set(data[4]),
        self.var_semester.set(data[5]),
        self.var_div.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_mob.set(data[9]),
        self.var_address.set(data[10]),
        self.var_roll.set(data[11]),
        self.var_email.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    # ========================================Update Function==========================
    def update_data(self):
        if (self.var_dep.get() == "Select Department" or
                self.var_course.get() == "Select Course" or
                self.var_year.get() == "Select Year" or
                self.var_semester.get() == "Select Semester" or
                self.var_std_id.get() == "" or
                self.var_std_name.get() == "" or
                self.var_div.get() == "" or
                self.var_roll.get() == "" or
                self.var_gender.get() == "" or
                self.var_dob.get() == "" or
                self.var_email.get() == "" or
                self.var_mob.get() == "" or
                self.var_address.get() == "" or
                self.var_teacher.get() == ""):

            messagebox.showerror("Error", "Please Fill All Fields are Required!", parent=self.root)
        else:
            # Validate student's name (only alphabetic characters and spaces allowed)
            if not re.match("^[A-Za-z ]+$", self.var_std_name.get()):
                messagebox.showerror("Error", "Invalid Student Name! Name should only contain alphabets and spaces.",
                                     parent=self.root)
                return
            if not re.match("^[A-Za-z ]+$", self.var_teacher.get()):
                messagebox.showerror("Error", "Invalid Teacher Name! Name should only contain alphabets and spaces.",
                                     parent=self.root)
                return
            # Validate mobile number (must be exactly 11 digits)
            if not re.match("^\d{11}$", self.var_mob.get()):
                messagebox.showerror("Error", "Invalid Mobile Number! It should be exactly 11 digits.",
                                     parent=self.root)
                return
            # Validate email address (standard email format)
            if not re.match(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", self.var_email.get()):
                messagebox.showerror("Error", "Invalid Email Address! Please enter a valid email.", parent=self.root)
                return
            try:
                Update = messagebox.askyesno("Update", "Do you want to Update this Student Details!", parent=self.root)
                if Update:
                    conn = mysql.connector.connect(user='root', password='@omama1234', host='localhost',
                                                   database='face_recognition', port=3307)
                    mycursor = conn.cursor()
                    # Check for duplicate roll number (excluding the current student being updated)
                    mycursor.execute("SELECT * FROM student WHERE Roll_No = %s AND Student_ID != %s",
                                     (self.var_roll.get(), self.var_std_id.get()))
                    row = mycursor.fetchone()
                    if row:
                        messagebox.showerror("Error", "Roll Number already exists!", parent=self.root)
                        conn.close()
                        return
                    # Update student details
                    mycursor.execute("""
                        UPDATE student 
                        SET Name=%s, Department=%s, Course=%s, Year=%s, Semester=%s, Division=%s, Gender=%s, DOB=%s, Mobile_No=%s, Address=%s, Roll_No=%s, Email=%s, Teacher_Name=%s, PhotoSample=%s 
                        WHERE Student_ID=%s
                    """, (
                        self.var_std_name.get(),
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_div.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_mob.get(),
                        self.var_address.get(),
                        self.var_roll.get(),
                        self.var_email.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                    ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "Successfully Updated!", parent=self.root)
                else:
                    return
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    # ==============================Delete Function=========================================
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student Id Must be Required!", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Do you want to Delete?", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(user='root', password='@omama1234', host='localhost',
                                                   database='face_recognition', port=3307)
                    mycursor = conn.cursor()

                    # Fetch the student name to construct the file path
                    mycursor.execute("SELECT Name FROM student WHERE Student_ID=%s", (self.var_std_id.get(),))
                    result = mycursor.fetchone()
                    if result:
                        student_name = result[0]
                    else:
                        student_name = ""
                        # Delete the database record
                    sql = "DELETE FROM student WHERE Student_ID=%s"
                    val = (self.var_std_id.get(),)
                    mycursor.execute(sql, val)
                    # Construct the file path for the images
                    file_pattern = f"data_img/student.{self.var_std_id.get()}.*.jpg"
                    # Delete images associated with the student
                    import os
                    import glob
                    for file_path in glob.glob(file_pattern):
                        os.remove(file_path)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Delete", f"Successfully Deleted {student_name}'s record!", parent=self.root)
                else:
                    if not delete:
                        return
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    # Reset Function
    def reset_data(self):
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_div.set("Morning"),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_mob.set(""),
        self.var_address.set(""),
        self.var_roll.set(""),
        self.var_email.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")

    # ===========================Search Data===================
    def search_data(self):
        if self.var_search.get() == "" or self.var_searchTX.get() == "Select":
            messagebox.showerror("Error", "Select Combo option and enter entry box", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(user='root', password='@omama1234', host='localhost',
                                               database='face_recognition', port=3307)
                my_cursor = conn.cursor()
                sql = "SELECT Student_ID,Name,Department,Course,Year,Semester,Division,Gender,DOB,Mobile_No,Address,Roll_No,Email,Teacher_Name,PhotoSample FROM student where Roll_No='" + str(
                    self.var_search.get()) + "'"
                my_cursor.execute(sql)
                # my_cursor.execute("select * from student where Roll_No= " +str(self.var_search.get())+" "+str(self.var_searchTX.get())+"")
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("", END, values=i)
                    if rows == None:
                        messagebox.showerror("Error", "Data Not Found", parent=self.root)
                        conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

    # =====================This part is related to Opencv Camera part=======================
    # ==================================Generate Data set take image=========================

    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_course.get == "Select Course" or self.var_year.get() == "Select Year" or self.var_semester.get() == "Select Semester" or self.var_std_id.get() == "" or self.var_std_name.get() == "" or self.var_div.get() == "" or self.var_roll.get() == "" or self.var_gender.get() == "" or self.var_dob.get() == "" or self.var_email.get() == "" or self.var_mob.get() == "" or self.var_address.get() == "" or self.var_teacher.get() == "":
            messagebox.showerror("Error", "Please Fill All Fields are Required!", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='@omama1234', host='localhost',
                                               database='face_recognition', port=3307)
                mycursor = conn.cursor()
                mycursor.execute("select * from student")
                myreslut = mycursor.fetchall()
                id = self.var_std_id.get()
                # for x in myreslut:
                ##    id+=1
                mycursor.execute(
                    "update student set Name=%s,Department=%s,Course=%s,Year=%s,Semester=%s,Division=%s,Gender=%s,DOB=%s,Mobile_No=%s,Address=%s,Roll_No=%s,Email=%s,Teacher_Name=%s,PhotoSample=%s where Student_ID=%s",
                    (
                        self.var_std_name.get(),
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_div.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_mob.get(),
                        self.var_address.get(),
                        self.var_roll.get(),
                        self.var_email.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ====================part of opencv=======================
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_croped(img):
                    # conver gary sacle
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    # Scaling factor 1.3
                    # Minimum naber 5
                    for (x, y, w, h) in faces:
                        face_croped = img[y:y + h, x:x + w]
                        return face_croped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_croped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_croped(my_frame), (200, 200))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_path = "data_img/stdudent." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Capture Images", face)
                    if cv2.waitKey(1) == 13 or int(img_id) == 150:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating dataset completed!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

                #######################################################

    # ===================== Update Dateset image ================
    def update_photo(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student ID is required!", parent=self.root)
        else:
            try:
                # Delete existing photos
                import os
                dir_path = "data_img"
                for file in os.listdir(dir_path):
                    if file.startswith("stdudent." + str(self.var_std_id.get()) + "."):
                        os.remove(os.path.join(dir_path, file))
                # Capture new photos
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_croped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        face_croped = img[y:y + h, x:x + w]
                        return face_croped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_croped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_croped(my_frame), (200, 200))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_path = "data_img/stdudent." + str(self.var_std_id.get()) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Capture Images", face)
                    if cv2.waitKey(1) == 13 or int(img_id) == 150:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Updating photos completed!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


if _name_ == "_main_":
    root = tkinter.Tk()
    obj = Student(root)
 root.mainloop()