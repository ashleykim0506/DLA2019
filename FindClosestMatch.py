import numpy as np
import matplotlib.pyplot as plt
from TIFF_reader import Read_Tiff
import time
from operator import itemgetter

path = 'playData/fullProcessedEvenData/'
pathTarget = 'playData/fullProcessedData/'


def getClosestMatch(dataDict, targetFile):
	try:
		targetI = plt.imread(pathTarget+targetFile, format='grayscale')
	except:
		print("the file does not exist in the dataset.\n")
		return -1

	matchStatus = []
	num_row = targetI.shape[0]

	for key in dataDict:
		euclidean_dist = 0
		similarity = 0 
		test = 0
		for row_test, row_target in zip(dataDict[key], targetI):
			#find the euclidean distance between 2 matrices
			euclidean_dist = np.linalg.norm(row_test-row_target)
			similarity += 1 / (1 + euclidean_dist)

		similarity_avg = similarity/num_row
		matchStatus.append((key, round(100*similarity_avg)))

	return matchStatus
 
def main():
	dataDict, num_file = Read_Tiff(path)

	targetFile = input("please enter the name of the target file. (ex. 0932.tiff)\n")
	k = input("please enter the number of closest matched images you would like. \n")

	while(int(k) > num_file):
		print("please select a smaller k. \n")
		k = input("please enter the number of closest matched images you would like. \n")

	start = time.time()
	result = getClosestMatch(dataDict, targetFile)
	end = time.time()

	result = sorted(result, reverse= True, key=lambda x: x[1])
	#print(result)
	result = result[:int(k)]

	print('Closest matches are:', list(map(itemgetter(0), result)) , "with", list(map(itemgetter(1), result)), "% match. Found in", round(end-start,3), "seconds.")
	

main()