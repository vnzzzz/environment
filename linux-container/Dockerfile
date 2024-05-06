FROM ubuntu:22.04

# Set environment variables
ARG USERNAME
ARG PASSWORD
ENV LANG=C.UTF-8
ENV TZ=Asia/Tokyo

# Install necessary packages
RUN apt-get update && apt-get install -y \
  openssh-server \
  sudo \
  ca-certificates \
  curl \
  gnupg \
  lsb-release \
  iputils-ping \
  net-tools

# Add user and configure sudo access
RUN adduser --gecos '' --disabled-password "${USERNAME}" && \
  echo "${USERNAME}:${PASSWORD}" | chpasswd
RUN echo "${USERNAME} ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/${USERNAME}

# Setup Docker GPG key and repository
RUN mkdir -p /etc/apt/keyrings
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg
RUN echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker and Docker Compose
RUN apt-get update && \
  apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin

# Allow the user to execute Docker commands without sudo
RUN usermod -aG docker "${USERNAME}"

# Configure SSH server
RUN mkdir /var/run/sshd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config
EXPOSE 22

# install go
RUN apt-get install -y \
  golang-go

# working firectory
WORKDIR /work

# Use a custom entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
