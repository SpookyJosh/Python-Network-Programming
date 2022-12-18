#Iterating through each list value
network_part="192.168.2."
host_parts = [20,40,60]
for host_part in host_parts:
    ip=network_part+str(host_part)
    print(f"The router ip is: {ip}")
#Using index value
network_part="192.168.2."
host_parts = [20,40,60]
for idx in range(len(host_parts)):
    host_part = host_parts[idx]
    ip = network_part+str(host_part)
    print(f"The router ip is: {ip}")
