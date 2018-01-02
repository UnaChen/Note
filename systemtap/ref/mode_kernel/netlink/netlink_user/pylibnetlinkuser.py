from ctypes import *

mylib = CDLL("./libnetlinkuser.so")

if ( mylib.netlink_init() == 0):
	print "succ"
print '---send'

while 1:
	mylib.netlink_recvMsg()
	if mylib.netlink_isExit():
		break
	mylib.netlink_initMsg()
	print '---send'
	mylib.netlink_sendMsg()

mylib.netlink_exit()
print 'exit'
	
