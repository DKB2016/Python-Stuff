from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result

def main():
    nr = InitNornir(config_file="c:\\Users\\david\\OneDrive\\Documents\\GitHub\\Python-Stuff\\nornir\\config.yml")

    # Define the task to send a command
    def get_config(task):
        result = task.run(netmiko_send_command, command_string="show ip interface brief")
        print(f"--- {task.host} ---\n{result.result}")

    # Run the task on the device
    result = nr.run(task=get_config)

    # Print the result
    print_result(result)

if __name__ == "__main__":
    main()
