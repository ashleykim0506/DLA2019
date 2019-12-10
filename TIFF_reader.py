from os import listdir
import numpy as np
import matplotlib.pyplot as plt
import time

#path = 'playData/dataset/'
#path = 'playData/8bitdataset/'
#path = 'playData/binary8bitdataset/'
#path = 'playData/otsu8bitbinarydata/'
path = 'playData/fullProcessedData/'

def Read_Tiff(path):
	dataset = {}

	fileList = listdir(path)
	num_data = len(fileList)

	for file in fileList:
		if(not file.startswith('.')):
			I = plt.imread(path+file, format='grayscale')
			dataset[file] = I 
		
	#return in dictionary where key is the name of the file
	#and value is the matrix of the image
	return dataset, num_data

def main():
	start = time.time()
	dataDict, num_data = Read_Tiff(path)
	end = time.time()

	print("iterated through", num_data, "files in", round(end-start,3), " seconds.")


main()
