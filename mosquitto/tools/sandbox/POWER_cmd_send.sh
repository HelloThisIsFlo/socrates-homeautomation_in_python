#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

CMD=$1

$DIR/publish.sh cmnd/demoswitch/POWER "$CMD"

