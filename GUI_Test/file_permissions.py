import subprocess
from CTkMessagebox import CTkMessagebox

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
        CTkMessagebox(title="Error", message=f"Failed to update permissions: {e}")


def flush_user_func(username, path):
    print(username.get(),path.get())
    if(username.get() == "" and path.get() == ""):
        username.configure(fg_color = "red")
        path.configure(fg_color = "red")
        ctkmsg = CTkMessagebox(title="Info", message="Username and Path is not specified")
        if(ctkmsg.get() == 'OK'):
            username.configure(fg_color="#ab23ff")
            path.configure(fg_color="#ab23ff")

    elif(username.get() == ""):
        username.configure(fg_color = "red")
        ctkmsg = CTkMessagebox(title="Info", message="Username is not specified")
        if(ctkmsg.get() == 'OK'):
            username.configure(fg_color = '#006653')
            path.configure(fg_color = '#006653')
    elif(path.get() == ""):
        path.configure(fg_color = "red")
        ctkmsg = CTkMessagebox(title="Info", message="File Path is not specified")
        if(ctkmsg.get() == 'OK'):
            username.configure(fg_color="transparent")
            path.configure(fg_color="transparent")
    else:
        subprocess.run(["pkexec", "setfacl", '-x', f"u:{username.get()}", path.get()])


def flush_all_func(path):
    subprocess.run(["pkexec", "setfacl", '--remove-all', path])


def create_file_permissions(parent_frame, ctk):
    file_permissions_frame = ctk.CTkFrame(parent_frame, corner_radius=0)
    file_permissions_frame.pack(fill=ctk.BOTH, expand=True)  

    title = ctk.CTkLabel(file_permissions_frame, text="File Permissions",font = ('Arial',24))
    title.pack(side=ctk.TOP, padx=10, pady=(20,10))

    frame1 = ctk.CTkFrame(file_permissions_frame)
    frame1.pack(side=ctk.TOP, padx=10, pady=10)

    entry_username = ctk.CTkEntry(frame1, placeholder_text="Enter Username",width = 300)
    entry_username.grid(row = 0,column = 0,padx = 10,pady = 10)

    entry_path = ctk.CTkEntry(frame1, placeholder_text="Enter File Path",width = 300)
    entry_path.grid(row = 1,column = 0,padx = 10,pady = 10)

    submit = ctk.CTkButton(frame1, text="SUBMIT",command=lambda: add_permissions(entry_username, entry_path, read_var, write_var,execute_var),width = 300)
    submit.grid(row = 2,column = 0,padx = 10,pady = 10)

    read_var = ctk.CTkCheckBox(frame1, text="Read",)
    read_var.grid(row = 0,column = 1,padx = 10,pady = 10)

    write_var = ctk.CTkCheckBox(frame1, text="Write")
    write_var.grid(row = 1,column = 1,padx = 10,pady = 10)

    execute_var = ctk.CTkCheckBox(frame1, text="Execute",)
    execute_var.grid(row = 2,column = 1,padx = 10,pady = 10)

    flush_all_btn = ctk.CTkButton(frame1, text="FLUSH FOR ALL",command=lambda: flush_all_func(entry_path),width = 300)
    flush_all_btn.grid(row = 3,column = 0,padx = 10,pady = 10)

    flush_user_btn = ctk.CTkButton(frame1, text="FLUSH FOR USER",command=lambda: flush_user_func(entry_username, entry_path),width = 200)
    flush_user_btn.grid(row = 3,column = 1,padx = 10,pady = 10)

    return file_permissions_frame