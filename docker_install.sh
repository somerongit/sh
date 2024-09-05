#!/bin/bash

echo "Docker Installation Started"
echo "Pkg Update"
apt update

apt install apt-transport-https ca-certificates curl software-properties-common

echo "Fetching Dcoker Insatller Started"
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" |  tee /etc/apt/sources.list.d/docker.list > /dev/null

apt update

echo "Fetching Dcoker Insatller Done"

apt-cache policy docker-ce

echo "Dokcer Installation Started"
apt install docker-ce
echo "Dokcer Installation Done"

sudo systemctl status docker