#!/bin/bash
set -e

echo "$(cat << EOM
user:deluser=pi
user:adduser=$WS_NAME|password=$WS_NAME
# apt-addrepo:repo=deb http://packages.ros.org/ros2/ubuntu/ noble|gpgkey=http://packages.ros.org/ros2/ubuntu/dists/noble/Release.gpg
# apps:apps=ros-jazzy-desktop
network:netman=network-manager|ifname=wlan0|wifissid=PBS4|wifipassword=DPS2home01|wificountry=US
network:netman=network-manager|ifname=eth0
L10n:keymap=us|locale=en_US.UTF-8|timezone=America/Chicago|wificountry=us
disables:piwiz|cloudinit
sshkey:sshuser=$WS_NAME|import-key=./id_ed25519|passphrase=
git-clone:repo=git@github.com:$REPO.git|gitdir=/home/$WS_NAME/$REPO_NAME|user=$WS_NAME
EOM
)" >> ./my.plugins

sudo sdm --customize --plugin @./my.plugins --extend --xmb 2048 --restart --logwidth 256 ubuntu.img
