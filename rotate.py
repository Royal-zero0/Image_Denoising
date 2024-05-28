import cv2
import imutils
class rotate:
 	
	def __init__(self,i,ang):
		imgs=str(i)
		path="Process_Image/Rotate/"
		image = cv2.imread(i)
		a=int(ang)
		rot = imutils.rotate(image, angle=a)
		cv2.imwrite(path+imgs, rot)
		
