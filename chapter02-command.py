from paramiko.client import SSHClient
from getpass import getpass

SSH_USER=input("Enter Username: ")
SSH_PASS=getpass(prompt='Password: ',stream=None)
SSH_HOST=input('Enter Host IP: ')
SSH_PORT=int(input('Enter Port: '))

client = SSHClient()
client.load_system_host_keys()
client.connect(SSH_HOST, port=SSH_PORT,username=SSH_USER,password=SSH_PASS)
cmd="ls -al ~/"
stdin,stdout,stderr=client.exec_command(cmd)
client.close()
stdin.close()
