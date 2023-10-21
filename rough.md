
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



