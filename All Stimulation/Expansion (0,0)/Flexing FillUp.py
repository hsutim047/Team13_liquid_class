#Flexing fillup function 
from vpython import*
from shapely.geometry import Point, Polygon
import numpy as np
import random
from functions import*


rt = shapes.star(pos=(0,0),n=5, radius=100)

fillUp(rt, 100, -5)