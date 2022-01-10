#!/bin/bash

# NOTE: this runs from the SlotRacr folder

# Setup backend timer service
pip3 install -r ~/SlotRacr/backend/requirements.txt

# Setup frontend display service
pip3 install -r ~/SlotRacr/frontend/requirements.txt
sudo apt-get install -y libopenjp2-7 libsdl-ttf2.0-0

sudo install -m 755 ~/SlotRacr/frontend/disable_cursor.service /etc/systemd/system
sudo systemctl enable disable_cursor.service

# Disable nginx to allow serving web content from backend
sudo systemctl disable nginx
sudo systemctl stop nginx

sudo setcap 'cap_net_bind_service=+ep' /usr/bin/python3.7

# Setup web frontend
# sudo cp -r ~/dist/FrontEnd/* /var/www/html

# Setup nginx
sudo cp ~/install/slotracr-nginx /etc/nginx/sites-available/slotracr

if [ -f /etc/nginx/sites-enabled/slotracr ]
then
    sudo rm /etc/nginx/sites-enabled/slotracr
fi

sudo ln -s /etc/nginx/sites-available/slotracr /etc/nginx/sites-enabled/slotracr

if [ -f /etc/nginx/sites-enabled/default ]
then
    sudo rm /etc/nginx/sites-enabled/default
fi

# Update systemd unit files after boot, then reboot if required
./update/post_boot.sh