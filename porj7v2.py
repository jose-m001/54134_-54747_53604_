#WORKING WITH OUTPUT DATES

from netmiko import Netmiko
import pathlib
from pathlib import Path
from datetime import datetime
import time
import string
import os

time_now = datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p")

drive_letter = r'C:\\' 
folder_name = r'Script Output'
folder_to_save_files = drive_letter + folder_name
file_base = "output_" + time_now
file_extension = ".txt"

if not os.path.exists(folder_to_save_files):
    os.mkdir(folder_to_save_files)

f1 = Path('C:/Users/joanna.narciso/PYSCRIPT/script/switch/ipadd.txt')
file1 = f1.read_text().splitlines()

f2 = Path('C:/Users/joanna.narciso/PYSCRIPT/script/switch/commands.txt')
file2 = f2.read_text().splitlines()

f3_folder = Path(folder_to_save_files)
f3_file_base = f3_folder / file_base
f3_file = f3_file_base.with_suffix(file_extension)

with f3_file.open('w') as file3:

        for device in file1:
                dict = {'device_type':'cisco_ios',
                'ip': device,
                'username':'username',
                'password':'password'    }
                
                ssh = Netmiko(**dict)
                print(f' \n CONNECTING TO  {device} \n')
                file3.write(f' \n CONNECTING TO {device} \n')

                for cmd in file2:
                 output = ssh.send_command(cmd)
                 print(f' \n *** Sending {cmd} *** \n')
                 print(f' {output} \n')
                 file3.write(f' \n *** Sending {cmd} *** \n')
                 file3.write(f' {output} \n')
        file3.close
  
 
