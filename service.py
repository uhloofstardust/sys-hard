import subprocess

import customtkinter as ctk
from CTkTable import *
import subprocess as sb
def getdata():
    process = sb.run("systemctl list-units --type=service", shell=True, capture_output=True)
    output = process.stdout.splitlines()
    a = list()
    for i in output:
        x = i.split(maxsplit=4)
        if (len(x) == 0):
            break
        a.append(x)
    data = list()
    for i in a:
        d = [i[0], i[3], i[4]]
        data.append(d)
    return data

def start_service(service_name):
    service_name=str(service_name).removeprefix("b'").removesuffix(".service'")
    print(f"Starting service: {service_name}")
    process=subprocess.run(f'systemctl start {service_name}',shell=True)
    if(process.returncode==0):
        print('service started successfully')
        refresh()


def stop_service(service_name):
    service_name = str(service_name).removeprefix("b'").removesuffix(".service'")
    print(f"Stopping service: {service_name}")
    process = subprocess.run(f'systemctl stop {service_name}', shell=True)
    if (process.returncode == 0):
        print('service Stopped successfully')
        refresh()

def restart_service(service_name):
    service_name = str(service_name).removeprefix("b'").removesuffix(".service'")
    print(f"Restarting service: {service_name}")
    process = subprocess.run(f'systemctl restart {service_name}', shell=True)
    if (process.returncode == 0):
        print('service restarted successfully')
        refresh()

def main():
    data=getdata()
    Font_tuple = ("Getona", 30, "bold")
    frame = ctk.CTkScrollableFrame(root, corner_radius=10, orientation='vertical', label_text="Service Dashboard",
                                   height=root.winfo_screenheight() - 200, width=root.winfo_screenwidth() - 40,
                                   label_font=Font_tuple)

    frame.grid(sticky="nsew", columnspan=5, column=0, row=0)

    t1 = ('Getona', 20, 'bold')
    t2 = ('Ubuntu', 16)
    ctk.CTkLabel(text='Service Name', master=frame, font=t1).grid(row=0, column=0)
    ctk.CTkLabel(text='Status', master=frame, font=t1).grid(row=0, column=1)
    ctk.CTkLabel(text='Description', master=frame, font=t1).grid(row=0, column=2)
    ctk.CTkLabel(text='Action', master=frame, font=t1).grid(row=0, column=3)
    for i in range(1, len(data)):
        service_name = data[i][0]
        status = data[i][1]
        description = data[i][2]

        ctk.CTkLabel(text=service_name, master=frame, font=t2).grid(row=i, column=0, padx=5, pady=3, sticky="")
        ctk.CTkLabel(text=status, master=frame, font=t2).grid(row=i, column=1, padx=5, pady=3, sticky='')
        ctk.CTkLabel(text=description, master=frame, font=t2).grid(row=i, column=2, padx=5, pady=3, sticky='')

        if status == b'running':
            ctk.CTkButton(text='Restart', master=frame, command=lambda name=service_name: restart_service(name)).grid(
                row=i, column=3, padx=5, pady=3)
            ctk.CTkButton(text='Stop', master=frame, fg_color='red', corner_radius=5, hover_color='#AA0000',
                          command=lambda name=service_name: stop_service(name)).grid(row=i, column=4, padx=5, pady=3)
        else:
            ctk.CTkButton(text='Start', master=frame, fg_color='green', corner_radius=5, hover_color='#006400',
                          command=lambda name=service_name: start_service(name)).grid(row=i, column=3, padx=5, pady=3)

def refresh():
    main()
root = ctk.CTk()
main()
root.mainloop()
