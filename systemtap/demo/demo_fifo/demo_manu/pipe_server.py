import os
import signal
import subprocess
import shutil 

stap_ok = 0
SIG_STPFIFO = 44

file_list = set()
backup_dir = "backup/"

def sig_handler (signum, frame):
	bufsize = 1024 # can use 
	rf = os.open("/proc/stp-fifo", os.O_RDONLY)
	bufR = os.read(rf, bufsize)
	print 'read: ',bufR
	syscall, argstr, retstr = bufR.split("==")
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
	os.close(rf)
	send_sem()
	print "--send succ"

def send_sem():
	procfs_sem = "/proc/stp-sem"
	f = os.open(procfs_sem, os.O_WRONLY)
	os.write(f,"hi")
	os.close(f)


signal.signal(SIG_STPFIFO, sig_handler)
signal.siginterrupt(SIG_STPFIFO, True)
print 'Pipe_Server pid', os.getpid()
while 1:	
	signal.pause()
#	send_sem()
	print '---pause'



print 'exit'


