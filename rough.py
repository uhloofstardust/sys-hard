import tkinter as tk
from tkinter import ttk
import subprocess

def send_log():
    ip = ip_entry.get()
    subprocess.run(f"logging -n {ip} -P 541 -f /var/logs/syslog --tcp", shell=True)

window = tk.Tk()
window.title("Log Sender")

ip_label = tk.Label(window, text="Enter IP Address:")
ip_label.pack()

ip_entry = tk.Entry(window)
ip_entry.pack()

send_button = tk.Button(window, text="Send Logs", command=send_log)
send_button.pack()

window.mainloop()
