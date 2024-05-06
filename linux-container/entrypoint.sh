#!/bin/bash
# Start Docker daemon directly
dockerd >/var/log/dockerd.log 2>&1 &

# Ensure the Docker daemon is fully up before proceeding
sleep 5

# Start SSH daemon
exec /usr/sbin/sshd -D
