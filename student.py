from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os

class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x750+0+0")
        self.root.title("Face Recognition System")
        



 #======Variables======
        self.var_department=StringVar()
        self.var_course_of_study=StringVar()
        self.var_unit_of_study=StringVar()
        self.var_year_of_study=StringVar()
        self.var_semester=StringVar()
        self.var_academic_year=StringVar()
        self.var_student_id=StringVar()
        self.var_student_name=StringVar()
        self.var_admission_number=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_lecturer_name=StringVar()
        self.var_photo_path=StringVar()

          

#first image
        img1=Image.open("/home/reagan/Face_Recognition/Project_photos/back.jpeg")
        img1=img1.resize((400,100),Image.LANCZOS)
        self.photo_img1=ImageTk.PhotoImage(img1)
                                         

        f_lbl=Label(self.root,image=self.photo_img1)
        f_lbl.place(x=0,y=0,width=420,height=100)

 #Second image
        img2=Image.open("/home/reagan/Face_Recognition/Project_photos/face.jpeg")
        img2=img2.resize((400,100),Image.LANCZOS)
        self.photo_img2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photo_img2)
        f_lbl.place(x=400,y=0,width=420,height=100)
        
        
        



#Third 
        img3=Image.open("/home/reagan/Face_Recognition/Project_photos/library.jpeg")
        img3=img3.resize((400,100),Image.LANCZOS)
        self.photo_img3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photo_img3)
        f_lbl.place(x=800,y=0,width=420,height=100)
        #reagan
        img16=Image.open("/home/reagan/Face_Recognition/Project_photos/help.jpeg")
        img16=img16.resize((400,100),Image.LANCZOS)
        self.photo_img16=ImageTk.PhotoImage(img16)

        f_lbl=Label(self.root,image=self.photo_img16)
        f_lbl.place(x=1200,y=0,width=150,height=100)
        


