#!/usr/bin/python

import sys
import yaml
node = sys.argv[1]
classification = {'classes': ['common','puppet','dns','ntp']}
print yaml.dump(classification, default_flow_style=False)
