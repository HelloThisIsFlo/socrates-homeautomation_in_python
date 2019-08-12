#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

SWITCH_ID="switch.demoswitch"
TOKEN=$(cat $DIR/token 2>/dev/null)

if [ -z "$TOKEN" ]; then
    echo "First, generate the Long-lived Token and store it in './token'"
    exit 1
fi

curl -X POST -H "Authorization: Bearer $(cat $DIR/token)" \
      -H "Content-Type: application/json" \
      -d '{"entity_id": "'$SWITCH_ID'"}' \
      http://localhost:8123/api/services/switch/turn_on

