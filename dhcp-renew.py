#!/usr/bin/python
import os
import sys
if len(sys.argv) == 1:
	interface = "en0"
else:
	interface = sys.argv[1]
os.system("ipconfig set %s BOOTP" % (interface,))
os.system("ipconfig set %s DHCP"%(interface,))
print ("New Ip?")
