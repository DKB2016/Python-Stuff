from scrapli import Scrapli

my_device = {
    "host":"192.168.1.10",
    "auth_username":"root",
    "auth_password":"juniper1",
    "auth_scrict_key":False,
    "platform": "Juniper_junos",
}

conn = Scrapli(**my_device)
conn.open()
#single command use 'send_command'
result = conn.send_command(command="show interfaces description")

#Multiple commands use 'send_commands'
#mydevice=["show configuration system", "show interfaces terse"]
#result = conn.send_commands(commands=mydevice)
print(result)
conn.close()