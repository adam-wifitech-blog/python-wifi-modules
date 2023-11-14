#!/usr/bin/env python3

from netmiko import ConnectHandler
import time

def connecthandlerc9800(device, send_command):
    # Record the start time of the operation.
    start_time = time.time()
    # Establish a connection to the network device using Netmiko.
    connect = ConnectHandler(**device)
    # Send the command to the device and store the output.
    send_command_output = connect.send_command(send_command, read_timeout=320)
    # Disconnect from the device.
    connect.disconnect()
    # Record the end time of the operation.
    end_time = time.time()
    # Calculate the total time taken for the operation.
    total_time = end_time - start_time
    if __name__ == '__main__':
        print(f'\n Total time script execution: {round(total_time, 3)} \n')
    # Return the output of the sent command.
    return send_command_output

# Main execution block (only runs if this script is the main program).
if __name__ == '__main__':
    # Collect device details and credentials from the user.
    device = {
        'host': input("Provide the device's IP address: "),
        'device_type': 'cisco_ios',
        'username': input("Enter your username: "),
        'password': input("Enter your password: "),
        'port': 22,
        'secret': input("Enter your secret password: "),
    }
    # Execute the connect handler to send a command to the device and receive output.
    send_command_output = connecthandlerc9800(device, input('Provide the command to send: '))
    print(f'Object created: \n \n {send_command_output}')
