sshd_config_file = '/etc/ssh/sshd_config'


with open(sshd_config_file, 'r') as file:
    lines = file.readlines()

modified_lines = []

for line in lines:
    if (line.strip().startswith('#PasswordAuthentication')) or (line.strip().startswith('PasswordAuthentication')):
        modified_lines.append('PasswordAuthentication no\n')
    elif (line.strip().startswith('#PermitRootLogin')) or (line.strip().startswith('PermitRootLogin')):
        modified_lines.append('PermitRootLogin no\n')
    elif (line.strip().startswith('#AddressFamily')) or (line.strip().startswith('AddressFamily')):
        modified_lines.append('AddressFamily inet\n')
    elif (line.strip().startswith('ClientAliveInterval')) or (line.strip().startswith('#ClientAliveInterval')):
        modified_lines.append('ClientAliveInterval 60\n')
    elif (line.strip().startswith('ClientAliveCountMax')) or (line.strip().startswith('#ClientAliveCountMax')):
        modified_lines.append('ClientAliveCountMax 3\n')
    elif (line.strip().startswith('PermitEmptyPasswords')) or (line.strip().startswith('#PermitEmptyPasswords')):
        modified_lines.append('PermitEmptyPasswords no\n')
    elif (line.strip().startswith('IgnoreRhosts')) or (line.strip().startswith('#IgnoreRhosts')):
        modified_lines.append('IgnoreRhosts yes\n')
    elif (line.strip().startswith('X11Forwarding')) or (line.strip().startswith('#X11Forwarding')):
        modified_lines.append('X11Forwarding no\n')
    elif (line.strip().startswith('MaxAuthTries')) or (line.strip().startswith('#MaxAuthTries')):
        modified_lines.append('MaxAuthTries 3\n')
    else:
        modified_lines.append(line)

with open(sshd_config_file, 'w') as file:
    file.writelines(modified_lines)

print('sshd_config updated.')

