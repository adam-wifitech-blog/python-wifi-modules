#!/usr/bin/env python3
import textfsm

def parsedtextfsm(template, send_command_output):
    # Initialize an empty list to hold dictionaries of parsed text.
    parsed_text_list_dict = []

    # Open the provided TextFSM template file.
    with open(template, 'r') as temp:
        # Create a TextFSM object for parsing the command output.
        fsm = textfsm.TextFSM(temp)
        # Parse the command output using the TextFSM template.
        parsed_text = fsm.ParseText(send_command_output)

    # Convert the parsed output into a list of dictionaries.
    for element in parsed_text:
        parsed_text_dict = dict(zip(fsm.header, element))
        parsed_text_list_dict.append(parsed_text_dict)

    # Return the list of dictionaries containing the parsed data.
    return parsed_text_list_dict

# Main execution block (only runs if this script is the main program).
if __name__ == '__main__':
    import connecthandlerc9800
    import json
    import time

    # Collect device details and credentials from the user.
    device = {
        'host': input("Provide the device's IP address: "),
        'device_type': 'cisco_ios',
        'username': input("Enter your username: "),
        'password': input("Enter your password: "),
        'port': 22,
        'secret': input("Enter your secret password: "),
    }

    # Record the start time of the operation.
    start_time = time.time()
    # Execute the connect handler to send a command to the device and receive output.
    send_command_output = connecthandlerc9800.connecthandlerc9800(device, input('Provide the command to send: '))
    # Record the end time of the operation.
    end_time = time.time()
    # Calculate the total time taken for the operation.
    total_time = end_time - start_time
    print(f'Output received:\n{send_command_output}')
    print(f'Time needed to get the output: {round(total_time, 3)}')

    # Get the name of the TextFSM template from the user.
    template_name = input('Provide the template name: ')
    # Create a filename for the JSON output.
    parsed_text_json = f'parsed_text_json_{template_name}'

    # Parse the command output using the provided TextFSM template.
    parsed_text_list_dict = parsedtextfsm(template_name, send_command_output)

    # Save the parsed output as a JSON file.
    with open(parsed_text_json, 'wt') as file:
        json.dump(parsed_text_list_dict, file, indent=4)

    print(f'File created and saved: {parsed_text_json}')
