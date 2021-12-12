#!/bin/bash

# NOTE: this runs from the SlotRacr folder

# Setup backend timer service
pip3 install -r ~/SlotRacr/backend/requirements.txt

# Setup frontend display service
pip3 install -r ~/SlotRacr/frontend/requirements.txt

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

