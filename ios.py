#!/usr/bin/env  python3

from netmiko import ConnectHandler
import getpass 
import sys

hostname = input("Hostname:")
username = input("Username:")
password = getpass.getpass()
enable_pass = getpass.getpass(prompt='Enter enable password:')
command  = input("Please raw command:")

device = ConnectHandler(device_type='cisco_ios',ip=hostname,username=username,password=password)
output = device.send_command(command)
print(output)
