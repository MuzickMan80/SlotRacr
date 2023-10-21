#!/bin/bash
sudo apt-get update
sudo apt-get install -y python3 python3-pip pigpiod nginx unclutter git vim

# Clean old directories
rm -rf ~/backend
rm -rf ~/frontend
rm -rf ~/SlotRacr
rm -f ~/restart.sh

# Clone repo
git clone https://github.com/MuzickMan80/SlotRacr ~/SlotRacr

fixup_service() {
    sudo sed -i "s:/home/pi:$HOME:g" /etc/systemd/system/$1
    sudo sed -i "s:User=pi:User=$USER:g" /etc/systemd/system/$1
}

# Setup auto-update service
sudo install -m 755 ~/SlotRacr/update/timer_update.service /etc/systemd/system
fixup_service timer_update.service
sudo systemctl enable timer_update.service

# Run post-update script
pushd ~/SlotRacr
./update/post_update.sh
popd

# Install services
sudo install -m 755 ~/SlotRacr/frontend/timer_frontend.service /etc/systemd/system
fixup_service timer_frontend.service
sudo systemctl enable timer_frontend.service

sudo install -m 755 ~/SlotRacr/backend/slot_timer.service /etc/systemd/system
fixup_service slot_timer.service
sudo systemctl enable slot_timer.service
sudo systemctl enable pigpiod

sudo ~/install/restart.sh
