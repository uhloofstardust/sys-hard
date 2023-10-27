import subprocess
import customtkinter as ctk
def get_service_data():
    process = subprocess.run("systemctl list-units --type=service", shell=True, capture_output=True)
    output = process.stdout.splitlines()
    data = []

    for line in output:
        parts = line.split(maxsplit=4)
        if len(parts) >= 5:
            data.append([parts[0], parts[3]])

    return data[1:]

def start_service(service_name, execute_systemctl_command):
    service_name = service_name.decode().replace(".service", "")
    execute_systemctl_command("start", service_name)

def stop_service(service_name, execute_systemctl_command):
    service_name = service_name.decode().replace(".service", "")
    execute_systemctl_command("stop", service_name)

def restart_service(service_name, execute_systemctl_command):
    service_name = service_name.decode().replace(".service", "")
    execute_systemctl_command("restart", service_name)

def execute_systemctl_command(action, service_name):
    command = f"systemctl {action} {service_name}"
    process = subprocess.run(command, shell=True)

    if process.returncode == 0:
        print(f"Service {service_name} {action}ed successfully")
    else:
        print(f"Failed to {action} service {service_name}")

def refresh_service_list(scroll, create_service_list):
    for widget in scroll.get_frame().winfo_children():
        widget.destroy()
    create_service_list(scroll)

def create_service_list(scroll, ctk):
    data = get_service_data()
    row = 0

    for service in data:
        service_name = service[0]
        status = service[1]

        name_label = ctk.CTkLabel(scroll, text=service_name.decode()[:24] + ("..." if len(service_name) > 24 else ""), font=("Ubuntu", 14))
        name_label.grid(row=row+1, column=0, sticky="w", padx=(3, 3), pady=20)

        status_label = ctk.CTkLabel(scroll, text=status.decode(),font=("Ubuntu", 14))
        status_label.grid(row=row+1, column=1, sticky="w", padx=(3, 3), pady=20)

        if status == b'running':
            stop_button = ctk.CTkButton(scroll, text="stop", font=("Ubuntu", 14), width=100, height=4,
                                        command=lambda service_name=service_name: stop_service(service_name, execute_systemctl_command))
            stop_button.grid(row=row+1, column=3, sticky="w", padx=(10, 20), pady=20, columnspan=1)

            restart_button = ctk.CTkButton(scroll, text="restart", font=("Ubuntu", 14), width=100, height=4,
                                        command=lambda service_name=service_name: restart_service(service_name, execute_systemctl_command))
            restart_button.grid(row=row+1, column=4, sticky="w", padx=(10, 20), pady=20, columnspan=1)
        else:
            start_button = ctk.CTkButton(scroll, text="start", font=("Ubuntu", 14), width=100, height=4,
                                        command=lambda service_name=service_name: start_service(service_name, execute_systemctl_command))
            start_button.grid(row=row+1, column=3, sticky="w", padx=(10, 20), pady=20, columnspan=1)

        row += 1

def create_service_management(parent_frame, ctk):

    mainFrame = ctk.CTkFrame(parent_frame)
    mainFrame.pack()
    title = ctk.CTkLabel(mainFrame,text = "Service Management",font = ('Ubuntu',24))
    title.pack(padx = 10,pady = 10)
    service_frame = ctk.CTkFrame(mainFrame, corner_radius=0)
    center_frame = ctk.CTkFrame(service_frame, corner_radius=10)
    scroll = ctk.CTkScrollableFrame(center_frame,width=800, height=600)
    refresh_button = ctk.CTkButton(center_frame, text="REFRESH", font=("Ubuntu", 14), command=lambda: refresh_service_list(scroll, create_service_list))

    service_frame.pack(expand=True, fill="both")
    center_frame.pack(expand=True, fill="both")
    scroll.pack()

    head1 = ctk.CTkLabel(scroll,text = "Service Name",font = ('Ubuntu',18))
    head1.grid(row=0, column=0, sticky="w", padx=(3, 3), pady=20)

    head2 = ctk.CTkLabel(scroll,text = "Status",font = ('Ubuntu',18))
    head2.grid(row=0, column=1, sticky="w", padx=(3, 3), pady=20,columnspan=2)

    head3 = ctk.CTkLabel(scroll,text = "Action",font = ('Ubuntu',18))
    head3.grid(row=0, column=3, sticky="w", padx = 40,pady=20)

    create_service_list(scroll, ctk)
    refresh_button.pack(side = 'right',padx = 10,pady = 10)

    return service_frame

