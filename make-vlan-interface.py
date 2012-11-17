#!/usr/bin/python
import os
import sys
def usage():
	return """
		Usage: 	%s <interface> <vlan-id>
	""" %(sys.argv[0],)



if len(sys.argv) == 1:
	print (usage())
	sys.exit(0)

(interface, vlan ) = sys.argv[1:]

print ("Creating  vlan interface : vlan%s and attaching it to interface: %s"%(vlan, interface))


# To make a vlan interface and attach it to a phys int.
# source: http://www.cyberciti.biz/faq/howto-configure-freebsd-vlans-with-ifconfig-command/
#ifconfig vlan99 create
#ifconfig vlan99 10.13.37.99 netmask 255.255.255.0 vlan 99 vlandev en0


os.system(
	"ifconfig vlan%s create" % (vlan) 
)
os.system(
	"ifconfig %s vlan %s vlandev %s"%(interface, vlan, interface)
)
