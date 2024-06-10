from sys import path
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
import cv2
import numpy as np
from tkinter import messagebox


class Train:

    def _init_(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Train Pannel")
        # backgorund image
        bg1 = Image.open(r"C:\Users\PMLS\Downloads\bb.webp")
        bg1 = bg1.resize((1366, 768), Image.ANTIALIAS)
        self.photobg1 = ImageTk.PhotoImage(bg1)
        # set image as lable
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=130, width=1366, height=768)
        # title section
        # Create a canvas
        canvas = Canvas(self.root, width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight())
        canvas.pack(fill="both", expand=True)
        # Set image as canvas background
        canvas.create_image(0, 0, image=self.photobg1, anchor="nw")
        # Add text on canvas
        canvas.create_text(self.root.winfo_screenwidth() // 2, 40, text="FACE RECOGNITION PANEL",
                           font=("Algerian", 30, "bold"), fill="white")
        # Create buttons below
        # -------------------------------------------------------------------------------------------------------------------
        # Training button 1
        std_img_btn = Image.open(r"C:\Users\PMLS\OneDrive\Documents\AI_Project\Images_GUI\t_btn1.png")
        std_img_btn = std_img_btn.resize((180, 180), Image.ANTIALIAS)
        self.std_img1 = ImageTk.PhotoImage(std_img_btn)
        std_b1 = Button(self.root, command=self.train_classifier, image=self.std_img1, cursor="hand2")
        canvas.create_window(650, 290, window=std_b1, width=180, height=180)
        std_b1_1 = Button(self.root, command=self.train_classifier, text="TRAIN DATASET", cursor="hand2",
                          font=("tahoma", 15, "bold"), bg="white", fg="#003151")
        canvas.create_window(650, 390, window=std_b1_1, width=180, height=45)

    # ==================Create Function of Training===================

    def train_classifier(self):
        data_dir = ("data_img")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        faces = []
        ids = []
        for image in path:
            img = Image.open(image).convert('L')  # converts in gray scale
            imageNp = np.array(img, 'uint8')  # Converts the grayscale image to a numpy array of type uint8.
            id = int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)

        # =================Train Classifier=============
        clf = cv2.face.LBPHFaceRecognizer_create()  # Local Binary Patterns Histograms
        clf.train(faces, ids)
        clf.write("clf.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Dataset Completed!", parent=self.root)


if _name_ == "_main_":
    root = Tk()
    obj = Train(root)
 root.mainloop()