#big image
       #big image
        img3=Image.open(r"/home/reagan/Face_Recognition/Project_photos/background.jpeg")
        img3=img3.resize((1350,750),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        big_img=Label(self.root,image=self.photoimg3)
        big_img.place(x=0,y=130,width=1350,height=700)
    
        title_lbl=Label(big_img,text="STUDENT MANAGEMENT",font=("times new roman",30,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=40)

        main_frame=Frame(big_img,bd=2,bg="white")
        main_frame.place(x=20,y=55,width=1440,height=600)

#Left label Frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",13,"bold"))
        Left_frame.place(x=0,y=0,width=660,height=505)


        img_left=Image.open(r"/home/reagan/Face_Recognition/Project_photos/student.jpeg")
        img_left=img_left.resize((550,130),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
                                         
        f_1b1=Label(self.root,image=self.photoimg_left)
        f_1b1.place(x=20,y=210,width=650,height=110)
 #Current Information
        current_course_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Current Information",font=("times new roman",13,"bold"))
        current_course_frame.place(x=0,y=130,width=650,height=138)
#Department
        department_lebel=Label(current_course_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        department_lebel.grid(row=0,column=0,padx=10,sticky=W)

        department_combo=ttk.Combobox(current_course_frame,textvariable=self.var_department,font=("times new roman",11,"bold"),state="Read Only",width=20)
        department_combo["values"]=("Select Department","Informatics And Computing","Education Science","Medicine","Engineering")
        department_combo.current(0)
        department_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

#Course Of Study
        course_of_study_lebel=Label(current_course_frame,text="Course Of Study:",font=("times new roman",12,"bold"),bg="white")
        course_of_study_lebel.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        course_of_study_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course_of_study,font=("times new roman",11,"bold"),state="Read Only",width=20)
        course_of_study_combo["values"]=("Select Course","Computer Science","Software Engineering","Mathematics & IT")
        course_of_study_combo.current(0)
        course_of_study_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

#Units Of Study
        unit_of_study_lebel=Label(current_course_frame,text="Unit Of Study:",font=("times new roman",12,"bold"),bg="white")
        unit_of_study_lebel.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        unit_of_study_combo=ttk.Combobox(current_course_frame,textvariable=self.var_unit_of_study,font=("times new roman",11,"bold"),state="Read Only",width=20)
        unit_of_study_combo["values"]=("Select Unit(s)","Introducton to Computer Application","Data Structures","Calculus 1","Linear Algebra","Digital Electronics 1","Antenna And Propagation")
        unit_of_study_combo.current(0)
        unit_of_study_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

#Year of Study
        year_of_study_lebel=Label(current_course_frame,text="Year Of Study:",font=("times new roman",12,"bold"),bg="white")
        year_of_study_lebel.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        year_of_study_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year_of_study,font=("times new roman",11,"bold"),state="Read Only",width=20)
        year_of_study_combo["values"]=("Select Current Year ","1","2","3","4","5","6")
        year_of_study_combo.current(0)
        year_of_study_combo.grid(row=2,column=1,padx=2,pady=10,sticky=W)
#
#Current Semester
        semester_label = Label(current_course_frame, text="Current Semester:", font=("times new roman", 12, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)  # Fixed variable name

        semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman", 11, "bold"), state="readonly", width=20)  # Fixed state
        semester_combo["values"] = ("Select", "1", "2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3, padx=2, pady=10, sticky=W)

 #Academic year
        academic_year_lebel=Label(current_course_frame,text="Current Academic Year:",font=("times new roman",12,"bold"),bg="white")
        academic_year_lebel.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        academic_year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_academic_year,font=("times new roman",11,"bold"),state="Read Only",width=20)
        academic_year_combo["values"]=("Select","2022/2023","2023/2024","2024/2025")
        academic_year_combo.current(0)
        academic_year_combo.grid(row=2,column=3,padx=2,pady=10,sticky=W)
 #Class Student information
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",11,"bold"))
        class_student_frame.place(x=0,y=250,width=650,height=230)

#Student id
        student_id_label=Label(class_student_frame,text="Student Id",font=("times new roman",12,"bold"),bg="white")
        student_id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        student_id_entry=ttk.Entry(class_student_frame,textvariable=self.var_student_id,width=20,font=("times new roman",11,"bold"))
        student_id_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
 
#Student Name
        student_name_label=Label(class_student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        student_name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        student_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_student_name,width=20,font=("times new roman",11,"bold"))
        student_name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)#Student Gender
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=20,font=("times new roman",11,"bold"))
        gender_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
#Student admission Number
        admission_number_label=Label(class_student_frame,text="Admission Number:",font=("times new roman",12,"bold"),bg="white")
        admission_number_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        admission_number_entry=ttk.Entry(class_student_frame,textvariable=self.var_admission_number,width=20,font=("times new roman",11,"bold"))
        admission_number_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
 #Student Email 
        email_label=Label(class_student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",11,"bold"))
        email_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
#Lecturer Name
        lecturer_name_label=Label(class_student_frame,text="Lecturer Name:",font=("times new roman",12,"bold"),bg="white")
        lecturer_name_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        lecturer_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_lecturer_name,width=20,font=("times new roman",11,"bold"))
        lecturer_name_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
                       
    

#radio button
        self.var_radio1=StringVar()
        radiobutton1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobutton1.grid(row=3,column=0)

        
        radiobutton2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="Yes")
        radiobutton2.grid(row=3,column=1)
 

#bbuttons Frame
        btn_frame1=Frame(self.root,bd=2,relief=RIDGE,bg="blue")
        btn_frame1.place(x=25,y=605,width=645,height=40)

        save_btn=Button(btn_frame1,text="Save",command=self.add_data, width=14,font=("times new roman",15,"bold"),fg="darkblue",bg="blue")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame1,text="Update",command=self.update_data,width=13,font=("times new roman",15,"bold"),fg="darkblue",bg="blue")
        update_btn.grid(row=0,column=1)
        

        delete_btn=Button(btn_frame1,text="Delete",command=self.delete_data,width=14,font=("times new roman",15,"bold"),fg="darkblue",bg="blue")
        delete_btn.grid(row=0,column=2)


        reset_btn=Button(btn_frame1,text="Reset",command=self.reset_data,width=13,font=("times new roman",15,"bold"),fg="darkblue",bg="blue")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=160,width=645,height=40)


        take_photo=Button(btn_frame1,text="Take Photo",command=self.generate_dataset,width=34,font=("times new roman",15,"bold"),fg="darkblue",bg="blue")
        take_photo.grid(row=0,column=0)

        update_photo=Button(btn_frame1,text="Update Photo",width=34,font=("times new roman",15,"bold"),fg="darkblue",bg="blue")
        update_photo.grid(row=0,column=1)


