#!/bin/bash
if grep -q "192.168.50.10" /etc/hosts
then
  # found
  echo "hosts entries found..."
else
  # not found
  echo "192.168.50.10  puppet.billcloud.local puppet" >> /etc/hosts
  echo "192.168.50.20  agent.billcloud.local agent" >> /etc/hosts
  echo "192.168.50.30  mongo.billcloud.local mongo" >> /etc/hosts
fi
