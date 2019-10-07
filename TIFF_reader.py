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

def main():
	dataDict = Read_Tiff()


main()
