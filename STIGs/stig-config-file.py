import xml.etree.ElementTree as ET

def parse_stig_file(stig_file_path):
    try:
        tree = ET.parse(stig_file_path)
        root = tree.getroot()
        return root
    except Exception as e:
        print(f"Error reading STIG file: {e}")
        return None

def extract_stig_data(root):
    stig_data = []
    for stig in root.findall('.//Vuln'):
        # Adjust the XPath according to your XML structure
        stig_id = stig.find('Group').attrib['id']  # If the ID is an attribute of the Group tag
        fix_text = stig.find('fixtext').text  # If fixtext is a direct child of Vuln

        config_commands = extract_config_commands(fix_text)
        stig_data.append((stig_id, fix_text, config_commands))
    return stig_data

def extract_config_commands(fix_text):
    # Implement logic to extract configuration commands from fix_text
    # This is a placeholder function; you'll need to adapt it based on how the configuration commands are presented in the fix text
    return "Configuration Commands Placeholder"

def write_config_file(stig_data, config_file_path):
    with open(config_file_path, 'w') as file:
        for stig_id, fix_text, config_commands in stig_data:
            file.write(f"{stig_id}: {fix_text}\n")
            file.write(f"Configuration: {config_commands}\n\n")

def main():
    stig_file_path = 'C:\\Users\\david\\Downloads\\U_Cisco_ASA_Y23M10_STIG\\U_Cisco_ASA_NDM_V1R6_Manual_STIG\\U_Cisco_ASA_NDM_STIG_V1R6_Manual-xccdf.xml'  # Replace with your STIG file path
    config_file_path = 'C:\\Users\\david\\Downloads\\output_config_file.txt'    # Replace with your desired output file path

    root = parse_stig_file(stig_file_path)
    if root is not None:
        stig_data = extract_stig_data(root)
        write_config_file(stig_data, config_file_path)
        print("Config file created successfully.")
    else:
        print("Failed to create config file.")

if __name__ == "__main__":
    main()