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
sudo gpasswd -a vagrant docker
sudo systemctl restart docker

# mkdir
mkdir ~/work