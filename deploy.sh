#!/bin/bash -x
IP=192.168.1.11

pushd web_frontend
#npm install
#ng build --configuration production
popd

sudo apt-get install -y sshpass
sshpass -p raspberry scp -r backend frontend web_frontend/dist install pi@$IP:~
sshpass -p raspberry ssh pi@$IP 'cd install && ./install.sh'
sshpass -p raspberry ssh pi@$IP rm -rf ~/install/install.sh dist
