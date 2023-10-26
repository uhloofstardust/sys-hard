import tkinter
import customtkinter
import subprocess
from tkinter import messagebox, scrolledtext, simpledialog
import os
import getpass
from tkinter.messagebox import askyesno

customtkinter.set_appearance_mode(
    "System"
)  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme(
    "blue"
)  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{1920}x{1080}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create radiobutton frame
        self.radiobutton_frame = customtkinter.CTkFrame(self, height=800)
        self.radiobutton_frame.grid(
            row=1, column=1, rowspan=4, columnspan=1, sticky="nsew"
        )

        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.appearance_mode_label = customtkinter.CTkLabel(
            self.sidebar_frame, text="Appearance Mode:", anchor="w"
        )
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))

        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(
            self.sidebar_frame,
            values=["Light", "Dark", "System"],
            command=self.change_appearance_mode_event,
        )
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(
            self.sidebar_frame, text="UI Scaling:", anchor="w"
        )
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(
            self.sidebar_frame,
            values=["80%", "90%", "100%", "110%", "120%"],
            command=self.change_scaling_event,
        )
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        self.label_1 = customtkinter.CTkLabel(
            master=self.radiobutton_frame,
            text="User Management",
            font=("Ubuntu", 35),
            justify=customtkinter.LEFT,
        )
        # # label_1.grid(row=0, column=0, columnspan=1, padx=20, pady=20)
        self.label_1.place(relx=0.3, rely=0.05)

        self.label_2 = customtkinter.CTkLabel(
            master=self.radiobutton_frame,
            text="Create User:",
            font=("Ubuntu", 22),
            justify=customtkinter.LEFT,
        )
        # label_2.grid(row=1, column=0, columnspan=1, padx=20, pady=20)
        self.label_2.place(relx=0.1, rely=0.2)

        self.label_3 = customtkinter.CTkLabel(
            master=self.radiobutton_frame,
            text="Set Password:",
            font=("Ubuntu", 22),
            justify=customtkinter.LEFT,
        )
        # label_2.grid(row=1, column=0, columnspan=1, padx=20, pady=20)
        self.label_3.place(relx=0.1, rely=0.3)

        self.label_4 = customtkinter.CTkLabel(
            master=self.radiobutton_frame,
            text="Create Group:",
            font=("Ubuntu", 22),
            justify=customtkinter.LEFT,
        )
        # label_2.grid(row=1, column=0, columnspan=1, padx=20, pady=20)
        self.label_4.place(relx=0.1, rely=0.45)

        self.label_5 = customtkinter.CTkLabel(
            master=self.radiobutton_frame,
            text="Grant Sudo Access:",
            font=("Ubuntu", 22),
            justify=customtkinter.LEFT,
        )
        # label_2.grid(row=1, column=0, columnspan=1, padx=20, pady=20)
        self.label_5.place(relx=0.1, rely=0.55)

        self.label_6 = customtkinter.CTkLabel(
            master=self.radiobutton_frame,
            text="Prevent Sudo Access:",
            font=("Ubuntu", 22),
            justify=customtkinter.LEFT,
        )
        # label_2.grid(row=1, column=0, columnspan=1, padx=20, pady=20)
        self.label_6.place(relx=0.1, rely=0.65)

        self.label_7 = customtkinter.CTkLabel(
            master=self.radiobutton_frame,
            text="Delete User:",
            font=("Ubuntu", 22),
            justify=customtkinter.LEFT,
        )
        # label_2.grid(row=1, column=0, columnspan=1, padx=20, pady=20)
        self.label_7.place(relx=0.1, rely=0.75)

        self.entry_username = customtkinter.CTkEntry(
            master=self.radiobutton_frame,
            placeholder_text="Username",
            font=("Ubuntu", 15),
        )
        # entry_username.grid(row=1, column=1, columnspan=4, padx=10, pady=10)
        self.entry_username.place(relx=0.3, rely=0.2, relwidth=0.2)
        self.entry_passwd1 = customtkinter.CTkEntry(
            master=self.radiobutton_frame,
            placeholder_text="Password",
            show="*",
            font=("Ubuntu", 15),
        )
        # entry_username.grid(row=1, column=1, columnspan=4, padx=10, pady=10)
        self.entry_passwd1.place(relx=0.3, rely=0.25, relwidth=0.2)
        
        self.entry_usrnm = customtkinter.CTkEntry(
            master=self.radiobutton_frame,
            placeholder_text="Username",
            font=("Ubuntu", 15),
        )
        # entry_username.grid(row=1, column=1, columnspan=4, padx=10, pady=10)
        self.entry_usrnm.place(relx=0.3, rely=0.3, relwidth=0.2)
        self.entry_passwd = customtkinter.CTkEntry(
            master=self.radiobutton_frame,
            placeholder_text="Password",
            show="*",
            font=("Ubuntu", 15),
        )
        # entry_username.grid(row=1, column=1, columnspan=4, padx=10, pady=10)
        self.entry_passwd.place(relx=0.3, rely=0.35, relwidth=0.2)

        self.entry_groupname = customtkinter.CTkEntry(
            master=self.radiobutton_frame,
            placeholder_text="Group Name",
            font=("Ubuntu", 15),
        )
        # entry_username.grid(row=1, column=1, columnspan=4, padx=10, pady=10)
        self.entry_groupname.place(relx=0.3, rely=0.45, relwidth=0.2)

        self.entry_sudo_user = customtkinter.CTkEntry(
            master=self.radiobutton_frame,
            placeholder_text="Username",
            font=("Ubuntu", 15),
        )
        # entry_username.grid(row=1, column=1, columnspan=4, padx=10, pady=10)
        self.entry_sudo_user.place(relx=0.3, rely=0.55, relwidth=0.2)

        self.entry_prevent_sudo_user = customtkinter.CTkEntry(
            master=self.radiobutton_frame,
            placeholder_text="Username",
            font=("Ubuntu", 15),
        )
        # entry_username.grid(row=1, column=1, columnspan=4, padx=10, pady=10)
        self.entry_prevent_sudo_user.place(relx=0.3, rely=0.65, relwidth=0.2)

        self.entry_delete_user = customtkinter.CTkEntry(
            master=self.radiobutton_frame,
            placeholder_text="Username",
            font=("Ubuntu", 15),
        )
        # entry_username.grid(row=1, column=1, columnspan=4, padx=10, pady=10)
        self.entry_delete_user.place(relx=0.3, rely=0.75, relwidth=0.2)

        self.button_1 = customtkinter.CTkButton(
            self.radiobutton_frame,
            text="Create User",
            font=("Ubuntu", 15),
            command=self.create_new_user,
        )
        self.button_1.place(relx=0.6, rely=0.2, relwidth=0.15)

        self.button_2 = customtkinter.CTkButton(
            self.radiobutton_frame,
            text="Set Password",
            font=("Ubuntu", 15),
            command=self.set_password,
        )
        self.button_2.place(relx=0.6, rely=0.35, relwidth=0.15)

        self.button_3 = customtkinter.CTkButton(
            self.radiobutton_frame,
            text="Create Group",
            font=("Ubuntu", 15),
            command=self.create_group,
        )
        self.button_3.place(relx=0.6, rely=0.45, relwidth=0.15)

        self.button_4 = customtkinter.CTkButton(
            self.radiobutton_frame,
            text="Grant Sudo Access",
            font=("Ubuntu", 15),
            command=self.grant_sudo_access,
        )
        self.button_4.place(relx=0.6, rely=0.55, relwidth=0.15)

        self.button_5 = customtkinter.CTkButton(
            self.radiobutton_frame,
            text="Prevent Sudo Access",
            font=("Ubuntu", 15),
            command=self.prevent_sudo_access,
        )
        self.button_5.place(relx=0.6, rely=0.65, relwidth=0.15)

        self.button_6 = customtkinter.CTkButton(
            self.radiobutton_frame,
            text="Delete User",
            font=("Ubuntu", 15),
            command=self.delete_user,
        )
        self.button_6.place(relx=0.6, rely=0.75, relwidth=0.15)

        self.button_7 = customtkinter.CTkButton(
            self.radiobutton_frame,
            text="Show User Permissions",
            font=("Ubuntu", 15),
            command=self.show_user_permissions,
        )
        self.button_7.place(relx=0.6, rely=0.85, relwidth=0.2)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")


    def create_new_user(self):
        username = self.entry_username.get()
        if username:
            password = self.entry_passwd1.get()
            fpasswd = password + '\n' + password
            # print("\n\n0000",password,"\n\n")
            if password is not None:
                try:
                    # print("\n\n0000",password,"\n\n")
                    subprocess.run(f"sudo adduser {username} --gecos {username}", shell=True, input=fpasswd.encode())
                    messagebox.showinfo("Success", f"User '{username}' created!")
                except subprocess.CalledProcessError as e:
                    messagebox.showerror("Error", f"Failed to create user: {e}")
        else:
            messagebox.showerror("Error", "Username cannot be empty.")

    def set_password(self):
        usrnm = self.entry_usrnm.get()
        pwd = self.entry_passwd.get()
        if pwd:
            try:
                subprocess.run(
                    ["sudo", "chpasswd"],
                    input=f"{usrnm}:{pwd}".encode(),
                    capture_output=True,
                )
                messagebox.showinfo("Success! Password succesfully changed.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to create group: {str(e)}")
        else:
            messagebox.showerror("Error", "Group name cannot be empty.")

    def create_group(self):
        groupname = self.entry_groupname.get()
        if groupname:
            try:
                subprocess.run(["sudo", "groupadd", groupname])
                messagebox.showinfo("Success", f"Group '{groupname}' created!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to create group: {str(e)}")
        else:
            messagebox.showerror("Error", "Group name cannot be empty.")

    def grant_sudo_access(self):
        username = self.entry_sudo_user.get()
        if username:
            try:
                subprocess.run(["sudo", "usermod", "-aG", "sudo", username])
                messagebox.showinfo(
                    "Success", f"User '{username}' granted sudo access!"
                )
            except Exception as e:
                messagebox.showerror("Error", f"Failed to grant sudo access: {str(e)}")
        else:
            messagebox.showerror("Error", "Username cannot be empty.")

    def prevent_sudo_access(self):
        username = self.entry_prevent_sudo_user.get()
        if username:
            try:
                with open("/etc/sudoers.d/restrict_sudo", "w") as file:
                    file.write(f"{username} ALL=(ALL) NOPASSWD: /bin/false\n")

                subprocess.run(["sudo", "deluser", username, "sudo"])

                messagebox.showinfo(
                    "Success", f"User '{username}' restricted from sudo access!"
                )
            except Exception as e:
                messagebox.showerror(
                    "Error", f"Failed to restrict sudo access: {str(e)}"
                )
        else:
            messagebox.showerror("Error", "Username cannot be empty.")

    userdel_exit_codes = {
        0: "Successful completion.",
        2: "Invalid command syntax. A usage message for the userdel command is displayed.",
        6: "The account to be removed does not exist.",
        8: "The account to be removed is in use.",
        10: "Cannot update the /etc/group or /etc/user_attr file but the login is removed from the /etc/passwd file.",
        12: "Cannot remove or otherwise modify the home directory.",
    }

    def delete_user(self):
        username = self.entry_delete_user.get()
        if username:
            try:
                rc = subprocess.run(["pkexec", "sudo", "userdel", "-f", username])
                if rc.returncode != 0:
                    #  ans = askyesno(title='Delete' , message='Do you want to delete?')
                    #  if ans:
                    #      root2.destroy()
                    messagebox.showinfo("Success", f"{rc.returncode}")
            except Exception as e:
                messagebox.showinfo("Error", f"Errorcode:{e}:: {userdel_exit_codes[0]}")
        else:
            messagebox.showerror("Error", "Username cannot be empty.")

    def give_program_access(self):
            username = self.entry_program_user.get()
            program_path = self.entry_program_path.get()
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
if __name__ == "__main__":
    app = App()
    app.mainloop()




