from netmiko import ConnectHandler

common_params = {
    "device_type": "juniper_junos",
    "username": "root",
    "password": "juniper1"
}

devices = [
    {"ip": "192.168.1.10"},
    {"ip": "192.168.1.11"},
    {"ip": "192.168.1.12"}
]

for device in devices:
    params = {**common_params, **device}
    conn = ConnectHandler(**params)
    # config_commands = [
    #     f"set system host-name {device['ip']}"
    # ]
    #output = conn.send_config_set(config_commands) #specific set commands only
    # output = conn.send_command("show configuration | display set |match host-name") #generic commands to send
    output = conn.send_config_from_file("config_file.txt")
    print(output)
    conn.disconnect()