import customtkinter as ctk
from tkinter import messagebox, IntVar
import subprocess

def create_two(parent_frame):
    two = ctk.CTkFrame(parent_frame, corner_radius=0)
    two.grid(row=0, column=1, sticky="nsew")
    title = ctk.CTkLabel(two, text="File Permissions", font=ctk.CTkFont(size=15, weight="bold"))
    title.place(relx=0.36, rely=0.05)

    label1 = ctk.CTkLabel(two, text="Enter the Username:  ", font=("Ubuntu", 20), justify=ctk.LEFT)
    label1.place(relx=0.10, rely=0.21)

    label2 = ctk.CTkLabel(two, text="Enter File Path: ", font=("Ubuntu", 20), justify=ctk.LEFT)
    label2.place(relx=0.10, rely=0.33)

    entry_username = ctk.CTkEntry(two, placeholder_text="", font=("Ubuntu", 20, "bold"), border_width=2)
    entry_username.place(relx=0.44, rely=0.20, relwidth=0.47, relheight=0.078)

    entry_path = ctk.CTkEntry(two, placeholder_text="", font=("Ubuntu", 20, "bold"), border_width=2)
    entry_path.place(relx=0.44, rely=0.32, relwidth=0.47, relheight=0.078)

    read_var = ctk.CTkCheckBox(two, text="Read", font=("Ubuntu", 20))
    read_var.place(relx=0.10, rely=0.57)

    write_var = ctk.CTkCheckBox(two, text="Write", font=("Ubuntu", 20))
    write_var.place(relx=0.44, rely=0.57)

    execute_var = ctk.CTkCheckBox(two, text="Execute", font=("Ubuntu", 20))
    execute_var.place(relx=0.76, rely=0.57)

    flush_all = ctk.CTkButton(two, text="FLUSH FOR ALL", font=("Ubuntu", 18), command=lambda : flush_all_func(entry_path))
    flush_all.place(relx=0.10, rely=0.75, relwidth=0.27, relheight=0.068)

    flush_user = ctk.CTkButton(two, text="FLUSH FOR USER", font=("Ubuntu", 18,), command=lambda : flush_user_func(entry_username,entry_path))
    flush_user.place(relx=0.402, rely=0.75, relwidth=0.27, relheight=0.068)

    submit = ctk.CTkButton(two, text="SUBMIT", font=("Ubuntu", 18), command=lambda : add_permissions(entry_username,entry_path,read_var,write_var,execute_var))
    submit.place(relx=0.7, rely=0.75, relwidth=0.27, relheight=0.068)

    return two
def flush_user_func(username, path):
    subprocess.run(["pkexec", "setfacl", '-x', f"u:{username}", path])


def flush_all_func(path):
    subprocess.run(["pkexec", "setfacl", '--remove-all', path])

def add_permissions(username, path, read_access, write_access, execute_access):
    subprocess.run(["pkexec", "setfacl", '-x', f"u:{username}", path])
    permission_string = ""
    if read_access:
        permission_string += "r"
    if write_access:
        permission_string += "w"
    if execute_access:
        permission_string += "x"

    try:
        subprocess.run(["pkexec", "setfacl", '-m', f"u:{username}:{permission_string}", path])
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to update permissions: {e}")


