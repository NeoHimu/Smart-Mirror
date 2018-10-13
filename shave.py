import numpy as np
import cv2
from copy import deepcopy

cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

#magnifier_region = (150,200)
#480, 640
cap = cv2.VideoCapture(0)
img_ad = cv2.imread('washing_powder.jpg')
#face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
print("hello")
image1 = None
#while cap.isOpened():
#	cv2.imshow('window',img_ad)
#	k = cv2.waitKey(33) & 0xff
#	if k == ord("c"):
#		break
while cap.isOpened():
	ret, img = cap.read() # img = frame
	#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	#faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	#print(len(faces))

	#print(img.shape)
	#This flipping is done to avoid the laterally inverted motion
	b=np.fliplr(img[:,:,0])
	g=np.fliplr(img[:,:,1])
	r=np.fliplr(img[:,:,2])
	img = cv2.merge([b, g, r])
	
	key = cv2.waitKey(33) & 0xFF
	if key == ord("a"):
		print("a")
		image1 = cv2.resize(img.copy(), (240, 320))
		
	elif key == ord("s") and image1 is not None:
		print("s")
		image2 = cv2.resize(img.copy(), (240, 320))
		bc = np.concatenate((image1[:,:,0],image2[:,:,0]), 1)
		gc = np.concatenate((image1[:,:,1],image2[:,:,1]), 1)
		rc = np.concatenate((image1[:,:,0],image2[:,:,0]), 1)
		
		while True:
			cv2.imshow('window',cv2.merge([bc, gc, rc]))
			k = cv2.waitKey(50) & 0xff
			if k == 27:
				break
	
	cv2.imshow('window',img)
	k = cv2.waitKey(33) & 0xff
	if k == 27:
		break
		
cap.release()
cv2.destroyAllWindows()
