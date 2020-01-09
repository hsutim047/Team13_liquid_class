from vpython import*
from shapely.geometry import Point, Polygon
import numpy as np
from functions import*
from render import*


#Stimulation Initialize:
#scene = canvas(width=1400, height=800, fov = 0.03, align = 'left', center=vec(0.3, 0, 0), background=vec(0.5,0.5,0))


fps = 30.0


initialize()

wallcount = 0

Wallleft = Wall(wallcount,vec(-5.5,0.0,0.0),10.0,10.0,1.0,vec(1.0,0.0,0.0),vec(0.0,0.0,0.0),vector(230,195,195)/255,1)
wallcount += 1 
Wallright = Wall(wallcount ,vec(5.5,0.0,0.0),10.0,10.0,1.0,vec(-1.0,0.0,0.0),vec(0.0,0.0,0.0),vector(230,195,195)/255,2)
wallcount += 1
Walldown = Wall(wallcount, vec(0.0,-5.5,0.0),10.0,10.0,1.0,vec(0.0,1.0,0.0),vec(0.0,0.0,0.0),vector(230,195,195)/255,3)
wallcount += 1
Wallback = Wall(wallcount ,vec(0.0,0.0,-5.5),10.0,10.0,1.0,vec(0.0,0.0,1.0),vec(0.0,0.0,0.0),vector(230,195,195)/255,4)
wallcount += 1
Wallfront = Wall(wallcount,vec(0.0,0.0,5.5),10.0,10.0,1.0,vec(0.0,0.0,-1.0),vec(0.0,0.0,0.0),vector(230,195,195)/255,5,0.0) 
wallcount += 1
Walls = set([Wallleft,Wallright,Walldown,Wallback,Wallfront])

rt = shapes.star(n=5, radius=4)

N = 0
t = 0
times = 100
dt = 1/times

#Fill Up the Container: 
fillUp(rt, 25, -5, 70)
print(len(Balls))

#Stimulation: 
while (t < 20):

    rate(times)

    for ball in Balls:

        if t%(times//fps) == 0:
            Ball_writepos(ball.selfnumber,ball.tempos)
            #ball.sphere.pos = ball.tempos
            #print("here5")
    if t%(times//fps) == 0:
        refresh()
    t += 1

end()

while True: 
    animation()
