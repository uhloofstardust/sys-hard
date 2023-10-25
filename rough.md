
<hr>

### usb
```
from serial.tools import list_ports

ports = [port.device for port in list_ports.comports()]
print(ports)
```

```serial.tools.list_ports.grep(regexp, include_links=False)```


> ['/dev/ttyS0', '/dev/ttyUSB0', '/dev/ttyACM0']

to ``` /etc/modprobe.d/blacklist.conf ``` add the line ``` blacklist <driver_module_name> ```
reboot the module using ``` sudo modprobe -r <driver_module_name> ```

Establish a terminal-like connection using ```serial.tools.miniterm```


<hr>

```
import re

pattern = re.compile(
    r'^(?P<allow_block>allow|deny)\s+'
    r'id\s+(?P<id>\S+)\s+'
    r'serial\s+"(?P<serial>[^"]+)"\s+'
    r'name\s+"(?P<name>[^"]+)"\s+'
    r'hash\s+"(?P<hash>[^"]+)"\s+'
    r'parent-hash\s+"(?P<parent_hash>[^"]+)"\s+'
    r'via-port\s+"(?P<via_port>[^"]+)"\s+'
    r'with-interface\s+(?P<interface>\d+)\s+'
    r'with-connect-type\s+"(?P<connect_type>[^"]+)"'
)

rules_conf_file = '/etc/usbguard/rules.conf'
parsed_rules = []

with open(rules_conf_file, 'r') as file:
    for line in file:
        line = re.sub(r'#.*$', '', line)
        line = line.strip()
        if not line:
            continue

        match = pattern.match(line)
        if match:
            rule_dict = match.groupdict()
            parsed_rules.append(rule_dict)

for rule in parsed_rules:
    print(rule)

```



```
import re

pattern = re.compile(
    r'^(?P<allow_block>allow|deny)\s+'
    r'id\s+(?P<id>[0-9a-fA-F:]+)\s+'
    r'serial\s*"(?P<serial>[^"]*)"?\s+'
    r'name\s*"(?P<name>[^"]*)"?\s+'
    r'hash\s*"(?P<hash>[^"]*)"?\s+'
    r'parent-hash\s*"(?P<parent_hash>[^"]*)"?\s+'
    r'via-port\s*"(?P<via_port>[^"]*)"?\s+'
    r'with-interface\s*"(?P<interface>[0-9a-fA-F:]+)"?\s+'
    r'with-connect-type\s*"(?P<connect_type>[^"]*)"?$'
)

rules_conf_file = '/etc/usbguard/rules.conf'

parsed_rules = []

with open(rules_conf_file, 'r') as file:
    for line in file:
        match = pattern.match(line)
        if match:
            rule_dict = match.groupdict()
            parsed_rules.append(rule_dict)

for rule in parsed_rules:
    print(rule)

```


```
import re

pattern = re.compile(
    r'^(?P<allow_block>allow|deny)\s+'
    r'id\s+(?P<id>[0-9a-fA-F:]+)\s+'
    r'serial\s*"(?P<serial>[^"]*)"?\s+'
    r'name\s*"(?P<name>[^"]*)"?\s+'
    r'hash\s*"(?P<hash>[^"]*)"?\s+'
    r'parent-hash\s*"(?P<parent_hash>[^"]*)"?\s+'
    r'via-port\s*"(?P<via_port>[^"]*)"?\s+'
    r'with-interface\s*"(?P<interface>[0-9a-fA-F:]+)"?\s+'
    r'with-connect-type\s*"(?P<connect_type>[^"]*)"?$'
)

rules_conf_file = '/etc/usbguard/rules.conf'

parsed_rules = []

try:
    with open(rules_conf_file, 'r') as file:
        for line in file:
            match = pattern.match(line)
            if match:
                rule_dict = match.groupdict()
                parsed_rules.append(rule_dict)

except FileNotFoundError:
    print(f"File not found: {rules_conf_file}")
except Exception as e:
    print(f"An error occurred: {e}")

for rule in parsed_rules:
    print(rule)

```


```
rules_conf_file = '/etc/usbguard/rules.conf'

parsed_rules = []

try:
    with open(rules_conf_file, 'r') as file:
        rule_dict = {}
        for line in file.readlines():
            line = line.strip()
            # Skip empty lines and comment lines
            if not line or line.startswith("#"):
                continue
            parts = line.split()
            if len(parts) == 2:
                key, value = parts
                rule_dict[key] = value
            elif len(parts) == 3:
                key, value, quoted_value = parts
                # Remove quotes from the quoted values
                rule_dict[key] = quoted_value.strip('""')
            else:
                parsed_rules.append(rule_dict)
                rule_dict = {}

    if rule_dict:
        parsed_rules.append(rule_dict)

    for rule in parsed_rules:
        print(rule)

except FileNotFoundError:
    print(f"File not found: {rules_conf_file}")
except Exception as e:
    print(f"An error occurred: {e}")

```


```
# Define the path to the rules.conf file
rules_conf_file = '/etc/usbguard/rules.conf'

# Create a list to store each line as a string
lines_list = []

try:
    with open(rules_conf_file, 'r') as file:
        for line in file:
            lines_list.append(line.strip())

    # Print the list of lines
    for line in lines_list:
        print(line)

except FileNotFoundError:
    print(f"File not found: {rules_conf_file}")
except Exception as e:
    print(f"An error occurred: {e}")

```


<hr><hr>

## Disable USB Storage

In ```/etc/modprobe.d/blacklist.conf``` add ```blacklist usb_storage```

In ```/etc/rc.local``` add
```
modprobe -r usb_storage
exit 0
```

<hr>

## Secure SSH

```/etc/ssh/sshd_config```
change default port # for ssh to sth else
disable root login ```PermitRootLogn no```

check ssh manual to understand these and modify accordingly or add more:
```
Protocol2
IgnoreRhosts to yes
HostbasedAuthentication no
PermitEmptyPasswords no
X11Forwarding no
MaxAuthTries 2
Ciphers aes128-ctr,aes192-ctr,aes256-ctr
ClientAliveInterval 600
ClientAliveCountMax 0
UsePAM yes
```

set permissions on the file ```/etc/ssh/sshd_config```

```
chown root:root /etc/ssh/sshd_config
chmod 600 /etc/ssh/sshd_config
```

<hr>

## enable SELinux
3 options: disabled, permissive(prints warnings), enforcing

In ```/etc/selinux/config``` 
```
SELinux=enforcing
```

<hr>

## Password Policies

Configure the file ```/etc/pam.d/common-password```

- enforce strong password hashing
- last 3 passwords shouldn't be reused
- strong lockout policy
- 14 character passwords
- ensure complexity

<hr>

## firewall 

```ufw enable```

<hr>

## Intrusion Detection

use AIDE


<hr>

## set a bios/firmware password

<hr>

## configure the device boot order to prevent unauthorized booting from alternate media

<hr>

## remove legacy services

- telnet-server
- rsh, rlogin, rcp
- ypserv, ypbind
- tftp-server
- talk, talk-server

<hr>

## protect system from rootkits

<hr>

## update

<hr>