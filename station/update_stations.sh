#!/bin/bash

cp /var/lib/misc/dnsmasq.leases .
ipaddrs=`cut -f3 -d' ' dnsmasq.leases`
for i in $ipaddrs; do echo hello $i; done