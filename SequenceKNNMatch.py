import numpy as np
import matplotlib.pyplot as plt
from TIFF_reader import Read_Tiff
import time
from operator import itemgetter

#path = 'playData/fullProcessedData/'
path = 'playData/testData/'
pathTarget = 'playData/testData/'

def getClosestSequence(dataDict, targetFiles, k):
	targetImages = []

	for targetFile in targetFiles:
		try:
			targetI = plt.imread(pathTarget+targetFile, format='grayscale')
			targetImages.append(targetI)
		except:
			print("the file does not exist in the dataset.\n")
			return -1

	sequenceStatus = []
	num_row = targetImages[0].shape[0]

	for targetI in targetImages:
		sequence = []
		for key in dataDict:
			euclidean_dist = 0
			similarity = 0 
			test = 0
			for row_test, row_target in zip(dataDict[key], targetI):
				#find the euclidean distance between 2 matrices
				euclidean_dist = np.linalg.norm(row_test-row_target)
				similarity += 1 / (1 + euclidean_dist)

			similarity_avg = similarity/num_row
			sequence.append((key, round(100*similarity_avg)))
		sequence = sorted(sequence, reverse= True, key=lambda x: x[1])[:k]
		sequenceStatus.append(sequence)

	ClosestSequence = [x[0] for x in sequenceStatus]

	return ClosestSequence


def main():
	dataDict, num_file = Read_Tiff(path)

	targetFile = input("please enter the name of the target files separated by , with no space in between (ex. 0932.tiff,0933.tiff,0934.tiff)\n")
	targetFiles = targetFile.split(",")
	k = input("please enter the number of closest sequence of images you would like (for now k is limited to 1). \n")

	while(int(k) > num_file or int(k) != 1):
		print("k is currently only limited to 1.")
		k = input("please enter the number of closest sequence of images you would like (for now k is limited to 1). \n")

	start = time.time()
	result = getClosestSequence(dataDict, targetFiles, int(k))
	end = time.time()
	print('Closest matches are:', list(map(itemgetter(0), result)) , "with", sum(list(map(itemgetter(1), result)))/len(result), "% match. Found in", round(end-start,3), "seconds.")

main()
