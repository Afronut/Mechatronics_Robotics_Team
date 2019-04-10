from roomba.ballScrew import*
from roomba.barcode_reader import *
from time import sleep
while True:
  if barcode_funder():
    print(barcode_funder())
  sleep(6)
