#!/bin/bash
wget https://apt.puppetlabs.com/puppetlabs-release-pc1-precise.deb
dpkg -i puppetlabs-release-pc1-precise.deb
apt-get update
apt-get install puppet-agent -y
