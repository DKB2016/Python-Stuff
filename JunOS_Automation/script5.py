from my_devices import INVENTORY
from netmiko import ConnectHandler

for device in INVENTORY:
    conn = ConnectHandler(
        device_type="juniper",
        host=device["host"],
        username=device["user"],
        password=device["password"],
    )
    result = conn.send_command(command_string="show configuration system")
    print(result)