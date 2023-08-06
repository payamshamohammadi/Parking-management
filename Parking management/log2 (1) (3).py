import tkinter as tk
from tkinter import Toplevel, messagebox
import sqlite3
import string

# create a database connection
conn = sqlite3.connect('users.db')

# create the users table (if it doesn't exist)
conn.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL);''')

# create the main window
root = tk.Tk()
root.title("Login App")
root.configure(bg='black')
root.geometry("1000x2000")

# create the username and password entry fields
username_label = tk.Label(root, text="نام کاربری")
username_label.pack()
username_entry = tk.Entry(root, width=50,font=('Arial 18'))
username_entry.pack( pady=10)

password_label = tk.Label(root, text="رمز عبور")
password_label.pack()
password_entry = tk.Entry(root, show='*',width=50,font=('Arial 18'))
password_entry.pack( pady=10)








def open_employee_management():
    # کد مربوط به صفحه مدیریت کارمندان را اینجا پیاده‌سازی کنید
    pass


def open_vehicle_management():
    # کد مربوط به صفحه مدیریت خودروها را اینجا پیاده‌سازی کنید
    pass


def backup_data():
    # کد مربوط به پشتیبان گیری اطلاعات را اینجا پیاده‌سازی کنید
    pass


def restore_data():
    # کد مربوط به بازیابی اطلاعات را اینجا پیاده‌سازی کنید
    pass




class Clerk:

    def __init__(self) -> None:
            
        messagebox.showinfo(title="ورود", message="ورود موفقیت آمیز بود")

        # تنظیمات رابط کاربری صفحه مدیر کلان
        employee_window = Toplevel(root)

        employee_window.title("کارمند")

        # نشان دادن نام کاربری
        username_label = tk.Label(employee_window, text="نام کاربری: کارمند")
        username_label.pack()

        # گزینه مدیریت کارمند
        employee_management_button = tk.Button(employee_window, text="مشخصات خودرو", command=open_employee_management)
        employee_management_button.pack()

        # اطلاعات ورود و خروج خودرو
        vehicle_management_button = tk.Button(employee_window, text="اطلاعات ورود و خروج خودرو", command=open_vehicle_management)
        vehicle_management_button.pack()

        # گزینه اطلاعات پارکینگ
        backup_button = tk.Button(employee_window, text="اطلاعات پارکینگ", command=backup_data)
        backup_button.pack()

        employee_window.mainloop()



class Manager:

    def __init__(self) -> None:
        super().__init__()
        
        messagebox.showinfo(title="ورود", message="ورود موفقیت آمیز بود")
            
        # تنظیمات رابط کاربری صفحه مدیر کلان
        manager_window = Toplevel(root)

        manager_window.title("صفحه مدیر")

        # نشان دادن نام کاربری
        username_label = tk.Label(manager_window, text="نام کاربری: مدیر")
        username_label.pack()

        # گزینه مدیریت کارمند
        employee_management_button = tk.Button(manager_window, text="مدیریت کارمندان", command=open_employee_management)
        employee_management_button.pack()

        # گزینه مدیریت خودرو
        vehicle_management_button = tk.Button(manager_window, text="مدیریت خودروها", command=open_vehicle_management)
        vehicle_management_button.pack()

        # گزینه پشتیبان گیری
        backup_button = tk.Button(manager_window, text="پشتیبان گیری", command=backup_data)
        backup_button.pack()

        # گزینه بازیابی
        restore_button = tk.Button(manager_window, text="بازیابی", command=restore_data)
        restore_button.pack()

        manager_window.mainloop()





# create the login button
class Login:
    # get the username and password entered by the user
    def __init__(self, username_entry, password_entry):

        self.username_entry = username_entry
        self.password_entry = password_entry
        

    def login(self):
        # get the username and password entered by the user
        username = self.username_entry.get()
        password = self.password_entry.get()

        # authenticate user
        cursor = conn.execute("SELECT * from users WHERE username=? AND password=?", (username, password))
        row = cursor.fetchone()

        if username == "manager" and password == "Manager123":
            # successful login
            manager = Manager()

        # if row is not None:
        elif row is not None:
            # successful login
            clerk = Clerk()

        else:
            # invalid credentials
            messagebox.showerror(title="ورود", message="رمز عبور یا نام کاربری را اشتباه وارد کردید")



login = Login(username_entry, password_entry)

login_button = tk.Button(root, text="ورود", command=login.login)
login_button.pack()

# log =login(username_entry.get(), password_entry.get())

# start the main loop
root.mainloop()








#-----------------------------------------------------------------------

# def signup():
#     # get the username and password entered by the user
#     username = username_entry.get()
#     password = password_entry.get()

#     # check if the password contains at least one uppercase letter
#     if not any(c.isupper() for c in password):
#         messagebox.showerror(title="خطای ثبت نام", message="رمز عبور باید دارای حداقل یک حرف بزرگ انگلیسی باشد ")
#         return

#     # check if the username already exists in the database
#     cursor = conn.execute("SELECT * from users WHERE username=?", (username,))
#     row = cursor.fetchone()

#     if row is not None:
#         # username already exists
#         messagebox.showerror(title="خطای ثبت نام", message="این نام کاربری ثبت شده است")
#     elif username == "username":
#         # do not allow signup with username 'username'
#         messagebox.showerror(title="ثبت نام", message="از 'نام کاربری' نمی توانید به عنوان نام کاربری استفاده کنید")
#     else:
#         # insert new user into database
#         conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
#         conn.commit()

#         # successful signup
#         messagebox.showinfo(title="ثبت نام", message="ثبت نام موفقیت آمیز بود")

# signup_button = tk.Button(root, text="ثبت نام", command=employee)
# signup_button.pack()






# def validate_login():
#     username = username_entry.get()
#     password = password_entry.get()
    
#     employee_list =list("SELECT * from users")
#     print(employee_list)

#     if username == "employee" and password == "employee123":
#         open_employee_page()
#     elif username == "manager" and password == "Manager123":
#         open_manager_page()
#     else:
#         error_label.config(text="نام کاربری یا رمز عبور نامعتبر است")


# def open_employee_page():
#     employee.destroy()

#     # کد مربوط به صفحه کارمند را اینجا پیاده‌سازی کنید


# def open_manager_page():
#     manager.destroy()

#     # کد مربوط به صفحه مدیر را اینجا پیاده‌سازی کنید







# # تنظیمات رابط کاربری صفحه ورود به سیستم
# login_window = tk.Tk() 

# login_window.title("ورود به سیستم")

# username_label = tk.Label(login_window, text="نام کاربری:")
# username_label.pack()

# username_entry = tk.Entry(login_window)
# username_entry.pack()

# password_label = tk.Label(login_window, text="رمز عبور:")
# password_label.pack()

# password_entry = tk.Entry(login_window, show="*")
# password_entry.pack()

# login_button = tk.Button(login_window, text="ورود", command=validate_login)
# login_button.pack()

# error_label = tk.Label(login_window, text="")
# error_label.pack()

# login_window.mainloop()





# def manager():

#     # تنظیمات رابط کاربری صفحه مدیر کلان
#     manager_window = Toplevel(root)

#     manager_window.title("صفحه مدیر")

#     # نشان دادن نام کاربری
#     username_label = tk.Label(manager_window, text="نام کاربری: مدیر")
#     username_label.pack()

#     # گزینه مدیریت کارمند
#     employee_management_button = tk.Button(manager_window, text="مدیریت کارمندان", command=open_employee_management)
#     employee_management_button.pack()

#     # گزینه مدیریت خودرو
#     vehicle_management_button = tk.Button(manager_window, text="مدیریت خودروها", command=open_vehicle_management)
#     vehicle_management_button.pack()

#     # گزینه پشتیبان گیری
#     backup_button = tk.Button(manager_window, text="پشتیبان گیری", command=backup_data)
#     backup_button.pack()

#     # گزینه بازیابی
#     restore_button = tk.Button(manager_window, text="بازیابی", command=restore_data)
#     restore_button.pack()

#     manager_window.mainloop()





# def employee():

#     # تنظیمات رابط کاربری صفحه مدیر کلان
#     employee_window = Toplevel(root)

#     employee_window.title("کارمند")

#     # نشان دادن نام کاربری
#     username_label = tk.Label(employee_window, text="نام کاربری: کارمند")
#     username_label.pack()

#     # گزینه مدیریت کارمند
#     employee_management_button = tk.Button(employee_window, text="مشخصات خودرو", command=open_employee_management)
#     employee_management_button.pack()

#     # اطلاعات ورود و خروج خودرو
#     vehicle_management_button = tk.Button(employee_window, text="اطلاعات ورود و خروج خودرو", command=open_vehicle_management)
#     vehicle_management_button.pack()

#     # گزینه اطلاعات پارکینگ
#     backup_button = tk.Button(employee_window, text="اطلاعات پارکینگ", command=backup_data)
#     backup_button.pack()

#     employee_window.mainloop()
            # # authenticate user
            # cursor = conn.execute("SELECT * from users WHERE username=? AND password=?", (username, password))
            # row = cursor.fetchone()
            # if username == "manager" and password == "Manager123":
            # # if row is not None:
            #     # successful login
            #     messagebox.showinfo(title="ورود", message="ورود موفقیت آمیز بود")
                
            #     # تنظیمات رابط کاربری صفحه مدیر کلان
            #     manager_window = Toplevel(root)

            #     manager_window.title("صفحه مدیر")

            #     # نشان دادن نام کاربری
            #     username_label = tk.Label(manager_window, text="نام کاربری: مدیر")
            #     username_label.pack()

            #     # گزینه مدیریت کارمند
            #     employee_management_button = tk.Button(manager_window, text="مدیریت کارمندان", command=open_employee_management)
            #     employee_management_button.pack()

            #     # گزینه مدیریت خودرو
            #     vehicle_management_button = tk.Button(manager_window, text="مدیریت خودروها", command=open_vehicle_management)
            #     vehicle_management_button.pack()

            #     # گزینه پشتیبان گیری
            #     backup_button = tk.Button(manager_window, text="پشتیبان گیری", command=backup_data)
            #     backup_button.pack()

            #     # گزینه بازیابی
            #     restore_button = tk.Button(manager_window, text="بازیابی", command=restore_data)
            #     restore_button.pack()

            #     manager_window.mainloop()

            # # if row is not None:
            # elif row is not None:
            #     # successful login
            #     messagebox.showinfo(title="ورود", message="ورود موفقیت آمیز بود")

            #     # تنظیمات رابط کاربری صفحه مدیر کلان
            #     employee_window = Toplevel(root)

            #     employee_window.title("کارمند")

            #     # نشان دادن نام کاربری
            #     username_label = tk.Label(employee_window, text="نام کاربری: کارمند")
            #     username_label.pack()

            #     # گزینه مدیریت کارمند
            #     employee_management_button = tk.Button(employee_window, text="مشخصات خودرو", command=open_employee_management)
            #     employee_management_button.pack()

            #     # اطلاعات ورود و خروج خودرو
            #     vehicle_management_button = tk.Button(employee_window, text="اطلاعات ورود و خروج خودرو", command=open_vehicle_management)
            #     vehicle_management_button.pack()

            #     # گزینه اطلاعات پارکینگ
            #     backup_button = tk.Button(employee_window, text="اطلاعات پارکینگ", command=backup_data)
            #     backup_button.pack()

            #     employee_window.mainloop()
            # else:
            #     messagebox.showerror(title="ورود", message="رمز عبور یا نام کاربری را اشتباه وارد کردید")
