Requirments:
Install module
1. Netmiko --> pip install netmiko
2. pathlib --> pip install pathlib
3. string --> pip install string
4. The rest are built in python

Steps:
1.	Make sure the device that you want to access are reachable. From command prompt run ping.
2.	Make sure the file path defined in the script and the ipadd and commands text file are the same.
3.	Open the text files and update which device and what command:
Ipadd.text  list of ip the device you want to access
Commands.text  list of commands you want to run
4.	Make sure the username and password in the script is correct. This will be use to access the device using ssh.
5.	Run the script. Navigate to the directory and use command prompt then python porj7.py command.
6.	The output will be saved in C drive Script Output folder. If the folder does not exist it will create a new one.
