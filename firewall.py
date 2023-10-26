import subprocess

def configure_firewall(source_ip, destination_ip, source_all, dest_all, port, allow_rule):
    try:
        if allow_rule:
            if source_all and dest_all:
                subprocess.run(['iptables', '-A', 'INPUT', '-p', 'tcp', '--dport', str(port), '-j', 'ACCEPT'])
                subprocess.run(['iptables', '-A', 'OUTPUT', '-p', 'tcp', '--dport', str(port), '-j', 'ACCEPT'])
                subprocess.run(['iptables', '-A', 'FORWARD', '-p', 'tcp', '--dport', str(port), '-j', 'ACCEPT'])
            elif source_all:
                subprocess.run(['iptables', '-A', 'INPUT', '-d', destination_ip, '-p', 'tcp', '--dport', str(port), '-j', 'ACCEPT'])
                subprocess.run(['iptables', '-A', 'OUTPUT', '-d', destination_ip, '-p', 'tcp', '--dport', str(port), '-j', 'ACCEPT'])
                subprocess.run(['iptables', '-A', 'FORWARD', '-d', destination_ip, '-p', 'tcp', '--dport', str(port), '-j', 'ACCEPT'])
            elif dest_all:
                subprocess.run(['iptables', '-A', 'INPUT', '-s', source_ip, '-p', 'tcp', '--dport', str(port), '-j', 'ACCEPT'])
                subprocess.run(['iptables', '-A', 'OUTPUT', '-s', source_ip, '-p', 'tcp', '--dport', str(port), '-j', 'ACCEPT'])
                subprocess.run(['iptables', '-A', 'FORWARD', '-s', source_ip, '-p', 'tcp', '--dport', str(port), '-j', 'ACCEPT'])
            else:
                subprocess.run(['iptables', '-A', 'INPUT', '-s', source_ip, '-d', destination_ip, '-p', 'tcp', '--dport', str(port), '-j', 'ACCEPT'])
                subprocess.run(['iptables', '-A', 'OUTPUT', '-s', source_ip, '-d', destination_ip, '-p', 'tcp', '--dport', str(port), '-j', 'ACCEPT'])
                subprocess.run(['iptables', '-A', 'FORWARD', '-s', source_ip, '-d', destination_ip, '-p', 'tcp', '--dport', str(port), '-j', 'ACCEPT'])
        else:
            if source_all and dest_all:
                subprocess.run(['iptables', '-A', 'INPUT', '-p', 'tcp', '--dport', str(port), '-j', 'DROP'])
                subprocess.run(['iptables', '-A', 'OUTPUT', '-p', 'tcp', '--dport', str(port), '-j', 'DROP'])
                subprocess.run(['iptables', '-A', 'FORWARD', '-p', 'tcp', '--dport', str(port), '-j', 'DROP'])
            elif source_all:
                subprocess.run(['iptables', '-A', 'INPUT', '-d', destination_ip, '-p', 'tcp', '--dport', str(port), '-j', 'DROP'])
                subprocess.run(['iptables', '-A', 'OUTPUT', '-d', destination_ip, '-p', 'tcp', '--dport', str(port), '-j', 'DROP'])
                subprocess.run(['iptables', '-A', 'FORWARD', '-d', destination_ip, '-p', 'tcp', '--dport', str(port), '-j', 'DROP'])
            elif dest_all:
                subprocess.run(['iptables', '-A', 'INPUT', '-s', source_ip, '-p', 'tcp', '--dport', str(port), '-j', 'DROP'])
                subprocess.run(['iptables', '-A', 'OUTPUT', '-s', source_ip, '-p', 'tcp', '--dport', str(port), '-j', 'DROP'])
                subprocess.run(['iptables', '-A', 'FORWARD', '-s', source_ip, '-p', 'tcp', '--dport', str(port), '-j', 'DROP'])
            else:
                subprocess.run(['iptables', '-A', 'INPUT', '-s', source_ip, '-d', destination_ip, '-p', 'tcp', '--dport', str(port), '-j', 'DROP'])
                subprocess.run(['iptables', '-A', 'OUTPUT', '-s', source_ip, '-d', destination_ip, '-p', 'tcp', '--dport', str(port), '-j', 'DROP'])
                subprocess.run(['iptables', '-A', 'FORWARD', '-s', source_ip, '-d', destination_ip, '-p', 'tcp', '--dport', str(port), '-j', 'DROP'])
        
        subprocess.run(['iptables-save'])
    except Exception as e:
        print(f"Error: {e}")
