#!/bin/bash

echo "---- This is worker ----------------------------------"

apt-get install -y sshpass
sshpass -p "vagrant" scp -o StrictHostKeyChecking=no vagrant@192.168.10.21:~/kubeadm_join_cmd.sh .
sudo sh ./kubeadm_join_cmd.sh
