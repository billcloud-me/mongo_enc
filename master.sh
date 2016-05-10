#!/bin/bash
wget https://apt.puppetlabs.com/puppetlabs-release-pc1-precise.deb
dpkg -i puppetlabs-release-pc1-precise.deb
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
echo "deb http://repo.mongodb.org/apt/ubuntu precise/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list
apt-get update
apt-get install puppetserver mongodb-org-shell -y
