from vpython import*
from shapely.geometry import Point, Polygon
import numpy as np
from functions import*
from render import*

print(type(random))

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
WallUp = Wall(wallcount,vec(0.0,5.5,0.0),10.0,10.0,1.0,vec(0.0,-1.0,0.0),vec(0.0,0.0,0.0),vector(230,195,195)/255,6, 0.0) 
wallcount += 1

Walls = set([Wallleft,Wallright,Walldown,Wallback,Wallfront, WallUp])

rt = shapes.rectangle(pos=(-2,2), width=5, height=5)

N = 0
t = 0
times = 100
dt = 1/times

#Fill Up the Container: 
fillUp(rt, 50, -5, 15)
print(len(Balls))


#Stimulation: 
while (t < 300):

    rate(times)

    
    for ball in Balls:
        for ball2 in Balls:
            if ball is ball2:
                #print("here1")
                pass

            elif ball.cc_distance(ball2) < ball.r + ball2.r and mag(ball.tempos - ball2.tempos) >\
                 mag(ball.tempos + ball.v * dt - ball2.tempos - ball2.v * dt):
                tmpv = ball.collision(ball2,Cr)
                ball2.v = ball2.collision(ball,Cr)
                ball.v = tmpv
                #print("here2")

        for i in Walls:
            ball.v = ball.wallreflection(i)
            #print("here4")
        
        ball.v = ball.v + vec(0.0,-9.8,0.0)*dt
        ball.tempos += ball.v * dt
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
