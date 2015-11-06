#!/bin/bash
mosquitto_url="http://repo.mosquitto.org/debian"
mosquitto_repo="mosquitto-repo"

sudo apt-get install curl

curl -O "$mosquitto_url"/"$mosquitto_repo".gpg.key
apt-key add "$mosquitto_repo".gpg.key
rm "$mosquitto_repo".gpg.key
cd /etc/apt/sources.list.d/
curl -O "$mosquitto_url"/"mosquitto-wheezy.list"

sudo apt-get update
sudo apt-get install mosquitto mosquitto-clients python-mosquitto
