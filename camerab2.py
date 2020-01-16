#   importing  opencv

import  cv2
import  time
#  now  i  can load any  image  by using  camera
cap=cv2.VideoCapture(0)

#  check   activeness of camera
#  now taking  picture 
while  True :
	status,frame=cap.read()
	# converting  image  from  color to gray scale 
	colorless=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	print(frame.shape)
	print(frame)
	cv2.imshow('live',frame/100)
	cv2.imshow('live1',colorless)
	if cv2.waitKey(10) &  0xff == 'q' :
#               0xff  means capture keyboard input
		break

#  destroy or close window if hanged 
cv2.destroyAllWindows()











