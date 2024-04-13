# Docker in Docker with SSH access
FROM docker:dind

# ARGS
ARG SSH_USERNAME
ARG SSH_PASSWORD

# Install dependencies
RUN apk add --no-cache \
  openssh \
  sudo

# ADD SSH user
RUN adduser -D "$SSH_USERNAME" && \
  echo "$SSH_USERNAME:$SSH_PASSWORD" | chpasswd && \
  echo "$SSH_USERNAME ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/$SSH_USERNAME

# Allow SSH with password
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
  sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config && \
  ssh-keygen -A

# docker without sudo
RUN adduser $SSH_USERNAME docker

# Expose SSH port
EXPOSE 22

# Start SSH and Docker Daemon
CMD ["sh", "-c", "/usr/sbin/sshd -D & dockerd-entrypoint.sh"]
