import customtkinter as ctk
import os
from PIL import Image
import subprocess
from temp import create_usb_port_management_frame
from frame2 import *
from one import create_one
from two import create_two

class App(ctk.CTk):
    
    def __init__(self):
        super().__init__()
        self.title("Dashboard")
        self.geometry("700x450")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.create_navigation_frame()

    def create_navigation_frame(self):
        self.navigation_frame = ctk.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)
        
        self.navigation_frame_label = ctk.CTkLabel(self.navigation_frame, text="  Ubuntu Hardening", font=ctk.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = self.create_nav_button(self.navigation_frame, "Frame 1", self.home_button_event)
        self.frame_2_button = self.create_nav_button(self.navigation_frame, "Frame 2", self.frame_2_button_event)
        self.frame_3_button = self.create_nav_button(self.navigation_frame, "Frame 3", self.frame_3_button_event)
        
        self.home_button.grid(row=1,column=0)
        self.frame_2_button.grid(row=2,column=0)
        self.frame_3_button.grid(row=3,column=0)

        self.appearance_mode_menu = ctk.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # Create the main frame where content will be displayed
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=0, column=1, sticky="nsew")

    def create_nav_button(self, parent_frame, text, command):
        return ctk.CTkButton(parent_frame, corner_radius=0, height=40, border_spacing=10, text=text,
                             fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                             anchor="w", command=command)

    def home_button_event(self):
        # Clear the existing content in the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        # Show Frame 1 content using the imported function
        frame1_content = create_one(self.main_frame)
        frame1_content.grid(row=0, column=1, sticky="nsew")

        

    def frame_2_button_event(self):
        # Clear the existing content in the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Show Frame 2 content (you can implement this similarly)
        frame2_content = create_two(self.main_frame)
        frame2_content.grid(row=0, column=1, sticky="nsew")

    def frame_3_button_event(self):
        # Clear the existing content in the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Show Frame 3 content (you can implement this similarly)

    def change_appearance_mode_event(self, new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)

if __name__ == "__main__":
    app = App()
    app.mainloop()
















############################################################
# in another file one.py

import customtkinter as ctk

def create_one(parent_frame):
    one = ctk.CTkFrame(parent_frame, corner_radius=0)
    one.grid(row=0, column=1, sticky="nsew")
    
    label = ctk.CTkLabel(one, text="Welcome to Frame 1", font=ctk.CTkFont(size=15, weight="bold"))
    label.pack(padx=20, pady=20)

    return one

