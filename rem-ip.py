#!/usr/bin/python
import os
import sys
def usage():
	return """
		Usage: 	%s <interface> <ip> <mask>
	""" %(sys.argv[0],)



if len(sys.argv) == 1:
	print (usage())
	sys.exit(0)

(interface, ip ) = sys.argv[1:]

#Adding an alias
print ("Removing ip: %s on interface: %s"%(ip, interface)) 
os.system(
	"ifconfig %s inet %s -alias"%(interface, ip)
)
