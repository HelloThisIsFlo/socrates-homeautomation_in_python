#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

TOPIC=$1

mqtt subscribe -h localhost -p 1883 -u mqttuser -P mqttpass "$TOPIC"

