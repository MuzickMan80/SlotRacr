#!/bin/bash
sudo apt-get update
sudo apt-get install -y python3 python3-pip pigpiod libsdl2-2.0-0 libsdl2-ttf-2.0-0 nginx unclutter git

# Clean old directories
rm -rf ~/backend
rm -rf ~/frontend
rm -rf ~/SlotRacr
rm -f ~/restart.sh

# Clone repo
git clone https://github.com/MuzickMan80/SlotRacr ~/SlotRacr

# Setup auto-update service
sudo install -m 755 ~/SlotRacr/update/timer_update.service /etc/systemd/system
sudo systemctl enable timer_update.service

# Run post-update script
pushd ~/SlotRacr
./update/post_update.sh
popd

# Install services
sudo install -m 755 ~/SlotRacr/frontend/timer_frontend.service /etc/systemd/system
sudo systemctl enable timer_frontend.service

sudo install -m 755 ~/SlotRacr/backend/slot_timer.service /etc/systemd/system
sudo systemctl enable slot_timer.service
sudo systemctl enable pigpiod

sudo ~/install/restart.sh
