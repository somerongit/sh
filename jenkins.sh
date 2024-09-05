# #!/bin/bash

# echo "Installing Jenkins Started"

# wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | gpg --dearmor -o /usr/share/keyrings/jenkins.gpg

# sh -c 'echo deb [signed-by=/usr/share/keyrings/jenkins.gpg] http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'

# echo "Jenkins Insatalling..."

# apt install jenkins

# echo "Starting Jenkins"

# systemctl start jenkins.service
# systemctl status jenkins

# echo "Jenkins Installation Done"