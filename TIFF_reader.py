from os import listdir
import numpy as np
import matplotlib.pyplot as plt

path = 'dataset/'

def Read_Tiff():
	dataset = {}

	fileList = listdir(path)

	for file in fileList:
		I = plt.imread(path+file, format='grayscale')
		dataset[file] = I 
		
	#return in dictionary where key is the name of the file
	#and value is the matrix of the image
	return dataset

def exactMatch(dataDict, targetFile='0937.tiff'):
	targetI = plt.imread(path+targetFile, format='grayscale')

	#O(n)a
	for key in dataDict:
		if(np.array_equal(dataDict[key], targetI)):
			return key

def main():
	dataDict = Read_Tiff()
	assert('0937.tiff'==exactMatch(dataDict))


main()