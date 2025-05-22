# import tkinter as tk
# from tkinter import simpledialog, messagebox
# from capture_images import capture_images
# from user_management import save_user
# from face_recognition_module import load_known_faces, recognize_faces

# def register_face():
#     name = simpledialog.askstring("Input", "Enter the user's name:")
#     if not name:
#         return
#     capture_images(name)
#     save_user(name)
#     messagebox.showinfo("Success", f"{name} added successfully!")

# def start_gui():
#     root = tk.Tk()
#     root.title("Attendance System")

#     tk.Button(root, text="Register Face", command=register_face, width=30).pack(pady=10)
#     tk.Button(root, text="Start Attendance", command=lambda: recognize_faces(*load_known_faces()), width=30).pack(pady=10)
#     tk.Button(root, text="Exit", command=root.destroy, width=30).pack(pady=10)

#     root.mainloop()


# <++++=================================================+++>
import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
from capture_images import capture_images
from user_management import save_user
from face_recognition_module import load_known_faces, recognize_faces
import datetime

class ModernDialog:
    def __init__(self, parent, title, prompt):
        self.result = None
        self.dialog = tk.Toplevel(parent)
        self.dialog.title(title)
        self.dialog.geometry("400x200")
        self.dialog.configure(bg='#2c3e50')
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        # Center the dialog
        self.dialog.geometry("+%d+%d" % (parent.winfo_rootx() + 50, parent.winfo_rooty() + 50))
        
        # Main frame
        main_frame = tk.Frame(self.dialog, bg='#2c3e50', padx=20, pady=20)
        main_frame.pack(fill='both', expand=True)
        
        # Prompt label
        prompt_label = tk.Label(main_frame, text=prompt, font=('Segoe UI', 12), 
                               fg='white', bg='#2c3e50')
        prompt_label.pack(pady=(0, 15))
        
        # Entry field
        self.entry = tk.Entry(main_frame, font=('Segoe UI', 11), width=30,
                             relief='flat', bd=5, highlightthickness=2,
                             highlightcolor='#3498db', highlightbackground='#bdc3c7')
        self.entry.pack(pady=(0, 20))
        self.entry.focus()
        
        # Buttons frame
        button_frame = tk.Frame(main_frame, bg='#2c3e50')
        button_frame.pack()
        
        # OK button
        ok_btn = tk.Button(button_frame, text="OK", command=self.ok_pressed,
                          font=('Segoe UI', 10, 'bold'), fg='white', bg='#3498db',
                          relief='flat', padx=20, pady=8, cursor='hand2',
                          activebackground='#2980b9', activeforeground='white')
        ok_btn.pack(side='left', padx=(0, 10))
        
        # Cancel button
        cancel_btn = tk.Button(button_frame, text="Cancel", command=self.cancel_pressed,
                              font=('Segoe UI', 10), fg='white', bg='#95a5a6',
                              relief='flat', padx=20, pady=8, cursor='hand2',
                              activebackground='#7f8c8d', activeforeground='white')
        cancel_btn.pack(side='left')
        
        # Bind Enter key
        self.entry.bind('<Return>', lambda e: self.ok_pressed())
        self.dialog.bind('<Escape>', lambda e: self.cancel_pressed())
    
    def ok_pressed(self):
        self.result = self.entry.get()
        self.dialog.destroy()
    
    def cancel_pressed(self):
        self.result = None
        self.dialog.destroy()

class AttendanceSystemGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.setup_window()
        self.create_widgets()
        
    def setup_window(self):
        self.root.title("Smart Attendance System")
        self.root.geometry("600x500")
        self.root.configure(bg='#ecf0f1')
        self.root.resizable(False, False)
        
        # Center window on screen
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (600 // 2)
        y = (self.root.winfo_screenheight() // 2) - (500 // 2)
        self.root.geometry(f"+{x}+{y}")
        
    def create_widgets(self):
        # Main container
        main_container = tk.Frame(self.root, bg='#ecf0f1')
        main_container.pack(fill='both', expand=True, padx=30, pady=30)
        
        # Header frame
        header_frame = tk.Frame(main_container, bg='#2c3e50', height=100)
        header_frame.pack(fill='x', pady=(0, 30))
        header_frame.pack_propagate(False)
        
        # Title
        title_label = tk.Label(header_frame, text="Smart Attendance System",
                              font=('Segoe UI', 24, 'bold'), fg='white', bg='#2c3e50')
        title_label.pack(expand=True)
        
        # Subtitle
        subtitle_label = tk.Label(header_frame, text="Face Recognition Based Attendance",
                                 font=('Segoe UI', 12), fg='#bdc3c7', bg='#2c3e50')
        subtitle_label.pack()
        
        # Button container
        button_container = tk.Frame(main_container, bg='#ecf0f1')
        button_container.pack(expand=True, fill='both')
        
        # Register button
        register_btn = tk.Button(button_container, text="👤 Register New Face",
                                command=self.register_face,
                                font=('Segoe UI', 14, 'bold'), fg='white', bg='#27ae60',
                                relief='flat', padx=40, pady=15, cursor='hand2',
                                activebackground='#229954', activeforeground='white')
        register_btn.pack(pady=15)
        self.add_hover_effect(register_btn, '#27ae60', '#229954')
        
        # Attendance button
        attendance_btn = tk.Button(button_container, text="📊 Start Attendance",
                                  command=self.start_attendance,
                                  font=('Segoe UI', 14, 'bold'), fg='white', bg='#3498db',
                                  relief='flat', padx=40, pady=15, cursor='hand2',
                                  activebackground='#2980b9', activeforeground='white')
        attendance_btn.pack(pady=15)
        self.add_hover_effect(attendance_btn, '#3498db', '#2980b9')
        
        # Exit button
        exit_btn = tk.Button(button_container, text="❌ Exit Application",
                            command=self.exit_application,
                            font=('Segoe UI', 14, 'bold'), fg='white', bg='#e74c3c',
                            relief='flat', padx=40, pady=15, cursor='hand2',
                            activebackground='#c0392b', activeforeground='white')
        exit_btn.pack(pady=15)
        self.add_hover_effect(exit_btn, '#e74c3c', '#c0392b')
        
        # Footer
        footer_frame = tk.Frame(main_container, bg='#ecf0f1', height=50)
        footer_frame.pack(fill='x', side='bottom')
        
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        footer_label = tk.Label(footer_frame, text=f"Current Time: {current_time}",
                               font=('Segoe UI', 10), fg='#7f8c8d', bg='#ecf0f1')
        footer_label.pack(pady=10)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = tk.Label(self.root, textvariable=self.status_var,
                             font=('Segoe UI', 10), fg='white', bg='#34495e',
                             anchor='w', padx=10, pady=5)
        status_bar.pack(side='bottom', fill='x')
        
    def add_hover_effect(self, button, normal_color, hover_color):
        def on_enter(e):
            button.configure(bg=hover_color)
        def on_leave(e):
            button.configure(bg=normal_color)
        
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
        
    def show_custom_input(self, title, prompt):
        dialog = ModernDialog(self.root, title, prompt)
        self.root.wait_window(dialog.dialog)
        return dialog.result
        
    def register_face(self):
        self.status_var.set("Registering new face...")
        self.root.update()
        
        name = self.show_custom_input("Register User", "Enter the user's name:")
        if not name:
            self.status_var.set("Registration cancelled")
            return
            
        roll = self.show_custom_input("Register User", "Enter the user's roll number:")
        if not roll:
            self.status_var.set("Registration cancelled")
            return
            
        try:
            capture_images(name, roll)
            save_user(name, roll)
            self.show_success_message(f"✅ Success!\n\n{name} ({roll}) has been registered successfully!")
            self.status_var.set(f"User {name} registered successfully")
        except Exception as e:
            self.show_error_message(f"❌ Error!\n\nFailed to register user: {str(e)}")
            self.status_var.set("Registration failed")
            
    def start_attendance(self):
        self.status_var.set("Starting attendance recognition...")
        self.root.update()
        
        try:
            recognize_faces(*load_known_faces())
            self.status_var.set("Attendance process completed")
        except Exception as e:
            self.show_error_message(f"❌ Error!\n\nFailed to start attendance: {str(e)}")
            self.status_var.set("Attendance process failed")
            
    def exit_application(self):
        if messagebox.askyesno("Exit", "Are you sure you want to exit?", 
                              icon='question'):
            self.root.destroy()
            
    def show_success_message(self, message):
        dialog = tk.Toplevel(self.root)
        dialog.title("Success")
        dialog.geometry("400x200")
        dialog.configure(bg='#2ecc71')
        dialog.transient(self.root)
        dialog.grab_set()
        dialog.geometry("+%d+%d" % (self.root.winfo_rootx() + 100, 
                                   self.root.winfo_rooty() + 100))
        
        tk.Label(dialog, text=message, font=('Segoe UI', 12, 'bold'),
                fg='white', bg='#2ecc71', wraplength=350, justify='center').pack(expand=True)
        
        tk.Button(dialog, text="OK", command=dialog.destroy,
                 font=('Segoe UI', 10, 'bold'), fg='white', bg='#27ae60',
                 relief='flat', padx=30, pady=8, cursor='hand2').pack(pady=20)
                 
    def show_error_message(self, message):
        dialog = tk.Toplevel(self.root)
        dialog.title("Error")
        dialog.geometry("400x200")
        dialog.configure(bg='#e74c3c')
        dialog.transient(self.root)
        dialog.grab_set()
        dialog.geometry("+%d+%d" % (self.root.winfo_rootx() + 100, 
                                   self.root.winfo_rooty() + 100))
        
        tk.Label(dialog, text=message, font=('Segoe UI', 12, 'bold'),
                fg='white', bg='#e74c3c', wraplength=350, justify='center').pack(expand=True)
        
        tk.Button(dialog, text="OK", command=dialog.destroy,
                 font=('Segoe UI', 10, 'bold'), fg='white', bg='#c0392b',
                 relief='flat', padx=30, pady=8, cursor='hand2').pack(pady=20)
        
    def run(self):
        self.root.mainloop()

def register_face():
    """Backward compatibility function"""
    app = AttendanceSystemGUI()
    app.register_face()

def start_gui():
    """Main function to start the GUI"""
    app = AttendanceSystemGUI()
    app.run()

if __name__ == "__main__":
    start_gui()