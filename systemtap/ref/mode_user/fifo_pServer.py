import os, time  

read_path = "/tmp/client_to_server_fifo"  
write_path = "/tmp/server_to_client_fifo"  
bufsize = 1024;

try:  
	os.mkfifo( write_path )  
	os.mkfifo( read_path )  
except OSError, e:  
	print "mkfifo error:", e  

rf = os.open( read_path, os.O_RDONLY )  
f = os.open( write_path, os.O_WRONLY )  
print "SERVER ON."


while True: 	

	bufR = os.read( rf, bufsize ) 
	bufR = bufR.rstrip('\x00')
	if bufR  == 'exit':
		print "Server off"
		break
	elif len(bufR) != 0:
		print "Receved: ", "-"+bufR+"-"
		time.sleep(3)
		print "Sending back...", bufR
		bufW = os.write(f, bufR)
		print "---------------"
			

os.close( f )  
os.close( rf )  
os.unlink(read_path)
os.unlink(write_path)
