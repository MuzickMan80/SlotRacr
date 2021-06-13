#!/bin/bash
sudo apt-get update
sudo apt-get install -y python3 python3-pip pigpiod libsdl2-2.0-0 libsdl2-ttf-2.0-0

# Setup backend timer service
pip3 install -r BackEnd/requirements.txt
sudo install -m 755 BackEnd/slot_timer.service /etc/systemd/system
sudo install -m 755 BackEnd/slotcar.py /usr/bin
sudo systemctl enable slot_timer.service
sudo systemctl enable pigpiod

# Setup frontend display service
pip3 install -r FrontEnd/requirements.txt
sudo install -m 755 FrontEnd/timer_frontend.service /etc/systemd/system
sudo systemctl enable timer_frontend.service

