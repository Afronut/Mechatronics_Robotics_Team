from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import datetime
import time
import imutils
import cv2

ap=argparse.ArgumentParser()
ap.add_argument("-o", "--output", type=str, default="barcodes.csv",
	help="path to output CSV file containing barcodes")
args=vars(ap.parse_args())

print("Starting video stream")

#vs=VideoStream(src=0).start()   #uncomment to use USB camera
vs=VideoStream(usePiCamera=True).start()
time.sleep(2.0)

csv=open(args["output"], "w")
found=set()

while True:
	frame=vs.read()
	frame=imutils.resize(frame, width=400)
	
	barcodes=pyzbar.decode(frame)
	
	for barcode in barcodes:
		(x, y, w, h)=barcode.rect
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
				
	cv2.imshow("Barcode Scanner", frame)
	key=cv2.waitKey(1) & 0xFF

	if key == ord("q"):
		break
		
print("cleaning up")
csv.close()
cv2.destroyAllWindows()
vs.stop()
          