def create_user_management(parent_frame, ctk):
    user_management_frame = ctk.CTkFrame(parent_frame, corner_radius=0)
    title = ctk.CTkLabel(user_management_frame, text="User Management", font=("Ubuntu", 35))
    entry_username = ctk.CTkEntry(user_management_frame, placeholder_text="Username", font=("Ubuntu", 15))
    entry_passwd1 = ctk.CTkEntry(user_management_frame, placeholder_text="Password", show="*", font=("Ubuntu", 15))
    create_user_button = ctk.CTkButton(user_management_frame, text="Create User", font=("Ubuntu", 15), command=create_user)

    user_management_frame.pack(expand=True, fill="both")
    title.place(relx=0.3, rely=0.05)
    entry_username.place(relx=0.1, rely=0.2, relwidth=0.2)
    entry_passwd1.place(relx=0.1, rely=0.3, relwidth=0.2)
    create_user_button.place(relx=0.6, rely=0.2, relwidth=0.15)

    def create_user():
        username = entry_username.get()
        password = entry_passwd1.get()
        if username:
            if password is not None:
                # Add your logic to create a new user using the provided username and password.
                print(f"Creating user '{username}' with password: {password}")
            else:
                print("Password cannot be empty.")
        else:
            print("Username cannot be empty.")

    return user_management_frame
