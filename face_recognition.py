from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import csv
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x750+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 30, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1400, height=40)
        
        image_left = Image.open(r"Project_photos/photos.jpeg")
        image_left = image_left.resize((650, 700), Image.LANCZOS)
        self.photo_image_left = ImageTk.PhotoImage(image_left)

        f_lbl = Label(self.root, image=self.photo_image_left)
        f_lbl.place(x=0, y=40, width=700, height=650)

        image_right = Image.open(r"Project_photos/R.jpg")
        image_right = image_right.resize((650, 700), Image.LANCZOS)
        self.photo_image_right = ImageTk.PhotoImage(image_right)

        f_lbl2 = Label(self.root, image=self.photo_image_right)
        f_lbl2.place(x=650, y=40, width=700, height=650)

        b1 = Button(f_lbl2, text="Face Recognition", cursor="hand2", 
                   command=self.face_recog, font=("times new roman", 18, "bold"), 
                   bg="darkblue", fg="white")
        b1.place(x=200, y=590, width=300, height=60)

    def mark_attendance(self, admission_number, name, department, course,unit):
        try:
            with open("attendance.csv", "a+", newline="") as f:
                f.seek(0)
                existing_data = f.readlines()
                
                today = datetime.now().strftime("%d/%m/%Y")
                already_marked = any(
                    admission_number in line and today in line 
                    for line in existing_data
                )
                
                if not already_marked:
                    now = datetime.now()
                    date_str = now.strftime("%d/%m/%Y")
                    time_str = now.strftime("%H:%M:%S")
                    
                    writer = csv.writer(f)
                    writer.writerow([
                        admission_number, 
                        name, 
                        department,
                        course,
                        unit,
                        time_str, 
                        date_str, 
                        "Present"
                    ])
                    return True
                return False
        except Exception as e:
            print(f"Error marking attendance: {e}")
            return False

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            face_detected = False
            
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 25, 255), 3)
                id, confidence = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = 100 - (confidence / 300) * 100
                
                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="Admin",
                        password="@730wanjala",
                        database="face_recognition_attendance"
                    )
                    cursor = conn.cursor()
                    
                    cursor.execute(
                        """SELECT admission_number, student_name, department, course_of_study,unit_of_study 
                        FROM students WHERE student_id=%s""",
                        (id,)
                    )
                    student_data = cursor.fetchone()
                    
                    if student_data and confidence > 77:
                        a, n, d, c,u = student_data
                        cv2.putText(img, f"Adm: {a}", (x, y-110), 
                                   cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                        cv2.putText(img, f"Name: {n}", (x, y-85), 
                                   cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                        cv2.putText(img, f"Dept: {d}", (x, y-60), 
                                   cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                        cv2.putText(img, f"Course: {c}", (x, y-35), 
                                   cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                        cv2.putText(img, f"unit: {u}", (x, y-10), 
                                   cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                        
                        if self.mark_attendance(a, n, d, c,u):
                            face_detected = True
                    else:
                        cv2.putText(img, "Unknown Face", (x, y-10), 
                                   cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                        
                except mysql.connector.Error as err:
                    print(f"Database error: {err}")
                finally:
                    if 'conn' in locals() and conn.is_connected():
                        conn.close()
            
            return img, face_detected

        def init_camera():
            for i in range(3):
                cap = cv2.VideoCapture(i)
                if cap.isOpened():
                    print(f"Camera index {i} opened successfully")
                    return cap
                cap.release()
            return None

        face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )
        
        try:
            recognizer = cv2.face.LBPHFaceRecognizer_create()
            recognizer.read("classifier.xml")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load classifier: {e}")
            return

        cap = init_camera()
        if cap is None:
            messagebox.showerror("Error", 
                "Could not access camera.\n"
                "Please check:\n"
                "1. Camera is connected\n"
                "2. No other app is using it\n"
                "3. Permissions are correct",
                parent=self.root)
            return

        recognized = False
        try:
         while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to capture frame")
                break

            # Process frame and check for recognition
            frame, detected = draw_boundary(frame, face_cascade, 1.1, 10, recognizer)
            cv2.imshow("Face Recognition System", frame)

            if detected:
                # Show result for 2 seconds before exiting
                cv2.waitKey(2000)
                recognized = True
                break

            # Check for manual exit with Enter key
            if cv2.waitKey(1) == 13:
                break

        except Exception as e:
            print(f"Recognition error: {e}")
        finally:
            cap.release()
            cv2.destroyAllWindows()

        if recognized:
            messagebox.showinfo("Success", "Attendance recorded successfully!", parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()