#!/usr/bin/env python
'''
ZCR Shellcoder

ZeroDay Cyber Research
Z3r0D4y.Com
Ali Razmjoo
'''
import os
import sys
from core import start
from core import color
if 'linux' in sys.platform:
	os.system('clear')
else:
	sys.exit(color.color('red')+'Sorry, This version of software just could be run on linux.'+color.color('reset'))
start.zcr()
executor = '''#!/bin/bash
python /usr/share/zcr_shellcoder/zsc.py "$@"'''
print color.color('cyan')+'Building Commandline'
commandline = open('/usr/bin/zsc','w')
commandline.write(executor)
commandline.close()
print color.color('green')+'Copying Files'+color.color('white')
os.system('rm -rf /usr/share/zcr_shellcoder && mkdir /usr/share/zcr_shellcoder && cp -r * /usr/share/zcr_shellcoder/ && chmod +x /usr/share/zcr_shellcoder/zsc.py && chmod +x /usr/bin/zsc')
print color.color('yellow') + '\nNow you can remove this folder\nfiles copied in /usr/share/zcr_shellcoder.\nto run zcr shellcoder please use "zsc" command line\n'+color.color('reset')
start.sig()
