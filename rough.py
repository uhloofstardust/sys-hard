import tkinter as tk
from tkinter import messagebox

def save_config():
    config_values = {
        "historynumber": historynumber_var.get(),
        "minlen": minlen_var.get(),
        "minclass": minclass_var.get(),
        "maxrepeat": maxrepeat_var.get(),
        "dictcheck": dictcheck_var.get(),
        "usercheck": usercheck_var.get(),
        "enforceroot": enforceroot_var.get(),
        "retry": retry_var.get(),
    }

    # Define the system files and their corresponding lines
    config_files = {
        "minlen": ("/etc/security/pwquality.conf", "minlen ="),
        "minclass": ("/etc/security/pwquality.conf", "minclass ="),
        "maxrepeat": ("/etc/security/pwquality.conf", "maxrepeat ="),
        "dictcheck": ("/etc/security/pwquality.conf", "dictcheck ="),
        "usercheck": ("/etc/security/pwquality.conf", "usercheck ="),
        "enforceroot": ("/etc/security/pwquality.conf", "enforce_for_root"),
        "retry": ("/etc/security/pwquality.conf", "retry ="),
    }

    for key, value in config_values.items():
        file_path, line_prefix = config_files.get(key, (None, None))
        if file_path and line_prefix is not None:
            with open(file_path, 'r') as file:
                lines = file.readlines()

            found = False
            for i, line in enumerate(lines):
                if line.startswith(line_prefix):
                    lines[i] = f"{line_prefix} {value}\n"
                    found = True
                    break

            if not found:
                lines.append(f"{line_prefix} {value}\n")

            with open(file_path, 'w') as file:
                file.writelines(lines)

    messagebox.showinfo("Success", "Configuration saved!")

root = tk.Tk()
root.title("System Configuration")

# Create variables to store user inputs
historynumber_var = tk.IntVar()
minlen_var = tk.IntVar()
minclass_var = tk.IntVar()
maxrepeat_var = tk.IntVar()
dictcheck_var = tk.IntVar()
usercheck_var = tk.IntVar()
enforceroot_var = tk.IntVar()
retry_var = tk.IntVar()

# Create labels, entry fields, and checkboxes for each configuration option
options = [
    {"name": "historynumber", "label": "History Number:"},
    {"name": "minlen", "label": "Minimum Length:"},
    {"name": "minclass", "label": "Minimum Classes:"},
    {"name": "maxrepeat", "label": "Maximum Repeat:"},
    {"name": "dictcheck", "label": "Dictionary Check:"},
    {"name": "usercheck", "label": "User Check:"},
    {"name": "enforceroot", "label": "Enforce for Root:"},
    {"name": "retry", "label": "Retry:"},
]

for i, option in enumerate(options):
    label = tk.Label(root, text=option["label"])
    label.grid(row=i, column=0, sticky='w')

    entry = tk.Entry(root, textvariable=option["name"] + "_var")
    entry.grid(row=i, column=1, sticky='w')

    enable_button = tk.Button(root, text="Enable", command=save_config)
    enable_button.grid(row=i, column=2)

    disable_button = tk.Button(root, text="Disable", command=save_config)
    disable_button.grid(row=i, column=3)

root.mainloop()

