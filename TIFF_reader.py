from os import listdir
import numpy as np
import matplotlib.pyplot as plt
import time

path = 'dataset/'

def Read_Tiff():
	dataset = {}

	fileList = listdir(path)
	num_data = len(fileList)

	for file in fileList:
		I = plt.imread(path+file, format='grayscale')
		dataset[file] = I 
		
	#return in dictionary where key is the name of the file
	#and value is the matrix of the image
	return dataset, num_data

def main():
	start = time.time()
	dataDict, num_data = Read_Tiff()
	end = time.time()

	print("iterated through ", num_data, " files in ", round(end-start,3), " seconds.")


main()
