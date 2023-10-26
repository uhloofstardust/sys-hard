import customtkinter as ctk
import tkinter
from tkinter import  messagebox

def create_two(parent_frame):
    two = ctk.CTkFrame(parent_frame, corner_radius=0)
    two.grid(row=0, column=1, sticky="nsew")
    title = ctk.CTkLabel(two, text="File Permissions", font=ctk.CTkFont(size=15, weight="bold"))
    title.place(relx=0.36, rely=0.05)

    label1 = ctk.CTkLabel(two, text="Enter the Username:  ", font=("Ubuntu", 20), justify=ctk.LEFT)
    label1.place(relx=0.10, rely=0.21)

    label2 = ctk.CTkLabel(two, text="Enter File Path: ", font=("Ubuntu", 20), justify=ctk.LEFT)
    label2.place(relx=0.10, rely=0.33)

    entry_button1 = ctk.CTkEntry(two, placeholder_text="", font=("Ubuntu", 20, "bold"), border_width=2)
    entry_button1.place(relx=0.44, rely=0.20, relwidth=0.47, relheight=0.078)

    entry_button2 = ctk.CTkEntry(two, placeholder_text="", font=("Ubuntu", 20, "bold"), border_width=2)
    entry_button2.place(relx=0.44, rely=0.32, relwidth=0.47, relheight=0.078)

    read = ctk.CTkCheckBox(two, text="Read", font=("Ubuntu", 20))
    read.place(relx=0.10, rely=0.57)

    write = ctk.CTkCheckBox(two, text="Write", font=("Ubuntu", 20))
    write.place(relx=0.44, rely=0.57)

    execute = ctk.CTkCheckBox(two, text="Execute", font=("Ubuntu", 20))
    execute.place(relx=0.76, rely=0.57)

    flush_all = ctk.CTkButton(two, text="FLUSH FOR ALL", font=("Ubuntu", 18), command=flush)
    flush_all.place(relx=0.10, rely=0.75, relwidth=0.27, relheight=0.068)

    flush_user = ctk.CTkButton(two, text="FLUSH FOR USER", font=("Ubuntu", 18,), command=flush)
    flush_user.place(relx=0.402, rely=0.75, relwidth=0.27, relheight=0.068)

    # submit = ctk.CTkButton(two, text="SUBMIT", font=("Ubuntu", 18), command=submit)
    # submit.place(relx=0.7, rely=0.75, relwidth=0.27, relheight=0.068)

    return two
def flush(self):
    print("Data Cleared!!!")


# def submit(self):
#     response = tkinter.messagebox.askyesno("Question", "Do you want to continue?")
#     if response:
#         print("File Permissions Modified!!!")
#     else:
#         print("Revert Changes!!!")

