#!/bin/bash -e
IP=$1

sudo apt-get install -y sshpass

read -p "Pi Username: " username
read -s -p "Pi Password: " password

OPT="-o StrictHostKeyChecking=no"
sshpass -p $password scp $OPT -r install $username@$IP:~
sshpass -p $password ssh $OPT $username@$IP 'cd install && ./install.sh'
