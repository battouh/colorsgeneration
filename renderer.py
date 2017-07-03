from PIL import Image
from colorvariation import Color, NormalizeRgb

# Create, Save and Show an image with all variations of color
def ImageGeneration(List,Name):
	im = Image.new("RGB",(len(List)*10,len(List)*10))
	pix = im.load()
	for i in range(len(List)):
		for x in range(i*10,(i+1)*10):
			for y in range(len(List)*10):
				pix[x,y]=(List[i].RGB[0],List[i].RGB[1],List[i].RGB[2])
	im.save(Name + ".png","PNG")

# Convert RGB to Hex and return a string containing the hex value with the #
def RgbToHexConverter(ColorInput):
	R = NormalizeRgb(ColorInput.RGB[0])
	G = NormalizeRgb(ColorInput.RGB[1])
	B = NormalizeRgb(ColorInput.RGB[2])
	
	RHex = hex(R).replace("0x","").upper()
	GHex = hex(G).replace("0x","").upper()
	BHex = hex(B).replace("0x","").upper()

	HexList = [RHex,GHex,BHex]

	if len(HexList[0]) == 1:
		HexList[0] = "0" + HexList[0]
	if len(HexList[1]) == 1:
		HexList[1] = "0" + HexList[1]
	if len(HexList[2]) == 1:
		HexList[2] = "0" + HexList[2]

	Hex = "#" + HexList[0] + HexList[1] + HexList[2]
	return Hex
