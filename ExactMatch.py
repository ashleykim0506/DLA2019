import numpy as np
import matplotlib.pyplot as plt
from TIFF_reader import Read_Tiff

path = 'dataset/'

def getExactMatch(dataDict, targetFile):
	targetI = plt.imread(path+targetFile, format='grayscale')

	#O(n)
	for key in dataDict:
		if(np.array_equal(dataDict[key], targetI)):
			return key

def main():
	dataDict = Read_Tiff()
	targetFile = input("please enter the name of the target file. (ex. 0932.tiff)\n")
	key = getExactMatch(dataDict, targetFile)

	if(key == targetFile):
		print('Success! Target file is: ', key)
	else:
		print('Failed to find target file')

main()
