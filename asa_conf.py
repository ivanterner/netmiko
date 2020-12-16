#!/usr/bin/env  python3

import os
import getpass
from termcolor import cprint
from netmiko import ConnectHandler


def get_command():
    command_list=[]
    file = open("command_asa.txt","r")
    for item in file:
        item=item.strip()
        command_list.append(item)
    file.close()
    return command_list


def get_username():
    username = os.getlogin()
    return username

def get_password():
    password = getpass.getpass()
    return password

def get_enable_password():
    enable_password = getpass.getpass()
    return enable_password



ip = ("172.16.1.2")
command = get_command()
username = get_username()
password = get_password()
enable_password = get_enable_password()
print(username)
cprint(ip,'green')
device = ConnectHandler(device_type='cisco_asa', ip=ip, username=username, password=password, secret=enable_password)
output = device.send_config_set(command)
cprint(output,'blue')
output = device.send_command("write")
cprint(output,'red')
