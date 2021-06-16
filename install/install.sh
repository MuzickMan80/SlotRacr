#!/bin/bash
sudo apt-get update
sudo apt-get install -y python3 python3-pip pigpiod libsdl2-2.0-0 libsdl2-ttf-2.0-0 nginx unclutter

# Setup backend timer service
pip3 install -r ~/backend/requirements.txt
sudo install -m 755 ~/backend/slot_timer.service /etc/systemd/system
sudo systemctl enable slot_timer.service
sudo systemctl enable pigpiod

# Setup frontend display service
pip3 install -r ~/frontend/requirements.txt
sudo install -m 755 ~/frontend/timer_frontend.service /etc/systemd/system
sudo systemctl enable timer_frontend.service

# Setup web frontend
sudo cp -r ~/dist/FrontEnd/* /var/www/html

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

sudo ~/install/restart.sh
