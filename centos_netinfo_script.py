#!/usr/bin/env python3

import subprocess

res = subprocess.check_output("hostname", shell=True).decode().strip()

# A line that gets the hostname.

print(res) # Prints the hostname that is used.

import socket

s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("1.1.1.1", 80)) # looks for the servers unique ip address.
print(s.getsockname() [0]) # prints the unqiue ip address.
s.close() # closes socket.

def is_connected():
	try:
	# connecting to the host.
	# reaches the host.
		socket.create_connection(("www.sony.com", 80))
		return True
	except OSError:
		pass
	return False

print("The connection was successful" if is_connected() else "The connection has failed")

import datetime # imports the date and times.

filename = f"{datetime.date.today()}_AngelAlmanzar_CentOS_NetworkInfo.txt"

# a command that defines the filename, and looks for the date and time.

# creates a file with my name and tells you what it is for, network information.

file = open(filename, "w") # A line that opens the file manually.

# w means write mode. like r means read mode etc.

file.write("Name: Angel Almanzar\n") # \n means new line.

file.write(f"Date: {datetime.date.today()}\n") # file.write writes strings into a file.

file.close() # closes the file manually.

