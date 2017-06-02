import random
import colorsys

class Color:
	def __init__(self,RGB,HLS,HSV):
		self.RGB = RGB
		self.HLS = HLS
		self.HSV = HSV

def RgbVariation(ColorInput):
	ColorVariation = {}
	z = 0
	for i in range(0,252,21):
		TupleAverage = (ColorInput.RGB[0] + ColorInput.RGB[1] + ColorInput.RGB[2])/3
		OffsetVariation = TupleAverage + 2 * random.random() * i - i
		Ratio = OffsetVariation / TupleAverage
		RGB = [round(ColorInput.RGB[0] * Ratio),round(ColorInput.RGB[1] * Ratio),round(ColorInput.RGB[2] * Ratio)]
		ColorVariation[z] = Color(RGB,"","")
		z += 1
	return ColorVariation

def HsvVariation(ColorInput,Tolerance):
	ColorVariation = {}
	z = 0
	startingH = round(ColorInput.HSV[0] * 360) - Tolerance
	endingH = round(ColorInput.HSV[0] * 360) + Tolerance

	for j in range(startingH,endingH,5):
			TupleAverage = (ColorInput.HSV[1] * 100 + ColorInput.HSV[2] * 100)/2
			OffsetVariation = TupleAverage + 2 * random.random() * j/5 - j/5
			Ratio = OffsetVariation / TupleAverage
			HSV = [j, ColorInput.HSV[1] * Ratio * 100, ColorInput.HSV[2] * Ratio * 100]
			ColorVariation[z] = Color("","",HSV)
			ColorVariation[z].RGB = list(colorsys.hsv_to_rgb(ColorVariation[z].HSV[0] / 360, ColorVariation[z].HSV[1] / 100, ColorVariation[z].HSV[2] / 100))
			ColorVariation[z].RGB = list(map(lambda v: round(v*255),ColorVariation[z].RGB))
			z+=1
	return ColorVariation

def HslVariation(ColorInput,Tolerance):
	ColorVariation = {}
	z = 0
	startingH = round(ColorInput.HLS[0] * 360) - Tolerance
	endingH = round(ColorInput.HLS[0] * 360) + Tolerance

	for j in range(startingH,endingH,5):
			TupleAverage = (ColorInput.HLS[1] * 100 + ColorInput.HLS[2] * 100)/2
			OffsetVariation = TupleAverage + 2 * random.random() * j/5 - j/5
			Ratio = OffsetVariation / TupleAverage
			HLS = [j, ColorInput.HLS[1] * Ratio * 100, ColorInput.HLS[2] * Ratio * 100]
			ColorVariation[z] = Color("",HLS,"")
			ColorVariation[z].RGB = list(colorsys.hls_to_rgb(ColorVariation[z].HLS[0] / 360 , ColorVariation[z].HLS[1] / 100, ColorVariation[z].HLS[2] / 100))
			ColorVariation[z].RGB = list(map(lambda v: round(v*255),ColorVariation[z].RGB))
			z+=1
	return ColorVariation