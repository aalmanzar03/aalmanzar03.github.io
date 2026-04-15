#!/bin/bash

echo "Choose the server you are currently using. 1 for Ubuntu, 2 for CentOS."

read -p "Server Choice: " server_choice # -p displays a prompt before reading input.

if [[ $server_choice == 1 ]]; then

# == is equality operator, comapares values.

# checks to see if variables or objects hold the same value.

# server_choice is a variable.

echo "Ubuntu troubleshooting instructions."

echo "Try pinging a site using ping -c a number of times."

echo "ping sends a request to a site, the site then responds with a message back."

echo "For example you can ping a website like nintendo by writing (ping -c 10 www.nintendo.com)."

echo "To get into the netplan directory for your server you can write something like /etc/ netplan."

echo "The netplan directory does not use a script. It uses a YAML configuration file."

echo "To see the current DNS of your server in netplan..."

echo " you can write a command like (resolvectl status)."

echo "A DNS for a server like Ubuntu can be (1.1.1.1)."

echo "The ifup or ifdown command installs different packages to your server with the names.."

echo "(ifup or ifdown)."

echo "The (arp) command shows serveral important server information."

echo "The (dig) command shows different server addresses and other important information."

else

echo "CentOS troubleshooting instructions."

echo "To find your server ip address you can write the command (ip addr)"

echo " this displays an ip like 10.02.14."

echo "To get into a directory in your CentOS server you can write (cd /etc/) or (cd /sysconfig/)."

echo "Writing (ls) in your directory can show you a list of different directories,"

echo "that are stored in your server by default."

echo "As well as files that are saved in the current directory you are in."

echo "To read important system information or print the results of a file in a terminal."

echo "we can write the (cat) command."

echo "The (cat) command displays different file text to the terminal, as well as system data."

echo "Writing the commmand (host or hostname), will get you,"

echo " the unique server name printed in the terminal."

echo "A command like (route) shows you the server ip address,default gateway, and subnet mask."

echo "The (tracepath) command shows different ip related information and settings."

fi
