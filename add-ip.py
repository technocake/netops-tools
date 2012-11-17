#!/usr/bin/python
import os
import sys
def usage():
	return """
		Usage: 	%s <interface> <ip> <mask>
	""" %(sys.argv[0],)



if len(sys.argv) != 4:
	print (usage())
	sys.exit(0)

(interface, ip, mask ) = sys.argv[1:]

#Adding an alias
print ("Adding ip: %s (%s) on interface: %s"%(ip, mask, interface))


os.system(
	"ifconfig %s inet %s netmask %s alias"%(interface, ip, mask)
)
