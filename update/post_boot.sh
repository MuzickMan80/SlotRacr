#!/bin/bash

# NOTE: this runs from the SlotRacr folder

# Update systemd unit files after boot, then reboot if required
sleep 5

updated=0

if ! cmp frontend/timer_frontend.service /etc/systemd/system/timer_frontend.service
then
    sudo cp frontend/timer_frontend.service /etc/systemd/system/timer_frontend.service
    sudo systemctl enable timer_frontend
    updated=1
fi

if ! cmp frontend/disable_cursor.service /etc/systemd/system/disable_cursor.service
then
    sudo cp frontend/disable_cursor.service /etc/systemd/system/disable_cursor.service
    sudo systemctl enable disable_cursor
    updated=1
fi

if ! cmp backend/slot_timer.service /etc/systemd/system/slot_timer.service
then
    sudo cp backend/slot_timer.service /etc/systemd/system/slot_timer.service
    sudo systemctl enable slot_timer
    updated=1
fi

if ! cmp update/timer_update.service /etc/systemd/system/timer_update.service
then
    sudo cp update/timer_update.service /etc/systemd/system/timer_update.service
    sudo systemctl enable timer_update
    updated=1
fi

if [[ $updated -eq 1 ]
then
    sudo reboot
fi
