import tkinter
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("IP")
        self.geometry(f"{500}x{500}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.home_frame = customtkinter.CTkFrame(self, width=500, height=500)
        self.home_frame.grid(row=0, column=1, rowspan=4, columnspan=1, sticky="nsew")
        self.IP = customtkinter.CTkLabel(master=self.home_frame, text='IP',
                                              font=('Ubuntu', 35),
                                              justify=customtkinter.LEFT)
        self.IP.place(relx=0.5, rely=0.2)

        self.IP_address_input = customtkinter.CTkEntry(master=self.home_frame, placeholder_text="IP Address",
                                              font=('Ubuntu', 20))
        self.IP_address_input.place(relx=0.2, rely=0.5, relwidth=0.3)


        self.submit_button = customtkinter.CTkButton(self.home_frame, text='Submit',
                                                font=('Ubuntu', 20),
                                                command=self.button_callback)
        self.submit_button.place(relx=0.6, rely=0.5, relwidth=0.2)
    def button_callback(self):
        print("IP SUBMITTED")

if __name__ == "__main__":
    app = App()
    app.mainloop()
