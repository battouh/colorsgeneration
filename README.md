# Color Generation

## Synopsis

Generate variations of a color input via a GUI.

On 3 different color spaces (RGB, HSV, HLS), we apply an algorithm to generate variations of a color. 
The algorithm is a basic application of an offset on each component of a color space.
From that, we get a list of variations. we evaluated the euclidean difference from the color input to eliminate repetitive, similar colors and outlier colors based on tolerances input by the user on the GUI.

## Manual

Go to your console

```
python3 main.py
```

## Installation

Code running with Python 3.x

We recommend to create a virtual environment:

with virtualenv
```
cd colors-generation
virtualenv vEnv --no-site-packages -p python3
source vEnv/bin/activate
pip install -r requirements.txt
```
with Python's venv (better for Mac OSX)
```
cd colors-generation
python3 -m venv vEnv
source vEnv/bin/activate
pip install -r requirements.txt
```



