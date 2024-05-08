#!/bin/bash
IP=$(hostname -I | awk '{print $1}')
/usr/sbin/cephadm bootstrap --mon-ip $IP --allow-fqdn-hostname