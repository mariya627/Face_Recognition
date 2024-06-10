from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from re import match


class Register:
    def _init_(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1366x768+0+0")

        # ============ Variables =================
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_cnum = StringVar()
        self.var_email = StringVar()
        self.var_ssq = StringVar()
        self.var_sa = StringVar()
        self.var_pwd = StringVar()
        self.var_cpwd = StringVar()
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\PMLS\Downloads\bb.webp")
        lb1_bg = Label(self.root, image=self.bg)
        lb1_bg.place(x=0, y=0, relwidth=1, relheight=1)
        frame = Frame(self.root, bg="#F2F2F2")
        frame.place(x=180, y=60, width=900, height=580)

        get_str = Label(frame, text="Registration", font=("Algerian", 30, "bold"), fg="#003151", bg="#F2F2F2")
        get_str.place(x=300, y=80)
        # label1
        fname = lb1 = Label(frame, text="First Name:", font=("times new roman", 15, "bold"), fg="#003151", bg="#F2F2F2")
        fname.place(x=100, y=200)
        # entry1
        self.txtuser = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=103, y=225, width=270)
        # label2
        lname = lb1 = Label(frame, text="Last Name:", font=("times new roman", 15, "bold"), fg="#003151", bg="#F2F2F2")
        lname.place(x=100, y=270)
        # entry2
        self.txtpwd = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15, "bold"))
        self.txtpwd.place(x=103, y=295, width=270)

        # ==================== section 2 -------- 2nd Columan===================
        # label1
        cnum = lb1 = Label(frame, text="Contact No:", font=("times new roman", 15, "bold"), fg="#003151", bg="#F2F2F2")
        cnum.place(x=530, y=200)
        # entry1
        self.txtuser = ttk.Entry(frame, textvariable=self.var_cnum, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=533, y=225, width=270)
        # label2
        email = lb1 = Label(frame, text="Email:", font=("times new roman", 15, "bold"), fg="#003151", bg="#F2F2F2")
        email.place(x=530, y=270)
        # entry2
        self.txtpwd = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15, "bold"))
        self.txtpwd.place(x=533, y=295, width=270)

        # ========================= Section 3 --- 1 Columan=================
        # label1
        ssq = lb1 = Label(frame, text="Select Security Question:", font=("times new roman", 15, "bold"), fg="#003151",
                          bg="#F2F2F2")
        ssq.place(x=100, y=350)
        # Combo Box1
        self.combo_security = ttk.Combobox(frame, textvariable=self.var_ssq, font=("times new roman", 15, "bold"),
                                           state="readonly")
        self.combo_security["values"] = ("Select", "Your Date of Birth", "Your Nick Name", "Your Favorite Book")
        self.combo_security.current(0)
        self.combo_security.place(x=103, y=375, width=270)
        # label2
        sa = lb1 = Label(frame, text="Security Answer:", font=("times new roman", 15, "bold"), fg="#003151",
                         bg="#F2F2F2")
        sa.place(x=100, y=420)
        # entry2
        self.txtpwd = ttk.Entry(frame, textvariable=self.var_sa, font=("times new roman", 15, "bold"))
        self.txtpwd.place(x=103, y=445, width=270)

        # ========================= Section 4-----Column 2=============================
        # label1
        pwd = lb1 = Label(frame, text="Password:", font=("times new roman", 15, "bold"), fg="#003151", bg="#F2F2F2")
        pwd.place(x=530, y=350)
        # entry1
        self.txtuser = ttk.Entry(frame, textvariable=self.var_pwd, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=533, y=375, width=270)
        # label2
        cpwd = lb1 = Label(frame, text="Confirm Password:", font=("times new roman", 15, "bold"), fg="#003151",
                           bg="#F2F2F2")
        cpwd.place(x=530, y=420)
        # entry2
        self.txtpwd = ttk.Entry(frame, textvariable=self.var_cpwd, font=("times new roman", 15, "bold"))
        self.txtpwd.place(x=533, y=445, width=270)
        # Creating Button Register
        loginbtn = Button(frame, command=self.reg, text="REGISTER", font=("times new roman", 15, "bold"), bd=0,
                          relief=RIDGE, fg="#fff", bg="#003151", activeforeground="white", activebackground="#007ACC")
        loginbtn.place(x=300, y=510, width=270, height=35)

    def reg(self):
        if (
                self.var_fname.get() == "" or self.var_lname.get() == "" or self.var_cnum.get() == "" or self.var_email.get() == "" or self.var_ssq.get() == "Select" or self.var_sa.get() == "" or self.var_pwd.get() == "" or self.var_cpwd.get() == ""):
            messagebox.showerror("Error", "All Field Required!")
        elif (self.var_pwd.get() != self.var_cpwd.get()):
            messagebox.showerror("Error", "Password & Confirm Password should be Same!")
        elif (not self.is_valid_string(self.var_fname.get()) or not self.is_valid_string(self.var_lname.get())):
            messagebox.showerror("Error", "First and Last Name should be a string!")
        elif (not self.is_valid_email(self.var_email.get())):
            messagebox.showerror("Error", "Invalid Email!")
        elif (not self.is_valid_phone(self.var_cnum.get())):
            messagebox.showerror("Error", "Invalid Phone Number!")
        else:
            try:
                conn = mysql.connector.connect(username='root', password='@omama1234', host='localhost',
                                               database='face_recognition', port=3307)
                mycursor = conn.cursor()
                query = ("select * from regteach where email=%s")
                value = (self.var_email.get(),)
                mycursor.execute(query, value)
                row = mycursor.fetchone()
                if row != None:
                    messagebox.showerror("Error", "User already exist,please try another email")
                else:
                    mycursor.execute("insert into regteach values(%s,%s,%s,%s,%s,%s,%s)", (
                        self.var_fname.get(),
                        self.var_lname.get(),
                        self.var_cnum.get(),
                        self.var_email.get(),
                        self.var_ssq.get(),
                        self.var_sa.get(),
                        self.var_pwd.get()
                    ))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "Successfully Registerd!", parent=self.root)
                    self.clear_input_fields()
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def is_valid_string(self, s):
        return s.isalpha()

    def is_valid_email(self, email):
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return bool(match(pattern, email))

    def is_valid_phone(self, phone):
        return len(phone) == 11 and phone.isdigit()

    def clear_input_fields(self):
        self.var_fname.set("")
        self.var_lname.set("")
        self.var_cnum.set("")
        self.var_email.set("")
        self.var_ssq.set("Select")
        self.var_sa.set("")
        self.var_pwd.set("")
        self.var_cpwd.set("")


if _name_ == "_main_":
    root = Tk()
    app = Register(root)
 root.mainloop()
