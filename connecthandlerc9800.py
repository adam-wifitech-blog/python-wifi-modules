#!/usr/bin/env python3

from netmiko import ConnectHandler, NetmikoAuthenticationException
import time
import socket

def connecthandlerc9800(device,send_command):
    # Establish a connection to the network device using Netmiko.
    connect = ConnectHandler(**device)
    # Send the command to the device and store the output.
    send_command_output = connect.send_command(send_command, read_timeout=320)
    # Disconnect from the device.
    connect.disconnect()
    # Return the output of the sent command.
    return send_command_output

"""Checking the TCP connection to the host."""
def test_tcp_connection(host,port=22,timeout=3):
    try:
        with socket.create_connection((host,port),timeout):
            return True
    except:
        return False

def check_access(ip_address,username,password,secret, device_type='cisco_ios', port=22):
    # Connection device details
    device = {
        'host': ip_address,
        'device_type': device_type,
        'username': username,
        'password': password,
        'port': port,
        'secret': secret,
    }

    #Check if authentication using credentials occurs successfully or not

    try:
        connection = ConnectHandler(**device)
        connection.disconnect()
        message = "Auth Success"
        return message
    except NetmikoAuthenticationException:
        message = "Auth Failed"
        return message

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
    # Record the start time of the operation.
    start_time = time.time()
    # Execute the connect handler to send a command to the device and receive output.
    send_command_output = connecthandlerc9800(device, input('Provide the command to send: '))
    # Record the end time of the operation.
    end_time = time.time()
    # Calculate the total time taken for the operation.
    total_time = end_time - start_time
    print(f'Object created: \n \n {send_command_output}')
    print(f'\n Total time script execution: {round(total_time, 3)} \n')
