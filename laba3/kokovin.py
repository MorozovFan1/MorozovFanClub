from graph import *
import math

windowSize(600, 400)
canvasSize(600, 400)
width, height = windowSize()

def branch(x, y, a, c1, c2):
    penSize(5)
    penColor(0, 100, 0)
    for i in range (c1,c2):
        c = a*i*i
        x1 = i+x
        y1 = c+y
        point (x1, y1, -1)

def ellipse(x, y, a, b, fi):
    penColor(0,100,0)
    c=math.cos(fi)
    d=math.sin(fi)
    penSize(2)
    
    for i in range (-a,a):
        v = (b**2-(i*b/a)**2)**0.5
        for j in range (-b,b):
    
            if  abs(j) <= v:
                x1 = i*c+j*d
                y1 = j*c-i*d
                x2 = x1+x
                y2 = y1+y
                
                point (x2, y2, -1)

def ellipsee(x, y, a, b, fi):
    penColor('white')
    c=math.cos(fi)
    d=math.sin(fi)
    penSize(2)
    
    for i in range (-a,a):
        v = (b**2-(i*b/a)**2)**0.5
        for j in range (-b,b):
            
            if  abs(j) <= v:
                x1 = i*c+j*d
                y1 = j*c-i*d
                x2 = x1+x
                y2 = y1+y
                
                point (x2, y2, -1)

def ellipseee(x, y, a, b, fi):
    penColor('black')
    c=math.cos(fi)
    d=math.sin(fi)
    penSize(2)
    
    for i in range (-a,a):
        v = (b**2-(i*b/a)**2)**0.5
        for j in range (-b,b):
            
            if  abs(j) <= v:
                x1 = i*c+j*d
                y1 = j*c-i*d
                x2 = x1+x
                y2 = y1+y
                
                point (x2, y2, -1)


def tree (x,y,h,l,m):
    penSize(3)
    
    penColor(0,100,0)
    brushColor(160, 82, 45)
    #circle(x+9*h, y-0.5*l, 50*l/18)
    brushColor(0,100,0)
    polygon([(x-0.2*h,y-22*l/18),(x+0.4*h, y-21*l/18),(x+h, y-33*l/18),(x+0.35*h, y-34*l/18)])
    polygon([(x+0.4*h,y-36*l/18),(x+0.7*h, y-35.2*l/18),(x+1.63*h, y-49*l/18),(x+1.3*h, y-50*l/18)])
    rectangle(x, y, x+h, y+l)
    rectangle(x, y-0.1*l, x+h, y-1.1*l)
    brushColor(160, 82 ,45)
    penSize(1)
    
    branch (x+4*h, y-26*l/18, 22*m/120000, int(-2.5*h), int(1.2*h))
    branch (x+8*h, y-50*l/18, 6*m/120000, int(-6.2*h), int(1.2*h))
    branch (x-2.4*h, y-13*l/18, 19*m/120000, int(-1.2*h), int(2.2*h))
    branch (x-5.5*h, y-38*l/18, 9*m/120000, int(-0.5*h), int(4.7*h))
    
    ellipse (x+3.3*h, y-16*l/18, int(h/5), int(l/3), 60)
    ellipse (x+4*h, y-19*l/18, int(h/5), int(l/3), 60)
    ellipse (x+4.8*h, y-18*l/18, int(h/5), int(l/3), 60)
    ellipse (x+5*h, y-38*l/18, int(h/5), int(l/3), 60)
    ellipse (x+5.8*h, y-40*l/18, int(h/5), int(l/3), 60)
    ellipse (x+6.6*h, y-42*l/18, int(h/5), int(l/3), 60)
    ellipse (x+7.4*h, y-44*l/18, int(h/5), int(l/3), 60)
    ellipse (x+8.4*h, y-43.5*l/18, int(h/5), int(l/3), 60)

    ellipse (x-3.3*h, y-6*l/18, int(h/5), int(l/3), -60)
    ellipse (x-2.7*h, y-7*l/18, int(h/5), int(l/3), -60)
    ellipse (x-2.1*h, y-6*l/18, int(h/5), int(l/3), -60)
    ellipse (x-3.3*h, y-26*l/18, int(h/5), int(l/3), -60)
    ellipse (x-3.9*h, y-28*l/18, int(h/5), int(l/3), -60)
    ellipse (x-4.7*h, y-31*l/18, int(h/5), int(l/3), -60)
    ellipse (x-5.4*h, y-32*l/18, int(h/5), int(l/3), -60)
    ellipse (x-6*h, y-32*l/18, int(h/5), int(l/3), -60)

