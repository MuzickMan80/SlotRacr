#!/bin/bash
ipaddrs=`cut -f3 -d' ' /var/lib/misc/dnsmasq.leases`
OPT="-o StrictHostKeyChecking=no"

for i in $ipaddrs
do
    echo hello $i;
    sshpass -p SlotRacr ssh $OPT slotracr@$i 'sudo systemctl kill station' || true
    sshpass -p SlotRacr scp $OPT -r station slotracr@$i:~
    sshpass -p SlotRacr ssh $OPT 'sudo timedatectl set-timezone "America/Chicago"'
    TIME=$(date +"%y-%m-%d %H:%M:%S")
    sshpass -p SlotRacr ssh $OPT "sudo timedatectl set-ntp false"
    sshpass -p SlotRacr ssh $OPT "sudo timedatectl set-time '$TIME'"
    sshpass -p SlotRacr ssh $OPT -R 8080 slotracr@$i 'http_proxy=socks5h://localhost:8080 ~/station/setup.sh'
done