import tkinter as tk
from tkinter import ttk, filedialog, messagebox, simpledialog
from models import User
from services import DataService
from controllers import UserController, AdminController
from mysql import connector

import mysql.connector

class RegisterPage:
    def __init__(self, root, app):
        self.root = root
        self.app = app
        self.create_widgets()

    def create_widgets(self):
        self.frame = ttk.Frame(self.root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(self.frame, text="Username").grid(row=0, column=0, padx=5, pady=5)
        self.username_entry = ttk.Entry(self.frame)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.frame, text="Password").grid(row=1, column=0, padx=5, pady=5)
        self.password_entry = ttk.Entry(self.frame, show="*")
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.frame, text="Role").grid(row=2, column=0, padx=5, pady=5)
        self.role_entry = ttk.Combobox(self.frame, values=["admin", "user"])
        self.role_entry.grid(row=2, column=1, padx=5, pady=5)

        self.register_button = ttk.Button(self.frame, text="Register", command=self.register)
        self.register_button.grid(row=3, column=0, columnspan=2, pady=10)

   
class LoginPage:
    def __init__(self, root, app):
        self.root = root
        self.app = app
        self.create_widgets()

    def create_widgets(self):
        self.frame = ttk.Frame(self.root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(self.frame, text="Username").grid(row=0, column=0, padx=5, pady=5)
        self.username_entry = ttk.Entry(self.frame)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.frame, text="Password").grid(row=1, column=0, padx=5, pady=5)
        self.password_entry = ttk.Entry(self.frame, show="*")
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.frame, text="Role").grid(row=2, column=0, padx=5, pady=5)
        self.role_entry = ttk.Combobox(self.frame, values=["admin", "user"])
        self.role_entry.grid(row=2, column=1, padx=5, pady=5)

        self.login_button = ttk.Button(self.frame, text="Login", command=self.login)
        self.login_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.register_button = ttk.Button(self.frame, text="Register", command=self.register)
        self.register_button.grid(row=4, column=0, columnspan=2, pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        role = self.role_entry.get()

        if not username or not password or not role:
            messagebox.showerror("Error", "All fields are required")
            return

        db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Robonull5388!!",
            database="data_viewer"
        )

        cursor = db.cursor()


        query = "SELECT * FROM users WHERE username = %s AND password = %s AND role = %s"
        values = (username, password, role)
        cursor.execute(query, values)

        result = cursor.fetchone()

        cursor.close()
        db.close()

        if result:
            user = User(username, password, role)
            self.app.set_user(user)
            self.frame.destroy()
            self.app.show_main_page()
        else:
            messagebox.showerror("Error", "Invalid credentials")

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        role = self.role_entry.get()

        if not username or not password or not role:
            messagebox.showerror("Error", "All fields are required")
            return

        db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Robonull5388!!",
            database="data_viewer"
        )

        cursor = db.cursor()

        query = "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)"
        values = (username, password, role)
        cursor.execute(query, values)

        db.commit()

        cursor.close()
        db.close()

        user = User(username, password, role)
        self.app.set_user(user)
        self.frame.destroy()
        self.app.show_login_page()


class MainPage:
    def __init__(self, root, app):
        self.root = root
        self.app = app
        self.create_widgets()

    def create_widgets(self):
        self.frame = ttk.Frame(self.root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.load_button = ttk.Button(self.frame, text="Load CSV", command=self.load_csv)
        self.load_button.grid(row=0, column=0, pady=5)

        self.view_button = ttk.Button(self.frame, text="View Data", command=self.view_data)
        self.view_button.grid(row=1, column=0, pady=5)

        if self.app.user.role == 'admin':
            self.edit_button = ttk.Button(self.frame, text="Edit Data", command=self.edit_data)
            self.edit_button.grid(row=2, column=0, pady=5)

            self.save_button = ttk.Button(self.frame, text="Save Data to Excel", command=self.save_data)
            self.save_button.grid(row=3, column=0, pady=5)

        self.quit_button = ttk.Button(self.frame, text="Logout", command=self.logout)
        self.quit_button.grid(row=4, column=0, pady=5)

        self.text_area = tk.Text(self.frame, wrap=tk.WORD, width=80, height=20)
        self.text_area.grid(row=0, column=1, rowspan=5, padx=10)

    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.app.data_service.load_data(file_path)
            messagebox.showinfo("Success", f"Data loaded from {file_path}")

    def view_data(self):
        data = self.app.controller.view_data()
        self.display_data(data)

    def edit_data(self):
        if self.app.user.role != 'admin':
            messagebox.showerror("Error", "You do not have permission to edit data")
            return

        pass

    def save_data(self):
        if self.app.user.role != 'admin':
            messagebox.showerror("Error", "You do not have permission to save data")
            return

        output_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
        if output_path:
            self.app.controller.save_data(output_path)
            messagebox.showinfo("Success", f"Data saved to {output_path}")

    def logout(self):
        self.frame.destroy()
        self.app.show_login_page()

    def display_data(self, data):
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, data.to_string(index=False))

class App:
    def __init__(self, root):
        self.root = root
        self.data_service = DataService()
        self.user = None
        self.controller = None
        self.show_login_page()

    def set_user(self, user):
        self.user = user
        if user.role == 'admin':
            self.controller = AdminController(user, self.data_service)
        else:
            self.controller = UserController(user, self.data_service)

    def show_login_page(self):
        LoginPage(self.root, self)

    def show_main_page(self):
        MainPage(self.root, self)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()