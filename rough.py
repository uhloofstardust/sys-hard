import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox



# rules in file


rules = ['minlen', 'minclass', 'maxrepeat', 'dictcheck', 'usercheck', 'retry']




def change_rule_status(filepath, rule, value=0, enable=True):
    newlines = []
    
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    for line in lines:
        if (line.strip().startswith('# '+rule) or line.strip().startswith(rule)):
            if enable:
                newlines.append(rule + '=' + value + '\n')
            else:
                newlines.append('# ' + rule + '=' + value + '\n')
        else:
            newlines.append(line)
    
    with open(filepath, 'w') as f:
        f.writelines(newlines)



def add_rule(filepath, rule, enable=True):
    newlines = []
    
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    for line in lines:
        if (line.strip().startswith('# '+rule) or line.strip().startswith(rule)):
            if enable:
                newlines.append(rule + '\n')
            else:
                newlines.append('# ' + rule + '\n')
        else:
            newlines.append(line)
    
    with open(filepath, 'w') as f:
        f.writelines(newlines)



def password_policy(rule, value=0, enable=True):
    if rule in rules:
        change_rule_status('/etc/security/pwquality', rule, value, enable)
    elif rule in ['enforce_for_root']:
        add_rule('/etc/security/pwquality', rule, enable)

root = ctk.CTk()
root.title("System Configuration")

# Create variables to store user inputs
historynumber_var = ctk.CTkEntry(master=root)
minlen_var = ctk.CTkEntry(master=root)
minclass_var = ctk.CTkEntry(master=root)
maxrepeat_var = ctk.CTkEntry(master=root)
dictcheck_var = ctk.CTkEntry(master=root)
usercheck_var = ctk.CTkEntry(master=root)
enforceroot_var = ctk.CTkEntry(master=root)
retry_var = ctk.CTkEntry(master=root)

# Create labels, entry fields, and checkboxes for each configuration option
options = [

    {"name": "minlen", "label": "Minimum Length:"},
    {"name": "minclass", "label": "Minimum Classes:"},
    {"name": "maxrepeat", "label": "Maximum Repeat:"},
    {"name": "dictcheck", "label": "Dictionary Check:"},
    {"name": "usercheck", "label": "User Check:"},
    {"name": "enforceroot", "label": "Enforce for Root:"},
    {"name": "retry", "label": "Retry:"},
]

for i, option in enumerate(options):
    label = ctk.CTkLabel(root, text=option["label"])
    label.grid(row=i, column=0, sticky='w')

    entry = ctk.CTkEntry(master=root,
                               placeholder_text=option["name"],
                               width=150,
                               height=25,
                               border_width=2,
                               corner_radius=5)
    entry.grid(row=i, column=1, sticky='w',padx=20,pady=10)

    enable_button = ctk.CTkButton(root, text="Enable", command=lambda : password_policy(rules[i]))
    enable_button.grid(row=i, column=2,padx = 10,pady = 10)

    disable_button = ctk.CTkButton(root, text="Disable", command=lambda : password_policy(rules[i]))
    disable_button.grid(row=i, column=3,padx = 10,pady = 10)

root.mainloop()

