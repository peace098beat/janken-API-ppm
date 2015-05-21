#!/usr/local/bin/python
# -*- coding: utf-8 -*- 
# pythonパスはもう一度試す

import cgitb
cgitb.enable()


import cgi
import os
import sys
import json

from PPM import *

p = Predict(5)
p.add("g")
p.add("c")
p.add("p")
p.add("g")
p.add("c")
p.add("p")
p.add("p")

if 'QUERY_STRING' in os.environ:
    query = cgi.parse_qs(os.environ['QUERY_STRING'])
else:
    query = {}


print "Content-Type: text/javascript\n\n"
print


if 'name' in query:
	s = query["player"]
	s_list=list(s)
	p.add_ary(s_list)

print json.dumps([{'next_hand':p.next_hand()},
	{'hand_set':p.history},{'histgram':p.accum}])
