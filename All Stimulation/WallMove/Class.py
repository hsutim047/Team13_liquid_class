from vpython import*
import numpy as np
import random
from render import*

Cr=0.47

def length(v):
    return (((v.x)**2 + (v.y)**2 + (v.z)**2)**0.5)


class obj():
    pass 
class Wall():
    
    def __init__(self,selfnumber, pos = vector(0.0, 0.0, 0.0), length = 10.0, height = 10.0, width = 10.0 ,up = vec(0.0,0.0,0.0),axis = vec(0.0,0.0,0.0),color = vec(1.0,1.0,1.0),H = 0,opacity = 1.0):
        #self.box = box(pos = pos, size = vector(length, width, height), opacity = opacity, color = vector(230,195,195)/255, up = up,axis = axis)
        self.pos = pos
        self.size = vec(length,width,height)
        self.up = up
        self.axis = axis
        Wall_writedata(selfnumber,pos,self.size,up,axis,opacity,color)
        self.selfnumber = selfnumber
        self.collisionable = True
        self.hash = H
        self.a=vec(0.0,0.0,0.0)
        self.v=vec(0.0,0.0,0.0)

    def __hash__(self):
        return self.hash

class Ball():
    
    def __init__(self,selfnumber,position = vector(0.0, 0.0, 0.0), r = 0.5, v = vector(1.0, 1.0, 1.0),color = vec(1.0,1.0,1.0), mass = 10.0,H = 0):
        self.wallfinish = True
        self.m = mass
        self.tempos = position 
        self.r  = r
        Ball_writedata(selfnumber,position,r,color)
        self.selfnumber = selfnumber
        self.collisionable = True
        self.v = v
        self.hash = H
        
    def cc_distance(self, self2): # circle center
        p1 = (self.tempos.x - self2.tempos.x) ** 2
        p2 = (self.tempos.y - self2.tempos.y) ** 2
        p3 = (self.tempos.z - self2.tempos.z) ** 2
        return (p1 + p2 + p3) ** 0.5
    

    def collision(self,self2,cr):
        v1 = self.v + dot((self2.v - self.v), (self.tempos - self2.tempos)) /\
             mag2(self.tempos - self2.tempos) * (self.tempos - self2.tempos)
        return v1

    def wallreflection(self,wall):
        a = (self.tempos - wall.pos).norm()
        b = (wall.up).norm()
        c = (wall.axis).norm()
        #tempv=self.v-wall.v

        #print(np.abs(length(self.tempos - wall.box.pos)*(a.x*b.x + a.y*b.y + a.z*b.z)))
        
        if np.abs(length(self.tempos - wall.pos*1.5)*(a.x*b.x + a.y*b.y + a.z*b.z)) < wall.size.y :
            
            if self.wallfinish is True:
                self.wallfinish = False
                b*length(self.v)
                c = self.v + b
                d = -self.v
                return Cr*(d + 2*c+wall.v)
            else:
                return self.v

        else:
            self.wallfinish = True
            return self.v

    def __hash__(self):
        return self.hash
