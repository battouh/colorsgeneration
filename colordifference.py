# -*- coding: utf-8 -*-
from colorvariation import Color
from math import sqrt
import statistics
import operator

# Return Euclidean Difference between two colors
def EuclideanDifference(InputA, InputB):
	DeltaColorR,DeltaColorG,DeltaColorB = map(operator.sub,InputA.RGB,InputB.RGB)
	DeltaColor = sqrt(2 * (DeltaColorR ** 2) + 4 * (DeltaColorG ** 2) + 3 * (DeltaColorB **2))
	return DeltaColor

# Return a table of the Euclidean Difference between one Color control and a dictionnary of colors
def ListComparator(Control,List):
	return list(map(lambda x : EuclideanDifference(Control,x),List))

# Return a table of the Euclidean Difference between Black color, White color and a dictionnary of colors
def BlackWhiteComparator(List):
	Black = Color([0,0,0],"","")
	White = Color([255,255,255],"","")
	return list(map(lambda x: [round(EuclideanDifference(Black,x)),round(EuclideanDifference(White,x))],List))

# Return a table of 4 elements. 1st is the name of the colorspace, 2nd the average, 3rd the standard deviation, 4th the variance
def ResultStatistics(ColorSpace,List):
	return [ColorSpace,
	round(statistics.mean(List),2),
	round(statistics.stdev(List),2),
	round(statistics.variance(List),2)]


# Eliminate repetetive, similar colors and outlier colors
def ColorCleaning(ColorList,DifferenceList,MinTolerance,MaxTolerance):
	# Comprehension List [ResultElement for IterationElement in ElementList if Condition]
	# Zip merges 2 lists in one list with Tuples
	return list(set([x[0] for x in zip(ColorList,DifferenceList) if (x[1] >= MinTolerance) and (x[1] <= MaxTolerance)]))