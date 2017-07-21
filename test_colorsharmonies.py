# -*- coding: utf-8 -*-
import unittest
from colorvariation import Color
from colorsharmonies import complementaryColor, triadicColor, splitComplementaryColor

# Obtain the complementary color of a color

class colorsHarmonies(unittest.TestCase):
	def test_complementaryColor(self):
		MagentaColor = Color([255,0,255],"","")
		YellowColor = Color([255,255,0],"","")
		CyanColor = Color([0,255,255],"","")
		PurpleColor = Color([222,170,255],"","")
		self.assertEqual(complementaryColor(MagentaColor),[0,255,0])
		self.assertEqual(complementaryColor(YellowColor),[0,0,255])
		self.assertEqual(complementaryColor(CyanColor),[255,0,0])
		self.assertEqual(complementaryColor(PurpleColor),[203,255,170])

	def test_triadicColor(self):
		MagentaColor = Color([255,0,255],"","")
		YellowColor = Color([255,255,0],"","")
		CyanColor = Color([0,255,255],"","")
		PurpleColor = Color([222,170,255],"","")
		GreenColor = Color([176,230,66],"","")
		WhiteColor = Color([255,255,255],"","")
		self.assertIn([0,255,255],triadicColor(MagentaColor))
		self.assertIn([255,255,0],triadicColor(MagentaColor))
		self.assertIn([255,0,255],triadicColor(YellowColor))
		self.assertIn([0,255,255],triadicColor(YellowColor))
		self.assertIn([255,255,0],triadicColor(CyanColor))
		self.assertIn([255,0,255],triadicColor(CyanColor))
		self.assertIn([170,255,222],triadicColor(PurpleColor))
		self.assertIn([255,222,170],triadicColor(PurpleColor))
		self.assertIn([230,66,176],triadicColor(GreenColor))
		self.assertIn([66,176,230],triadicColor(GreenColor))
		self.assertIn([255,255,255],triadicColor(WhiteColor))

	def test_splitComplementaryColor(self):
		MagentaColor = Color([255,0,255],"","")
		YellowColor = Color([255,255,0],"","")
		CyanColor = Color([0,255,255],"","")
		PurpleColor = Color([222,170,255],"","")
		GreenColor = Color([176,230,66],"","")
		WhiteColor = Color([255,255,255],"","")
		self.assertIn([0,255,128],splitComplementaryColor(MagentaColor))
		self.assertIn([128,255,0],splitComplementaryColor(MagentaColor))
		self.assertIn([0,127,255],splitComplementaryColor(YellowColor))
		self.assertIn([127,0,255],splitComplementaryColor(YellowColor))
		self.assertIn([255,128,0],splitComplementaryColor(CyanColor))
		self.assertIn([255,0,128],splitComplementaryColor(CyanColor))
		self.assertIn([170,255,180],splitComplementaryColor(PurpleColor))
		self.assertIn([245,255,170],splitComplementaryColor(PurpleColor))
		self.assertIn([66,94,230],splitComplementaryColor(GreenColor))
		self.assertIn([202,66,230],splitComplementaryColor(GreenColor))
		self.assertIn([255,255,255],splitComplementaryColor(WhiteColor))

if __name__ == '__main__':
    unittest.main()