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
    pallet, rack, row, col, dock = rack_finder(assignement)
    code = barcode_funder()[0]
    start = floor_finder(code)
    print(start)
    end = rack['rack_id']
    path_to_take, inter = path_finder(start[1], end)
    print('got the path {}'.format(path_to_take))
    sleep(2)
    arduino.write("go_straight")
    print('Leaving for party')
# #     message=arduino.readline()
# #     if message:
# #         print (message)
# #     else:
# #         print('receive no message')
    for i in range(len(path_to_take)):
        code = barcode_funder()[0]
        if code.find('rack') != -1:
            floor = floor_rack_finder()[0]
        else:
            floor = floor_finder(code)[0]
        path = path_to_take[i]
        if path in path_to_take:
            if path in inter:
                for inte in inter:
                    if inte == path:
                        arduino.write(turn_finder(path, inte))
                sleep(6)
                arduino.write('line')
            else:
                pass
        else:
            path_to_take = path_finder(code[1], end)
            i = 0
        sleep(4)
