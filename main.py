
from tkinter import*
from tkinter import ttk
import tkinter.messagebox
from PIL import Image,ImageTk
import tkinter
import os
import sys
import subprocess
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help

class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x750+0+0")
        self.root.title("Face Recognition System")

#first image
        img1=Image.open(r"Project_photos/background.jpeg")
        img1=img1.resize((400,100),Image.LANCZOS)
        self.photo_img1=ImageTk.PhotoImage(img1)
                                         

        f_lbl=Label(self.root,image=self.photo_img1)
        f_lbl.place(x=0,y=0,width=420,height=100)


 #Second image
        img2=Image.open(r"Project_photos/att.jpg")
        img2=img2.resize((400,100),Image.LANCZOS)
        self.photo_img2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photo_img2)
        f_lbl.place(x=400,y=0,width=420,height=100)
        



#Third image
        img3=Image.open(r"Project_photos/library.jpeg")
        img3=img3.resize((400,100),Image.LANCZOS)
        self.photo_img3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photo_img3)
        f_lbl.place(x=800,y=0,width=420,height=100)


        img16=Image.open(r"Project_photos/help.jpeg")
        img16=img16.resize((400,100),Image.LANCZOS)
        self.photo_img16=ImageTk.PhotoImage(img16)

        f_lbl=Label(self.root,image=self.photo_img16)
        f_lbl.place(x=1200,y=0,width=150,height=100)
        


#big image
        img4=Image.open(r"Project_photos/background.jpeg")
        img4=img4.resize((1350,750),Image.LANCZOS)
        self.photo_img4=ImageTk.PhotoImage(img4)

        big_img=Label(self.root,image=self.photo_img4)
        big_img.place(x=0,y=130,width=1350,height=600)
    
        title_lbl=Label(big_img,text="DIGITECH UNIVERSITY OF SCIENCE AND TECHNOLOGY",font=("times new roman",30,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=10,width=1400,height=55)

   

#Student button
        img5=Image.open(r"Project_photos/help.jpeg")
        img5=img5.resize((220,220),Image.LANCZOS)
        self.photo_img5=ImageTk.PhotoImage(img5)

        b1=Button(big_img,image=self.photo_img5,command=self.student_details,cursor="hand2")
        b1.place(x=5,y=100,width=300,height=220)


        b1=Button(big_img,text="Student Details",cursor="hand2",command=self.student_details,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=5,y=300,width=300,height=40)

#Face detector Button
        img6=Image.open(r"Project_photos/face.jpeg")
        img6=img6.resize((220,220),Image.LANCZOS)
        self.photo_img6=ImageTk.PhotoImage(img6)

        b1=Button(big_img,image=self.photo_img6,cursor="hand2",command=self.face_data)
        b1.place(x=240,y=100,width=300,height=220)


        b1=Button(big_img,text="Face Recognition",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=240,y=300,width=300,height=40)


#Face Attendance Button
        img7=Image.open(r"Project_photos/att.jpg")
        img7=img7.resize((220,220),Image.LANCZOS)
        self.photo_img7=ImageTk.PhotoImage(img7)

        b1=Button(big_img,image=self.photo_img7,cursor="hand2",command=self.attendance_data)
        b1.place(x=460,y=100,width=300,height=200)


        b1=Button(big_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=460,y=300,width=300,height=40)
#Train Button
        img9=Image.open(r"Project_photos/train.jpeg")
        img9=img9.resize((220,220),Image.LANCZOS)
        self.photo_img9=ImageTk.PhotoImage(img9)

        b1=Button(big_img,image=self.photo_img9,cursor="hand2",command=self.train_data)
        b1.place(x=725,y=100,width=300,height=220)


        b1=Button(big_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=725,y=300,width=300,height=40)
#Help option
        img10=Image.open(r"Project_photos/hel.jpeg")
        img10=img10.resize((220,220),Image.LANCZOS)
        self.photo_img10=ImageTk.PhotoImage(img10)

        b1=Button(big_img,image=self.photo_img10,cursor="hand2",command=self.help_data)
        b1.place(x=200,y=340,width=300,height=200)


        b1=Button(big_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=200,y=520,width=300,height=40)
#Developer option
        img12=Image.open(r"Project_photos/dev.jpg")
        img12=img12.resize((220,220),Image.LANCZOS)
        self.photo_img12=ImageTk.PhotoImage(img12)

        b1=Button(big_img,image=self.photo_img12,cursor="hand2",command=self.developer_data)
        b1.place(x=500,y=340,width=300,height=220)


        b1=Button(big_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=500,y=520,width=300,height=40)

#Photo Option
        img13=Image.open(r"Project_photos/photos.jpeg")
        img13=img13.resize((220,220),Image.LANCZOS)
        self.photo_img13=ImageTk.PhotoImage(img13)

        b1=Button(big_img,image=self.photo_img13,cursor="hand2",command=self.open_img)
        b1.place(x=1040,y=100,width=300,height=220)


        b1=Button(big_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=1040,y=300,width=300,height=40)
         #Exit Option
        img14=Image.open(r"Project_photos/exit.jpeg")
        img14=img14.resize((220,220),Image.LANCZOS)
        self.photo_img14=ImageTk.PhotoImage(img14)

        b1=Button(big_img,image=self.photo_img14,cursor="hand2",command=self.iExit)
        b1.place(x=800,y=340,width=300,height=220)


        b1=Button(big_img,text="EXIT",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=800,y=520,width=300,height=40)

    def open_img(self):
      try:
        # Get absolute path to data folder
        script_dir = os.path.dirname(os.path.abspath(__file__))
        data_path = os.path.join(script_dir, "data")
        
        # Debugging: Show path in console
        print(f"Attempting to open: {data_path}")
        
        # Create folder if it doesn't exist
        if not os.path.exists(data_path):
            os.makedirs(data_path)
            print(f"Created missing directory: {data_path}")

        # Cross-platform opening
        if sys.platform == "win32":
            os.startfile(data_path)
        elif sys.platform == "darwin":
            subprocess.run(["open", data_path], check=True)
        else:  # Linux variants
            subprocess.run(["xdg-open", data_path], check=True)
            
      except Exception as e:
        print(f"Error opening directory: {str(e)}")
        # Consider showing error to user in GUI


            #====Exit option====
    def iExit(self):
          self.iExit=tkinter.messagebox.askyesno("Face Recognition System","Are you sure you want to logout?",parent=self.root)
          if self.iExit >0:
                self.root.destroy()
          else:
                return
              
        #=======functionbuttons=====
    def student_details(self):
             self.new_window=Toplevel(self.root)
             self.app=Student(self.new_window)



    def train_data(self):
             self.new_window=Toplevel(self.root)
             self.app=Train(self.new_window)


    def face_data(self):
          self.new_window=Toplevel(self.root)
          self.app=Face_Recognition(self.new_window)


    def attendance_data(self):
          self.new_window=Toplevel(self.root)
          self.app=Attendance(self.new_window)       
         


    def developer_data(self):
               self.new_window=Toplevel(self.root)
               self.app=Developer(self.new_window)      

    def help_data(self):
               self.new_window=Toplevel(self.root)
               self.app=Help(self.new_window)       
          
         
         
if __name__ == "__main__":
          root =Tk()
          obj=Face_Recognition_System(root)
          root.mainloop()


