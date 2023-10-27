import subprocess
def create_usb_port_management_frame(parent_frame,ctk):
        rules_conf_file = '/etc/usbguard/rules.conf'
        lines_list = []

        try:
            with open(rules_conf_file, 'r') as file:
                for line in file:
                    lines_list.append(line.strip())
        except FileNotFoundError:
            print(f"File not found: {rules_conf_file}")
        except Exception as e:
            print(f"An error occurred: {e}")

        objects = []

        for line in lines_list:
            if line != "":
                temp_list = line.split('"')
                temp_0 = temp_list[0]
                temp_0_split = temp_0.split(' ')
                temp_dict = {}
                temp_dict["status"] = temp_0_split[0]
                temp_dict["id"] = temp_0_split[2]
                temp_dict["serial"] = temp_list[1]
                temp_dict["name"] = temp_list[3]
                objects.append(temp_dict)

        def change_rule_status(id_to_block, new_status):
            with open(rules_conf_file, 'r') as file:
                lines = file.readlines()

            for i, line in enumerate(lines):
                if id_to_block in line:
                    if "allow" in line:
                        lines[i] = line.replace("allow", new_status)
                    elif "block" in line:
                        lines[i] = line.replace("block", new_status)

            with open(rules_conf_file, 'w') as file:
                file.writelines(lines)
            subprocess.run("pkexec service usbguard restart", shell=True)

        def update_status(index, new_status):
            update_display()
            change_rule_status(objects[index]["id"], new_status)
            objects[index]["status"] = new_status
            update_display()

        title = ctk.CTkLabel(parent_frame, text="USB PORTS MANAGEMENT", font=("Arial", 24), pady=14)
        title.pack()
        frame = ctk.CTkFrame(parent_frame)
        frame.pack()

        circle_labels = []

        for index, obj in enumerate(objects):
            circle = ctk.CTkLabel(frame, text="●", font=("Arial", 24), width=1, anchor="w")
            circle.grid(row=index, column=0, padx=10, pady=5)
            circle_labels.append(circle)

            label = ctk.CTkLabel(frame, font=("Arial", 16), text=f"ID: {obj['id']}, Name: {obj['name']}")
            label.grid(row=index, column=1, padx=10, pady=8)

            allow_button = ctk.CTkButton(frame, text="Allow", command=lambda i=index: update_status(i, "allow"))
            allow_button.grid(row=index, column=2, padx=5, pady=8)

            block_button = ctk.CTkButton(frame, text="Block", command=lambda i=index: update_status(i, "block"))
            block_button.grid(row=index, column=3, padx=5, pady=8)

        def update_display():
            for i, obj in enumerate(objects):
                if obj["status"] == "block":
                    circle_labels[i].configure(text_color="red")
                else:
                    circle_labels[i].configure(text_color="green")

        update_display()

