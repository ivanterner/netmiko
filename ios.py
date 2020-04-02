#!/usr/bin/env  python3

import getpass

from netmiko import ConnectHandler

hostname_list = ["sw1", "sw2", "sw3"]
username = input("Username:")
password = getpass.getpass()
enable_pass = getpass.getpass(prompt='Enter enable password:')
command = input("Please raw command:")

for ip in hostname_list:
    device = ConnectHandler(device_type='cisco_ios', ip=ip, username=username, password=password)
    output = device.send_command(command)
    print(output)
