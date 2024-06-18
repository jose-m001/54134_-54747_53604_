from netmiko import Netmiko
from pathlib import Path
from datetime import datetime
import os

time_now = datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p")

folder_to_save_files = 'script_output'
file_base = "output_" + time_now
file_extension = ".txt"

if not os.path.exists(folder_to_save_files):
    os.mkdir(folder_to_save_files)

# Construct paths using GITHUB_WORKSPACE environment variable
workspace = os.getenv('GITHUB_WORKSPACE', '')
Path = TeamApplication
repo_root = Path(workspace) # Adjust as per your repository structure

# Verify the constructed paths and print them
f1 = repo_root / 'script' / 'switch' / 'ipadd1.txt'
print(f1)  # Print the path to ipadd1.txt
file1 = f1.read_text().splitlines()

f2 = repo_root / 'script' / 'switch' / 'commands.txt'
print(f2)  # Print the path to commands.txt
file2 = f2.read_text().splitlines()

f3_folder = repo_root / folder_to_save_files
f3_file_base = f3_folder / file_base
f3_file = f3_file_base.with_suffix(file_extension)

with f3_file.open('w') as file3:
    for device in file1:
        device_params = {
            'device_type': 'cisco_ios',
            'ip': device,
            'username': 'username',
            'password': 'password'
        }

        ssh = Netmiko(**device_params)
        print(f'\n CONNECTING TO {device} \n')
        file3.write(f'\n CONNECTING TO {device} \n')

        for cmd in file2:
            output = ssh.send_command(cmd)
            print(f'\n *** Sending {cmd} *** \n')
            print(f'{output} \n')
            file3.write(f'\n *** Sending {cmd} *** \n')
            file3.write(f'{output} \n')
