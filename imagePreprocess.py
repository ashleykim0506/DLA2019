from Convert8bit import * 
from OtsuBinarize import * 


def main():
	
	print("converting to 8bit...\n")
	convert8bit('playData/fullData/', 'playData/tmp/')
	print("converted to 8bit\n")

	print("binarizing the images...\n")
	OtsuBinarize('playData/tmp/', 'playData/fullProcessedData')
	print("images binarized\n")




main()
