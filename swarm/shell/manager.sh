#!/bin/bash

echo "---- This is manager ----------------------------------"

# private ip & hostname
IPADDR=$(ip a show enp0s8 | grep inet | grep -v inet6 | awk '{print $2}' | cut -f1 -d/)
HOSTNAME=$(hostname -s)

# docker swarm
docker swarm init --advertise-addr $IPADDR

# save docker swarm join command
docker swarm join-token worker | grep "docker swarm join" > swarm_join_cmd.sh
chmod +x swarm_join_cmd.sh

# allow ssh with password
sed -i "/^[^#]*PasswordAuthentication[[:space:]]no/c\PasswordAuthentication yes" /etc/ssh/sshd_config
systemctl restart sshd