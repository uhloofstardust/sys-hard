import customtkinter as ctk
import os
from PIL import Image
import subprocess
from usb_management import create_usb_port_management_frame
from file_permissions import create_file_permissions

class DashboardApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Dashboard")
        self.geometry("700x450")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.create_navigation_frame()
        self.frame_1 = None
        self.frame_2 = None

    def create_navigation_frame(self):
        self.navigation_frame = ctk.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = ctk.CTkLabel(
            self.navigation_frame, text="Ubuntu Hardening", font=ctk.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.frame_1_button = self.create_nav_button(
            self.navigation_frame, "PortMaster", self.frame_1_button_clicked)
        self.frame_2_button = self.create_nav_button(
            self.navigation_frame, "File Permissions", self.frame_2_button_clicked)

        self.frame_1_button.grid(row=1, column=0)
        self.frame_2_button.grid(row=2, column=0)

        self.appearance_mode_menu = ctk.CTkOptionMenu(
            self.navigation_frame, values=["Light", "Dark", "System"], command=self.change_appearance_mode)
        self.appearance_mode_menu.grid(row=3, column=0, padx=20, pady=20, sticky="s")

    def create_frame_1(self):
        if self.frame_2:
            self.frame_2.grid_forget()  # Hide the other frame if it exists
        if self.frame_1:
            self.frame_1.grid(row=0, column=1, sticky="nsew")  # Show the frame if it already exists
        else:
            self.frame_1 = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
            self.frame_1.grid(row=0, column=1, sticky="nsew")
            create_usb_port_management_frame(self.frame_1, ctk)

    def create_nav_button(self, parent_frame, text, command):
        return ctk.CTkButton(parent_frame, corner_radius=0, height=40, border_spacing=10, text=text, fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=command)

    def frame_1_button_clicked(self):
        self.create_frame_1()

    def frame_2_button_clicked(self):
        if self.frame_1:
            self.frame_1.grid_forget()  # Hide the other frame if it exists
        self.create_file_permissions()

    def change_appearance_mode(self, new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)

    def create_file_permissions(self):
        if self.frame_1:
            self.frame_1.grid_forget()  # Hide the other frame if it exists
        if self.frame_2:
            self.frame_2.grid(row=0, column=1, sticky="nsew")  # Show the frame if it already exists
        else:
            self.frame_2 = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
            self.frame_2.grid(row=0, column=1, sticky="nsew")
            create_file_permissions(self.frame_2, ctk)

if __name__ == "__main__":
    app = DashboardApp()
    app.mainloop()
