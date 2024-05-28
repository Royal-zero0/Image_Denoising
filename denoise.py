import cv2
import os
from keras.models import load_model
from model import Models
from noise_adder import noise
from keras.preprocessing.image import img_to_array
import matplotlib.pyplot as plt
import numpy as np
class denoiser_m:
	
	def __init__(self,img,n,m):
		imgs=str(img)
		path="Process_Image/Denoise/"
		img=cv2.imread(img,1)
		img=cv2.resize(img,(240,240))
		img2=img
		img2=img2.astype('float')/255.0
		img2=img_to_array(img2)
		img2=np.expand_dims(img2,axis=0)
		mod=m.Arch1()
		mod.load_weights('noise.h5')
		img2=mod.predict(img2)[0]
		plt.imsave(path+imgs,img2)

