import socket
from roomba.ballScrew import ballScrewForward, ballScrewBackward
from roomba.barcode_reader import barcode_funder, string_processor
from nanpy import SerialManager
from threading import Thread
from roomba.server import run_server
import roomba.setting as st
from time import sleep
from roomba.map import *

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
    if code.find('ack') != -1:
        floor = front_rack_finder(code)
        start = floor[2]
        print(floor, "rack")
    else:
        floor = floor_finder(code)
        print(floor)
        start = floor[1]
        print(start)
    end = rack['rack_id']
    path_to_take, inter = path_finder(start, end)
    print('got the path {}'.format(path_to_take))
    sleep(2)
    arduino.write("line")
    print('Leaving for party')
# #     message=arduino.readline()
# #     if message:
# #         print (message)
# #     else:
# #         print('receive no message')
    # path_to_take.pop(0)
    for i in range(len(path_to_take)):
        print(path_to_take)
        code = barcode_funder()[0]
        # start = code
        print(code)
        sleep(1)
        floor = None
        if code.find('ack') != -1:
            floor = front_rack_finder(code)
            start = floor[2]
            print(floor, "rack")
        else:
            floor = floor_finder(code)
            print(floor)
            start = floor[1]
        print(i)
        path = path_to_take[i]
        if floor[0] in path_to_take:
            if path in inter:
                print(path)
                for inte in inter:
                    if inte == path:
                        turn = turn_finder(path, inte)
                        print(turn)
                        if turn is not None:
                            arduino.write(turn)
                            break
                sleep(6)
                arduino.write('line')
        else:
            path_to_take, inter = path_finder(start, end)
            i = 0
        sleep(4)
