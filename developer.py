from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os

class Developer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x750+0+0")
        self.root.title("Face Recognition System")


        help=Label(self.root,text="DEVELOPER",font=("times new roman",30,"bold"),bg="white",fg="darkgreen")
        help.place(x=0,y=0,width=1380,height=40)

        img4=Image.open(r"Project_photos/dev.jpg")
        img4=img4.resize((1350,750),Image.LANCZOS)
        self.photo_img4=ImageTk.PhotoImage(img4)

        big_img=Label(self.root,image=self.photo_img4)
        big_img.place(x=0,y=50,width=1350,height=630)
        
        main_frame=Frame(big_img,bd=2,bg="white")
        main_frame.place(x=900,y=0,width=500,height=500)

        top=Image.open(r"Project_photos/developer.jpeg")
        top=top.resize((200,200),Image.LANCZOS)
        self.photo_top=ImageTk.PhotoImage(top)

        big_img=Label(main_frame,image=self.photo_top)
        big_img.place(x=250,y=20,width=200,height=200)

       


        title_lbl=Label(main_frame,text="Hellow!,Welcome to DigiDev Developers!",font=("times new roman",13,"bold"),bg="white",fg="blue")
        title_lbl.place(x=50,y=0,height=20)

        lower=Image.open(r"Project_photos/d.jpg")
        lower=lower.resize((455,400),Image.LANCZOS)
        self.photo_lower=ImageTk.PhotoImage(lower)

        big_img=Label(main_frame,image=self.photo_lower)
        big_img.place(x=0,y=220,width=500,height=300)



        

      

        






if __name__ == "__main__":
          root =Tk()
          obj=Developer(root)
          root.mainloop()


        
