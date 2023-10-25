import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox


rules = ['minlen', 'minclass', 'maxrepeat', 'dictcheck', 'usercheck', 'retry']




def change_rule_status(filepath, rule, value=0, enable=True):
    newlines = []
    
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    for line in lines:
        if (line.strip().startswith('# '+rule) or line.strip().startswith(rule)):
            if enable:
                newlines.append(rule + '=' + str(value) + '\n')
            else:
                newlines.append('# ' + rule + '=' + str(value) + '\n')
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
        change_rule_status('/etc/security/pwquality.conf', rule, value, enable)
    elif rule in ['enforce_for_root']:
        add_rule('/etc/security/pwquality.conf', rule, enable)

root = ctk.CTk()
root.title("System Configuration")


historynumber_var = ctk.CTkEntry(master=root)
minlen_var = ctk.CTkEntry(master=root)
minclass_var = ctk.CTkEntry(master=root)
maxrepeat_var = ctk.CTkEntry(master=root)
dictcheck_var = ctk.CTkEntry(master=root)
usercheck_var = ctk.CTkEntry(master=root)
enforceroot_var = ctk.CTkEntry(master=root)
retry_var = ctk.CTkEntry(master=root)


options = [
    {"name": "minlen", "label": "Minimum Length:"},
    {"name": "minclass", "label": "Minimum Classes:"},
    {"name": "maxrepeat", "label": "Maximum Repeat:"},
    {"name": "dictcheck", "label": "Dictionary Check:"},
    {"name": "usercheck", "label": "User Check:"},
    {"name": "enforceroot", "label": "Enforce for Root:"},
    {"name": "retry", "label": "Retry:"},
]


# minlen 

minlen_label = ctk.CTkLabel(root, text=options[0]['label'])
minlen_label.grid(row=0, column=0, sticky='w')

minlen_entry = ctk.CTkEntry(master=root, placeholder_text='aaa', width=150, height=25, border_width=2, corner_radius=5)
minlen_entry.grid(row=0, column=1, sticky='w',padx=20,pady=10)

minlen_enable_button = ctk.CTkButton(root, text="Enable", command=lambda : password_policy('minlen', minlen_entry.get(), True))
minlen_enable_button.grid(row=0, column=2,padx = 10,pady = 10)

minlen_disable_button = ctk.CTkButton(root, text="Disable", command=lambda : password_policy('minlen', 14, False))
minlen_disable_button.grid(row=0, column=3,padx = 10,pady = 10)


# minclass 

minclass_label = ctk.CTkLabel(root, text=options[0]['label'])
minclass_label.grid(row=1, column=0, sticky='w')

minclass_entry = ctk.CTkEntry(master=root, placeholder_text='aaa', width=150, height=25, border_width=2, corner_radius=5)
minclass_entry.grid(row=1, column=1, sticky='w',padx=20,pady=10)

minclass_enable_button = ctk.CTkButton(root, text="Enable", command=lambda : password_policy('minclass', minclass_entry.get(), True))
minclass_enable_button.grid(row=1, column=2,padx = 10,pady = 10)

minclass_disable_button = ctk.CTkButton(root, text="Disable", command=lambda : password_policy('minclass', minclass_entry.get(), False))
minclass_disable_button.grid(row=1, column=3,padx = 10,pady = 10)


# maxrepeat 

maxrepeat_label = ctk.CTkLabel(root, text=options[0]['label'])
maxrepeat_label.grid(row=2, column=0, sticky='w')

maxrepeat_entry = ctk.CTkEntry(master=root, placeholder_text='aaa', width=150, height=25, border_width=2, corner_radius=5)
maxrepeat_entry.grid(row=2, column=1, sticky='w',padx=20,pady=10)

maxrepeat_enable_button = ctk.CTkButton(root, text="Enable", command=lambda : password_policy('maxrepeat', maxrepeat_entry.get(), True))
maxrepeat_enable_button.grid(row=2, column=2,padx = 10,pady = 10)

maxrepeat_disable_button = ctk.CTkButton(root, text="Disable", command=lambda : password_policy('maxrepeat', maxrepeat_entry.get(), False))
maxrepeat_disable_button.grid(row=2, column=3,padx = 10,pady = 10)


# dictcheck 

dictcheck_label = ctk.CTkLabel(root, text=options[0]['label'])
dictcheck_label.grid(row=3, column=0, sticky='w')

dictcheck_entry = ctk.CTkEntry(master=root, placeholder_text='ab', width=150, height=25, border_width=2, corner_radius=5)
dictcheck_entry.grid(row=3, column=1, sticky='w',padx=20,pady=10)

dictcheck_enable_button = ctk.CTkButton(root, text="Enable", command=lambda : password_policy('dictcheck', dictcheck_entry.get(), True))
dictcheck_enable_button.grid(row=3, column=2,padx = 10,pady = 10)

dictcheck_disable_button = ctk.CTkButton(root, text="Disable", command=lambda : password_policy('dictcheck', dictcheck_entry.get(), False))
dictcheck_disable_button.grid(row=3, column=3,padx = 10,pady = 10)


# usercheck 

usercheck_label = ctk.CTkLabel(root, text=options[0]['label'])
usercheck_label.grid(row=4, column=0, sticky='w')

usercheck_entry = ctk.CTkEntry(master=root, placeholder_text='usercheck', width=150, height=25, border_width=2, corner_radius=5)
usercheck_entry.grid(row=4, column=1, sticky='w',padx=20,pady=10)

usercheck_enable_button = ctk.CTkButton(root, text="Enable", command=lambda : password_policy('usercheck', usercheck_entry.get(), True))
usercheck_enable_button.grid(row=4, column=2,padx = 10,pady = 10)

usercheck_disable_button = ctk.CTkButton(root, text="Disable", command=lambda : password_policy('usercheck', usercheck_entry.get(), False))
usercheck_disable_button.grid(row=4, column=3,padx = 10,pady = 10)



# enforce_for_root

enforce_for_root_label = ctk.CTkLabel(root, text=options[0]['label'])
enforce_for_root_label.grid(row=5, column=0, sticky='w')

enforce_for_root_entry = ctk.CTkEntry(master=root, placeholder_text='enforce_for_root', width=150, height=25, border_width=2, corner_radius=5)
enforce_for_root_entry.grid(row=5, column=1, sticky='w', padx=20, pady=10)

enforce_for_root_enable_button = ctk.CTkButton(root, text="Enable", command=lambda: password_policy('enforce_for_root', enforce_for_root_entry.get(), True))
enforce_for_root_enable_button.grid(row=5, column=2, padx=10, pady=10)

enforce_for_root_disable_button = ctk.CTkButton(root, text="Disable", command=lambda: password_policy('enforce_for_root', enforce_for_root_entry.get(), False))
enforce_for_root_disable_button.grid(row=5, column=3, padx=10, pady=10)


# retry

retry_label = ctk.CTkLabel(root, text='retry')
retry_label.grid(row=6, column=0, sticky='w')

retry_entry = ctk.CTkEntry(master=root, placeholder_text='retry', width=150, height=25, border_width=2, corner_radius=5)
retry_entry.grid(row=6, column=1, sticky='w', padx=20, pady=10)

retry_enable_button = ctk.CTkButton(root, text="Enable", command=lambda: password_policy('retry', retry_entry.get(), True))
retry_enable_button.grid(row=6, column=2, padx=10, pady=10)

retry_disable_button = ctk.CTkButton(root, text="Disable", command=lambda: password_policy('retry', retry_entry.get(), False))
retry_disable_button.grid(row=6, column=3, padx=10, pady=10)






root.mainloop()
