#!/usr/bin/env  python3

import os
import getpass
from netmiko import ConnectHandler


def get_hosts():
    hostname_list=[]
    file = open("devices.txt","r")
    for item in file:
        item=item.strip()
        hostname_list.append(item)
    file.close()
    return hostname_list

def get_username():
    username = os.getlogin()
    return username

def get_password():
    password = getpass.getpass()
    return password



command = input("Please raw command:")
hosts = get_hosts()
username = get_username()
password = get_password()
for ip in hosts:
    print(ip)
    device = ConnectHandler(device_type='cisco_ios', ip=ip, username=username, password=password, verbose=1, auth_timeout=5)
    output = device.send_command(command)
    print(output)
