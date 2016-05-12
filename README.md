# Mongo Based Puppet ENC

## Introduction

This repo is an attempt to develop a POC to see if/how [MongoDB](https://www.mongodb.com/)
 can be used as an ENC with Puppet.  This enables me to use a costom web interface to interact with my environments configuration in any way I see fit.

## Diagram

![Puppet ENC with MongoDB](https://raw.githubusercontent.com/billcloud-me/mongo_enc/master/img/diagram.png "Puppet ENC with MongoDB")

## Process

Puppet agent runs on agent.billcloud.local which calls the Puppet server for it's configuration.  The puppet server is configured to use Python ENC Script as an External Node Classifier.  This script accepts a single argument which is the node name.  The python script uses PyMongo to communicate with the MondoDB instance running on mongo.billcloud.local.  MongoDB has a database called puppet with a 'nodes' collection.  Here is what it looks like in this instance:

```json
> use puppet
switched to db puppet
> db.nodes.find()
{ "_id" : ObjectId("5732b225f2888be4e1d0df83"), "node" : "agent.billcloud.local", "classes" : [ "common", "puppet", "dns", "ntp" ] }
>
```

This will tell puppet that the agent.billcloud.local agent needs to have the common, puppet, dns, and ntp modules included in its configuration.

```
(venv) vagrant@puppet:/vagrant/enc$ python mongo.py agent.billcloud.local
classes:
- common
- puppet
- dns
- ntp
```

## DJango WebApp

To be completed

## Puppet API

To be completed
