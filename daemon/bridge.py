#!/usr/bin/python
import os

def xen():
	os.system("/etc/xen/scripts/network-bridge ")
	
# add eth0:1 (file conf)
# brctl addbr xenbr1
# brctl addif xenbr1 eth0:1
# ifconfig xenbr1 up
	
if __name__ == '__main__':
	xen
	
	
	
#	>>> import os
#	>>> os.system("cp /opt/vcm/imgxen/centos.5-2.img /xen/testttttt")
