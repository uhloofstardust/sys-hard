import customtkinter as ctk
import os
from PIL import Image
import subprocess

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Dashboard")
        self.geometry("700x450")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.create_navigation_frame()
        self.create_home_frame()

    def create_navigation_frame(self):
        self.navigation_frame = ctk.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = ctk.CTkLabel(self.navigation_frame, text="  Ubuntu Hardening", font=ctk.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = self.create_nav_button(self.navigation_frame, "PortMaster", self.home_button_event)
        self.frame_2_button = self.create_nav_button(self.navigation_frame, "Frame 2", self.frame_2_button_event)
        self.frame_3_button = self.create_nav_button(self.navigation_frame, "Frame 3", self.frame_3_button_event)

        self.appearance_mode_menu = ctk.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

    def create_home_frame(self):
        self.home_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)
        self.create_usb_port_management_frame(self.home_frame)

    def create_usb_port_management_frame(self, parent_frame):
        # Your code for USB port management here
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

    def create_nav_button(self, parent_frame, text, command):
        return ctk.CTkButton(parent_frame, corner_radius=0, height=40, border_spacing=10, text=text,
                             fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                             anchor="w", command=command)

    def home_button_event(self):
        # Handle the home button event
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        # Handle the frame 2 button event
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        # Handle the frame 3 button event
        self.select_frame_by_name("frame_3")

    def change_appearance_mode_event(self, new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

if __name__ == "__main__":
    app = App()
    app.mainloop()

