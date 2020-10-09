#!/usr/bin/env  python3

import getpass
from netmiko import ConnectHandler


def get_hosts():
    hostname_list=[]
    file = open("devices.txt","r")
    for item in file:
        item=item.strip()
        hostname_list.append(item)
    file.close()
    print(hostname_list)
    return hostname_list


hosts = get_hosts()
print(hosts)
username = input("Username:")
password = getpass.getpass()
#enable_pass = getpass.getpass(prompt='Enter enable password:')
command = input("Please raw command:")

for ip in hosts:
    print(ip)
    device = ConnectHandler(device_type='cisco_ios', ip=ip, username=username, password=password, verbose=1, auth_timeout=5)
    output = device.send_command(command)
    print(output)
