#!/bin/bash

# NOTE: this runs from the SlotRacr folder

# Setup backend timer service
pip3 install -r ~/SlotRacr/backend/requirements.txt

# Setup kivy dependencies
sudo apt install pkg-config libgl1-mesa-dev libgles2-mesa-dev \
   libgstreamer1.0-dev \
   gstreamer1.0-plugins-{bad,base,good,ugly} \
   gstreamer1.0-{omx,alsa} libmtdev-dev \
   xclip xsel libjpeg-dev
sudo apt install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev
sudo apt install xorg-server lightdm

# Setup frontend display service
pip3 install -r ~/SlotRacr/frontend/requirements.txt
sudo apt-get install -y libopenjp2-7

sudo install -m 755 ~/SlotRacr/frontend/disable_cursor.service /etc/systemd/system
sudo systemctl enable disable_cursor.service

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

