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
sudo systemctl enable pigpiod

if ! grep -xF 'interface eth0' /etc/dhcpcd.conf
then
	echo 'interface eth0' >> /etc/dhcpcd.conf
	echo 'static ip_address=192.168.2.2/24' >> /etc/dhcpcd.conf
    updated=1
fi

if ! grep -xF 'interface=eth0' /etc/dnsmasq.conf
then
	echo 'interface=eth0' >> /etc/dnsmasq.conf
	echo 'bind-dynamic' >> /etc/dnsmasq.conf
	echo 'domain-needed' >> /etc/dnsmasq.conf
	echo 'bogus-priv' >> /etc/dnsmasq.conf
	echo 'dhcp-range=192.168.2.100,192.168.2.200,255.255.255.0,24h' >> /etc/dnsmasq.conf
    updated=1
fi

if [[ $updated -eq 1 ]]
then
    sudo reboot
fi
