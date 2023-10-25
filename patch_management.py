import tkinter as tk
import subprocess

def start_patch_management():
    # Bash script for patch management
    patch_script = """
    #!/bin/bash

    # Update the package list and upgrade installed packages
    sudo apt update
    sudo apt upgrade -y

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

# Create the main window
root = tk.Tk()
root.title("Patch Management")

# Create a "Start" button
start_button = tk.Button(root, text="Start", command=start_patch_management)
start_button.pack(padx=20, pady=20)

# Start the GUI main loop
root.mainloop()
