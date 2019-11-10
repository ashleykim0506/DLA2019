"""
Title: 
Author: 
Address: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html
"""
from os import listdir
import os
import numpy as np
import cv2
#from matplotlib import pyplot as plt

#path = '8bitdataset/'
path = '8bitdataset/'
savePath = 'binary8bitdataset'


def OtsuBinarize():
	fileList = listdir(path)
	num_data = len(fileList)

	for file in fileList:
		if(not file.startswith('.')):
			#im = plt.imread(path+file, format='grayscale')
			img = cv2.imread(path+file,0)

			# global thresholding
			ret1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

			'''
			# Otsu's thresholding
			ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

			# Otsu's thresholding after Gaussian filtering
			blur = cv2.GaussianBlur(img,(5,5),0)
			ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
			'''

			cv2.imwrite(os.path.join(savePath, file), th1)




def main():
	OtsuBinarize()

main()
