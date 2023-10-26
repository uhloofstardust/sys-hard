import platform
import os
from customtkinter import *
def block_domains(domains):
    try:
        # Determine the path to the hosts file based on the operating system
        hosts_file_path = "/etc/hosts"
        # Check if the script is run with administrative privileges
        if not os.geteuid() == 0:
            print("Please run this script with administrative privileges (e.g., using sudo).")
            return

        # Check if the hosts file exists
        if not os.path.exists(hosts_file_path):
            print(f"Hosts file not found: {hosts_file_path}")
            return

        # Add entries to block the specified domains
        with open(hosts_file_path, "a") as hosts_file:
                with open(hosts_file_path, "r") as file:
                    if any(domains in line for line in file):
                        print(f"Domain '{domains}' is already blocked.")
                    else:
                        hosts_file.write(f"127.0.0.1 {domains}\n")
                        print(f"Blocking domain: {domains}")

    except Exception as e:
        print(f"An error occurred: {e}")

def getdomain():
    domain = inputfied.get()
    domain = domain.strip()
    block_domains(domain)
app = CTk()
scrollable = CTkScrollableFrame(master=app,
                                width=560,
                                height=200,
                                corner_radius=10)
app.geometry("600x500")
set_appearance_mode("dark")
inputfied = CTkEntry(master=app,width=220,placeholder_text="Enter domain name")
inputfied.pack(padx = 10,pady = 10)
btk = CTkButton(master=app,text="submit",command=getdomain)
btk.pack(padx = 10,pady = 10)
scrollable.pack(padx = 10,pady = 10)
with open('/etc/hosts','r') as file:
    data =  [line  for line in file if 'www.' in line]
    print(data)

for i in data:
   s=i.split()
   label=CTkLabel(master=scrollable,text=s[1]).pack()
app.mainloop()
