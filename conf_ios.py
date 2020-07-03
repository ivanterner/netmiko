#!/usr/bin/env  python3

import getpass

from netmiko import ConnectHandler

hostname_list = ["sw1", "sw10", "sw11",
                 "sw12", "sw14", "sw15",
                 "sw16", "sw18", "sw19",
                 "sw2" , "sw20", "sw21",
                 "sw22", "sw23", "sw24",
                 "sw25", "sw3" ,"sw31",
                 "sw32", "sw33" ,"sw5",
                 "sw6", "sw9", "swvoip1",
                 "swvoip2", "swvoip3", "swvoip4"]
username = input("Username:")
password = getpass.getpass()
#enable_pass = getpass.getpass(prompt='Enter enable password:')
command = ["no logging console"]

for ip in hostname_list:
    device = ConnectHandler(device_type='cisco_ios', ip=ip, username=username, password=password)
    output = device.send_config_set(command)
    print(output)
    output = device.send_command("write")
    print(output)