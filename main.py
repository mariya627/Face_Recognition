from tkinter import *
from tkinter import ttk
import tkinter
from tkinter import messagebox
# from login import Login
from train import Train
from PIL import Image, ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
import os


class Face_Recognition_System:
    def _init_(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face_Recogonition_System")
        # Get screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # This part is image labels setting start
        # backgorund image
        bg1 = Image.open(r"C:\Users\PMLS\Downloads\ff.jpg")
        bg1 = bg1.resize((screen_width, screen_height), Image.ANTIALIAS)
        self.photobg1 = ImageTk.PhotoImage(bg1)
        # set image as lable
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=0, width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight())
        # title section
        # Create a canvas
        canvas = Canvas(self.root, width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight())
        canvas.pack(fill="both", expand=True)
        # Set image as canvas background
        canvas.create_image(0, 0, image=self.photobg1, anchor="nw")
        # Add text on canvas
        canvas.create_text(self.root.winfo_screenwidth() // 2, 40,
                           text="Attendance Management System Using Facial Recognition", font=("Algerian", 30, "bold"),
                           fill="white")

        # Create buttons
        # -------------------------------------------------------------------------------------------------------------------
        # student button 1
        std_img_btn = Image.open(r"C:\Users\PMLS\Downloads\std.png")
        std_img_btn = std_img_btn.resize((60, 60), Image.ANTIALIAS)
        self.std_img1 = ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(self.root, command=self.student_pannels, image=self.std_img1, cursor="hand2")
        canvas.create_window(150, 200, window=std_b1, width=60, height=60)

        std_b1_1 = Button(self.root, command=self.student_pannels, text="STUDENT PANEL", cursor="hand2",
                          font=("tahoma", 15, "bold"), bg="white", fg="#003151")
        canvas.create_window(300, 200, window=std_b1_1, width=200, height=45)

        # Detect Face  button 2
        det_img_btn = Image.open(r"C:\Users\PMLS\Downloads\det1.png")
        det_img_btn = det_img_btn.resize((60, 60), Image.ANTIALIAS)
        self.det_img1 = ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(self.root, command=self.face_rec, image=self.det_img1, cursor="hand2")
        canvas.create_window(200, 280, window=det_b1, width=60, height=60)

        det_b1_1 = Button(self.root, command=self.face_rec, text="FACE DETECTOR", cursor="hand2",
                          font=("tahoma", 15, "bold"), bg="white", fg="#003151")
        canvas.create_window(350, 280, window=det_b1_1, width=200, height=45)

        # Attendance System button 3
        att_img_btn = Image.open(r"C:\Users\PMLS\Downloads\att.png")
        att_img_btn = att_img_btn.resize((60, 60), Image.ANTIALIAS)
        self.att_img1 = ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(self.root, command=self.attendance_pannel, image=self.att_img1, cursor="hand2")
        canvas.create_window(270, 360, window=att_b1, width=60, height=60)

        att_b1_1 = Button(self.root, command=self.attendance_pannel, text="ATTENDANCE", cursor="hand2",
                          font=("tahoma", 15, "bold"), bg="white", fg="#003151")
        canvas.create_window(420, 360, window=att_b1_1, width=200, height=45)

        # Train button 4
        tra_img_btn = Image.open(r"C:\Users\PMLS\Downloads\train2-removebg-preview.png")
        tra_img_btn = tra_img_btn.resize((60, 60), Image.ANTIALIAS)
        self.tra_img1 = ImageTk.PhotoImage(tra_img_btn)

        tra_b1 = Button(self.root, command=self.train_pannels, image=self.tra_img1, cursor="hand2")
        canvas.create_window(270, 440, window=tra_b1, width=60, height=60)

        tra_b1_1 = Button(self.root, command=self.train_pannels, text="TRAIN DATA", cursor="hand2",
                          font=("tahoma", 15, "bold"), bg="white", fg="#003151")
        canvas.create_window(420, 440, window=tra_b1_1, width=200, height=45)

        # Data button 5
        exi_img_btn = Image.open(r"C:\Users\PMLS\Downloads\dta1.png")
        exi_img_btn = exi_img_btn.resize((60, 60), Image.ANTIALIAS)
        self.exi_img1 = ImageTk.PhotoImage(exi_img_btn)

        exi_b1 = Button(self.root, command=self.Data, image=self.exi_img1, cursor="hand2")
        canvas.create_window(200, 520, window=exi_b1, width=60, height=60)

        exi_b1_1 = Button(self.root, command=self.Data, text="IMAGES DATA", cursor="hand2", font=("tahoma", 15, "bold"),
                          bg="white", fg="#003151")
        canvas.create_window(350, 520, window=exi_b1_1, width=200, height=45)

        # Logout button 6
        exi_img_btn1 = Image.open(r"C:\Users\PMLS\Downloads\lo.png")
        exi_img_btn1 = exi_img_btn1.resize((60, 60), Image.ANTIALIAS)
        self.exi_img2 = ImageTk.PhotoImage(exi_img_btn1)

        exi_b1 = Button(self.root, command=self.Close, image=self.exi_img2, cursor="hand2")
        canvas.create_window(150, 600, window=exi_b1, width=60, height=60)

        exi_b1_1 = Button(self.root, command=self.Close, text="LOG OUT", cursor="hand2", font=("tahoma", 15, "bold"),
                          bg="white", fg="#003151")
        canvas.create_window(300, 600, window=exi_b1_1, width=200, height=45)

    # ==================Funtion to Open Images Folder==================
    def open_img(self):
        os.startfile("dataset")

    # ==================Functions Buttons=====================

    def student_pannels(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_pannels(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_rec(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)
        # self.root.destroy()

    def attendance_pannel(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def Data(self):
        os.startfile("data_img")

    def Close(self):
        self.root.destroy()


if _name_ == "_main_":
    root = tkinter.Tk()
    obj = Face_Recognition_System(root)
 root.mainloop()
