import cv2

class resize:
	def __init__(self,img,si1,si2):
		imgs=str(img)
		path="Process_Image/Resize/"
		img=cv2.imread(img)
		s1=int(si1)
		s2=int(si2)
		img=cv2.resize(img,(s1,s2))
		cv2.imwrite(path+imgs, img)
