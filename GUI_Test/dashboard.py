import customtkinter as ctk
from usb_management import create_usb_port_management_frame
from file_permissions import create_file_permissions
from service_management import create_service_management
from remote_logging import create_logging
from firewall import create_firewall_management
from patch_management import create_patch_management
import os

class DashboardApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Dashboard")
        self.geometry("1200x600")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.create_navigation_frame()
        self.frame_1 = None
        self.frame_2 = None
        self.frame_3 = None
        self.frame_4 = None
        self.frame_5 = None
        self.frame_6 = None
        self.frame_7 = None

    def create_navigation_frame(self):
        self.navigation_frame = ctk.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(12, weight=1)

        self.navigation_frame_label = ctk.CTkLabel(
            self.navigation_frame, text="Ubuntu Hardening", font=ctk.CTkFont(size=15, weight="bold", family="Ubuntu"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.frame_1_button = self.create_nav_button(
            self.navigation_frame, "  PortMaster  ", self.frame_1_button_clicked)
        self.frame_2_button = self.create_nav_button(
            self.navigation_frame, "  File Permissions  ", self.frame_2_button_clicked)
        self.frame_3_button = self.create_nav_button(
            self.navigation_frame, "  Service Management  ", self.frame_3_button_clicked)
        self.frame_4_button = self.create_nav_button(
            self.navigation_frame, "  Remote Logging  ", self.frame_4_button_clicked)
        self.frame_5_button = self.create_nav_button(
            self.navigation_frame, "  Firewall  ", self.frame_5_button_clicked)
        self.frame_6_button = self.create_nav_button(
            self.navigation_frame, "  Patch Management  ", self.frame_6_button_clicked)
        self.frame_7_button = self.create_nav_button(
            self.navigation_frame, "  Application Whitelisting  ", self.frame_7_button_clicked)

        self.frame_1_button.grid(row=1, column=0)
        self.frame_2_button.grid(row=2, column=0)
        self.frame_3_button.grid(row=3, column=0)
        self.frame_4_button.grid(row=4, column=0)
        self.frame_5_button.grid(row=5, column=0)
        self.frame_6_button.grid(row=6, column=0)
        self.frame_7_button.grid(row=7, column=0)

        self.appearance_mode_menu = ctk.CTkOptionMenu(
            self.navigation_frame, values=["Light", "Dark", "System"], command=self.change_appearance_mode)
        self.appearance_mode_menu.grid(row=12, column=0, padx=0, pady=20, ipadx=0,sticky="s")

    def create_frame_1(self):
        if self.frame_2:
            self.frame_2.grid_forget()
        if self.frame_3:
            self.frame_3.grid_forget()
        if self.frame_4:
            self.frame_4.grid_forget()
        if self.frame_5:
            self.frame_5.grid_forget()
        if self.frame_6:
            self.frame_6.grid_forget()
        if self.frame_7:
            self.frame_7.grid_forget()
        if self.frame_1:
            self.frame_1.grid(row=0, column=1, sticky="nsew")
        else:
            self.frame_1 = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
            self.frame_1.grid(row=0, column=1, sticky="nsew")
            create_usb_port_management_frame(self.frame_1, ctk)

    def create_frame_2(self):
        if self.frame_1:
            self.frame_1.grid_forget()
        if self.frame_3:
            self.frame_3.grid_forget()
        if self.frame_4:
            self.frame_4.grid_forget()
        if self.frame_5:
            self.frame_5.grid_forget()
        if self.frame_6:
            self.frame_6.grid_forget()
        if self.frame_7:
            self.frame_7.grid_forget()
        if self.frame_2:
            self.frame_2.grid(row=0, column=1, sticky="nsew")
        else:
            self.frame_2 = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
            self.frame_2.grid(row=0, column=1, sticky="nsew")
            create_file_permissions(self.frame_2, ctk)

    def create_frame_3(self):
        if self.frame_1:
            self.frame_1.grid_forget()
        if self.frame_2:
            self.frame_2.grid_forget()
        if self.frame_4:
            self.frame_4.grid_forget()
        if self.frame_5:
            self.frame_5.grid_forget()
        if self.frame_6:
            self.frame_6.grid_forget()
        if self.frame_7:
            self.frame_7.grid_forget()
        if self.frame_3:
            self.frame_3.grid(row=0, column=1, sticky="nsew")
        else:
            self.frame_3 = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
            self.frame_3.grid(row=0, column=1, sticky="nsew")
            create_service_management(self.frame_3, ctk)

    def create_frame_4(self):
        if self.frame_1:
            self.frame_1.grid_forget()
        if self.frame_2:
            self.frame_2.grid_forget()
        if self.frame_3:
            self.frame_3.grid_forget()
        if self.frame_5:
            self.frame_5.grid_forget()
        if self.frame_6:
            self.frame_6.grid_forget()
        if self.frame_7:
            self.frame_7.grid_forget()
        if self.frame_4:
            self.frame_4.grid(row=0, column=1, sticky="nsew")
        else:
            self.frame_4 = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
            self.frame_4.grid(row=0, column=1, sticky="nsew")
            create_logging(self.frame_4, ctk)

    def create_frame_5(self):
        if self.frame_1:
            self.frame_1.grid_forget()
        if self.frame_2:
            self.frame_2.grid_forget()
        if self.frame_3:
            self.frame_3.grid_forget()
        if self.frame_4:
            self.frame_4.grid_forget()
        if self.frame_6:
            self.frame_6.grid_forget()
        if self.frame_7:
            self.frame_7.grid_forget()
        if self.frame_5:
            self.frame_5.grid(row=0, column=1, sticky="nsew")
        else:
            self.frame_5 = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
            self.frame_5.grid(row=0, column=1, sticky="nsew")
            create_firewall_management(self.frame_5, ctk)

    def create_frame_6(self):
        if self.frame_1:
            self.frame_1.grid_forget()
        if self.frame_2:
            self.frame_2.grid_forget()
        if self.frame_3:
            self.frame_3.grid_forget()
        if self.frame_4:
            self.frame_4.grid_forget()
        if self.frame_5:
            self.frame_5.grid_forget()
        if self.frame_7:
            self.frame_7.grid_forget()
        if self.frame_6:
            self.frame_6.grid(row=0, column=1, sticky="nsew")
        else:
            self.frame_6 = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
            self.frame_6.grid(row=0, column=1, sticky="nsew")
            create_patch_management(self.frame_6, ctk)
    
    def create_frame_7(self):
        if self.frame_1:
            self.frame_1.grid_forget()
        if self.frame_2:
            self.frame_2.grid_forget()
        if self.frame_3:
            self.frame_3.grid_forget()
        if self.frame_4:
            self.frame_4.grid_forget()
        if self.frame_5:
            self.frame_5.grid_forget()
        if self.frame_6:
            self.frame_6.grid_forget()
        if self.frame_7:
            self.frame_7.grid(row=0, column=1, sticky="nsew")
        else:
            self.frame_7 = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
            self.frame_7.grid(row=0, column=1, sticky="nsew")
            create_patch_management(self.frame_7, ctk)

    def create_nav_button(self, parent_frame, text, command):
        return ctk.CTkButton(parent_frame, corner_radius=0, height=40, border_spacing=10, text=text, fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=command)

    def frame_1_button_clicked(self):
        self.create_frame_1()

    def frame_2_button_clicked(self):
        self.create_frame_2()

    def frame_3_button_clicked(self):
        self.create_frame_3()

    def frame_4_button_clicked(self):
        self.create_frame_4()

    def frame_5_button_clicked(self):
        self.create_frame_5()

    def frame_6_button_clicked(self):
        self.create_frame_6()
    
    def frame_7_button_clicked(self):
        self.create_frame_7()

    def change_appearance_mode(self, new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)

if __name__ == "__main__":
    app = DashboardApp()
    app.mainloop()
