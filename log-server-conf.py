#   create server config file
#   restart rsyslog
#   allow TCP

import subprocess

user_ip = "10.0.2.15"

try:
    subprocess.run("pkexec touch /etc/rsyslog.d/my.conf", shell=True)
    subprocess.run(f'pkexec echo -e "module(load=\"imtcp\")\ninput(type=\"imtcp\" port=\"514\")\n\n\$TCPServerAddress {user_ip}" > /etc/rsyslog.d/my.conf', shell=True)
    subprocess.run("pkexec service rsyslog restart", shell=True)
except Exception as e:
    print(f"Error: {e}")
