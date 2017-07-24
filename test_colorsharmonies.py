# -*- coding: utf-8 -*-
import unittest
from colorvariation import Color
from colorsharmonies import complementaryColor, triadicColor, splitComplementaryColor, tetradicColor

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
		self.assertEqual(sorted(triadicColor(MagentaColor)),sorted([[0,255,255],[255,255,0]]))
		self.assertEqual(sorted(triadicColor(YellowColor)),sorted([[255,0,255],[0,255,255]]))
		self.assertEqual(sorted(triadicColor(CyanColor)),sorted([[255,255,0],[255,0,255]]))
		self.assertEqual(sorted(triadicColor(PurpleColor)),sorted([[170,255,222],[255,222,170]]))
		self.assertEqual(sorted(triadicColor(GreenColor)),sorted([[230,66,176],[66,176,230]]))
		self.assertEqual(sorted(triadicColor(WhiteColor)),sorted([[255,255,255],[255,255,255]]))

	def test_splitComplementaryColor(self):
		MagentaColor = Color([255,0,255],"","")
		YellowColor = Color([255,255,0],"","")
		CyanColor = Color([0,255,255],"","")
		PurpleColor = Color([222,170,255],"","")
		GreenColor = Color([176,230,66],"","")
		WhiteColor = Color([255,255,255],"","")
		self.assertEqual(sorted(splitComplementaryColor(MagentaColor)),sorted([[0,255,128],[128,255,0]]))
		self.assertEqual(sorted(splitComplementaryColor(YellowColor)),sorted([[0,127,255],[127,0,255]]))
		self.assertEqual(sorted(splitComplementaryColor(CyanColor)),sorted([[255,128,0],[255,0,128]]))
		self.assertEqual(sorted(splitComplementaryColor(PurpleColor)),sorted([[170,255,180],[245,255,170]]))
		self.assertEqual(sorted(splitComplementaryColor(GreenColor)),sorted([[66,94,230],[202,66,230]]))
		self.assertEqual(sorted(splitComplementaryColor(WhiteColor)),sorted([[255,255,255],[255,255,255]]))

	def test_tetradicColor(self):
		MagentaColor = Color([255,0,255],"","")
		YellowColor = Color([255,255,0],"","")
		CyanColor = Color([0,255,255],"","")
		PurpleColor = Color([222,170,255],"","")
		GreenColor = Color([176,230,66],"","")
		WhiteColor = Color([255,255,255],"","")
		self.assertEqual(sorted(tetradicColor(MagentaColor)),sorted([[0,255,0],[0,255,255],[255,0,0]]))
		self.assertEqual(sorted(tetradicColor(YellowColor)),sorted([[0,0,255],[255,0,255],[0,255,0]]))
		self.assertEqual(sorted(tetradicColor(CyanColor)),sorted([[255,0,0],[255,255,0],[0,0,255]]))
		self.assertEqual(sorted(tetradicColor(PurpleColor)),sorted([[203,255,170],[170,255,222],[255,170,203]]))
		self.assertEqual(sorted(tetradicColor(GreenColor)),sorted([[120,66,230],[230,66,176],[66,230,120]]))
		self.assertEqual(sorted(tetradicColor(WhiteColor)),sorted([[255,255,255],[255,255,255],[255,255,255]]))

if __name__ == '__main__':
    unittest.main()