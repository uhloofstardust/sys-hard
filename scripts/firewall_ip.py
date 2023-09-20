import socket,subprocess

domainname="www.jspmrscoe.edu.in"
subprocess.run(["iptables","-D","INPUT","-j",domainname],capture_output=True)
subprocess.run(["ip6tables","-D","INPUT","-j",domainname],capture_output=True)
create_new_chain=['iptables','-N',domainname]
subprocess.run(create_new_chain,capture_output=True)
subprocess.run(["iptables","-F",domainname],capture_output=True)
subprocess.run(["ip6tables","-N",domainname],capture_output=True)
subprocess.run(["ip6tables","-F",domainname],capture_output=True)
subprocess.run(["iptables","-A",'INPUT','-j',domainname],capture_output=True)
subprocess.run(["ip6tables","-A",'INPUT','-j',domainname],capture_output=True)
ipaddress=socket.getaddrinfo(domainname,None)
ipv4addr=set()
ipv6addr=set()
for address in ipaddress:
    s=address[4][0]
    if(len(s)<=15):
        ipv4addr.add(s)
    else:
        ipv6addr.add(s)

for ip in ipv4addr:
    query=["iptables", '-A', domainname, '-s',ip ,'-j',"DROP"]
     
    p=subprocess.run(query,capture_output=True)
    if(p.returncode==0):
        print("ip Address "+ip +"is blocked")
    else:
        print("Something went wrong "+ip)


for ip in ipv6addr:
    query=["ip6tables", '-A', domainname, '-s',ip ,'-j',"DROP"]
     
    p=subprocess.run(query,capture_output=True)
    if(p.returncode==0):
        print("ip Address "+ip +"is blocked")
    else:
        print("Something went wrong "+ip)

