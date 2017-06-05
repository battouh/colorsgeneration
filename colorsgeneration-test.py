import unittest
from colorvariation import Color
from colordifference import EuclideanDifference, ListComparator, BlackWhiteComparator, ResultStatistics

class ColorDifference(unittest.TestCase):

    def test_EuclideanDifference_SameColors(self):
        ColorA = Color([43,84,115],"","")
        ColorB = Color([43,84,115],"","")
        self.assertEqual(EuclideanDifference(ColorA,ColorB), 0)

    def test_EuclideanDifference_Generic(self):
        ColorA = Color([43,84,115],"","")
        ColorB = Color([15,100,270],"","")
        self.assertEqual(EuclideanDifference(ColorA,ColorB), 273.25263036245417)

    def test_ListComparator(self):
        ColorReference = Color([43,84,115],"","")
        ColorA = Color([15,100,270],"","")
        ColorB = Color([0,70,245],"","")
        ColorDict = {"1": ColorA, "2": ColorB}
        self.assertEqual(ListComparator(ColorReference,ColorDict), [273.25263036245417,234.90849282220512])

    def test_BlackWhiteComparator(self):
        ColorA = Color([15,100,270],"","")
        ColorB = Color([0,70,245],"","")
        ColorDict = {"1": ColorA, "2": ColorB}
        self.assertEqual(BlackWhiteComparator(ColorDict),[[509,460],[447,517]])

    def test_ResultStatistics(self):
        self.assertEqual(ResultStatistics("Test",[2.15,5,8.6,-2]), ["Test", 3.44, 4.48, 20.11])

if __name__ == '__main__':
    unittest.main()