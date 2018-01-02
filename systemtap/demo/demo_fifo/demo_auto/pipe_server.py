import os
import signal
import subprocess
import shutil 
import threading
import time

stap_ok = 0
SIG_STPFIFO = 44

file_list = set()
backup_dir = "backup/"
procf_fifo = "/proc/stp-fifo"
procf_sem = "/proc/stp-sem"

def run_mal():
	#while "systemtap_module_init() returned 0" not in proc.stderr.readline():
	#	pass
	while 1:
		if os.path.exists(procf_fifo) and os.path.exists(procf_sem):break
	#time.sleep(1)
	#print time.time()
	#time.sleep(2)
	sub = subprocess.Popen(["python", "mal.py"])
	print 'start malware', sub.pid


def sig_handler (signum, frame):
	bufsize = 1024 # can use 
	rf = os.open(procf_fifo, os.O_RDONLY)
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
	f = os.open(procf_sem, os.O_WRONLY)
	os.write(f,"hi")
	os.close(f)

print "start Analyzer.py pid", os.getpid() 
signal.signal(SIG_STPFIFO, sig_handler)
proc = subprocess.Popen(["staprun", "-vv","-x", str(os.getpid()),"-o", "stap.log","stap_.ko",], stderr=subprocess.PIPE)
runMal = threading.Thread(target=run_mal, name='runMal')
runMal.start()
#signal.siginterrupt(SIG_STPFIFO, True)
#print 'Pipe_Server pid', os.getpid()
while 1:	
	signal.pause()
#	send_sem()
	print '---pause'



print 'exit'


