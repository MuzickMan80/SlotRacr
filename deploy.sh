#!/bin/bash -x
IP=$1

sudo apt-get install -y sshpass
sshpass -p raspberry scp -r install pi@$IP:~
sshpass -p raspberry ssh pi@$IP 'cd install && ./install.sh'
sshpass -p raspberry ssh pi@$IP rm -rf ~/install/install.sh
