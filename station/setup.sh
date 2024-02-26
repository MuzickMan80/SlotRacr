#!/bin/bash
sudo apt-get install -y python3-pygame python3-pip python3-socks
sudo pip install --upgrade --proxy socks5h://127.0.0.1:8080 pip
sudo pip install -r station/requirements.txt --proxy socks5h://127.0.0.1:8080
sudo chmod a+x station/station.py
sudo cp station/station.service /lib/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable station.service
# sudo systemctl start station.service
sudo reboot