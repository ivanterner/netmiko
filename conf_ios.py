#!/usr/bin/env  python3

import getpass

from netmiko import ConnectHandler
hostname_list=[]
file = open("devices.txt","r")
for item in file:
    item=item.strip()
    hostname_list.append(item)
file.close()
print(hostname_list)

username = input("Username:")
password = getpass.getpass()
#enable_pass = getpass.getpass(prompt='Enter enable password:')
command = ["ip name-server 172.16.10.3"]

for ip in hostname_list:
    print(ip)
    device = ConnectHandler(device_type='cisco_ios', ip=ip, username=username, password=password)
    output = device.send_config_set(command)
    print(output)
    output = device.send_command("write")
    print(output)