#Right label Frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=660,y=0,width=660,height=505)


        img_right=Image.open(r"/home/reagan/Face_Recognition/Project_photos/student.jpeg")
        img_right=img_right.resize((500,130),Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_1b1=Label(self.root,image=self.photoimg_right)
        f_1b1.place(x=700,y=210,width=640,height=110)
    

#========Search System==========
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="System Search",font=("times new roman",13,"bold"))
        search_frame.place(x=5,y=110,width=650,height=90)
         
        search_label=Label(search_frame,text="Search By:",font=("times new roman",13,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)


        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="Read Only",width=15)
        search_combo["values"]=("Select ","admission_number","studentName")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",11,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
                       
    

       
        search_btn=Button(search_frame,text="Search",width=13,font=("times new roman",11,"bold"),fg="blue",bg="white")
        search_btn.grid(row=0,column=3,padx=4)
        

        showAll_btn=Button(search_frame,text="Show All",width=13,font=("times new roman",11,"bold"),fg="blue",bg="white")
        showAll_btn.grid(row=0,column=4,padx=4)

        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE,)
        table_frame.place(x=5,y=210,width=650,height=270)
        Scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.students_table=ttk.Treeview(table_frame,column=("department","year_of_study","academic_year","semester","unit_of_study","student_name","student_id","admission_number","course_of_study","gender","email","photo_path","","lecturer_name"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)

        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)

        Scroll_x.config(command=self.students_table.xview)
        Scroll_y.config(command=self.students_table.yview)

      

# Format columns

        self.students_table.column("department", width=120)
        self.students_table.column("year_of_study", width=100)
        self.students_table.column("academic_year", width=120)
        self.students_table.column("semester", width=100)
        self.students_table.column("unit_of_study", width=120)
        self.students_table.column("student_name", width=150)
        self.students_table.column("admission_number",width=130)
        self.students_table.column("course_of_study", width=150)
        self.students_table.column("gender", width=100)
        self.students_table.column("email", width=180)
        self.students_table.column("student_id", width=130)
        self.students_table.column("photo_path", width=120)
        self.students_table.column("lecturer_name", width=150)

        
