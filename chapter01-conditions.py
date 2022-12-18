infra_network_part="10.2.10."
user_network_part="10.20.1."
device_type=input("What type? [infra/user] ")
host_part=input("What's the host part? ")

if device_type=="infra":
    ip=str(infra_network_part)+str(host_part)
    print(f"Your infra ip is {ip}")
elif device_type=="user":
    ip=str(user_network_part)+str(host_part)
    print(f"Your ip is {ip}")
else:
    print(f"Sorry, I don't know how to handle the type {device_type}")
