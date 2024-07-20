#!/bin/bash

echo "Test Started"
speedtest-cli  --simple | awk -F ':' '{print $2}'
echo "Test Ended"

# apt install speedtest-cli
