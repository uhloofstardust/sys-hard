import subprocess
import customtkinter as ctk



def upgrade_and_update():
    # Bash script for patch management
    patch_script = """
    #!/bin/bash

    # Update the package list and upgrade installed packages
    sudo apt update
    sudo apt upgrade -y

    # Automatically reboot if required
    if [ -f /var/run/reboot-required ]; then
        echo "Rebooting the system..."
        sudo reboot
    fi
    """

    # Create a temporary Bash script file
    with open("/tmp/patch_management_script.sh", "w") as script_file:
        script_file.write(patch_script)

    # Run the temporary Bash script
    subprocess.run(["/bin/bash", "/tmp/patch_management_script.sh"])

    # Clean up the temporary script
    subprocess.run(["rm", "/tmp/patch_management_script.sh"])



def remove_unnecessary():
    # Bash script for patch management
    patch_script = """
    #!/bin/bash

    # Remove unnecessary packages and clean up
    sudo apt autoremove -y
    sudo apt clean

    # Automatically reboot if required
    if [ -f /var/run/reboot-required ]; then
        echo "Rebooting the system..."
        sudo reboot
    fi
    """

    # Create a temporary Bash script file
    with open("/tmp/patch_management_script.sh", "w") as script_file:
        script_file.write(patch_script)

    # Run the temporary Bash script
    subprocess.run(["/bin/bash", "/tmp/patch_management_script.sh"])

    # Clean up the temporary script
    subprocess.run(["rm", "/tmp/patch_management_script.sh"])


def start_patch_management():
    pass


def patch_management(parent_frame,ctk):

    # Create a "Start" button
    label = ctk.CTkLabel(parent_frame, text="Patch Management",font = ("Arial", 24))
    label.pack(padx = 10,pady = (20,10))
    mainFrame = ctk.CTkFrame(parent_frame,fg_color="transparent")
    mainFrame.pack()
    upgrade_and_update_button = ctk.CTkButton(mainFrame, text="Upgrade & \nUpdate", command=upgrade_and_update)
    upgrade_and_update_button.pack(padx=10, pady=10)
    mainFrame2 = ctk.CTkFrame(mainFrame,fg_color="transparent")
    mainFrame2.pack()
    remove_unnecessary_button = ctk.CTkButton(mainFrame2, text="Remove \nUnnecessary", command=remove_unnecessary)
    remove_unnecessary_button.pack(padx=10, pady=5,side = "left")
    build_essentials_button = ctk.CTkButton(mainFrame2, text="Build\nEssentials", command=start_patch_management)
    build_essentials_button.pack(padx=10, pady=10)



    scroll = ctk.CTkScrollbar(parent_frame,width = 600,corner_radius=0)
    scroll.pack()

    tk_textbox = ctk.CTkTextbox(scroll,width=600)
    tk_textbox.pack()

    tk_textbox.insert("0.0",""""Where does it come from?
    Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.Where does it come from?
    Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.""")




# Create the main window
root = ctk.CTk()
root.title("Patch Management")
patch_management(root,ctk)
root.mainloop()
