import syslog

server_ip = "192.168.203.33"
#remoteserver-port = 0
   
def send_to_remote(msg):
    try:
        syslog.openlog(ident="sanved", logoption=syslog.LOG_PID, facility=syslog.LOG_LOCAL0, address=server_ip)
        syslog.syslog(6, msg)
        # 0: emergency, 1: alert, 2: critical, 3: error, 4: warning, 5: notice, 6: info, 7: debug
        syslog.closelog()
        print("logged message")
    except Exception as e:
        print(f"Error: {e}")
        
while True:
    send_to_remote("hello there")