def panda(x,y,h):
    
    
    penColor('black')
    brushColor('black')
    polygon([(x-1.5*h,y),(x-1.3*h,y+1.5*h),(x-1.7*h,y+2*h),(x-2.5*h,y+1.7*h),(x-2.25*h,y+0.3*h)])
    ellipseee(x-(2.25*h+2.5*h)/2, y+h, int(h/5), int(5*h/6), -19*3.14/180)
    ellipseee(x-(1.7*h+2.5*h)/2, y+(1.7*h+2*h)/2, int(2*h/3), int(h/5), (-20)*3.14/180)
    brushColor(160,82,45)
    penColor(160,82,45)
    polygon([(x-1.3*h,y+1.5*h),(x-2.1*h,y+2.5*h),(x-1.2*h, y+2.1*h)])

    brushColor('white')
    penColor('white')
    ellipsee(x,y,int(2*h),h,0)
    
    brushColor('black')
    penColor('black')
    polygon([(x+h/7,y-7*h/6),(x+h/7,y+7*h/6),(x,y+14*h/7),(x-h/2,y+17*h/7),(x-5*h/6,y+10*h/7)])
    brushColor('white')
    penColor('white')
    circle(x-h/8,y+2*h/3-h/8,h/4)
    polygon([(x,y+2*h/3),(x,y-2*h/3),(x-h,y-1.5*h),(x-2*h,y-2*h/3),(x-2*h, y+5*h/6)])
    ellipseee(x-(h/2+5*h/6)/2, y+(27*h/7)/2, int(1.2*h/2), int(h/2), 12*3.14/180)
    
    ellipsee(x, y, int(h/4), int(2*h/3), 0)
    
    ellipsee(x-h/2, y-(1.5*h+2*h/3)/2, int(h/4), int(2*h/3+h/10), -40)
    ellipsee(x-1.5*h, y-(1.5*h+2*h/3)/2, int(h/4), int(2*h/3), 40)
    ellipsee(x-2*h, y-(2*h/3-5*h/6)/2, int(h/4), int(2*h/3+h/7), 0)
    ellipsee(x-h, y+(5*h/6+2*h/3)/2, int(h/4), int(2*h/3+h/3), -88*3.14/180)
    
    
    circle(x-h-h/10, y+h/3-2*h/10, h/3)
    ellipseee(x-2*h, y+h/3-1.5*h/5, int(h/4), int(h/3), 0 )
    ellipseee(x-2*h+h/10, y+h-h/5, int(h/3), int(h/4), 0 )
    brushColor('black')
    ellipseee(x-2*h+h/10, y-(5*h/6+2*h/3)/2-h/3, int(h/4), int(h/3+h/3), -40*3.14/180)
    ellipseee(x, y-(5*h/6+2*h/3)/2-h/15, int(h/4), int(h/3+h/3), 30*3.14/180)
    
    circle(x-1.1*h,y+0.25*h,h/4)

    ellipseee(x+1.2*h,y+1.3*h,int(1.3*h),int(0.5*h), 60*3.14/180)


brushColor(160, 82, 45)
rectangle(0,0, 600,400)
tree (270, 200, 20, 70, 100)
tree (170, 230, 8, 50, 200)
tree (70, 225, 12, 50, 250)
tree (510, 200, 9, 60, 300)

brushColor('white')
penColor('white')
panda(400,250,40)
panda(230, 330, 20)
#ellipse(500, 500, 50,10, 30)
#branch(400, 400, 0.001, -90, 60)

penColor('black')
#penSize(1)
#for i in range (100):
#polygon([(0,i*20),(2000,i*20)])
#polygon([(i*20,0),(i*20, 2000)])

run()
