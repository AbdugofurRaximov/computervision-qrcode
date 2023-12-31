import cv2
import numpy as np
from pyzbar.pyzbar import decode


cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

with open('data.text') as f:
    datalist = f.read().splitlines()
while True:
    success, img = cap.read()
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        print(myData)
        if myData in datalist:
            output = "Kirish mumkin !!!!"
            rang = (0, 255, 0)
        else:
            output = "Kirish mumkin emas !!!!"
            rang = (0, 0, 255)
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, (255,0,255), 5)
        pts2 = barcode.rect
        cv2.putText(img, output, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, rang, 2)
    cv2.imshow("Natija", img)
    if cv2.waitKey(1) == ord("q"):
        break
