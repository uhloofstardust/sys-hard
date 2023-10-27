
import customtkinter as ctk
import subprocess
from CTkMessagebox import CTkMessagebox


def send_log(IP_address_input):
  ip = IP_address_input.get()
  if(ip == ""):
    IP_address_input.configure(fg_color = "red")
    ctkmsg = CTkMessagebox(title="Info", message="Need to specify IP address")
    if(ctkmsg.get() == 'OK'):
        IP_address_input.configure(fg_color="#ab23ff")
  else:
    subprocess.run(f"logging -n {ip} -P 541 -f /var/logs/syslog --tcp", shell=True)

def create_logging(parent_frame, ctk):
    title = ctk.CTkLabel(parent_frame, text="Remote Logging",font = ('Arial',24))
    title.pack(side=ctk.TOP, padx=10, pady=(20,10))
    ip_frame = ctk.CTkFrame(parent_frame)
    IP_address_input = ctk.CTkEntry(ip_frame, placeholder_text="IP Address",width = 300)
    IP_address_input.grid(row = 0,column = 0,padx = 10,pady = 10)
    
    submit_button = ctk.CTkButton(ip_frame, text="Submit", command=lambda: send_log(IP_address_input))
    submit_button.grid(row = 1,column = 0,padx = 10,pady = 10)
    ip_frame.pack()
    
    description_frame = ctk.CTkFrame(master = parent_frame)
    description_frame.pack(padx = 15,pady = 15)
    textbox = ctk.CTkTextbox(master=description_frame, width=600,fg_color = "transparent",font = ('Arial',14))
    textbox.pack(padx = 10,pady = 10)
    textbox.insert("0.0", """Why do we use it?
It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).
""")

