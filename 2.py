import subprocess
import customtkinter as ctk
def application_whitelisting(parent_frame,ctk):

    # Create a "Start" button
    Modify_label = ctk.CTkLabel(parent_frame, text="Application Whitelisting",font = ("Arial", 24))
    Modify_label.pack(padx = 10,pady = (20,10))

    mainFrame = ctk.CTkFrame(parent_frame)
    mainFrame.pack()
    mainFrame1 = ctk.CTkFrame(mainFrame)
    mainFrame1.pack(fill = 'both')
    modify = ctk.CTkLabel(mainFrame1,text = "Modify : ",font = ('Arial',18))
    modify.grid(row = 0,column = 0,padx = (10,0),pady = (10,0),sticky = 'w')

    AppName = ctk.CTkEntry(mainFrame1,width = 270, placeholder_text = "Application Name")
    AppName.grid(row = 1,column = 1,padx = (0,10))
    serviceName = ctk.CTkEntry(mainFrame1,width = 270,placeholder_text = "Service Name")
    serviceName.grid(row = 1,column = 2,padx = (0,10))
    modify_btn = ctk.CTkButton(mainFrame1,text = "Modify",width = 260)
    modify_btn.grid(row = 2,column = 2)
    checkBoxFrame = ctk.CTkFrame(mainFrame1,fg_color="transparent")


    checkBoxFrame.grid(row = 2,column = 1)
    read = ctk.CTkCheckBox(checkBoxFrame,text = "read")
    read.grid(row = 0,column = 1,pady = 10)
    write = ctk.CTkCheckBox(checkBoxFrame,text = "write")
    write.grid(row = 0,column = 2,pady = 10)
    execute = ctk.CTkCheckBox(checkBoxFrame,text = "execute")
    execute.grid(row = 0,column = 3,pady = 10)
    


    scroll = ctk.CTkScrollbar(mainFrame,width = 600,corner_radius=0)
    scroll.pack(padx = 10,pady = (10,20))

    tk_textbox = ctk.CTkTextbox(scroll,width=600)
    tk_textbox.pack()

    tk_textbox.insert("0.0",""""Where does it come from?
    Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.Where does it come from?
    Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.""")



root = ctk.CTk()
application_whitelisting(root,ctk)
root.mainloop()
