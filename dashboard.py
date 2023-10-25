import customtkinter as ctk
import os
import json
from PIL import Image
import subprocess

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("dashboard")
        self.geometry("700x450")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "")
        self.logo_image = ctk.CTkImage(Image.open(os.path.join(image_path, "./assets/ubuntu.png")), size=(26, 26))
        self.large_test_image = ctk.CTkImage(Image.open(os.path.join(image_path, "./assets/usb_port.png")), size=(500, 150))
        self.image_icon_image = ctk.CTkImage(Image.open(os.path.join(image_path, "./assets/usb_port.png")), size=(20, 20))
        self.home_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "./assets/usb_port.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "./assets/usb_port.png")), size=(30, 30))
        self.chat_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "./assets/user_manage.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "./assets/user_manage.png")), size=(30, 30))
        self.add_user_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "./assets/ubuntu.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "./assets/ubuntu.png")), size=(30, 30))

        self.navigation_frame = ctk.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = ctk.CTkLabel(self.navigation_frame, text="  Ubuntu Hardening", image=self.logo_image,
                                                             compound="left", font=ctk.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="PortMaster",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Frame 2",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Frame 3",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_menu = ctk.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create usb port management frame
        self.home_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)





# ***************************************************edited****************************************************



        rules_conf_file = '/etc/usbguard/rules.conf'
        #rules_conf_file = './sample.txt'

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



        title = ctk.CTkLabel(master=self.home_frame,text="USB PORTS MANAGEMENT",font=("Arial",24), pady=14)
        title.pack()
        frame = ctk.CTkFrame(self.home_frame)
        frame.pack()

        circle_labels = []

        for index, obj in enumerate(objects):
            circle = ctk.CTkLabel(frame, text="●", font=("Arial", 24), width=1, anchor="w")
            circle.grid(row=index, column=0, padx=10, pady=5)
            circle_labels.append(circle)

            label = ctk.CTkLabel(frame, font=("Arial", 16),text=f"ID: {obj['id']}, Name: {obj['name']}")
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









# **********************************************************************************************************







    #     self.home_frame_button_1 = ctk.CTkButton(self.home_frame, text="", image=self.image_icon_image)
    #     self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
    #     self.home_frame_button_2 = ctk.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="right")
    #     self.home_frame_button_2.grid(row=2, column=0, padx=20, pady=10)
    #     self.home_frame_button_3 = ctk.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="top")
    #     self.home_frame_button_3.grid(row=3, column=0, padx=20, pady=10)
    #     self.home_frame_button_4 = ctk.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="bottom", anchor="w")
    #     self.home_frame_button_4.grid(row=4, column=0, padx=20, pady=10)

    #     # create second frame
    #     self.second_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")

    #     # create third frame
    #     self.third_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")

    #     # select default frame
    #     self.select_frame_by_name("home")

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

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def change_appearance_mode_event(self, new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()

