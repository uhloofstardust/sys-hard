import tkinter as tk
import subprocess
from tkinter import messagebox

# Function to create a user
def create_user():
    username = entry_username.get()
    if username:
        try:
            subprocess.run(["sudo", "adduser", username])
            messagebox.showinfo("Success", f"User '{username}' created!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create user: {str(e)}")
    else:
        messagebox.showerror("Error", "Username cannot be empty.")

# Function to create a group
def create_group():
    groupname = entry_groupname.get()
    if groupname:
        try:
            subprocess.run(["sudo", "groupadd", groupname])
            messagebox.showinfo("Success", f"Group '{groupname}' created!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create group: {str(e)}")
    else:
        messagebox.showerror("Error", "Group name cannot be empty.")

# Function to grant sudo access
def grant_sudo_access():
    username = entry_sudo_user.get()
    if username:
        try:
            subprocess.run(["sudo", "usermod", "-aG", "sudo", username])
            messagebox.showinfo("Success", f"User '{username}' granted sudo access!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to grant sudo access: {str(e)}")
    else:
        messagebox.showerror("Error", "Username cannot be empty.")

# Function to prevent sudo access
def prevent_sudo_access():
    username = entry_prevent_sudo_user.get()
    if username:
        try:
            with open('/etc/sudoers.d/restrict_sudo', 'w') as file:
                file.write(f"{username} ALL=(ALL) NOPASSWD: /bin/false\n")
                subprocess.run(["sudo", "usermod", "-G", "", username])
            messagebox.showinfo("Success", f"User '{username}' restricted from sudo access!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to restrict sudo access: {str(e)}")
    else:
        messagebox.showerror("Error", "Username cannot be empty.")

# Create the main window
root = tk.Tk()
root.title("User and Group Management")

# Create User Section
label_username = tk.Label(root, text="Create User:")
label_username.pack()
entry_username = tk.Entry(root)
entry_username.pack()
create_user_button = tk.Button(root, text="Create User", command=create_user)
create_user_button.pack()

# Create Group Section
label_groupname = tk.Label(root, text="Create Group:")
label_groupname.pack()
entry_groupname = tk.Entry(root)
entry_groupname.pack()
create_group_button = tk.Button(root, text="Create Group", command=create_group)
create_group_button.pack()

# Grant Sudo Access Section
label_sudo_user = tk.Label(root, text="Grant Sudo Access:")
label_sudo_user.pack()
entry_sudo_user = tk.Entry(root)
entry_sudo_user.pack()
grant_sudo_button = tk.Button(root, text="Grant Sudo Access", command=grant_sudo_access)
grant_sudo_button.pack()

# Prevent Sudo Access Section
label_prevent_sudo_user = tk.Label(root, text="Prevent Sudo Access:")
label_prevent_sudo_user.pack()
entry_prevent_sudo_user = tk.Entry(root)
entry_prevent_sudo_user.pack()
prevent_sudo_button = tk.Button(root, text="Prevent Sudo Access", command=prevent_sudo_access)
prevent_sudo_button.pack()

# Start the application
root.mainloop()
