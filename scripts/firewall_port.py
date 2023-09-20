import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

def configure_firewall(source_ip, destination_ip, port, allow_rule):
    try:
        if allow_rule:
            # Allow traffic from source IP to destination IP on specified port
            subprocess.run(['iptables', '-A', 'INPUT', '-s', source_ip, '-d', destination_ip, '-p', 'tcp', '--dport', str(port), '-j', 'ACCEPT'])
        else:
            # Deny traffic from source IP to destination IP on specified port
            subprocess.run(['iptables', '-A', 'INPUT', '-s', source_ip, '-d', destination_ip, '-p', 'tcp', '--dport', str(port), '-j', 'DROP'])
        
        # Save the firewall rules
        subprocess.run(['iptables-save'])

        return "Firewall configuration updated successfully."
    except Exception as e:
        return f"Error: {str(e)}"

