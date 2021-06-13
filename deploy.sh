#!/bin/bash
IP=192.168.1.11

pushd web_frontend
npm install
ng build
popd

sudo apt-get install -y sshpass
sshpass -p raspberry scp -r backend frontend web_frontend/dist install.sh restart.sh pi@$IP:~
sshpass -p raspberry ssh pi@$IP ./install.sh
sshpass -p raspberry ssh pi@$IP rm -rf install.sh dist
sshpass -p raspberry ssh pi@$IP ./restart.sh