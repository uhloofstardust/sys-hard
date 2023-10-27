import os
def block_by_port():
    pass

def block_by_ip_address():
    pass

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

    

def create_firewall_management(parent_frame, ctk):
    firewall_frame = ctk.CTkFrame(parent_frame)
    firewall_frame.pack()

    tab_control = ctk.CTkTabview(master=firewall_frame, height=500, width=800, corner_radius=20)
    tab_control.add('port-management')
    block_by_port_frame = ctk.CTkFrame(master=tab_control.tab('port-management'))
    port_label = ctk.CTkLabel(master=block_by_port_frame, text="Port Management", font=('Ubuntu', 20, 'bold'))
    port_label.grid_configure(padx=10, pady=20, row=0, column=0, columnspan=5)

    port_entry = ctk.CTkEntry(master=block_by_port_frame, placeholder_text='Enter The Port Number', corner_radius=10, width=200)
    port_entry.grid_configure(padx=10, pady=10, columnspan=4, row=1, column=0)

    tcp_protocol_var = ctk.StringVar()
    tcp_checkbox = ctk.CTkCheckBox(master=block_by_port_frame, text="TCP", variable=tcp_protocol_var, onvalue="TCP", offvalue="", font=('Ubuntu', 15, 'bold'))
    tcp_checkbox.grid_configure(column=1, row=2, padx=10)

    udp_protocol_var = ctk.StringVar()
    udp_checkbox = ctk.CTkCheckBox(master=block_by_port_frame, text="UDP", variable=udp_protocol_var, onvalue="UDP", offvalue="", font=('Ubuntu', 15, 'bold'))
    udp_checkbox.grid_configure(column=2, row=2, padx=10)

    # Rest of the code to create components within the frame...

    interface_label = ctk.CTkLabel(master=block_by_port_frame, text="Select The Interface to block :",font=('verdana', 15, 'bold'))
    interface_label.grid_configure(pady=10, padx=10, column=0, row=3)

    input_interface_var = ctk.IntVar()
    input_interface_checkbox = ctk.CTkCheckBox(master=block_by_port_frame, text="Input Interface", variable=input_interface_var,font=('verdana', 15, 'bold'))
    input_interface_checkbox.grid_configure(column=1 ,row=3, padx=10)

    output_interface_var = ctk.IntVar()
    output_interface_checkbox = ctk.CTkCheckBox(master=block_by_port_frame, text="Output Interface", variable=output_interface_var,font=('verdana', 15, 'bold'))
    output_interface_checkbox.grid_configure(column=2, row=3, padx=10)

    forwarding_var = ctk.IntVar()
    forwarding_checkbox = ctk.CTkCheckBox(master=block_by_port_frame, text="Forwarding", variable=forwarding_var,font=('verdana', 15, 'bold'))
    forwarding_checkbox.grid_configure(column=1, row=4, padx=10,pady=(5,20))

    block_button = ctk.CTkButton(master=block_by_port_frame, text="Block", command=block_by_port, corner_radius=10,font=('verdana', 15, 'bold'))
    block_button.grid_configure(padx=10, pady=10, columnspan=4, row=6, column=0)
    block_by_port_frame.pack()
  
    tab_control.add('ip-address-blocker')
    block_by_ip_address_frame = ctk.CTkFrame(master=tab_control.tab('ip-address-blocker'))

 #ip section
    ip_label = ctk.CTkLabel(master=block_by_ip_address_frame, text="Block Ip Address", font=('verdana', 20, 'bold'))
    ip_label.grid_configure(padx=10, pady=20, row=0, column=0, columnspan=5)

    ip_entry = ctk.CTkEntry(master=block_by_ip_address_frame, placeholder_text='Enter ip address', corner_radius=10, width=250)
    ip_entry.grid_configure(padx=10, pady=10, columnspan=4, row=1, column=0)

    protocol_label = ctk.CTkLabel(master=block_by_ip_address_frame, text="Select Protocol :",font=('verdana', 15, 'bold'))
    protocol_label.grid_configure(pady=(20,25), padx=10, column=0, row=2)

    protocol_var = ctk.StringVar()

    tcp_checkbox = ctk.CTkCheckBox(master=block_by_ip_address_frame, text="TCP", variable=tcp_protocol_var, onvalue="TCP", offvalue="",font=('verdana', 15, 'bold'))
    tcp_checkbox.grid_configure(column=1, row=2, padx=10)
    tcp_checkbox.grid_configure(column=1, row=2, padx=10)

    udp_protocol_var = ctk.StringVar()
    udp_checkbox = ctk.CTkCheckBox(master=block_by_ip_address_frame, text="UDP", variable=udp_protocol_var, onvalue="UDP",
                                   offvalue="", font=('verdana', 15, 'bold'))
    udp_checkbox.grid_configure(column=2, row=2, padx=10)

    interface_label = ctk.CTkLabel(master=block_by_ip_address_frame, text="Select The Interface to block :",
                                   font=('verdana', 15, 'bold'))
    interface_label.grid_configure(pady=10, padx=10, column=0, row=3)

    input_interface_var = ctk.IntVar()
    input_interface_checkbox = ctk.CTkCheckBox(master=block_by_ip_address_frame, text="Input Interface",
                                               variable=input_interface_var, font=('verdana', 15, 'bold'))
    input_interface_checkbox.grid_configure(column=1, row=3, padx=10)

    output_interface_var = ctk.IntVar()
    output_interface_checkbox = ctk.CTkCheckBox(master=block_by_ip_address_frame, text="Output Interface",
                                                variable=output_interface_var, font=('verdana', 15, 'bold'))
    output_interface_checkbox.grid_configure(column=2, row=3, padx=10)

    forwarding_var = ctk.IntVar()
    forwarding_checkbox = ctk.CTkCheckBox(master=block_by_ip_address_frame, text="Forwarding", variable=forwarding_var,
                                          font=('verdana', 15, 'bold'))
    forwarding_checkbox.grid_configure(column=1, row=4, padx=10, pady=(5, 20))

    block_button = ctk.CTkButton(master=block_by_ip_address_frame, text="Block", command=block_by_port, corner_radius=10,
                                 font=('verdana', 15, 'bold'))
    block_button.grid_configure(padx=10, pady=10, columnspan=4, row=6, column=0)
    block_by_ip_address_frame.pack()
    # Block by Domain Name Section
    tab_control.add('domain-name-blocker')
    block_by_domain_frame = ctk.CTkFrame(master=tab_control.tab('domain-name-blocker'))

    domain_label = ctk.CTkLabel(master=block_by_domain_frame, text="Domain Name Blocker",font=('verdana', 20, 'bold'))
    domain_label.grid_configure(padx=10, pady=10, row=0, column=0)

    domain_entry = ctk.CTkEntry(master=block_by_domain_frame, placeholder_text='Enter Domain Name', width=220, corner_radius=10)
    domain_entry.grid_configure(padx=10, pady=10, row=1, column=0)

    block_button = ctk.CTkButton(master=block_by_domain_frame, text="Block", command= lambda: block_domains(domain_entry.get()), corner_radius=10)
    block_button.grid_configure(padx=10, pady=10, row=2, column=0, columnspan=2)

    block_history_frame = ctk.CTkScrollableFrame(master=block_by_domain_frame, width=560, height=200, corner_radius=10)
    block_history_frame.grid(column=0,row=4)
    block_by_domain_frame.pack()
   
    # Pack the block_by_port_frame and other frames within tab_control as needed.
    # block_by_port_frame.pack()
    tab_control.pack()

    return firewall_frame
