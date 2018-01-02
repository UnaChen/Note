import os 
import sys

write_path = "/tmp/client_to_server_fifo"  
read_path = "/tmp/server_to_client_fifo"  
f = os.open( write_path, os.O_WRONLY)   
rf = os.open(read_path, os.O_RDONLY)  
  
#f = os.open( write_path, os.O_WRONLY | os.O_NONBLOCK)   
#rf = os.open(read_path, os.O_RDONLY | os.O_NONBLOCK)  
print os.read(rf,1024)
while True:  
	req = sys.argv[1]
	len_send = os.write( f, req ) 
	print "request", req  
	
	if rf == None:  
		rf = os.open( read_path, os.O_RDONLY )  
		print "client opened rf", rf  
	if req != 'exit':
		s = os.read(rf, 1024)
#		while len(s) == 0:
#			s = os.read( rf, 1024 )  
#			print "wait.."
		print "received", s  
	break



