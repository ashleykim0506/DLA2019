""" Title: KNN Algorithm implementation in Python
Author: Nazanin1369
Date: 2017
Availability: https://github.com/Nazanin1369/DataMining-KNN/blob/master/main.py """
from os import listdir
import numpy as np
import matplotlib.pyplot as plt
from TIFF_reader import Read_Tiff
import time
import math
import operator

#path = 'dataset/'
#pathTarget = 'dataset/'
path = '8bitdatatest/'
pathTarget = '8bitdataset/'

def euclidianDistance(sample1, sample2, length):
    distance = 0
    for x in range(length):
        distance += pow(sample1[x] - sample2[x], 2)
    return math.sqrt(distance)


def getNeighbors(train_set, test_sample, k):
    distances = []
    neighbors = []
    length = len(test_sample - 1)

    for y in train_set:
        for x in y:
            #dist = euclidianDistance(test_sample, x, length)
            dist = np.linalg.norm(test_sample-x)
            distances.append((x , dist))

    distances.sort(key=operator.itemgetter(1))

    for x in range(k):
        neighbors.append(distances[x][0])

    return neighbors


def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]


def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x] == predictions[x]:
            correct += 1
    return round((correct/float(len(testSet))) * 100.0, 3)


def getClosestKNNMatch(k, test_data, train_data):
    print('*******************************************')
    print('************    K = ', k , '  ******************')
    print('*******************************************')
    predictions = []

    print('--> Calculating KNN...')
    for index, test_sample in enumerate(test_data):
        neighbors = getNeighbors(train_data, test_sample, k)
        #neighbors_prediction = getResponse(neighbors)
        predictions.append(neighbors)

    return predictions


def main():
    dataset = []

    fileList = listdir(path)
    num_data = len(fileList)

    for file in fileList:
        if(not file.startswith('.')):
            I = plt.imread(path+file, format='grayscale')
            dataset.append(I)

    start = time.time()

    targetFile = input("please enter the name of the target file. (ex. 0932.tiff)\n")

    try:
        targetI = plt.imread(pathTarget+targetFile, format='grayscale')
    except:
        print("the file does not exist in the dataset.\n")
        return -1

    k = input("please enter the number of closest matched images you would like. \n")

    closestNeighbors = getClosestKNNMatch(int(k), targetI, dataset)
    end = time.time()

    print(k, 'closest neighbors: ', closestNeighbors, 'Found in ', round(end-start,3), 'seconds.')

    print('--> Calculating Accuracy...')
    accuracy = getAccuracy(test_data, predicted_data)
    print('Accuracy = ', accuracy, '%')



main()
