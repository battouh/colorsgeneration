# Color Generation

## Synopsis

Generate variations of a color and do some statistics and math.

On 3 different color spaces (RGB, HSV, HLS), we apply an algorithm to generate variations of a color. 
The algorithm is a basic application of an offset on each component of a color space.
From that, we get a list of variations where we do some statistics (average, standard deviation, variance) in order to evaluate the performance of the algorithm.
Last thing, we position each variation on a graph that represent their difference from the white color and their difference from the black color.

## Manual

Go to main.py and change the R, G and B value (0 to 255) of the variable TestColor

```
TestColor = Color([R,G,B],"","")
```

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



