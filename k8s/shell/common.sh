#!/bin/bash

echo "---- This is common ----------------------------------"


#---- install docker ----
sudo apt-get update
sudo apt-get install -y \
  ca-certificates \
  curl \
  gnupg \
  lsb-release

# add docker gpg key
sudo mkdir -m 0755 -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list >/dev/null

# install docker
sudo apt-get update
sudo apt-get install -y docker-ce

# setup
sudo systemctl start docker
sudo systemctl enable docker

# add priviledge
sudo gpasswd -a $USER docker
sudo systemctl restart docker


#---- install k8s ----
# add repogitory
sudo apt-get update && sudo apt-get install -y apt-transport-https gnupg2
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee -a /etc/apt/sources.list.d/kubernetes.list

# install kubeadm、kubelet、kubectl
sudo apt-get update
sudo apt-get install -y kubelet kubeadm kubectl
sudo apt-mark hold kubelet kubeadm kubectl


# modify kubelet ip config
IPADDR=$(ip a show enp0s8 | grep inet | grep -v inet6 | awk '{print $2}' | cut -f1 -d/)
echo "KUBELET_EXTRA_ARGS=--node-ip=$IPADDR" >> /etc/default/kubelet

# restart kubelet
systemctl daemon-reload
systemctl restart kubelet

# bug fix
sudo rm /etc/containerd/config.toml
sudo systemctl restart containerd
