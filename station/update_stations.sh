#!/bin/bash
ipaddrs=`cut -f3 -d' ' dnsmasq.leases`
OPT="-o StrictHostKeyChecking=no"

for i in $ipaddrs
do
    echo hello $i;
    sshpass -p SlotRacr scp $OPT -r station slotracr@$i:~
    sshpass -p SlotRacr ssh $OPT -R 8080 http_proxy=socks5h://localhost:8080 ~/station/setup.sh
done