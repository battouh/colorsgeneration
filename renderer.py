from PIL import Image
import matplotlib.pyplot as plt

def ImageGeneration(Dict,Name):
	im = Image.new("RGB",(len(Dict)*10,len(Dict)*10))
	pix = im.load()
	for k,v in Dict.items():
		for x in range(k*10,(k+1)*10):
			for y in range(len(Dict)*10):
				pix[x,y]=(v.RGB[0],v.RGB[1],v.RGB[2])
	im.save(Name + ".png","PNG")
	im.show()

def GraphGeneration(List,Name):
	x = []
	y = []
	for i in range(len(List)):
		x.append(List[i][0])
		y.append(List[i][1])
	plt.plot(x,y, 'ro', markersize=4)
	plt.xlabel('Euclidean Difference to Black')
	plt.ylabel('Euclidean Difference to White')
	plt.title(Name)
	plt.show()