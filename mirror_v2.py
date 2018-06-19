import numpy as np
import cv2
import os, errno
import time

#This is done to show images in full window
#cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
#cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480), True)
flag_1 = 0 # recording mode if not set
flag_2 = 0 # nothing has been recorded as of now if not set
count = 0 # Total count (contiguous) of the image without face
end_count=0# This is used to append "offset" frames in the video to avoid it from crashing and also so that user can see his face at the end
offset_start = 20 #This is the max value
offset_end = 20 #this is done because user will get bored if he has to wiat for more time.
queue = []
min_no_frames = 40 #contiguous number of frames that does not have any face
do_it_n_times = 2
while cap.isOpened():
	ret, img = cap.read() # img = frame
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	print(len(faces))
	
	#This flipping is done to avoid the laterally inverted motion
	b=np.fliplr(img[:,:,0])
	g=np.fliplr(img[:,:,1])
	r=np.fliplr(img[:,:,2])
	img = cv2.merge([b, g, r])
	
	if len(faces)==0: #no face found
		if flag_1 == 0:
			# Define the codec and create VideoWriter object
			fourcc = cv2.VideoWriter_fourcc(*'XVID')
			out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
			flag_1 = 1 #it should be minimum min_no_frames to get displayed
			count=0
		out.write(img)
		count += 1

	else:#play the recorded video and after playing start the camera
		
		#record "offset" number of frames to prepend in the video
		if flag_1 == 0:	#but face is present in the frame
			if len(queue)<offset_start:
				queue.append(img)
			else:
				queue.pop(0)
				queue.append(img)
	
	
		if flag_1 == 1 and end_count<=offset_end: #it has just came from non-face mode. So, append some images to the video
			out.write(img)
			end_count += 1
			count += 1
		elif end_count==offset_end+1:
			flag_1 = 0
			flag_2 = 1 #something has been recorded i.e. end of the recording
			out.release()
		
		#ignore some random fluctuations
		if flag_2 != 0 and count-end_count>min_no_frames: #play because something has been recorded
			cap.release() # release the previous video capture object
			#play the video
			count += end_count # extra appended frames have been included in the count
			end_count = 0 # this extra count is made to zero for next time
			temp_count = count
			for i in range(0, do_it_n_times):
				count = temp_count
				cap_temp = cv2.VideoCapture('output.avi') # allocate new video capture object
				#show images stored in the queue first
				for images in queue:
					cv2.imshow('window',images)
					k = cv2.waitKey(50) & 0xff
					if k == 27:
						break
			
				while cap_temp.isOpened() and count>0: # this count is necessary otherwise it'll crash
					ret_temp, frame_temp = cap_temp.read() 
					#print(ret_temp)
					#print("Your are inside!")
				
					if ret_temp == True:
						cv2.imshow('window',frame_temp)
						k = cv2.waitKey(50) & 0xff
						if k == 27:
							break
					count -= 1
			del queue#make the queue empty
			queue = [] # declare a new queue
			cap_temp.release() # release new video capture object
			flag_2=0 #nothng new is recorded
			cap = cv2.VideoCapture(0) # start the cam
		else:
			print("Entered!")
			#for (x,y,w,h) in faces:
			#	cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
			#show the black image to make the mirror show user's face
			img = np.zeros((640,480))
			cv2.imshow('window',img.T)
			k = cv2.waitKey(50) & 0xff
			if k == 27:
				break

cv2.destroyAllWindows()
