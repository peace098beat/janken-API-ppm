#!/usr/local/bin/python
# -*- coding: utf-8 -*- 

import cgitb
cgitb.enable()


import cgi
import os
import sys
import json

from PPM import *
p = Predict(10)
p.add("g")
p.add("c")
p.add("p")
p.add("g")
p.add("c")
p.add("p")
p.add("g")
p.add("c")
p.add("p")
p.add("g")
p.add("c")
p.add("p")


if 'QUERY_STRING' in os.environ:
    query = cgi.parse_qs(os.environ['QUERY_STRING'])
else:
    query = {}


# print "Content-Type: text/html\n\n"
# print query
print "Content-Type: text/javascript\n\n"
print
# print "<HTML>"
# print "<h2>リンク</h2>"
# print "<a href='http://fififactory.sakura.ne.jp/API/index.cgi?name=ggccpp'>API/index.cgi?name=''</a>"

# print "</HTML>"


if 'name' in query:
	s = query["player"]
	s_list=list(s)
	p.add_ary(s_list)

# print p.history
# print '<p>next hand:\n'
# print p.next_hand()
print json.dumps([{'next_hand':p.next_hand()},
	{'hand_set':p.history},{'histgram':p.accum}])
