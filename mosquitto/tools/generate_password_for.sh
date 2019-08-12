#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Use this script to override the existing credentials for accessing
# the MQTT broker
#
# To generate the credential USER / PASS:
#
#     $ docker-compose up
#
#     $ ./generate_password_for.sh USER
#     $
#     $   Password: PASS
#     $   Reenter Password: PASS
#     $
#


USERNAME=$1
MOSQUITTO_CONTAINER='mosquitto'
PASSWORD_FILE_LOCATION_IN_CONTAINER=/mqtt/config/password_file
CMD="mosquitto_passwd -c $PASSWORD_FILE_LOCATION_IN_CONTAINER $USERNAME"


if [ -z "$(docker-compose ps -q $MOSQUITTO_CONTAINER)" ]; then
  echo "Run the '$MOSQUITTO_CONTAINER' container before trying to generate a new password"
  exit 1
fi
docker-compose exec $MOSQUITTO_CONTAINER $CMD
