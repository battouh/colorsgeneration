import colorsys
from colorvariation import Color, RgbVariation, HsvVariation, HlsVariation
from renderer import ImageGeneration, GraphGeneration
from colordifference import ListComparator, BlackWhiteComparator, ResultStatistics
from terminaltables import AsciiTable

TestColor = Color([43,84,115],"","")

# Convert RGB (base 256) to HSV (between 0 and 1 )
TestColor.HSV = list(colorsys.rgb_to_hsv(TestColor.RGB[0] / 255, TestColor.RGB[1] / 255, TestColor.RGB[2] / 255))

# Convert RGB (base 256) to HSV (between 0 and 1 )
TestColor.HLS = list(colorsys.rgb_to_hls(TestColor.RGB[0] / 255, TestColor.RGB[1] / 255, TestColor.RGB[2] / 255))

# Generate Color variations using the RGB Color space
RgbDict = RgbVariation(TestColor)

# Generate Color variations using the HSV Color space with 30° tolerance on H
HsvDict = HsvVariation(TestColor,30)

# Generate Color variations using the HLS Color space with 30° tolerance on H
HlsDict = HlsVariation(TestColor,30)

# Create an image with all color variations
ImageGeneration(RgbDict,"RGB")
ImageGeneration(HsvDict,"HSV")
ImageGeneration(HlsDict,"HLS")

# Calculate the Euclidean difference between the color reference and the color variations
RgbDifference = ListComparator(TestColor,RgbDict)
HsvDifference = ListComparator(TestColor,HsvDict)
HlsDifference = ListComparator(TestColor,HlsDict)

# Calculate Euclidean difference average, Stdev and variance for each Color Space Variation
TableData = [["Color Space Variation","Euclidean Difference Average","Euclidean Difference Stdev"," Euclidean Difference Variance"],"","",""]
TableData[1] = ResultStatistics("RGB",RgbDifference)
TableData[2] = ResultStatistics("HSV",HsvDifference)
TableData[3] = ResultStatistics("HLS",HlsDifference)

# Create result table to be displayed via the console
Result = AsciiTable(TableData)

# Calculate Euclidean Difference between Black color, White color and a dictionnary of colors
RgbBlackWhiteDifference = BlackWhiteComparator(RgbDict)
HsvBlackWhiteDifference = BlackWhiteComparator(HsvDict)
HlsBlackWhiteDifference = BlackWhiteComparator(HlsDict)

GraphGeneration(RgbBlackWhiteDifference,"RGB")
GraphGeneration(HsvBlackWhiteDifference,"HSV")
GraphGeneration(HlsBlackWhiteDifference,"HLS")

print (Result.table)