import tkinter as tk
from tkinter import messagebox, IntVar
import subprocess

def manage_permissions(username, path, read_access, write_access, execute_access):
    try:
        setfacl_command = ["sudo", "setfacl", "-m", f"user:{username}:---"]
        if read_access:
            setfacl_command.extend(["-m", f"user:{username}:r--"])
        if write_access:
            setfacl_command.extend(["-m", f"user:{username}:-w-"])
        if execute_access:
            setfacl_command.extend(["-m", f"user:{username}:--x"])
        setfacl_command.append(path)

        subprocess.run(setfacl_command, check=True)
        messagebox.showinfo("Success", f"Permissions for '{path}' updated for user '{username}'!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to update permissions: {e}")

def create_manage_permissions_page():
    subprocess.run(["pwd"])
    manage_permissions_window = tk.Toplevel(root)
    manage_permissions_window.title("Manage File Permissions")

    tk.Label(manage_permissions_window, text="Username:").pack()
    entry_username = tk.Entry(manage_permissions_window)
    entry_username.pack()

    tk.Label(manage_permissions_window, text="File/Directory Path:").pack()
    entry_path = tk.Entry(manage_permissions_window)
    entry_path.pack()

    read_var = IntVar()
    write_var = IntVar()
    execute_var = IntVar()

    tk.Checkbutton(manage_permissions_window, text="Read Access", variable=read_var).pack()
    tk.Checkbutton(manage_permissions_window, text="Write Access", variable=write_var).pack()
    tk.Checkbutton(manage_permissions_window, text="Execute Access", variable=execute_var).pack()

    submit_button = tk.Button(manage_permissions_window, text="Submit", command=lambda: manage_permissions(entry_username.get(), entry_path.get(), read_var.get(), write_var.get(), execute_var.get()))
    submit_button.pack()

root = tk.Tk()
root.title("File Permission Manager")

manage_permissions_button = tk.Button(root, text="Manage File Permissions", command=create_manage_permissions_page)
manage_permissions_button.pack()

root.mainloop()
