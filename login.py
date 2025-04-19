from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import re  # For email validation

def main():
        win=Tk()
        app=LoginWindow(win)
        win.mainloop()
        
class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
    
        # Load and display images
        self.load_images()
        
        # Main frame for login components
        main_frame = Frame(self.root, bd=2, bg="black")
        main_frame.place(x=500, y=180, width=400, height=400)

        # Login components
        Label(main_frame, text="Get Started", font=("times new roman", 20, "bold"),fg="white", bg="black").place(x=120, y=50)
        
        # Username
        Label(main_frame, text="Username:", font=("times new roman", 15, "bold"),fg="white", bg="black").place(x=0, y=85)
        self.txt_user = ttk.Entry(main_frame, font=("times new roman", 15, "bold"))
        self.txt_user.place(x=94, y=85, width=250)
        
        # Password
        Label(main_frame, text="Password:", font=("times new roman", 15, "bold"),fg="white", bg="black").place(x=0, y=170)
        self.txt_pass = ttk.Entry(main_frame, font=("times new roman", 15, "bold"), show="*")
        self.txt_pass.place(x=94, y=170, width=250)
        
        # Login button
        Button(main_frame, text="LOGIN", command=self.login, font=("times new roman", 15, "bold"),bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white",activebackground="red").place(x=135, y=220, width=150, height=35)
        
        # Additional options
        Button(main_frame, text="Forget Password", command=self.forgot_password_window,font=("times new roman", 10, "bold"), borderwidth=0, fg="white",bg="black",activeforeground="white", activebackground="black").place(x=8, y=330, width=150, height=15)
        
        Button(main_frame, text="New User Register", command=self.register_window,font=("times new roman", 10, "bold"),borderwidth=0,fg="white",bg="black",activeforeground="white", activebackground="black").place(x=8, y=350, width=150, height=15)

    def load_images(self):
        """Load and display all images for the login window"""
        try:
            # First image
            img1 = Image.open("Project_photos/background.jpeg")
            img1 = img1.resize((400, 100), Image.LANCZOS)
            self.photo_img1 = ImageTk.PhotoImage(img1)
            Label(self.root, image=self.photo_img1).place(x=0, y=0, width=420, height=100)

            # Second image
            img2 = Image.open("Project_photos/att.jpg")
            img2 = img2.resize((400, 100), Image.LANCZOS)
            self.photo_img2 = ImageTk.PhotoImage(img2)
            Label(self.root, image=self.photo_img2).place(x=400, y=0, width=420, height=100)

            # Third image
            img3 = Image.open("Project_photos/library.jpeg")
            img3 = img3.resize((400, 100), Image.LANCZOS)
            self.photo_img3 = ImageTk.PhotoImage(img3)
            Label(self.root, image=self.photo_img3).place(x=800, y=0, width=420, height=100)

            # Help image
            img16 = Image.open("Project_photos/help.jpeg")
            img16 = img16.resize((400, 100), Image.LANCZOS)
            self.photo_img16 = ImageTk.PhotoImage(img16)
            Label(self.root, image=self.photo_img16).place(x=1200, y=0, width=150, height=100)

            # Background image
            img4 = Image.open("Project_photos/background.jpeg")
            img4 = img4.resize((1350, 750), Image.LANCZOS)
            self.photo_img4 = ImageTk.PhotoImage(img4)
            big_img = Label(self.root, image=self.photo_img4)
            big_img.place(x=0, y=130, width=1350, height=550)
            
            Label(big_img, text="Welcome To Digitech University Of Science And Technology",font=("times new roman", 30, "bold"), bg="white", fg="red").place(x=0, y=10, width=1400, height=40)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load images: {str(e)}")

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = RegisterWindow(self.new_window)

    def login(self):
        username = self.txt_user.get()
        password = self.txt_pass.get()
        
        if not username or not password:
            messagebox.showerror("Error", "All fields are required")
            return
            
        # Hardcoded admin credentials (remove in production)
        if username.lower() in ["Admin", "Admin"] and password == "@730wanjala":
            messagebox.showinfo("Success", "Welcome to Digitech University")
           
            return
        
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="Admin",
                password="@730wanjala",
                database="face_recognition_attendace"
            )
            cursor = conn.cursor()
            
            cursor.execute(
                "SELECT * FROM register WHERE username=%s AND password=%s",
                (username, password)
            )
            
            if cursor.fetchone():
                if messagebox.askyesno("Access", "Access only admin?"):
                   
                    pass
            else:
                messagebox.showerror("Error", "Invalid username or password")
                
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", str(err))
        finally:
            if 'conn' in locals() and conn.is_connected():
                conn.close()

    def forgot_password_window(self):
        username = self.txt_user.get()
        
        if not username:
            messagebox.showerror("Error", "Please enter your email address to reset password")
            return
            
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="Admin",
                password="@730wanjala",
                database="face_recognition_attendance"
            )
            cursor = conn.cursor()
            
            cursor.execute("SELECT * FROM register WHERE email=%s", (username,))
            if not cursor.fetchone():
                messagebox.showerror("Error", "Please enter a valid username")
                return
                
            # Create password reset window
            reset_window = Toplevel(self.root)
            reset_window.title("Forgot Password")
            reset_window.geometry("340x450+610+170")
            
            Label(reset_window, text="Forgot Password",font=("times new roman", 15, "bold"), fg="red").pack(fill=X)
                  
            # Security question
            Label(reset_window, text="Select Security Question",font=("times new roman", 15, "bold")).place(x=50, y=80)
            self.combo_security_q = ttk.Combobox( reset_window,font=("times new roman", 15, "bold"),state="readonly",values=("Select", "Your Birth place", "Your dad name", "Your mother name"))
            self.combo_security_q.current(0)
            self.combo_security_q.place(x=50, y=110, width=250)
            
            # Security answer
            Label(reset_window, text="Security Answer",font=("times new roman", 15, "bold")).place(x=50, y=150)
            self.txt_security = ttk.Entry(reset_window, font=("times new roman", 15))
            self.txt_security.place(x=50, y=180, width=250)
            
            # New password
            Label(reset_window, text="New Password",font=("times new roman", 15, "bold")).place(x=50, y=220)
            self.txt_newpass = ttk.Entry(reset_window, font=("times new roman", 15), show="*")
            self.txt_newpass.place(x=50, y=250, width=250)
            
            # Reset button
            Button(reset_window, text="Reset", command=self.reset_password,ont=("times new roman", 15, "bold"), bg="orange", fg="green").place(x=100, y=300)
            
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", str(err))
        finally:
            if 'conn' in locals() and conn.is_connected():
                conn.close()

    def reset_password(self):
        # Implementation for password reset
        pass


class RegisterWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Form")
        self.root.geometry("1600x800+0+0")
        
        # Variables
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_security_q = StringVar()
        self.var_security_a = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()
        self.var_check = IntVar()
        
        # Main frame
        frame = Frame(self.root, bg="white")
        frame.place(x=400, y=50, width=800, height=550)
        
        Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"),fg="green", bg="white").place(x=20, y=20)
        
        # Registration form frame
        reg_frame = LabelFrame(frame, bd=2, bg="white", relief=RIDGE,text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="blue")
        reg_frame.place(x=5, y=5, width=670, height=400)
        
        # Form fields
        # First name
        Label(reg_frame, text="First and Middle Name", font=("times new roman", 15, "bold"), bg="white").grid(row=1, column=1, padx=10, pady=5, sticky=W)
        fname_entry = ttk.Entry(reg_frame,textvariable=self.var_fname,width=25, font=("times new roman", 13, "bold"))
        fname_entry.grid(row=2, column=1,padx=10, pady=5,sticky=W)
        fname_entry.config(validate='key',validatecommand=(self.root.register(self.validate_name), '%P'))
        
        # Last name
        Label(reg_frame, text="Last Name",font=("times new roman", 15, "bold"), bg="white").grid(row=1, column=2, padx=10, pady=5, sticky=W)
        lname_entry = ttk.Entry(reg_frame, textvariable=self.var_lname, width=25, font=("times new roman", 13, "bold"))
        lname_entry.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        lname_entry.config(validate='key',validatecommand=(self.root.register(self.validate_name), '%P'))
        
        # Contact
        Label(reg_frame, text="Contact No.", font=("times new roman", 15, "bold"),bg="white").grid(row=3, column=1, padx=10, pady=5, sticky=W)
        contact_entry = ttk.Entry(reg_frame, textvariable=self.var_contact, 
        width=25, font=("times new roman", 13, "bold"))
        contact_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)
        contact_entry.config(validate='key',validatecommand=(self.root.register(self.validate_phone), '%P'))
        
        # Email
        Label(reg_frame, text="Email or Username", font=("times new roman", 15, "bold"),bg="white").grid(row=3, column=2, padx=10, pady=5, sticky=W)
        email_entry = ttk.Entry(reg_frame, textvariable=self.var_email,width=25, font=("times new roman", 13, "bold"))
        email_entry.grid(row=4, column=2, padx=10, pady=5, sticky=W)
        Label(reg_frame, text="*Please enter valid email: ex123@gmail.com",font=("times new roman", 8, "bold"), fg="red", bg="white").place(x=250, y=139)
        
        # Security question
        Label(reg_frame, text="Security Question", font=("times new roman", 15, "bold"),bg="white").grid(row=5, column=1, padx=5, pady=5, sticky=W)
        security_combo = ttk.Combobox(reg_frame, textvariable=self.var_security_q,font=("times new roman", 13, "bold"), state="readonly", width=23)
        security_combo["values"] = ("Select Security Question", "Your Dad's Name", "Your Mom's name")
        security_combo.current(0)
        security_combo.grid(row=6, column=1, padx=5, pady=10, sticky=W)
        
        # Security answer
        Label(reg_frame, text="Security Answer", font=("times new roman", 15, "bold"),bg="white").grid(row=5, column=2, padx=10, pady=5, sticky=W)
        ttk.Entry(reg_frame, textvariable=self.var_security_a, width=25,font=("times new roman", 13, "bold")).grid(row=6, column=2, padx=10, pady=5, sticky=W)
        
        # Password
        Label(reg_frame, text="Password", font=("times new roman", 15, "bold"),bg="white").grid(row=7, column=1, padx=10, pady=5, sticky=W)
        ttk.Entry(reg_frame, textvariable=self.var_pass, width=25, font=("times new roman", 13, "bold"), show="*").grid(row=8, column=1, padx=10, pady=5, sticky=W)
        Label(reg_frame, text="*Please enter strong password",font=("times new roman", 10, "bold"), fg="red", bg="white").place(x=35, y=305)
        
        # Confirm password
        Label(reg_frame, text="Confirm Password", font=("times new roman", 15, "bold"),bg="white").grid(row=7, column=2, padx=10, pady=5, sticky=W)
        ttk.Entry(reg_frame, textvariable=self.var_confpass, width=25,font=("times new roman", 13, "bold"), show="*").grid(row=8, column=2, padx=10, pady=5, sticky=W)
        
        # Terms checkbox
        Checkbutton(frame, variable=self.var_check,text="I agree with terms and conditions",font=("times new roman", 12, "bold"), bg="white",onvalue=1, offvalue=0).place(x=50, y=370)
        
        # Buttons
        Button(frame, text="Register", command=self.register_data,font=("times new roman", 15, "bold"), bg="green", fg="white").place(x=50, y=420, width=120)
        
        Button(frame, text="Return to Login", command=self.return_login,font=("times new roman", 15, "bold"), bg="gray", fg="white").place(x=200, y=420, width=150)

    def validate_name(self, name):
        """Validate that name contains only letters and spaces"""
        return name.isalpha() or ' ' in name

    def validate_phone(self, phone):
        """Validate phone number format"""
        return phone.isdigit() and len(phone) <= 10 or phone == ""

    def register_data(self):
        # Validate all fields
        if not all([self.var_fname.get(), self.var_lname.get(), self.var_contact.get(), 
                   self.var_email.get(), self.var_pass.get(), self.var_confpass.get()]):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return
            
        if self.var_security_q.get() == "Select Security Question":
            messagebox.showerror("Error", "Please select a security question", parent=self.root)
            return
            
        if self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password and confirm password must match", parent=self.root)
            return
            
        if not self.var_check.get():
            messagebox.showerror("Error", "Please agree to the terms and conditions", parent=self.root)
            return
            
        # Validate email format
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.var_email.get()):
            messagebox.showerror("Error", "Invalid email format", parent=self.root)
            return
            
        # Validate password strength
        if len(self.var_pass.get()) < 8 or not any(c.isupper() for c in self.var_pass.get()) or not any(c.isdigit() for c in self.var_pass.get()):
            messagebox.showerror("Error", "Password must be at least 8 characters with uppercase and numbers", parent=self.root)
            return
            
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="Admin",
                password="@730wanjala",
                database="face_recognition_attendance"
            )
            cursor = conn.cursor()
            
            # Check if email already exists
            cursor.execute("SELECT * FROM register WHERE email=%s", (self.var_email.get(),))
            if cursor.fetchone():
                messagebox.showerror("Error", "Email already registered", parent=self.root)
                return
                
            # Insert new user
            cursor.execute(
    "INSERT INTO register (fname, lname, contact, email, security_q, security_a, pass, confpass, terms_accepted) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
    (
        self.var_fname.get(),
        self.var_lname.get(),
        self.var_contact.get(),
        self.var_email.get(),
        self.var_security_q.get(),
        self.var_security_a.get(),
        self.var_pass.get(),
        self.var_confpass.get(),
        self.var_check.get()
    )
)
            conn.commit()
            messagebox.showinfo("Success", "Registration successful", parent=self.root)
            self.root.destroy()
            
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", str(err), parent=self.root)
        finally:
            if 'conn' in locals() and conn.is_connected():
                conn.close()

    def return_login(self):
        self.root.destroy()


def main():
    root = Tk()
    app = LoginWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()