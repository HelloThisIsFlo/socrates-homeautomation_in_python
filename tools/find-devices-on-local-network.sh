#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"


IP=$($DIR/local-ip.sh)
CLASS_C_NETWORK=${IP%.*}.0/24

echo "Local IP: ${IP}"
echo "Class C Network: ${CLASS_C_NETWORK}"
echo ""

nmap -sP ${CLASS_C_NETWORK}