# Show only the defined headings


        self.students_table.heading("department",text="Department")
        self.students_table.heading("year_of_study",text="Year Of Study")
        self.students_table.heading("admission_number",text="Admission Number")
        self.students_table.heading("semester",text="Current Semester")
        self.students_table.heading("unit_of_study",text="Unit(S)")
        self.students_table.heading("student_name",text="Student Name")
        self.students_table.heading("academic_year", text="Academic Year")
        self.students_table.heading("course_of_study",text="Course Of Study")
        self.students_table.heading("gender",text="Gender")
        self.students_table.heading("email",text="Email Address")
        self.students_table.heading("student_id",text="Student Id")
        self.students_table.heading("photo_path",text="Photo Status")
        self.students_table.heading("lecturer_name",text="Name Of the Lecturer")
        self.students_table["show"]="headings"


        self.students_table.pack(fill=BOTH,expand=1)
        self.students_table.bind("<ButtonRelease >",self.get_cursor)
        self.connect_db
        self.fetch_data()
        self.connection = None
        
        
    def connect_db(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="Admin",
                password="@730wanjala",
                database="face_recognition_attendance",
                autocommit=True
            )
            if self.connection.is_connected():
                print("Successfully connected to MySQL database")
        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to connect: {str(e)}")
            
    def get_cursor(self):
        try:
            if not self.connection or not self.connection.is_connected():
                self.connect_db()
            return self.connection.cursor()
        except Exception as e:
            messagebox.showerror("Database Error", f"Cursor error: {str(e)}")
            return None

    
    def execute_query(self, query, params=None):
        """Execute database queries with proper error handling"""
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="Admin",
                password="@730wanjala",
                database="face_recognition_attendance"
            )
            cursor = conn.cursor()
            
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
                
            conn.commit()
            return True
            
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}", parent=self.root)
            return False
        except Exception as e:
            messagebox.showerror("Error", f"Unexpected error: {str(e)}", parent=self.root)
            return False
        finally:
            if 'conn' in locals() and conn.is_connected():
                cursor.close()
                conn.close()


        #========function declaration======
    def add_data(self):
        if (self.var_department.get() == "Select Department" or 
            not self.var_student_name.get() or 
            not self.var_admission_number.get()):
            messagebox.showerror("Error", "Department, Name and Admission Number are required!", parent=self.root)
            return
    
        query = """INSERT INTO students 
               (department, course_of_study, unit_of_study, year_of_study, 
                semester, academic_year, admission_number, student_name, 
                gender, email, lecturer_name, photo_path) 
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    
        params = (
        self.var_department.get(),
        self.var_course_of_study.get(),
        self.var_unit_of_study.get(),
        self.var_year_of_study.get(),
        self.var_semester.get(),
        self.var_academic_year.get(),
        self.var_admission_number.get(),
        self.var_student_name.get(),
        self.var_gender.get(),
        self.var_email.get(),
        self.var_lecturer_name.get(),
        "No" if not self.var_radio1.get() else "Yes"
    )
    
        if self.execute_query(query, params):
           self.fetch_data()
           messagebox.showinfo("Success", "Student added successfully", parent=self.root)
        self.reset_data()
#======================fetch data================
    def fetch_data(self):
        try:
              conn = mysql.connector.connect(host="localhost",user="Admin",password="@730wanjala",database="face_recognition_attendance"
        )
              my_cursor = conn.cursor()
              my_cursor.execute("SELECT * FROM students")
              data = my_cursor.fetchall()
              self.students_table.delete(*self.students_table.get_children())  # Clear existing data
              for row in data:
               self.students_table.insert("", END, values=row)  # Insert each row of data
               conn.close()  # Close connection after processing
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
       

        #==========================getCursor===========
    def get_cursor(self,event=""):
           cursor_focus=self.students_table.focus()
           content=self.students_table.item(cursor_focus)
           data=content["values"]
           if data and len(data) >= 14:  # Ensure we have enough columns
              self.var_department.set(data[1])          # department
              self.var_course_of_study.set(data[2])     # course_of_study
              self.var_unit_of_study.set(data[3])       # unit_of_study
              self.var_year_of_study.set(data[4])       # year_of_study
              self.var_semester.set(data[5])            # semester
              self.var_academic_year.set(data[6])       # academic_year
              self.var_student_id.set(data[0])          # student_id (primary key)
              self.var_student_name.set(data[8])        # student_name
              self.var_admission_number.set(data[7])    # admission_number
              self.var_gender.set(data[9])              # gender
              self.var_email.set(data[10])              # email
              self.var_lecturer_name.set(data[11])      # lecturer_name
              self.var_photo_path.set(data[13])         # photo_path
           #===============update function===============
    def update_data(self):
                  if self.var_department.get()=="Select Department" or self.var_student_name.get()==""or self.var_student_id.get()=="":
                      messagebox.showerror("Error","All Fields are Required!",parent=self.root)
                  else:
                         try:
                                Update=messagebox.askyesno("Update","Do You Want To Update This Student Details?",parent=self.root)
                                if Update>0:
                                       conn=mysql.connector.connect(host="localhost",username="Admin",password="@730wanjala",database="face_recognition_attendance")
                                       my_cursor=conn.cursor()
                                       my_cursor.execute("update students set department=%s,course_of_study=%s,"
                                       "unit_of_study=%s,year_of_study=%s,semester=%s,academic_year=%s,"
                                       "student_name=%s,admission_number=%s,gender=%s,email=%s,"
                                       "lecturer_name=%s,photo_path=%s where student_id=%s",(
                                              
                                                                self.var_department.get(),
                                                                self.var_course_of_study.get(),
                                                                self.var_unit_of_study.get(),
                                                                self.var_year_of_study.get(),
                                                                self.var_semester.get(),
                                                                self.var_academic_year.get(),
                                                                
                                                                self.var_student_name.get(),
                                                                self.var_admission_number.get(),
                                                                self.var_gender.get(),
                                                                self.var_email.get(),             
                                                                self.var_lecturer_name.get(), 
                                                                self.var_radio1.get(),
                                                                self.var_student_id.get()

                                                                             ))
                                else:
                                       if not Update:
                                              return
                                       messagebox.showinfo("Success!","Student Details Updated Successfully",parent=self.root)
                                       conn.commit()
                                       self.fetch_dat()
                                       conn.close()
                                       
                         except Exception as es:
                                        messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
                                        #==============delete==============
    def delete_data(self):
                 if self.var_student_id.get()=="":
                    messagebox.showerror("Error","Student id Must be required!",parent=self.root)
                 else:
                     try:
                            delete=messagebox.askyesno("Student Delete Page","Do you want to delete this Student!?",parent=self.root)
                            if delete>0:
                                     conn=mysql.connector.connect(host="localhost",username="Admin",password="@730wanjala",database="face_recognition_attendance")
                                     my_cursor=conn.cursor()
                                     sql="delete from students where student_id=%s"
                                     val=(self.var_student_id.get(),)
                                     my_cursor.execute(sql,val)
                            else:
                                    if not delete:
                                            return
                                    
                                    conn.commit()
                                    self.fetch_data()
                                    conn.close()
                                    messagebox.showinfo("Delete","Successfully Deleted the student",parent=self.root)
                     except Exception as es:
                                     messagebox.showerrorshowerror("Error",f"Due To :{str(es)}",parent=self.root)
                                     #=========reset data=====
    def reset_data(self):
            self.var_department.set("select Department"),
            self.var_course_of_study.set("Select Course"),
            self.var_unit_of_study.set("Select Unit(s)"),
            self.var_year_of_study.set("Select Current Year"),
            self.var_semester.set("select"),
            self.var_academic_year.set("select"),
            self.var_student_id.set(""), 
            self.var_student_name.set(""),
            self.var_admission_number.set(""),
            self.var_gender.set(""),
            self.var_email.set(""),             
            self.var_lecturer_name.set(""), 
            self.var_radio1.set("")
            #===================generate data set or Take photo samples=====
    def generate_dataset(self):
         if (self.var_department.get() == "Select Department" or 
             not self.var_student_name.get() or 
             not self.var_student_id.get()):
             messagebox.showerror("Error", "All Fields are Required!", parent=self.root)
             return
         try:
                student_id=self.var_student_id.get()
        # Initialize face classifier
                face_classifier = cv2.CascadeClassifier(
                    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        )
        # Create data directory if it doesn't exist
                if not os.path.exists("data"):
                   os.makedirs("data")
            
        # Initialize video capture
                cap = cv2.VideoCapture(0)
                img_id = 0
                face_detected = False

                while img_id < 100:
                  ret, frame = cap.read()
                  if not ret:
                    break

                  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                  faces = face_classifier.detectMultiScale(gray, 1.3, 5)

                  for (x, y, w, h) in faces:
                    face_detected = True
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                    face_roi = frame[y:y+h, x:x+w]
                
                # Save face image
                    img_id += 1
                    face_gray = cv2.cvtColor(face_roi, cv2.COLOR_BGR2GRAY)
                    file_path = f"data/user.{student_id}.{img_id}.jpg"
                    cv2.imwrite(file_path, face_gray)
                
                 # Display count
                    cv2.putText(frame, f"Samples: {img_id}", (30, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

                  cv2.imshow("Face Capture", frame)
            
            # Break on ESC press or when 100 samples collected
                  if cv2.waitKey(1) == 27 or img_id >= 100:
                   break

                cap.release()
                cv2.destroyAllWindows()

                if not face_detected:
                    messagebox.showerror("Error", "No faces detected during capture!", parent=self.root)
                    return

        # Update database with photo status
                try:
                    conn = mysql.connector.connect( host="localhost",user="Admin",password="@730wanjala", database="face_recognition_attendance"
            )
                    cursor = conn.cursor()
            
                    update_query = """
                    UPDATE students 
                    SET photo_path=%s 
                    WHERE student_id=%s
            """
                    cursor.execute(update_query, ("Yes", student_id))
                    conn.commit()
                    messagebox.showinfo("Success", "Face samples captured and database updated!", parent=self.root)
            
                except mysql.connector.Error as err:
                   messagebox.showerror("Database Error", f"Error: {err}", parent=self.root)
                finally:
                  if conn.is_connected():
                   cursor.close()
                   conn.close()
                
                   self.fetch_data()
                   self.reset_data()
         except Exception as e:
                messagebox.showerror("Error",f"An error occurred:{str(e)}",parent=self.root)
          
            
if __name__ == "__main__":
          root =Tk()
          obj=Student(root)
          root.mainloop()



