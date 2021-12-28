#!/bin/bash -x
IP=$1
OPT='-o "StrictHostKeyChecking no"'
sudo apt-get install -y sshpass
sshpass -p raspberry scp $OPT -r install pi@$IP:~
sshpass -p raspberry ssh $OPT pi@$IP 'cd install && ./install.sh'
sshpass -p raspberry ssh $OPT pi@$IP rm -rf ~/install/install.sh
