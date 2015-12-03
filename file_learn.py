#!/usr/bin/env python
import os
fp = open(r'hello.py')
print 'open file:hello.py'
for each_line in fp:
    print each_line
fp.close()
print os.curdir

