# -*- coding: utf-8 -*-
import unittest
from colorvariation import Color
from colorsharmonies import complementaryColor, triadicColor

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
		self.assertIn([0,255,255],triadicColor(MagentaColor))
		self.assertIn([255,255,0],triadicColor(MagentaColor))
		self.assertIn([255,0,255],triadicColor(YellowColor))
		self.assertIn([0,255,255],triadicColor(YellowColor))
		self.assertIn([255,255,0],triadicColor(CyanColor))
		self.assertIn([255,0,255],triadicColor(CyanColor))
		self.assertIn([170,255,222],triadicColor(PurpleColor))
		self.assertIn([255,222,170],triadicColor(PurpleColor))

if __name__ == '__main__':
    unittest.main()