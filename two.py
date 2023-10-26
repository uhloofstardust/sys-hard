import subprocess
from tkinter import messagebox

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

def flush_user(username, path):
    subprocess.run(["pkexec", "setfacl", '-x', f"u:{username}", path])
    
def flush_all(path):
    subprocess.run(["pkexec", "setfacl", '--remove-all', path])


def create_frame_2(parent_frame, ctk):
    two = ctk.CTkFrame(parent_frame, corner_radius=0)
    two.pack(fill=ctk.BOTH, expand=True)  # Use pack to place the 'two' frame

    title = ctk.CTkLabel(two, text="File Permissions", font=ctk.CTkFont(size=15, weight="bold"))
    title.pack(side=ctk.TOP, padx=10, pady=10)

    label1 = ctk.CTkLabel(two, text="Enter the Username:  ", font=("Ubuntu", 20), justify=ctk.LEFT)
    label1.pack(side=ctk.TOP, padx=10, pady=10)

    label2 = ctk.CTkLabel(two, text="Enter File Path: ", font=("Ubuntu", 20), justify=ctk.LEFT)
    label2.pack(side=ctk.TOP, padx=10, pady=10)

    entry_username = ctk.CTkEntry(two, placeholder_text="", font=("Ubuntu", 20, "bold"), border_width=2)
    entry_username.pack(side=ctk.TOP, padx=10, pady=10)

    entry_path = ctk.CTkEntry(two, placeholder_text="", font=("Ubuntu", 20, "bold"), border_width=2)
    entry_path.pack(side=ctk.TOP, padx=10, pady=10)

    read_var = ctk.CTkCheckBox(two, text="Read", font=("Ubuntu", 20))
    read_var.pack(side=ctk.TOP, padx=10, pady=10)

    write_var = ctk.CTkCheckBox(two, text="Write", font=("Ubuntu", 20))
    write_var.pack(side=ctk.TOP, padx=10, pady=10)

    execute_var = ctk.CTkCheckBox(two, text="Execute", font=("Ubuntu", 20))
    execute_var.pack(side=ctk.TOP, padx=10, pady=10)

    flush_all = ctk.CTkButton(two, text="FLUSH FOR ALL", font=("Ubuntu", 18), command=lambda: flush_all_func(entry_path))
    flush_all.pack(side=ctk.TOP, padx=10, pady=10)

    flush_user = ctk.CTkButton(two, text="FLUSH FOR USER", font=("Ubuntu", 18), command=lambda: flush_user_func(entry_username, entry_path))
    flush_user.pack(side=ctk.TOP, padx=10, pady=10)

    submit = ctk.CTkButton(two, text="SUBMIT", font=("Ubuntu", 18), command=lambda: add_permissions(entry_username, entry_path, read_var, write_var, execute_var))
    submit.pack(side=ctk.TOP, padx=10, pady=10)

    return two
