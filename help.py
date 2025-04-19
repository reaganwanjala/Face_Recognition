from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os

class Help:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x750+0+0")
        self.root.title("Face Recognition System")

        help=Label(self.root,text="HELP DESK",font=("times new roman",30,"bold"),bg="white",fg="darkgreen")
        help.place(x=0,y=0,width=1380,height=40)

        img4=Image.open(r"Project_photos/dev.jpg")
        img4=img4.resize((1350,750),Image.LANCZOS)
        self.photo_img4=ImageTk.PhotoImage(img4)

        big_img=Label(self.root,image=self.photo_img4)
        big_img.place(x=0,y=50,width=1350,height=630)

       

        help=Label(big_img,text="CONTACT US ON:Digitech@helpsupportgmail.com",font=("times new roman",20,"bold"),bg="white",fg="blue")
        help.place(x=320,y=250)

        



if __name__ == "__main__":
          root =Tk()
          obj=Help(root)
          root.mainloop()

