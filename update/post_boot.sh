#!/bin/bash

# NOTE: this runs from the SlotRacr folder

# Update systemd unit files after boot, then reboot if required
sleep 5

updated=0

check_update_service () {
    SRC=$1
    SERVICE=$2

    cp $SRC/$SERVICE /tmp/$SERVICE
    sudo sed -i "s:/home/pi:$HOME:g" /tmp/$SERVICE
    sudo sed -i "s:User=pi:User=$USER:g" /tmp/$SERVICE

    if ! cmp /tmp/$SERVICE /etc/systemd/system/$SERVICE
    then
        sudo cp /tmp/$SERVICE /etc/systemd/system/$SERVICE
        sudo systemctl enable $SERVICE
        updated=1
    fi

    rm /tmp/$SERVICE
}

check_update_service frontend timer_frontend.service
check_update_service frontend disable_cursor.service
check_update_service backend slot_timer.service
check_update_service update timer_update.service

if [[ $updated -eq 1 ]]
then
    sudo reboot
fi
