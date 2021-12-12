#!/bin/bash
sudo apt-get update
sudo apt-get install -y python3 python3-pip pigpiod libsdl2-2.0-0 libsdl2-ttf-2.0-0 nginx unclutter git

# Clean old directories
rm -rf ~/backend
rm -rf ~/frontend
rm -rf ~/SlotRacr
rm -f ~/restart.sh

# Clone repo
git clone http://github.com/MuzickMan80/SlotRacr ~/SlotRacr

# Setup auto-update service
sudo install -m 755 ~/SlotRacr/update/timer_update.service /etc/systemd/system
sudo systemctl enable timer_update.service

# Run post-update script
pushd ~/SlotRacr
./post_update.sh
popd

sudo ~/install/restart.sh
