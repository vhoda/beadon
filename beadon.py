import cv2
import numpy as np
import tkinter as tk

cap = cv2.VideoCapture('C:\\Users\\vhoda\\Desktop\\bea\\beadon.mp4')

if (cap.isOpened()== False): 
  print("lol")

while(cap.isOpened()):
  ret, frame = cap.read()
  if ret == True:
    cv2.imshow('bea',frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
  else: 
    break

cap.release()
cv2.destroyAllWindows()
