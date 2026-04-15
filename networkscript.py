#!/usr/bin/env python 3

import subprocess

res = subprocess.check_output("hostname", shell=True).decode().strip()

# line that gets the hostname.

print(res) # prints the hostname.

import socket

s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("1.1.1.1", 80)) # looks for the servers unique ip address.
print(s.getsockname()[0]) # prints the unique ip address.
s.close() # closes socket.

def is_connected():
	try:
	# connecting to the host.
	# reaches the host.
		socket.create_connection(("www.nintendo.com", 80))
		return True
	except OSError:
		pass
	return False
print("Successful Connection" if is_connected() else "The connection has failed")

import datetime # imports dates and times.

filename = f"{datetime.date.today()}_AngelAlmanzar_NetworkInfo.txt"

 # a command that defines the filename, and looks for the date and time.

 # creates a file with my name and tells you what it is for, network information.

file = open(filename, "w") # line that opens the file manually.

# w means write mode. like r means read mode.

file.write("Name: Angel Almanzar\n") # \n means new line.

file.write(f"Date: {datetime.date.today()}\n") # file.write writes strings into a file.

file.close() # closes the file manually.
