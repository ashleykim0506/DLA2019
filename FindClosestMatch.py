import numpy as np
import matplotlib.pyplot as plt
from TIFF_reader import Read_Tiff
import time

path = 'datatest/'

def getClosestMatch(dataDict, targetFile):
	try:
		targetI = plt.imread('dataset/'+targetFile, format='grayscale')
	except:
		print("the name of the file does not exist in the dataset.\n")
		return -1

	matchStatus = []
	num_row = targetI.shape[0]

	for key in dataDict:
		euclidean_dist = 0
		similarity = 0 
		for row_test, row_target in zip(dataDict[key], targetI):
			#find the euclidean distance between 2 matrices
			euclidean_dist = np.linalg.norm(row_test-row_target)
			similarity += 1 / (1 + euclidean_dist)
		similarity_avg = similarity/num_row
		matchStatus.append((key, similarity_avg))

	return matchStatus
 
def main():
	dataDict, num_file = Read_Tiff(path)
	start = time.time()

	targetFile = input("please enter the name of the target file. (ex. 0932.tiff)\n")
	result = getClosestMatch(dataDict, targetFile)
	end = time.time()

	result = sorted(result, reverse= True, key=lambda x: x[1])
	print(result)

	print('Closest match is:', result[0][0], "with", round(100*result[0][1],3), "% match.",  'Found in', round(end-start,3), 'seconds.')
	

main()