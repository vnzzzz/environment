#!/bin/bash

# util
sudo apt update
sudo apt install -y gnome-keyring tree

# install vscode server
wget -O- https://aka.ms/install-vscode-server/setup.sh | sh

# create token
sudo mkdir /etc/vscode-server
openssl rand -hex 16 | sudo tee /etc/vscode-server/token

# run as a daemon
sudo tee /etc/systemd/system/vscode-server.service <<EOL >/dev/null
[Unit]
Description = VSCode Server Service

[Service]
ExecStart = /usr/local/bin/code-server serve-local --accept-server-license-terms --connection-token-file /etc/vscode-server/token --host 0.0.0.0 --port 9000
Restart = always
User = vagrant

[Install]
WantedBy = multi-user.target
EOL

sudo systemctl daemon-reload
sudo systemctl start vscode-server
sudo systemctl enable vscode-server
