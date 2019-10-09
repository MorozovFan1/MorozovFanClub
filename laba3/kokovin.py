from graph import *
import math

counter = 0
t_fi = 0
t = 0
v1 = 5

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

def ellipse (x, y, a, b, fi):
    penSize (1)
    c = math.cos (math.radians(fi))
    d = math.sin (math.radians(fi))
    dots = []

    for i in range (-a, a):
        y1 = b * math.sqrt(1 - (i/a)**2)
        dots.append ((i * c - y1 * d + x, i * d + y1 * c + y))
    for i in range (a, -a, -1):
        y1 = -b * math.sqrt(1 - (i/a)**2)
        dots.append ((i * c - y1 * d + x, i * d + y1 * c + y))

    polygon (dots)

def ellipsee(x, y, a, b, fi):
    penColor('white')
    c=math.cos(fi)
    d=math.sin(fi)
    penSize(10)
    
    for i in range (-a,a, 5):
        v = (b**2-(i*b/a)**2)**0.5
        for j in range (-b,b, 5):
            
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
    penSize(10)
    
    for i in range (-a,a, 5):
        v = (b**2-(i*b/a)**2)**0.5
        for j in range (-b,b, 5):
            
            if  abs(j) <= v:
                x1 = i*c+j*d
                y1 = j*c-i*d
                x2 = x1+x
                y2 = y1+y
                
                point (x2, y2, -1)


def tree (x,y,h,l,m, fi_leaves):
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

    penColor(0, 100, 0)
    brushColor(0, 100, 0)

    ellipse(x + 3.3 * h, y - 16 * l / 18, int(h / 5), int(l / 3), -3437.75 + fi_leaves)
    ellipse(x + 4 * h, y - 19 * l / 18, int(h / 5), int(l / 3), -3437.75 + fi_leaves)
    ellipse(x + 4.8 * h, y - 18 * l / 18, int(h / 5), int(l / 3), -3437.75 + fi_leaves)
    ellipse(x + 5 * h, y - 38 * l / 18, int(h / 5), int(l / 3), -3437.75 + fi_leaves)
    ellipse(x + 5.8 * h, y - 40 * l / 18, int(h / 5), int(l / 3), -3437.75 + fi_leaves)
    ellipse(x + 6.6 * h, y - 42 * l / 18, int(h / 5), int(l / 3), -3437.75 + fi_leaves)
    ellipse(x + 7.4 * h, y - 44 * l / 18, int(h / 5), int(l / 3), -3437.75 + fi_leaves)
    ellipse(x + 8.4 * h, y - 43.5 * l / 18, int(h / 5), int(l / 3), -3437.75 + fi_leaves)

    ellipse(x - 2.7 * h, y - 7 * l / 18, int(h / 5), int(l / 3), 3437.75 + fi_leaves)
    ellipse(x - 2.1 * h, y - 6 * l / 18, int(h / 5), int(l / 3), 3437.75 + fi_leaves)
    ellipse(x - 3.3 * h, y - 26 * l / 18, int(h / 5), int(l / 3), 3437.75 + fi_leaves)
    ellipse(x - 3.9 * h, y - 28 * l / 18, int(h / 5), int(l / 3), 3437.75 + fi_leaves)
    ellipse(x - 4.7 * h, y - 31 * l / 18, int(h / 5), int(l / 3), 3437.75 + fi_leaves)
    ellipse(x - 5.4 * h, y - 32 * l / 18, int(h / 5), int(l / 3), 3437.75 + fi_leaves)
    ellipse(x - 6 * h, y - 32 * l / 18, int(h / 5), int(l / 3), 3437.75 + fi_leaves)



