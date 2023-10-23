#   create server config file
#   restart rsyslog
#   allow TCP

import subprocess

user_ip = "10.0.2.15"
command=f'''module load=(\"imtcp\")
input(type=\"imtcp\" port=\"514\")
$TCPServerAddress {user_ip}'''

try:
    subprocess.run("pkexec touch /etc/rsyslog.d/my.conf", shell=True)
    subprocess.run(f"pkexec echo '{command}' > /etc/rsyslog.d/my.conf", shell=True)
    subprocess.run("pkexec service rsyslog restart", shell=True)
except Exception as e:
    print(f"Error: {e}")
