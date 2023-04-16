#!/bin/bash

echo "---- This is worker ----------------------------------"

apt-get install -y sshpass
sshpass -p "vagrant" scp -o StrictHostKeyChecking=no vagrant@192.168.10.31:~/swarm_join_cmd.sh .
sudo sh ./swarm_join_cmd.sh
