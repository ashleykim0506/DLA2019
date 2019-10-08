import numpy as np
import matplotlib.pyplot as plt
from TIFF_reader import Read_Tiff
import time

path = 'dataset/'

def getExactMatch(dataDict, targetFile):
	try:
		targetI = plt.imread(path+targetFile, format='grayscale')
	except:
		print("the name of the file does not exist in the dataset.\n")
		return -1

	#O(n)
	for key in dataDict:
		if(np.array_equal(dataDict[key], targetI)):
			return key

def main():
	dataDict, num_file = Read_Tiff()
	start = time.time()

	targetFile = input("please enter the name of the target file. (ex. 0932.tiff)\n")
	key = getExactMatch(dataDict, targetFile)

	end = time.time()
	if(key == targetFile):
		print('Success! Target file (', key, ") found in ", round(end-start,3), "seconds.")
	else:
		print('Failed to find target file')

main()
