import socket
from roomba.ballScrew import ballScrewForward, ballScrewBackward
from roomba.barcode_reader import barcode_funder, string_processor
from nanpy import SerialManager
from threading import Thread
from roomba.server import run_server
import roomba.setting as st
from time import sleep
from roomba.map import*

# Thread(target=run_server).start()
assignement = None
try:
    arduino = SerialManager(device='/dev/ttyACM0')
except:
    pass

while True:
    # Import required modules

    #connection.write('Hi there')
    # sleep(2)
    # message=connection.readline()
    # if message:
     #   print(message)
    # else:
   #     print('no message yet')
    sleep(2)
    if not assignement:
        assignement = barcode_funder()[0]
        print(assignement)
    sleep(4)
    #     pallet, rack, row, col,dock=rack_finder(assignement)
    #     code=barcode_funder()[0]
    #     start=floor_finder(code)
    #     end=rack['rack_id']
    #     path_to_take=path_finder(start[1],end)
    sleep(2)
    arduino.write("go_straight")
# #     message=arduino.readline()
# #     if message:
# #         print (message)
# #     else:
# #         print('receive no message')
    while True:
        code = barcode_funder()[0]
        print(code)
        sleep(4)
