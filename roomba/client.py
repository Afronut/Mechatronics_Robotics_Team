import socket
import barcode_reader as br

HOST = '10.201.92.66'  # Enter IP or Hostname of your server
# Pick 345an open Port (1000+ recommended), must match the server port
PORT =  12397 #new comment
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# Lets loop awaiting for your input
while True:
	command = raw_input('Enter your command: ')
	s.send(command)
	reply = s.recv(1024)
	if reply :
		code = br.barcode_funder()
                if code !='':
		    s.send(code)
	print code 
        code = ''
