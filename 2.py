import tkinter
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{1920}x{1080}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)


        # create radiobutton frame
        self.radiobutton_frame = customtkinter.CTkFrame(self, height=800)
        self.radiobutton_frame.grid(row=1, column=1,rowspan=4, columnspan=1, sticky="nsew")
        # self.radiobutton_frame.grid(pady=60, padx=60, fill="both", expand=True)

        # self.radio_var = tkinter.IntVar(value=0)
        # # self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame)
        # # self.label_radio_group.grid(row=0, column=3, columnspan=1, padx=10, pady=10, sticky="")
        # self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text='Create User', font=('Ubuntu', 20), variable=self.radio_var, value=0)
        # # self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        # self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text='Delete User', font=('Ubuntu', 20), variable=self.radio_var, value=1)
        # # self.radio_button_2.grid(row=1, column=3, pady=10, padx=20, sticky="n")
        # self.radio_button_3 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text='Change Password', font=('Ubuntu', 20), variable=self.radio_var, value=2)
        # # self.radio_button_3.grid(row=1, column=4, pady=10, padx=20, sticky="n")
        # self.radio_button_4 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, text='Give Sudo Access', font=('Ubuntu', 20), variable=self.radio_var, value=3)
        # # self.radio_button_3.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        # self.radio_button_5 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, text='Restrict Sudo Access', font=('Ubuntu', 20), variable=self.radio_var, value=4)
        # # self.radio_button_3.grid(row=2, column=3, pady=10, padx=20, sticky="n")
        # self.radio_button_1.place(relx=0.15, rely=0.45)
        # self.radio_button_2.place(relx=0.45, rely=0.45)
        # self.radio_button_3.place(relx=0.70, rely=0.45)
        # self.radio_button_4.place(relx=0.15, rely=0.55)
        # self.radio_button_5.place(relx=0.45, rely=0.55)


        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))

        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                                       values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                               values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        self.label_1 = customtkinter.CTkLabel(master=self.radiobutton_frame, text='User Management', font=('Ubuntu', 35),
                                              justify=customtkinter.LEFT)
        # # label_1.grid(row=0, column=0, columnspan=1, padx=20, pady=20)
        self.label_1.place(relx=0.3, rely=0.05)

        self.label_2 = customtkinter.CTkLabel(master=self.radiobutton_frame, text='Create User:', font=('Ubuntu', 22),
                                             justify=customtkinter.LEFT)
        # label_2.grid(row=1, column=0, columnspan=1, padx=20, pady=20)
        self.label_2.place(relx=0.1, rely=0.2)

        self.label_3 = customtkinter.CTkLabel(master=self.radiobutton_frame, text='Set Password:', font=('Ubuntu', 22),
                                              justify=customtkinter.LEFT)
        # label_2.grid(row=1, column=0, columnspan=1, padx=20, pady=20)
        self.label_3.place(relx=0.1, rely=0.3)

        self.label_4 = customtkinter.CTkLabel(master=self.radiobutton_frame, text='Create Group:', font=('Ubuntu', 22),
                                              justify=customtkinter.LEFT)
        # label_2.grid(row=1, column=0, columnspan=1, padx=20, pady=20)
        self.label_4.place(relx=0.1, rely=0.45)

        self.label_5 = customtkinter.CTkLabel(master=self.radiobutton_frame, text='Grant Sudo Access:', font=('Ubuntu', 22),
                                              justify=customtkinter.LEFT)
        # label_2.grid(row=1, column=0, columnspan=1, padx=20, pady=20)
        self.label_5.place(relx=0.1, rely=0.55)

        self.label_6 = customtkinter.CTkLabel(master=self.radiobutton_frame, text='Prevent Sudo Access:',
                                              font=('Ubuntu', 22),
                                              justify=customtkinter.LEFT)
        # label_2.grid(row=1, column=0, columnspan=1, padx=20, pady=20)
        self.label_6.place(relx=0.1, rely=0.65)

        self.label_7 = customtkinter.CTkLabel(master=self.radiobutton_frame, text='Delete User:',
                                              font=('Ubuntu', 22),
                                              justify=customtkinter.LEFT)
        # label_2.grid(row=1, column=0, columnspan=1, padx=20, pady=20)
        self.label_7.place(relx=0.1, rely=0.75)

        self.entry_1 = customtkinter.CTkEntry(master=self.radiobutton_frame, placeholder_text="Username", font=('Ubuntu', 15))
        # entry_1.grid(row=1, column=1, columnspan=4, padx=10, pady=10)
        self.entry_1.place(relx=0.3, rely=0.2, relwidth=0.2)

        self.entry_2 = customtkinter.CTkEntry(master=self.radiobutton_frame, placeholder_text="Username", font=('Ubuntu', 15))
        # entry_1.grid(row=1, column=1, columnspan=4, padx=10, pady=10)
        self.entry_2.place(relx=0.3, rely=0.3, relwidth=0.2)
        self.entry_3 = customtkinter.CTkEntry(master=self.radiobutton_frame, placeholder_text="Password", show="*",
                                              font=('Ubuntu', 15))
        # entry_1.grid(row=1, column=1, columnspan=4, padx=10, pady=10)
        self.entry_3.place(relx=0.3, rely=0.35, relwidth=0.2)

        self.entry_4 = customtkinter.CTkEntry(master=self.radiobutton_frame, placeholder_text="Group Name",
                                              font=('Ubuntu', 15))
        # entry_1.grid(row=1, column=1, columnspan=4, padx=10, pady=10)
        self.entry_4.place(relx=0.3, rely=0.45, relwidth=0.2)

        self.entry_5 = customtkinter.CTkEntry(master=self.radiobutton_frame, placeholder_text="Username",
                                              font=('Ubuntu', 15))
        # entry_1.grid(row=1, column=1, columnspan=4, padx=10, pady=10)
        self.entry_5.place(relx=0.3, rely=0.55, relwidth=0.2)

        self.entry_6 = customtkinter.CTkEntry(master=self.radiobutton_frame, placeholder_text="Username",
                                              font=('Ubuntu', 15))
        # entry_1.grid(row=1, column=1, columnspan=4, padx=10, pady=10)
        self.entry_6.place(relx=0.3, rely=0.65, relwidth=0.2)

        self.entry_7 = customtkinter.CTkEntry(master=self.radiobutton_frame, placeholder_text="Username",
                                              font=('Ubuntu', 15))
        # entry_1.grid(row=1, column=1, columnspan=4, padx=10, pady=10)
        self.entry_7.place(relx=0.3, rely=0.75, relwidth=0.2)

        self.button_1 = customtkinter.CTkButton(self.radiobutton_frame, text='Create User', font=('Ubuntu', 15), command=self.button_callback)
        self.button_1.place(relx=0.6, rely=0.2, relwidth=0.15)

        self.button_2 = customtkinter.CTkButton(self.radiobutton_frame, text='Set Password', font=('Ubuntu', 15),
                                                command=self.button_callback)
        self.button_2.place(relx=0.6, rely=0.35, relwidth=0.15)

        self.button_3 = customtkinter.CTkButton(self.radiobutton_frame, text='Create Group', font=('Ubuntu', 15),
                                                command=self.button_callback)
        self.button_3.place(relx=0.6, rely=0.45, relwidth=0.15)

        self.button_4 = customtkinter.CTkButton(self.radiobutton_frame, text='Grant Sudo Access', font=('Ubuntu', 15),
                                                command=self.button_callback)
        self.button_4.place(relx=0.6, rely=0.55, relwidth=0.15)

        self.button_5 = customtkinter.CTkButton(self.radiobutton_frame, text='Prevent Sudo Access', font=('Ubuntu', 15),
                                                command=self.button_callback)
        self.button_5.place(relx=0.6, rely=0.65, relwidth=0.15)

        self.button_6 = customtkinter.CTkButton(self.radiobutton_frame, text='Delete User', font=('Ubuntu', 15),
                                                command=self.button_callback)
        self.button_6.place(relx=0.6, rely=0.75, relwidth=0.15)

        self.button_7 = customtkinter.CTkButton(self.radiobutton_frame, text='Show User Permissions', font=('Ubuntu', 15),
                                                command=self.button_callback)
        self.button_7.place(relx=0.6, rely=0.85, relwidth=0.2)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

    def button_callback(self):
        print("Button click")


if __name__ == "__main__":
    app = App()
    app.mainloop()
