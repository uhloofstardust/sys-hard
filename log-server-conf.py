import subprocess

command=f'''module (load=\"imtcp\")
input(type=\"imtcp\" port=\"514\")'''

try:
    subprocess.run("pkexec touch /etc/rsyslog.d/my.conf", shell=True)
    subprocess.run(f"pkexec echo '{command}' > /etc/rsyslog.d/my.conf", shell=True)
    subprocess.run("pkexec service rsyslog restart", shell=True)
    subprocess.run("pkexec ufw allow 514/tcp", shell=True)
except Exception as e:
    print(f"Error: {e}")
