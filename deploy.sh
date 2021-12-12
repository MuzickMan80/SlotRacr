#!/bin/bash -x
IP=192.168.1.109

sudo apt-get install -y sshpass
sshpass -p raspberry scp -r install pi@$IP:~
sshpass -p raspberry ssh pi@$IP 'cd install && ./install.sh'
sshpass -p raspberry ssh pi@$IP rm -rf ~/install/install.sh
