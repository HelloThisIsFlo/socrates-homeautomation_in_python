#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

TOPIC=$1
MESSAGE=$2

mqtt publish -h localhost -p 1883 -u mqttuser -P mqttpass "$TOPIC" "$MESSAGE"

