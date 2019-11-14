"""
Title: 
Author: 
Address: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html
"""
from os import listdir
import os
import numpy as np
import cv2
from PIL import Image, ImageDraw
#from matplotlib import pyplot as plt

#path = 'playData/bitdataset/'
path = 'playData/8bitdataset/'
#savePath = 'playData/binary8bitdataset'

savePath = 'playData/otsu8bitbinarydata'


def OtsuBinarize():
	fileList = listdir(path)
	num_data = len(fileList)

	for file in fileList:
		if(not file.startswith('.')):
			#im = plt.imread(path+file, format='grayscale')
			img = cv2.imread(path+file,0)

			x = 0
			y = 0
			r = 930
			rectX = (x - r) 
			rectY = (y - r)
			crop_img = img[y:(y+2*r), x:(x+2*r)]
			blur = cv2.GaussianBlur(crop_img,(5,5),0)
			ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
			

			#img = Image.fromarray(crop_img)
			# global thresholding
			#ret1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

			#cv2.imwrite(os.path.join(savePath, file), th1)
			cv2.imwrite(os.path.join(savePath, file), th3)


def main():
	OtsuBinarize()

main()
