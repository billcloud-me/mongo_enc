#!/usr/bin/python

import sys
import yaml
from pymongo import MongoClient
import unicodedata

def convert(input):
  if isinstance(input, dict):
    return dict((convert(key), convert(value)) for key, value in input.iteritems())
  elif isinstance(input, list):
    return [convert(element) for element in input]
  elif isinstance(input, unicode):
    return input.encode('utf-8')
  else:
    return input

node = sys.argv[1]
#prod client
client = MongoClient('mongo.billcloud.local', 27017)
#test client
#client = MongoClient('localhost', 27017)
db = client['puppet']
nodes = db.nodes
result_id = nodes.find_one({"node": node})
if result_id is not None:
  classes = result_id["classes"]
  classes = convert(classes)
  classification = {'classes': classes }
  print yaml.dump(classification, default_flow_style=False)
