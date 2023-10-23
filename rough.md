
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







file:///home/prl/Downloads/5000-Sales-Records.zip
