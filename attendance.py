from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog



mydata=[]

class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x750+0+0")
        self.root.title("Face Recognition System")
        #===variable=======
        self.var_attendance=StringVar()
        self.var_name=StringVar()
        self.var_admin=StringVar()
        self.var_department=StringVar()
        self.var_course=StringVar()
        self.var_unit=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_lect=StringVar()
        self.var_status=StringVar()



        image_left=Image.open(r"Project_photos/att.jpg")
        image_left=image_left.resize((400,100),Image.LANCZOS)
        self.photo_image_left=ImageTk.PhotoImage(image_left)

        f_lbl=Label(self.root,image=self.photo_image_left)
        f_lbl.place(x=0,y=0,width=420,height=100)

        image_left1=Image.open(r"Project_photos/att.jpg")
        image_left1=image_left.resize((400,100),Image.LANCZOS)
        self.photo_image_left1=ImageTk.PhotoImage(image_left1)

        f_lbl=Label(self.root,image=self.photo_image_left1)
        f_lbl.place(x=400,y=0,width=420,height=100)

        image_left2=Image.open(r"Project_photos/att.jpg")
        image_left2=image_left2.resize((400,100),Image.LANCZOS)
        self.photo_image_left2=ImageTk.PhotoImage(image_left2)

        f_lbl=Label(self.root,image=self.photo_image_left2)
        f_lbl.place(x=800,y=0,width=420,height=100)


        img2=Image.open(r"Project_photos/att.jpg")
        img2=img2.resize((400,100),Image.LANCZOS)
        self.photo_img2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photo_img2)
        f_lbl.place(x=1200,y=0,width=150,height=100)

        img4=Image.open(r"Project_photos/background.jpeg")
        img4=img4.resize((1350,750),Image.LANCZOS)
        self.photo_img4=ImageTk.PhotoImage(img4)

        big_img=Label(self.root,image=self.photo_img4)
        big_img.place(x=0,y=100,width=1350,height=600)

        title_lbl=Label(big_img,text="CLASS ATTENDANCE",font=("times new roman",30,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=10,width=1400,height=55)

        main_frame=Frame(big_img,bd=2,bg="white")
        main_frame.place(x=0,y=55,width=1440,height=600)


        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",13,"bold"))
        Left_frame.place(x=0,y=0,width=670,height=535)

        img_right=Image.open(r"Project_photos/att.jpg")
        img_right=img_right.resize((500,130),Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_1b1=Label(self.root,image=self.photoimg_right)
        f_1b1.place(x=683,y=182,width=655,height=110)

        left_inside_frame=Frame(Left_frame,bd=2,bg="white",relief=RIDGE)
        left_inside_frame.place(x=0,y=115,width=660,height=395)
#====LABEL ENTRY===
      
      
      # attendance id
        Attendance_id_label=Label(left_inside_frame,text="Attendance Id",font=("times new roman",12,"bold"),bg="white")
        Attendance_id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        Attendance_id_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attendance,font=("times new roman",11,"bold"))
        Attendance_id_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
 
#Student Name
        student_name_label=Label(left_inside_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        student_name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        student_name_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_name,font=("times new roman",11,"bold"))
        student_name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
 #Student course
        course_lebel=Label(left_inside_frame,text="Course Of Study:",font=("times new roman",12,"bold"),bg="white")
        course_lebel.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        course_combo=ttk.Combobox(left_inside_frame,font=("times new roman",11,"bold"),state="Read Only",width=20)
        course_combo["values"]=("Select Course","Computer Science","Software Engineering","Mathematics & IT")
        course_combo.current(0)
        course_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
#Student admission Number
        admission_number_label=Label(left_inside_frame,text="Admission No:",font=("times new roman",12,"bold"),bg="white")
        admission_number_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        admission_number_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_admin,font=("times new roman",11,"bold"))
        admission_number_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
 #Department
        
        department_lebel=Label(left_inside_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        department_lebel.grid(row=2,column=0,padx=10,sticky=W)

        department_combo=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_department,font=("times new roman",11,"bold"),state="readonly")
        department_combo["values"]=("Select Department","Informatics And Computing","Education Science","Medicine","Engineering")
        department_combo.current(0)
        department_combo.grid(row=2,column=1,padx=2,pady=10,sticky=W)


        #Units Of Study
        unit_of_study_lebel=Label(left_inside_frame,text="Unit:",font=("times new roman",12,"bold"),bg="white")
        unit_of_study_lebel.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        unit_of_study_combo=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_unit,font=("times new roman",11,"bold"),state="readonly")
        unit_of_study_combo["values"]=("Select Unit(s)","Introducton to Computer Application","Data Structures","Calculus 1","Linear Algebra","Digital Electronics 1","Antenna And Propagation")
        unit_of_study_combo.current(0)
        unit_of_study_combo.grid(row=2,column=3,padx=2,pady=10,sticky=W)


#Lecturer Name
        lecturer_name_label=Label(left_inside_frame,text="Lecturer Name:",font=("times new roman",12,"bold"),bg="white")
        lecturer_name_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        lecturer_name_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_lect,font=("times new roman",11,"bold"))
        lecturer_name_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
