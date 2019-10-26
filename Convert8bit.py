from os import listdir
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

path = 'dataset/'
savePath = '8bitdataset/'

def main():
	fileList = listdir(path)
	num_data = len(fileList)

	for file in fileList:
		if(not file.startswith('.')):
			I = plt.imread(path+file, format='grayscale')
			im = Image.fromarray(I)
			im.save(savePath+file)
			#img8 = (I/256).astype('uint8')
			#img8.save(savePath+file+'.tiff')


main()