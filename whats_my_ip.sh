#!/bin/bash

# Get local IP address
local_ip=$(ip addr show | awk '/inet 192.168/ {print $2}')

# Get public IP address using curl (alternative methods exist)
public_ip=$(curl -s https://ipinfo.io/ip)

# Print results
echo "Local IP: $local_ip"
echo "Public IP: $public_ip"

# Explanation of commands:
#  - #!/bin/bash: This line specifies the interpreter for the script, which is bash in this case.
#  - ip addr show | awk '/inet 192.168/ {print $2}': This retrieves local IP addresses.
#      - ip addr show displays network interface details.
#      - awk is a text processing tool.
#      - '/inet 192.168/ filters lines starting with "inet 192.168" (common local IP range).
#      - '{print $2}' prints the second field (IP address) of those lines.
#  - curl -s https://ipinfo.io/ip: This retrieves the public IP address using curl.
#      - curl is a command-line tool for transferring data.
#      - -s suppresses output from curl itself (only captures the content).
#      - https://ipinfo.io/ip is a web service that provides your public IP address.
#  - echo "Local IP: $local_ip" ... : This prints formatted messages with the retrieved IPs.
