import customtkinter as ctk
import subprocess

def send_log(ip):
  subprocess.run(f"logging -n {ip} -P 541 -f /var/logs/syslog --tcp", shell=True)

def create_logging(parent_frame, ctk):
    ip_frame = ctk.CTkFrame(parent_frame, corner_radius=0)
    title = ctk.CTkLabel(ip_frame, text="Remote Logging", font=("Ubuntu", 35))
    IP_address_input = ctk.CTkEntry(ip_frame, placeholder_text="IP Address", font=("Ubuntu", 20))
    ip = IP_address_input.get()
    submit_button = ctk.CTkButton(ip_frame, text="Submit", font=("Ubuntu", 20), command=lambda: send_log(ip))

    ip_frame.pack(expand=True, fill="both")
    ip_frame.pack(expand=True, fill="both")
    title.place(relx=0.075, rely=0.05)
    IP_address_input.place(relx=0.2, rely=0.5, relwidth=0.3)
    submit_button.place(relx=0.6, rely=0.5, relwidth=0.2)

    return ip_frame
