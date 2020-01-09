from vpython import*
from shapely.geometry import Point, Polygon
import numpy as np
import random
from Class import*

#Variables: 
nowVolume = 0 
Balls=set()
bs=0
ballcount = 0

#Functions: 
def transform(shapes): #transform Vpython Shape into Polygon 
    rtr=[] #Polygon Points List 
    for points in shapes:
        if all(isinstance(point, float) for point in points): #append point 
            rtr.append((points[0],points[1]))
        else:
            transform(points) 
    
    poly = Polygon(rtr) #turn the List into a Polygon object
    return poly
def fillUp(shapes, volume1, y_min, num=15):

    global nowVolume
    global Balls
    global bs
    global ballcount

    nowVolume = 0 
    
    polygon = transform(shapes)

    x_min, z_min, x_max, z_max = polygon.bounds
    
    
    #bs= np.sqrt((volume1*3/(5000*pi)))

    bs=(x_max-x_min)/num

    y = y_min+bs

    while (nowVolume-volume1)<=0.00001:
        for z in np.arange(z_min+bs,z_max-bs,bs*2):
            for x in np.arange(x_min+bs,x_max-bs,bs*2):
                point =  Point(x,z)
                if polygon.contains(point):
                    ball=Ball(ballcount,position=vec(x,y,z),r=bs,v=vector.random(),color = vec(0.4,1.0,1.0))
                    ballcount += 1
                    Balls.add(ball)
                    nowVolume+=4/3*pi*(bs)**3
                if (nowVolume-volume1)>=0.00001:
                    break
        y+=bs*2