#====Time
                       
        time_name_label=Label(left_inside_frame,text="Time:",font=("times new roman",12,"bold"),bg="white")
        time_name_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        time_name_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_time,font=("times new roman",11,"bold"))
        time_name_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
 #=====Date====

        date_name_label=Label(left_inside_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
        date_name_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        date_name_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_date,font=("times new roman",11,"bold"))
        date_name_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
 #====attendance status===
        status_lebel=Label(left_inside_frame,text="Attendance Status:",font=("times new roman",12,"bold"),bg="white")
        status_lebel.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        status_combo=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_status,font=("times new roman",11,"bold"),state="readonly")
        status_combo["values"]=("Status","Present","Absent")
        status_combo.current(0)
        status_combo.grid(row=4,column=3,padx=2,pady=10,sticky=W)


        btn_frame1=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="blue")
        btn_frame1.place(x=0,y=350,width=655,height=40)

        save_btn=Button(btn_frame1,text="Import csv",command=self.importCsv, width=14,font=("times new roman",15,"bold"),fg="darkblue",bg="blue")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame1,text="Export csv",command=self.exportCsv,width=13,font=("times new roman",15,"bold"),fg="darkblue",bg="blue")
        update_btn.grid(row=0,column=1)
        

        delete_btn=Button(btn_frame1,text="Update",width=14,font=("times new roman",15,"bold"),fg="darkblue",bg="blue")
        delete_btn.grid(row=0,column=2)


        reset_btn=Button(btn_frame1,text="Reset",command=self.reset_data,width=13,font=("times new roman",15,"bold"),fg="darkblue",bg="blue")
        reset_btn.grid(row=0,column=3)

       
    

#radio button
        
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Studence Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=678,y=0,width=662,height=535)

        img_left=Image.open(r"/home/reagan/Face_Recognition/Project_photos/att.jpg")
        img_left=img_left.resize((550,130),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
                                         
        f_1b1=Label(self.root,image=self.photoimg_left)
        f_1b1.place(x=5,y=182,width=665,height=110)

        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=0,y=115,width=658,height=395)

        Scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.AttendanceReporttable=ttk.Treeview(table_frame,column=("Id","Name","Admin.No","Department","Course","Unit","Time","Date","Lecturer","Status"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
        
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)

        Scroll_x.config(command=self.AttendanceReporttable.xview)
        Scroll_y.config(command=self.AttendanceReporttable.yview)

        self.AttendanceReporttable.heading("Id",text="Attendance Id")
        self.AttendanceReporttable.heading("Name",text="student Name")
        self.AttendanceReporttable.heading("Admin.No",text="Admission Number")
        self.AttendanceReporttable.heading("Department",text="Department")
        self.AttendanceReporttable.heading("Course",text="Course")
        self.AttendanceReporttable.heading("Unit",text="Unit")
        self.AttendanceReporttable.heading("Time",text="Time")
        self.AttendanceReporttable.heading("Date", text="Date")
        self.AttendanceReporttable.heading("Lecturer",text="Lecturer Name")
        self.AttendanceReporttable.heading("Status",text="Attendance Status")
        
        self.AttendanceReporttable["show"]="headings"



        self.AttendanceReporttable.column("Id", width=120)
        self.AttendanceReporttable.column("Name", width=100)
        self.AttendanceReporttable.column("Admin.No", width=120)
        self.AttendanceReporttable.column("Department", width=100)
        self.AttendanceReporttable.column("Course", width=120)
        self.AttendanceReporttable.column("Unit", width=150)
        self.AttendanceReporttable.column("Time",width=130)
        self.AttendanceReporttable.column("Date", width=150)
        self.AttendanceReporttable.column("Lecturer", width=130)
        self.AttendanceReporttable.column("Status", width=180)
        
        
        self.AttendanceReporttable.pack(fill=BOTH,expand=1)
        #======Fetch data======
    def fetchData(self,rows=None):
          self.AttendanceReporttable.delete(*self.AttendanceReporttable.get_children())
          for i in  rows:
                self.AttendanceReporttable.insert("",END,values=1)
                #==========Import csv

    def importCsv(self):
          global mydata
          mydata.clear()
          fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open csv",filetypes=(("csv File","*.csv"),("All File","*.*")),parent=self.root)
          with open(fln) as myfile:
                csvread=csv.reader(myfile,delimiter=",")
                for i in csvread:
                      mydata.append(i)
                      self.fetchData(mydata)
                      #===========export csv
    def exportCsv(self):
          try:
                if len(mydata)<1:
                      messagebox.showerror("No  Data","No data Found to export",parent=self.root)
                      return False
                fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open csv",filetypes=(("csv File","*.csv"),("All File","*.*")),parent=self.root)
                with open(fln,mode="w",newline="") as myfile:
                      exp_write=csv.write(myfile,delimiter=",")
                      for i in mydata:
                            exp_write.writerow(i)
                            messagebox.showinfo("Data export", "Your data exported to " + os.path.basename(fln) + " Successfully")
          except Exception as es:
                             messagebox.showerrorshowerror("Error",f"Due To :{str(es)}",parent=self.root)
            
    def get_cursor(self,event=""):
           cursor_focus=self.AttendanceReporttablefocus()
           content=self.AttendanceReporttable.item(cursor_focus)
           rows=content["values"]


           self.var_attendance.set(rows[0])
           self.var_name.st(rows[1])
           self.var_admin.set(rows[2])
           self.var_department.set(rows[3])
           self.var_course.set(rows[4])
           self.var_unit.set(rows[5])
           self.var_time.set(rows[6])
           self.var_date.set(rows[7])
           self.var_lect.set(rows[8])
           self.var_status.set(rows)

           #====Reset data=====
    def reset_data(self):
           self.var_attendance.set("")
           self.var_name.st("")
           self.var_admin.set("")
           self.var_department.set("")
           self.var_course.set("")
           self.var_unit.set("")
           self.var_time.set("")
           self.var_date.set("")
           self.var_lect.set("")
           self.var_status.set("")

       



                

          
          
              






    
        






if __name__ == "__main__":
          root =Tk()
          obj=Attendance(root)
          root.mainloop()
        