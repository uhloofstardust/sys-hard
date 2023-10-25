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
        title = ctk.CTkLabel(parent_frame, text="USB PORTS MANAGEMENT", font=("Arial", 24), pady=14)
        title.pack()
        frame = ctk.CTkFrame(parent_frame)
        frame.pack()

        # Your code for USB port management here
        # You can create labels, buttons, and other widgets in this frame

    def create_nav_button(self, parent_frame, text, command):
        return ctk.CTkButton(parent_frame, corner_radius=0, height=40, border_spacing=10, text=text,
                             fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                             anchor="w", command=command)

    def home_button_event(self):
        # Handle the home button event
        pass

    def frame_2_button_event(self):
        # Handle the frame 2 button event
        pass

    def frame_3_button_event(self):
        # Handle the frame 3 button event
        pass

    def change_appearance_mode_event(self, new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)

if __name__ == "__main__":
    app = App()
    app.mainloop()

