import numpy as np
import matplotlib.pyplot as plt
from TIFF_reader import Read_Tiff
import time

#path = 'playData/fullProcessedData/'
path = 'playData/testData/'

def getExactMatch(dataDict, targetFiles):
	targetI = []
	for targetFile in targetFiles:
		try:
			targetI.append(plt.imread(path+targetFile, format='grayscale'))
		except:
			print("the files does not exist in the dataset.\n")
			return -1

	seq = []

	#avg O(n^2) 
	for target in targetI:
		for key in dataDict:
			#worst O(n) else O(1)
			if(np.array_equal(dataDict[key], target)):
				seq.append(key)

	return seq

def main():
	dataDict, num_file = Read_Tiff(path)

	targetFile = input("please enter the name of the target files separated by , with no space in between (ex. 0932.tiff,0933.tiff,0934.tiff)\n")
	targetFiles = targetFile.split(",")

	start = time.time()
	keys = getExactMatch(dataDict, targetFiles)

	end = time.time()
	if(keys == targetFiles):
		print('Success! Target files (', keys, ") found in", round(end-start,3), "seconds.")
	else:
		print('Failed to find target file')

main()
