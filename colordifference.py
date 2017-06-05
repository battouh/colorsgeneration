from colorvariation import Color
from math import sqrt
import statistics

# Return Euclidean Difference between two colors
def EuclideanDifference(InputA, InputB):
	DeltaColorR = InputA.RGB[0] - InputB.RGB[0]
	DeltaColorG = InputA.RGB[1] - InputB.RGB[1]
	DeltaColorB = InputA.RGB[2] - InputB.RGB[2]
	DeltaColor = sqrt(2 * (DeltaColorR ** 2) + 4 * (DeltaColorG ** 2) + 3 * (DeltaColorB **2))
	return DeltaColor

# Return a table of the Euclidean Difference between one Color control and a dictionnary of colors
def ListComparator(Control,Dict):
	result = []
	for key in Dict:
		DeltaColor = EuclideanDifference(Control,Dict[key])
		result.append(DeltaColor)
	return result

# Return a table of the Euclidean Difference between Black color, White color and a dictionnary of colors
def BlackWhiteComparator(Dict):
	result = []
	Black = Color([0,0,0],"","")
	White = Color([255,255,255],"","")
	for key in Dict:
		DeltaBlack = round(EuclideanDifference(Black,Dict[key]))
		DeltaWhite = round(EuclideanDifference(White,Dict[key]))
		result.append([DeltaBlack,DeltaWhite])
	return result

# Return a table of 4 elements. 1st is the name of the colorspace, 2nd the average, 3rd the standard deviation, 4th the variance
def ResultStatistics(ColorSpace,List):
	result = [ColorSpace,"","",""]
	result[1] = round(statistics.mean(List),2)
	result[2] = round(statistics.stdev(List),2)
	result[3] = round(statistics.variance(List),2)
	return result


