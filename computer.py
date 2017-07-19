# -*- coding: utf-8 -*-
import colorsys
from colorvariation import Color, RgbVariation, HsvVariation, HlsVariation
from renderer import ImageGeneration
from colordifference import ListComparator, BlackWhiteComparator, ResultStatistics, ColorCleaning
from terminaltables import AsciiTable

def ColorComputing(RColorInput,GColorInput,BColorInput,MinTolerance,MaxTolerance):

	TestColor = Color([RColorInput,GColorInput,BColorInput],"","")

	##############  Color spaces differences  #############

	# Convert RGB (base 256) to HSV (between 0 and 1 )
	TestColor.HSV = list(colorsys.rgb_to_hsv(TestColor.RGB[0] / 255, TestColor.RGB[1] / 255, TestColor.RGB[2] / 255))

	# Convert RGB (base 256) to HSV (between 0 and 1 )
	TestColor.HLS = list(colorsys.rgb_to_hls(TestColor.RGB[0] / 255, TestColor.RGB[1] / 255, TestColor.RGB[2] / 255))

	# Generate Color variations using the RGB Color space
	RgbList = RgbVariation(TestColor)

	# Generate Color variations using the HSV Color space with 30° tolerance on H
	HsvList = HsvVariation(TestColor,30)

	# Generate Color variations using the HLS Color space with 30° tolerance on H
	HlsList = HlsVariation(TestColor,30)

	# Calculate the Euclidean difference between the color reference and the color variations
	RgbDifference = ListComparator(TestColor,RgbList)
	HsvDifference = ListComparator(TestColor,HsvList)
	HlsDifference = ListComparator(TestColor,HlsList)

	# Calculate Euclidean difference average, Stdev and variance for each Color Space Variation
	TableData = [["Color Space Variation","Euclidean Difference Average","Euclidean Difference Stdev"," Euclidean Difference Variance"],"","",""]
	TableData[1] = ResultStatistics("RGB",RgbDifference)
	TableData[2] = ResultStatistics("HSV",HsvDifference)
	TableData[3] = ResultStatistics("HLS",HlsDifference)

	# Create result table to be displayed via the console
	Result = AsciiTable(TableData)
	print (Result.table)

	##############  All Color Spaces  #############

	# Merge RGB, HSV, HLS color variations lists
	CompleteList = RgbList + HsvList + HlsList

	# Calculate the Euclidean difference between the color reference and the color variations
	ListDifference = ListComparator(TestColor,CompleteList)

	# Eliminate repetetive colors and outlier colors
	CleanCompleteList = ColorCleaning(CompleteList,ListDifference,MinTolerance,MaxTolerance)

	# Create an image with all color variations 
	ImageGeneration(CleanCompleteList,"Full")
	
	return CleanCompleteList