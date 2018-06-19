import numpy as np
import cv2
from copy import deepcopy

cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

#magnifier_region = (300,400)
#480, 640
cap = cv2.VideoCapture(0)

while cap.isOpened():
	ret, img = cap.read() # img = frame
	print(img.shape)
	#This flipping is done to avoid the laterally inverted motion
	b=np.fliplr(img[:,:,0])
	g=np.fliplr(img[:,:,1])
	r=np.fliplr(img[:,:,2])
	img = cv2.merge([b, g, r])
	temp_img = deepcopy(img[90:390,0:400,:])
	newimg = cv2.resize(temp_img,(900,1200))
	img[90:390,0:400,:] = newimg[150:450,200:600,:]
	#img = newimg[0:400,0:640,:] Full Screen magnifier
	cv2.imshow('window',img)
	
	k = cv2.waitKey(50) & 0xff
	if k == 27:
		break
		
cap.release()
cv2.destroyAllWindows()
