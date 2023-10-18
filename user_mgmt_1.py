import tkinter as tk
from tkinter import messagebox, scrolledtext, simpledialog
import subprocess
import os
import getpass


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




def create_new_user():
    username = entry_username.get()
    if username:
        # Create a password entry dialog
        password = tk.simpledialog.askstring("Password Entry", f"Enter the password for user '{username}':", show='*')
        if password is not None:
            try:
                # Set the user's information including the full name and other details
                subprocess.run(["sudo", "adduser", "--disabled-password", "--gecos", f"{username}", username])
                # Set the password separately
                subprocess.run(["echo", f"{username}:{password}" "|", "sudo", "chpasswd"])
                # Unlock the user account
                subprocess.run(["sudo", "passwd", "-u", username])
                messagebox.showinfo("Success", f"User '{username}' created!")
            except subprocess.CalledProcessError as e:
                messagebox.showerror("Error", f"Failed to create user: {e}")
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

# Function to prevent sudo access and remove from sudo group
def prevent_sudo_access():
    username = entry_prevent_sudo_user.get()
    if username:
        try:
            # Write the sudoers entry to restrict sudo access
            with open('/etc/sudoers.d/restrict_sudo', 'w') as file:
                file.write(f"{username} ALL=(ALL) NOPASSWD: /bin/false\n")
            
            # Remove the user from the sudo group
            subprocess.run(["sudo", "deluser", username, "sudo"])
            
            messagebox.showinfo("Success", f"User '{username}' restricted from sudo access!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to restrict sudo access: {str(e)}")
    else:
        messagebox.showerror("Error", "Username cannot be empty.")

# Function to delete a user
def delete_user():
    username = entry_delete_user.get()
    if username:
        try:
            subprocess.run(["sudo", "deluser", "--remove-home", username])
            messagebox.showinfo("Success", f"User '{username}' deleted!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete user: {str(e)}")
    else:
        messagebox.showerror("Error", "Username cannot be empty.")

# Function to give a user access to a specific program
def give_program_access():
    username = entry_program_user.get()
    program_path = entry_program_path.get()
    if username and program_path:
        try:
            os.makedirs(f"/home/{username}/programs", exist_ok=True)
            subprocess.run(["sudo", "cp", program_path, f"/home/{username}/programs/"])
            subprocess.run(["sudo", "chown", f"{username}:{username}", f"/home/{username}/programs/{os.path.basename(program_path)}"])
            subprocess.run(["sudo", "chmod", "755", f"/home/{username}/programs/{os.path.basename(program_path)}"])
            messagebox.showinfo("Success", f"User '{username}' granted access to '{program_path}'!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to grant program access: {str(e)}")
    else:
        messagebox.showerror("Error", "Username or program path cannot be empty.")

# Function to show user list and permissions
def show_user_permissions():
    try:
        users = subprocess.check_output(["cut", "-d", ":", "-f", "1", "/etc/passwd"]).decode("utf-8").split("\n")[:-1]
        user_permissions = {}
        for user in users:
            permissions = subprocess.check_output(["sudo", "lsof", "-u", user]).decode("utf-8")
            user_permissions[user] = permissions
        result = "\n".join([f"User: {user}\n{permissions}\n" for user, permissions in user_permissions.items()])
        messagebox.showinfo("User List and Permissions", result)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to retrieve user list and permissions: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("User and Group Management")

# Create User Section
label_username = tk.Label(root, text="Create User:")
label_username.pack()
entry_username = tk.Entry(root)
entry_username.pack()
create_user_button = tk.Button(root, text="Create User", command=create_new_user)
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

# Delete User Section
label_delete_user = tk.Label(root, text="Delete User:")
label_delete_user.pack()
entry_delete_user = tk.Entry(root)
entry_delete_user.pack()
delete_user_button = tk.Button(root, text="Delete User", command=delete_user)
delete_user_button.pack()





# Function to show user permissions
#def show_user_permissions():
#    try:
#        users = subprocess.check_output(["cut", "-d", ":", "-f", "1", "/etc/passwd"]).decode("utf-8").split("\n")[:-1]
#        user_permissions = {}
#        for user in users:
#            try:
#                permissions = subprocess.check_output(["sudo", "lsof", "-u", user]).decode("utf-8")
#                user_permissions[user] = permissions
#            except subprocess.CalledProcessError:
#                # Handle cases where 'lsof' may not return any results for a user
#                user_permissions[user] = "No open files"
#        result = "\n".join([f"User: {user}\n{permissions}\n" for user, permissions in user_permissions.items()])
#        messagebox.showinfo("User List and Permissions", result)
#    except Exception as e:
#        messagebox.showerror("Error", f"Failed to retrieve user list and permissions: {str(e)}")




# Function to show list of users and open file counts
# Function to show list of all users and their open file counts
def show_user_permissions():
    try:
        users = subprocess.check_output(["cut", "-d", ":", "-f", "1", "/etc/passwd"]).decode("utf-8").split("\n")[:-1]
        user_permissions = {}

        for user in users:
            try:
                permissions = subprocess.check_output(["sudo", "lsof", "-u", user]).decode("utf-8")
                open_file_count = len(permissions.strip().split('\n')[1:])  # Count of open files
                user_permissions[user] = open_file_count
            except subprocess.CalledProcessError:
                # Handle cases where 'lsof' may not return any results for a user
                user_permissions[user] = 0

        # Create a clean and readable report
        result = "\n".join([f"User: {user}\nOpen Files: {count}\n" for user, count in user_permissions.items()])

        # Create a new window for the scrollable text
        window = tk.Toplevel(root)
        window.title("User List and Open File Counts")
        st = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=40, height=15)
        st.insert(tk.END, result)
        st.pack()

    except Exception as e:
        messagebox.showerror("Error", f"Failed to retrieve user list and permissions: {str(e)}")






# Show User Permissions
show_permissions_button = tk.Button(root, text="Show User Permissions", command=show_user_permissions)
show_permissions_button.pack()








# Start the application
root.mainloop()

