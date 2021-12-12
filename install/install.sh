#!/bin/bash
sudo apt-get update
sudo apt-get install -y python3 python3-pip pigpiod libsdl2-2.0-0 libsdl2-ttf-2.0-0 nginx unclutter git

# Clean old directories
rm -rf ~/backend
rm -rf ~/frontend
rm -rf ~/SlotRacr
rm -f restart.sh

# Clone repo
git clone http://github.com/MuzickMan80/SlotRacr ~/SlotRacr

# Setup backend timer service
pip3 install -r ~/SlotRacr/backend/requirements.txt
sudo install -m 755 ~/SlotRacr/backend/slot_timer.service /etc/systemd/system
sudo systemctl enable slot_timer.service
sudo systemctl enable pigpiod

# Setup frontend display service
pip3 install -r ~/SlotRacr/frontend/requirements.txt
sudo install -m 755 ~/SlotRacr/frontend/timer_frontend.service /etc/systemd/system
sudo systemctl enable timer_frontend.service

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

sudo ~/install/restart.sh
