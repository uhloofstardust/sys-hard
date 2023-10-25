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
inputfied = CTkEntry(master=scrollable,width=220,placeholder_text="Enter domain name")
app.geometry("600x500")
set_appearance_mode("dark")
btk = CTkButton(master=app,text="submit",command=getdomain)
btk.place(relx=0.5,rely=0.59,anchor="center")
scrollable.place(relx=0.5, rely=0.3, anchor=CENTER)
inputfied.pack()
app.mainloop()