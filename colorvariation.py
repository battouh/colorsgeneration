# -*- coding: utf-8 -*-
import random
import colorsys

# Color is a class with 3 variables, one per color space.
# Each Color Space is represented as a table with 3 elements.
# For RGB, 1st element is R, 2nd element is G, 3rd element is B.
# For HLS, 1st element is H, 2nd element is L, 3rd element is S.
# For HSV, 1st element is H, 2nd element is S, 3rd element is V.

class Color:
	def __init__(self,RGB,HLS,HSV):
		self.RGB = RGB
		self.HLS = HLS
		self.HSV = HSV

def Normalize(Value,Min,Max):
	Output = Value
	if Value > Max:
		Output = Max
	elif Value < Min:
		Output = Min
	return Output

# From a RGB triplet, we generate variations of a color by applying an offset.
# The output is a dictionnary of variations.
def RgbVariation(ColorInput):
	ColorVariation = []
	for i in range(0,108,9):
		TupleAverage = (ColorInput.RGB[0] + ColorInput.RGB[1] + ColorInput.RGB[2])/3
		OffsetVariation = TupleAverage + 2 * random.random() * i - i
		Ratio = OffsetVariation / TupleAverage
		RGB = [Normalize(round(ColorInput.RGB[0] * Ratio),0,255),Normalize(round(ColorInput.RGB[1] * Ratio),0,255),Normalize(round(ColorInput.RGB[2] * Ratio),0,255)]
		ColorVariation.append(Color(RGB,"",""))
	return ColorVariation

# From a HSV triplet, we vary H between H +/- a tolerance and we apply an offset on S and V. 
# The output is a dictionnary of variations.
def HsvVariation(ColorInput,Tolerance):
	ColorVariation = []
	z = 0
	startingH = round(ColorInput.HSV[0] * 360) - Tolerance
	endingH = round(ColorInput.HSV[0] * 360) + Tolerance

	for j in range(startingH,endingH,5):
			TupleAverage = (ColorInput.HSV[1] * 100 + ColorInput.HSV[2] * 100)/2
			OffsetVariation = TupleAverage + 2 * random.random() * j/5 - j/5
			Ratio = OffsetVariation / TupleAverage
			HSV = [j, ColorInput.HSV[1] * Ratio * 100, ColorInput.HSV[2] * Ratio * 100]
			ColorVariation.append(Color("","",HSV))
			ColorVariation[z].RGB = list(colorsys.hsv_to_rgb(ColorVariation[z].HSV[0] / 360, ColorVariation[z].HSV[1] / 100, ColorVariation[z].HSV[2] / 100))
			ColorVariation[z].RGB = list(map(lambda v: Normalize(round(v*255)),ColorVariation[z].RGB),0,255)
			z+=1
	return ColorVariation

# From a HLS triplet, we vary H between H +/- a tolerance and we apply an offset on S and V. 
# The output is a dictionnary of variations.
def HlsVariation(ColorInput,Tolerance):
	ColorVariation = []
	z = 0
	startingH = round(ColorInput.HLS[0] * 360) - Tolerance
	endingH = round(ColorInput.HLS[0] * 360) + Tolerance

	for j in range(startingH,endingH,5):
			TupleAverage = (ColorInput.HLS[1] * 100 + ColorInput.HLS[2] * 100)/2
			OffsetVariation = TupleAverage + 2 * random.random() * j/5 - j/5
			Ratio = OffsetVariation / TupleAverage
			HLS = [j, ColorInput.HLS[1] * Ratio * 100, ColorInput.HLS[2] * Ratio * 100]
			ColorVariation.append(Color("",HLS,""))
			ColorVariation[z].RGB = list(colorsys.hls_to_rgb(ColorVariation[z].HLS[0] / 360 , ColorVariation[z].HLS[1] / 100, ColorVariation[z].HLS[2] / 100))
			ColorVariation[z].RGB = list(map(lambda v: Normalize(round(v*255)),ColorVariation[z].RGB),0,255)
			z+=1
	return ColorVariation




