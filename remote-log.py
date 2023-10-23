import subprocess

def send_log(ip):
  subprocess.run(f"logging -n {ip} -P 541 -f /var/logs/syslog --tcp", shell=True)

