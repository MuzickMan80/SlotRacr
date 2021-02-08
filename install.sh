#!/bin/bash
pip3 install -r BackEnd/requirements.txt
sudo install -m 755 BackEnd/slot_timer.service /etc/systemd/system
sudo install -m 755 BackEnd/slotcar.py /usr/bin
sudo systemctl enable slot_timer.service
sudo cp -r FrontEnd/dist/FrontEnd/* /var/www/html
sudo systemctl enable pigpiod

echo '@xset s off' | sudo tee -a /etc/xdg/lxsession/LXDE-pi/autostart
echo '@xset -dpms' | sudo tee -a /etc/xdg/lxsession/LXDE-pi/autostart
echo '@xset s noblank' | sudo tee -a /etc/xdg/lxsession/LXDE-pi/autostart
echo '@/home/pi/kiosk.sh' | sudo tee -a /etc/xdg/lxsession/LXDE-pi/autostart
