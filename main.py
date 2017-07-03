
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.colorchooser import *
from computer import ColorComputing
from renderer import RgbToHexConverter

# Generate a list of color variation from colorpicker input and clean on the same time the application before displaying new color variations.
def GenerateColorVariations():
      print("RGB: %s,%s,%s with ToleranceMin = %s and ToleranceMax = %s" % (RInput.get(),GInput.get(),BInput.get(),ToleranceMinInput.get(),ToleranceMaxInput.get()))

      ColorList = ColorComputing(int(RInput.get()),int(GInput.get()),int(BInput.get()),int(ToleranceMinInput.get()),int(ToleranceMaxInput.get()))
      height = len(ColorList)

      global GridContent
      for element in GridContent:
            element.destroy()
      GridContent = []
      for i in range(height):
                  a = Frame(Grid, bd=3)
                  a.config(width=15, height=15, background = RgbToHexConverter(ColorList[i]))
                  a.grid(row=i,column=1)
                  b = Label(Grid, bd=3, text = " (" + str(ColorList[i].RGB[0]) + "," + str(ColorList[i].RGB[1]) + "," + str(ColorList[i].RGB[2]) + ")")
                  b.grid(row=i,column=2)
                  GridContent.append(a)
                  GridContent.append(b)

# Get color from the system colorpicker
def getColor():
      RInput.delete(0,END)
      GInput.delete(0,END)
      BInput.delete(0,END)

      colorpicker = askcolor() 

      RInput.insert(1,round(colorpicker[0][0]))
      GInput.insert(1,round(colorpicker[0][1]))
      BInput.insert(1,round(colorpicker[0][2]))
      ColorSquare.config(background = colorpicker[1])

####### APPLICATION GUI #######

master = Tk()
window = Frame(master)
window.pack()

# Split the window in two rows
RowTop = Frame(window)
RowTop.pack(side=TOP)
RowBottom = Frame(window)
RowBottom.pack(side=TOP)

# Split RowTop in 2 columns
ColumnCenter = Frame(RowTop, bd=10)
ColumnCenter.pack(side=LEFT)
ColumnRight = Frame(RowTop, bd=10)
ColumnRight.pack(side=LEFT)

# Split ColumnCenter in 7 rows
ColumnCenterRow1 = Frame(ColumnCenter)
ColumnCenterRow1.pack(side=TOP)
ColumnCenterRow2 = Frame(ColumnCenter)
ColumnCenterRow2.pack(side=TOP)
ColumnCenterRow3 = Frame(ColumnCenter)
ColumnCenterRow3.pack(side=TOP)
ColumnCenterRow4 = Frame(ColumnCenter)
ColumnCenterRow4.pack(side=TOP)
ColumnCenterRow5 = Frame(ColumnCenter)
ColumnCenterRow5.pack(side=TOP)
ColumnCenterRow6 = Frame(ColumnCenter)
ColumnCenterRow6.pack(side=TOP)
ColumnCenterRow7 = Frame(ColumnCenter)
ColumnCenterRow7.pack(side=TOP)

# Content of RowTop.ColumnCenter
# Title
ParametersLabel = Label(ColumnCenterRow1, text="Parameters")
ParametersLabel.pack()
# Button to select a Color. It opens the colorpicker
ColorButton = Button(ColumnCenterRow2, text='Select Color', command=getColor)
ColorButton.pack(side = LEFT)
# Display the color selected via the colorpicker
ColorSquare = Frame(ColumnCenterRow2, width=15, height=15)
ColorSquare.pack(side = RIGHT)
# Entry to input the R value of a color. Automatically filled by the colorpicker
RInputLabel = Label(ColumnCenterRow3, text="R")
RInputLabel.pack(side=LEFT)
RInput = Entry(ColumnCenterRow3)
RInput.pack(side=LEFT)
# Entry to input the G value of a color. Automatically filled by the colorpicker
GInputLabel = Label(ColumnCenterRow4, text="G")
GInputLabel.pack(side=LEFT)
GInput = Entry(ColumnCenterRow4)
GInput.pack(side=LEFT)
# Entry to input the B value of a color. Automatically filled by the colorpicker
BInputLabel = Label(ColumnCenterRow5, text="B")
BInputLabel.pack(side=LEFT)
BInput = Entry(ColumnCenterRow5)
BInput.pack(side=LEFT)
# Entry to input a tolerance to eliminate similar colors from the input
ToleranceMinInputLabel = Label(ColumnCenterRow6, text="Tolerance Min")
ToleranceMinInputLabel.pack(side=LEFT)
ToleranceMinInput = Scale(ColumnCenterRow6, from_=0, to= 400, orient=HORIZONTAL)
ToleranceMinInput.pack(side=LEFT)
ToleranceMinInput.set(10)
# Entry to input a tolerance to eliminate outliers colors from the input
ToleranceMaxInputLabel = Label(ColumnCenterRow7, text="Tolerance Max")
ToleranceMaxInputLabel.pack(side=LEFT)
ToleranceMaxInput = Scale(ColumnCenterRow7, from_=0, to= 400, orient=HORIZONTAL)
ToleranceMaxInput.pack(side=LEFT)
ToleranceMaxInput.set(200)

# Content of RowTop.ColumnRight
# Grid that will contain the list of colors generated via the algorithm
global Grid
global GridContent
GridContent = []
Grid = Frame(ColumnRight)
Grid.pack()

# Content of RowBottom
# Button to exit the program
ExitButton = Button(RowBottom, text="Quit", command=window.quit)
ExitButton.pack(side=LEFT)
# Button to generate a list of color variations from the input and tolerances and display in on the GUI
GenerateButton = Button(RowBottom, text="Generate", command=GenerateColorVariations)
GenerateButton.pack(side = LEFT)

mainloop()