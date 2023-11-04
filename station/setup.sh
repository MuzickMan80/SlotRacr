#!/bin/bash
sudo apt-get install -y python3-pygame python3-pip python3-socks
sudo pip install -r station/requirements.txt
sudo chmod a+x station/station.py
sudo cp station/station.service /lib/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable station.service
# sudo systemctl start station.service
sudo reboot