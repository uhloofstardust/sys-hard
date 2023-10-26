import subprocess

def get_service_data():
    process = subprocess.run("systemctl list-units --type=service", shell=True, capture_output=True)
    output = process.stdout.splitlines()
    data = []

    for line in output:
        parts = line.split(maxsplit=4)
        if len(parts) >= 5:
            data.append([parts[0], parts[3]])

    return data

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

        name_label = ctk.CTkLabel(scroll, text=service_name.decode()[:24] + ("..." if len(service_name) > 24 else ""), font=("Verdana", 18))
        name_label.grid(row=row, column=0, sticky="w", padx=(3, 3), pady=20)

        status_label = ctk.CTkLabel(scroll, text=status.decode(), font=("Verdana", 18))
        status_label.grid(row=row, column=1, sticky="w", padx=(3, 3), pady=20)

        if status == b'running':
            stop_button = ctk.CTkButton(scroll, text="STOP", font=("Verdana", 18), width=100, height=4,
                                        command=lambda service_name=service_name: stop_service(service_name, execute_systemctl_command))
            stop_button.grid(row=row, column=3, sticky="w", padx=(10, 20), pady=20, columnspan=1)

            restart_button = ctk.CTkButton(scroll, text="RESTART", font=("Verdana", 18), width=100, height=4,
                                        command=lambda service_name=service_name: restart_service(service_name, execute_systemctl_command))
            restart_button.grid(row=row, column=4, sticky="w", padx=(10, 20), pady=20, columnspan=1)
        else:
            start_button = ctk.CTkButton(scroll, text="START", font=("Verdana", 18), width=100, height=4,
                                        command=lambda service_name=service_name: start_service(service_name, execute_systemctl_command))
            start_button.grid(row=row, column=3, sticky="w", padx=(10, 20), pady=20, columnspan=1)

        row += 1

def create_service_management(parent_frame, ctk):
    service_frame = ctk.CTkFrame(parent_frame, corner_radius=0)
    center_frame = ctk.CTkFrame(service_frame, corner_radius=10)
    title = ctk.CTkLabel(center_frame, text="Service Management", font=("Verdana", 35))
    scroll = ctk.CTkScrollableFrame(center_frame)
    refresh_button = ctk.CTkButton(center_frame, text="REFRESH", font=("Verdana", 18), command=lambda: refresh_service_list(scroll, create_service_list))

    service_frame.pack(expand=True, fill="both")
    center_frame.pack(expand=True, fill="both")
    title.place(relx=0.075, rely=0.05)
    scroll.place(relx=0.025, rely=0.23, relwidth=0.95, relheight=0.60)
    create_service_list(scroll, ctk)
    refresh_button.place(relx=0.70, rely=0.88, relwidth=0.16, relheight=0.07)

    return service_frame
