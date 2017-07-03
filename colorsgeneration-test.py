import unittest
from colorvariation import Color, NormalizeRgb
from colordifference import EuclideanDifference, ListComparator, BlackWhiteComparator, ResultStatistics, ColorCleaning
from renderer import RgbToHexConverter

class ColorDifference(unittest.TestCase):

    def test_EuclideanDifference_Generic(self):
        ColorA = Color([43,84,115],"","")
        ColorB = Color([15,100,270],"","")
        self.assertEqual(EuclideanDifference(ColorA,ColorB), 273.25263036245417)

    def test_EuclideanDifference_SameColors(self):
        ColorA = Color([43,84,115],"","")
        ColorB = Color([43,84,115],"","")
        self.assertEqual(EuclideanDifference(ColorA,ColorB), 0)

    def test_EuclideanDifference_NullColor(self):
        ColorA = Color([43,84,115],"","")
        ColorB = Color([0,0,0],"","")
        self.assertEqual(EuclideanDifference(ColorA,ColorB), 267.5761573832766)

    def test_EuclideanDifference_NegativeValue(self):
        ColorA = Color([43,84,115],"","")
        ColorB = Color([-15,-100,200],"","")
        self.assertEqual(EuclideanDifference(ColorA,ColorB), 404.7554817417548)

    def test_ListComparator(self):
        ColorReference = Color([43,84,115],"","")
        ColorA = Color([15,100,270],"","")
        ColorB = Color([0,70,245],"","")
        ColorList = [ColorA,ColorB]
        self.assertEqual(ListComparator(ColorReference,ColorList), [273.25263036245417,234.90849282220512])

    def test_BlackWhiteComparator(self):
        ColorA = Color([15,100,270],"","")
        ColorB = Color([0,70,245],"","")
        ColorList = [ColorA,ColorB]
        self.assertEqual(BlackWhiteComparator(ColorList),[[509,460],[447,517]])

    def test_ResultStatistics(self):
        self.assertEqual(ResultStatistics("Test",[2.15,5,8.6,-2]), ["Test", 3.44, 4.48, 20.11])

    def test_ColorCleaning(self):
        ListA = ["A","B","C","D","E","F","G"]
        ListB = [10,3,-5,40,98.5,100,19]
        self.assertEqual(ColorCleaning(ListA,ListB,-1,56.4),["A","B","D","G"])
        self.assertIn("D",ColorCleaning(ListA,ListB,0,40))
        self.assertNotIn("C",ColorCleaning(ListA,ListB,0,40))
        self.assertIn("E",ColorCleaning(ListA,ListB,98.5,98.5))
        self.assertNotIn("F",ColorCleaning(ListA,ListB,98.5,98.5))

    def test_RgbToHexConverter(self):
        ColorA = Color([15,100,270],"","")
        ColorB = Color([-10,0,255],"","")
        self.assertEqual(RgbToHexConverter(ColorA),"#0F64FF")
        self.assertEqual(RgbToHexConverter(ColorB),"#0000FF")

    def test_NormalizeRgb(self):
        self.assertEqual(NormalizeRgb(-5),0)
        self.assertEqual(NormalizeRgb(0),0)
        self.assertEqual(NormalizeRgb(5),5)
        self.assertEqual(NormalizeRgb(255),255)
        self.assertEqual(NormalizeRgb(270),255)


if __name__ == '__main__':
    unittest.main()