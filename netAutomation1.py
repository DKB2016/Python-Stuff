import os
import json
from netmiko import ConnectHandler

# This gets the username and password from environment variables
from dotenv import load_dotenv

load_dotenv()

user = os.environ.get('username')
password = os.environ.get('password')
secret = os.environ.get('secret')
euser = os.environ.get('eusername')
epassword = os.environ.get('epassword')


switch = {
    "device_type": 'cisco_ios_telnet',
    "ip": '192.168.200.250',
    "username": user,
    "password": password,
    "secret": secret,
    "port": 23
}

try:
    c = ConnectHandler(**switch)
    c.enable()
    interfaces = c.send_command('show ip int brief', use_textfsm=True)
    #print(json.dumps(interfaces, indent=2)) # stores everything as a python dictionary
    for interface in interfaces:
        if interfaces['status'] == 'down':
            print(f"{interface['int']} is down!") # this will show what interfaces are down!
    c.close()
except Exception as e:
    print(e)
    
    