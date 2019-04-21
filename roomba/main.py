import socket
from roomba.ballScrew import ballScrewForward, ballScrewBackward
from roomba.ardiuno2pi import send_arduino_message
from roomba.barcode_reader import barcode_funder, string_processor
from nanpy import SerialManager
# Server IP or Hostname
connection = SerialManager(device='/dev/ttyUSB0')
HOST = socket.gethostname()
# Pick an open Port (1000+ recommended), must match the client sport
PORT = 12397
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

# managing error exception
try:
	s.bind(("", PORT))
except socket.error:
	print 'Bind failed'
    return
	
s.listen(5)
print 'Socket awaiting messages'
(conn, addr) = s.accept()
print 'Connected'
ballScrew_is_forward=False
ballScrew_is_backward=True
# awaiting for message
while True:
	try:
		data = conn.recv(1024)
	except:
		pass
	# process your message
	if data == None or data == '':
		barcode=barcode_funder()
		decoded = string_processor(barcode)
		connection.write('Hello there')
	if data == 'pallet_picked':
		send_arduino_message('90')
		data=''
    elif data =='':
		
	conn.send(reply)
conn.close() # Close connections
