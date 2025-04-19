from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x750+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",30,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1400,height=40)

        image_left=Image.open(r"Project_photos/face.jpeg")
        image_left=image_left.resize((400,100),Image.LANCZOS)
        self.photo_image_left=ImageTk.PhotoImage(image_left)

        f_lbl=Label(self.root,image=self.photo_image_left)
        f_lbl.place(x=0,y=40,width=420,height=100)

        image_left1=Image.open(r"Project_photos/face.jpeg")
        image_left1=image_left.resize((400,100),Image.LANCZOS)
        self.photo_image_left1=ImageTk.PhotoImage(image_left1)

        f_lbl=Label(self.root,image=self.photo_image_left1)
        f_lbl.place(x=400,y=40,width=420,height=100)

        image_left2=Image.open(r"Project_photos/face.jpeg")
        image_left2=image_left2.resize((400,100),Image.LANCZOS)
        self.photo_image_left2=ImageTk.PhotoImage(image_left2)

        f_lbl=Label(self.root,image=self.photo_image_left2)
        f_lbl.place(x=800,y=40,width=420,height=100)
        

        img2=Image.open(r"Project_photos/face.jpeg")
        img2=img2.resize((400,100),Image.LANCZOS)
        self.photo_img2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photo_img2)
        f_lbl.place(x=1200,y=40,width=150,height=100)

        b1=Button(self.root,text="TRAIN DATA ",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="darkblue",fg="darkgreen")
        b1.place(x=0,y=140,width=1400,height=40)

        img4=Image.open(r"Project_photos/background.jpeg")
        img4=img4.resize((1350,750),Image.LANCZOS)
        self.photo_img4=ImageTk.PhotoImage(img4)

        big_img=Label(self.root,image=self.photo_img4)
        big_img.place(x=0,y=175,width=1350,height=510)

   
    
    def train_classifier(self):
        data_dir = "data"
        paths = [os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.endswith('.jpg')]

        faces = []
        ids = []
        
        for path in paths:
            try:
                # Convert to grayscale
                img = Image.open(path).convert('L')  # Fixed: added 'L' for grayscale conversion
                img_np = np.array(img, 'uint8')
                
                # Extract ID from filename (format: user.id.number.jpg)
                id = int(os.path.split(path)[1].split('.')[1])
                
                faces.append(img_np)
                ids.append(id)
                
                # Show training progress
                cv2.imshow("Training", img_np)
                if cv2.waitKey(1) == 27:  # Press ESC to exit
                    break
                    
            except Exception as e:
                print(f"Error processing {path}: {str(e)}")

        ids = np.array(ids)
        
        # Train and save classifier
        try:
            recognizer = cv2.face.LBPHFaceRecognizer_create()
            recognizer.train(faces, ids)
            recognizer.write("classifier.xml")
            messagebox.showinfo("Success", "Training completed successfully!")
            
        except Exception as e:
            messagebox.showerror("Error", f"Training failed: {str(e)}")
            
        finally:
            cv2.destroyAllWindows()



               
if __name__ == "__main__":
          root =Tk()
          obj=Train(root)
          root.mainloop()



