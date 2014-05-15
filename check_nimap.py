#!/bin/env python

import os, sys, re

a = 'doveadm -f flow who'
b = os.popen(a, 'r', 10240)
c = 0
t = 0
for line in b:
        m = re.search(r'#=(\d+)', line, re.I)
        if m:
                c = c + 1
                t = t + int(m.group(1))
print "# IMAP OK - ({1}/{0}) (users/total)|nimap={0};0;0;0".format(t,c)
sys.exit(0)
