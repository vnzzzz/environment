#!/bin/bash

echo "---- This is master ----------------------------------"

# private ip & hostname
IPADDR=$(ip a show enp0s8 | grep inet | grep -v inet6 | awk '{print $2}' | cut -f1 -d/)
HOSTNAME=$(hostname -s)

# kubeadm init
kubeadm init --apiserver-advertise-address=$IPADDR --apiserver-cert-extra-sans=$IPADDR --node-name $HOSTNAME --pod-network-cidr=10.244.0.0/16

# add priviledge
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

# install flannel
sudo sysctl net.bridge.bridge-nf-call-iptables=1
curl -s -L -O https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
kubectl apply -f kube-flannel.yml

# save kubectl join command
kubeadm token create --print-join-command > kubeadm_join_cmd.sh
chmod +x kubeadm_join_cmd.sh

# allow ssh with password
sed -i "/^[^#]*PasswordAuthentication[[:space:]]no/c\PasswordAuthentication yes" /etc/ssh/sshd_config
systemctl restart sshd