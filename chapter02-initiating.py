from paramiko.client import SSHClient, AutoAddPolicy
from getpass import getpass
SSH_USER = input('Username: ')
SSH_PASSWORD = getpass(prompt='Password: ',stream=None)
SSH_HOST = input("Host IP: ")
SSH_PORT = 22

client = SSHClient()
client.set_missing_host_key_policy(AutoAddPolicy())
client.load_system_host_keys()
try:
    client.connect(SSH_HOST,port=SSH_PORT,username=SSH_USER,look_for_keys=True)
    print("Connected Successfully!")
except Exception:
    print("Failed to establish connection")
finally:
    client.close()