def panda(x, y, h):
    
    
    penColor('black')
    brushColor('black')
    polygon([(x-1.5*h,y),(x-1.3*h,y+1.5*h),(x-1.7*h,y+2*h),(x-2.5*h,y+1.7*h),(x-2.25*h,y+0.3*h)])
    ellipse(x-(2.25*h+2.5*h)/2, y+h, int(h/5), int(5*h/6), 19)
    ellipse(x-(1.7*h+2.5*h)/2, y+(1.7*h+2*h)/2, int(2*h/3), int(h/5), 20)
    brushColor(160,82,45)
    penColor(160,82,45)
    polygon([(x-1.3*h,y+1.5*h),(x-2.1*h,y+2.5*h),(x-1.2*h, y+2.1*h)])

    brushColor('white')
    penColor('white')
    ellipse (x,y,int(2*h),h,0)
    
    brushColor('black')
    penColor('black')
    polygon([(x+h/7,y-7*h/6),(x+h/7,y+7*h/6),(x,y+14*h/7),(x-h/2,y+17*h/7),(x-5*h/6,y+10*h/7)])
    brushColor('white')
    penColor('white')
    circle(x-h/8,y+2*h/3-h/8,h/4)
    polygon([(x,y+2*h/3),(x,y-2*h/3),(x-h,y-1.5*h),(x-2*h,y-2*h/3),(x-2*h, y+5*h/6)])
    brushColor('black')
    penColor('black')
    ellipse(x-(h/2+5*h/6)/2, y+(27*h/7)/2, int(1.2*h/2), int(h/2), 12*3.14/180)
    brushColor('white')
    penColor('white')
    ellipse(x, y, int(h/4), int(2*h/3), 0)
    
    ellipse(x-h/2, y-(1.5*h+2*h/3)/2, int(h/4), int(2*h/3+h/10), 40 * 180/math.pi)
    ellipse(x-1.5*h, y-(1.5*h+2*h/3)/2, int(h/4), int(2*h/3), -40 * 180/math.pi)
    ellipse(x-2*h, y-(2*h/3-5*h/6)/2, int(h/4), int(2*h/3+h/7), 0)
    ellipse(x-h, y+(5*h/6+2*h/3)/2, int(h/4), int(2*h/3+h/3), -88)
    
    
    circle(x-h-h/10, y+h/3-2*h/10, h/3)
    brushColor('black')
    penColor('black')
    ellipse (x-2*h, y+h/3-1.5*h/5, int(h/4), int(h/3), 0)
    ellipse (x-2*h+h/10, y+h-h/5, int(h/3), int(h/4), 0)
    ellipse (x-2*h+h/10, y-(5*h/6+2*h/3)/2-h/3, int(h/4), int(h/3+h/3), 40)
    ellipse (x, y-(5*h/6+2*h/3)/2-h/15, int(h/4), int(h/3+h/3), -30)
    
    circle(x-1.1*h,y+0.25*h,h/4)

    ellipse(x+1.2*h,y+1.3*h,int(1.3*h),int(0.5*h), -60)


def Anime ():

    global t
    global t_fi
    global counter
    brushColor(160, 82, 45)
    rectangle(0, 0, 600, 400)
    tree (270, 200, 20, 70, 100 + 10 * t_fi, v1 * t_fi)
    tree (170, 230, 8, 50, 200 + 10 * t_fi, v1 * t_fi)
    tree (70, 225, 12, 50, 250 + 10 * t_fi, v1 * t_fi)
    tree (510, 200, 9, 60, 300 + 10 * t_fi, v1 * t_fi)

    brushColor('white')
    penColor('white')
    panda(400 - t, 250, 40)
    panda(230, 330, 20 + t_fi)
    #ellipse(500, 500, 50,10, 30)
    #branch(400, 400, 0.001, -90, 60)

    penColor('black')
    #penSize(1)
    #for i in range (100):
    #polygon([(0,i*20),(2000,i*20)])
    #polygon([(i*20,0),(i*20, 2000)])
    if t_fi == 1:
        t_fi = -1
    else:
        t_fi = 1

    counter += 1
    t_fi = math.sin (counter)

    t += 1


onTimer (Anime, 20)
#oval (100, 100, 30, 30, 45)

run()
