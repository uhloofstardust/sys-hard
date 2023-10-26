import customtkinter as ctk

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Service Management")
        self.geometry(f"{985}x{500}")

        self.sidebar_frame = ctk.CTkFrame(self, width=100, corner_radius=10)
        self.sidebar_frame.place(relx=0, rely=0, relwidth=0.22, relheight=0.999)

        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w", font=("Verdana", 18))
        self.appearance_mode_label.place(relx=0.1, rely=0.68, relwidth=0.8, relheight=0.078)

        self.appearance_mode_option_menu = ctk.CTkOptionMenu(self.sidebar_frame,
            values=["Light", "Dark", "System"],
            command=self.change_appearance_mode_event, font=("Verdana", 18))
        self.appearance_mode_option_menu.place(relx=0.1, rely=0.75, relwidth=0.8, relheight=0.068)

        self.scaling_label = ctk.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w", font=("Verdana", 18))
        self.scaling_label.place(relx=0.1, rely=0.50, relwidth=0.8, relheight=0.078)

        self.scaling_option_menu = ctk.CTkOptionMenu(self.sidebar_frame,
            values=["80%", "90%", "100%", "110%", "120%"],
            command=self.change_scaling_event, font=("Verdana", 18), hover=True)
        self.scaling_option_menu.place(relx=0.10, rely=0.57, relwidth=0.8, relheight=0.068)

        self.appearance_mode_option_menu.set("Dark")
        self.scaling_option_menu.set("100%")

        self.center_frame = ctk.CTkFrame(self, corner_radius=10)
        self.center_frame.place(relx=0.23, rely=0.0, relwidth=0.760, relheight=0.999)

        title = ctk.CTkLabel(self.center_frame, text="Service Management", font=("Verdana", 35))
        title.place(relx=0.075, rely=0.05)

        # create scrollable frame
        self.scroll = ctk.CTkScrollableFrame(self.center_frame)
        self.scroll.place(relx=0.025, rely=0.23, relwidth=0.95, relheight=0.60)



        lines_list = [
                        'account loaded "active" "running" "accounts_service"',
                        'Keyboard loaded "active" "running" "create_layout"',
                        'hddtemp loaded "inactive" "excited" "firmware"',
                        'mysql loaded "active" "running" "mysql_server"',
                        'network loaded "active" "running" "network_mgm"',
                        'snapd loaded "inactive" "excited" "snapdaemon"',
                        'openVPN loaded "inactive" "excited" "VPN_Config"',
                        'colord loaded "active" "running" "Coloured_Profile"',
                        'lmsensors loaded "inactive" "excited" "init_h/w_sensors"',
                        'cups loaded "active" "running" "cups_scheduler"',
                        'rsyslog loaded "active" "running" "system_logging_service"',
        ]

        objects = []
        for line in lines_list:
            if line != "":
                temp_list = line.split('"')
                temp_0 = temp_list[0]
                temp_0_split = temp_0.split(' ')
                temp_dict = {}
                temp_dict["Service Name"] = temp_0_split[0]
                temp_dict["load"] = temp_0_split[1]
                temp_dict["status"] = temp_list[1]
                temp_dict["sub"] = temp_list[3]
                temp_dict["description"] = temp_list[5]
                objects.append(temp_dict)
 

        # Number each service
        for i, obj in enumerate(objects):
            obj["Number"] = str(i + 1)

       
        for idx, obj in enumerate(objects):

            names = ctk.CTkLabel(master=self.scroll, text=f"{obj['Number']} {obj['Service Name']}", font=("Verdana", 18))
            names.grid(row=idx, column=0, sticky="w", padx=(5, 5), pady=20)

            status = ctk.CTkLabel(master=self.scroll, text=f"{obj['status']}", font=("Verdana", 18))
            status.grid(row=idx, column=1, sticky="w", padx=(5, 10), pady=20)

            decs = ctk.CTkLabel(master=self.scroll, text=f"{obj['description']}", font=("Verdana", 18))
            decs.grid(row=idx, column=2, sticky="w", padx=(5, 10), pady=20)

            if obj["status"] == "active":
                stop = ctk.CTkButton(master = self.scroll, text="STOP",font=("Verdana", 18), width = 100, height = 4)
                stop.grid(row=idx, column=3, sticky="w",padx = (10,20), pady = 20, columnspan = 1)
                

                restart = ctk.CTkButton(master = self.scroll, text="RESTART",font=("Verdana", 18), width =100, height = 4)
                restart.grid(row=idx, column=4, sticky="w", padx = (10,20), pady = 20, columnspan = 1)
            else:
                start = ctk.CTkButton(master = self.scroll, text="START",font=("Verdana", 18), width = 100, height = 4)
                start.grid(row=idx, column=3, sticky="w",padx = (10,20), pady = 20, columnspan = 1)

                
        refresh = ctk.CTkButton(self.center_frame, text="REFRESH", font=("Verdana", 18))
        refresh.place(relx=0.70, rely=0.88, relwidth=0.16, relheight=0.07)

     

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)


app = App()
app.mainloop()
