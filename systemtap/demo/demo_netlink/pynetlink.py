import signal
import time
import subprocess
import threading
import os
from ctypes import *
import shutil

file_list = set()
backup_dir = "backup/"

def dosth(msg):
	print '----dosth', msg
	syscall, argstr, retstr = msg.split("==")
	if syscall == "open":
		filename = argstr.split(",")[0]
		flag = argstr.split(",")[1]
		if "O_CREAT" in flag or "O_RDWR" in flag or "O_WRONLY" in flag:
			file_list.add(filename[1:-1])
	elif syscall == "unlink":
		filename = argstr[1:-1]
		if filename in file_list:
			shutil.copy(filename, backup_dir)
                        file_list.remove(filename)
	print '----dosth FIN', msg

def run_mal():
	while 1:
		mylib.netlink_recvMsg.restype = c_char_p
		recvMsg_p = mylib.netlink_recvMsg()
		recvMsg = string_at(recvMsg_p)
		print recvMsg
		dosth(recvMsg)
		mylib.netlink_initMsg()
		mylib.netlink_sendMsg()
	mylib.netlink_exit()
	print 'exit run'

mylib = CDLL("./libnetlinkuser.so")
print "load lib"

proc = subprocess.Popen(["staprun", "-vv","-x", str(os.getpid()),"-o", "stap.log","stap_.ko",], stderr=subprocess.PIPE)
while "systemtap_module_init() returned 0" not in proc.stderr.readline():
        pass

if ( mylib.netlink_init() == 0):
	print "succ"

print "netlink init"
#mylib.netlink_sendMsg()

runMal = threading.Thread(target=run_mal, name='runMal')
runMal.setDaemon(True)
runMal.start()

print "thread start"
#runMal._stop()
#flag = 1
sub = subprocess.Popen(["python", "mal.py"])
sub.wait()

try:
	#r = proc.poll()
	#print "stap subprocess retval %r", r
	#time.sleep(10)
	print proc.pid
	proc.kill()
	#proc.wait()
except Exception as e:
	print "Exception killing stap: %s", e

print "exit"

