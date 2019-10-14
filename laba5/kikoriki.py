from graph import *
import math
from random import randrange as rnd, choice
windowSize(800, 800)
canvasSize(800, 800)
width, height = windowSize()
t = 0

m = rnd (3, 7)
n = 6
balls = [[0] * n for i in range (m)]
for i in range (m):
    balls[i][0] = rnd (50, 750)
    balls[i][1] = rnd (50, 750)
    balls[i][2] = rnd (5, 7)
    balls[i][3] = rnd (5, 7)
    balls[i][4] = rnd (20, 50)
    balls[i][5] = "green"

movingballs = [[0] * n for i in range(m)]

def Ball (coord, counter):

    penColor(coord[counter][5])
    brushColor(coord[counter][5])
    circle(coord [counter][0], coord [counter][1], coord [counter][4])

#def Collision (balls):
#    {
#    for i in range (len (balls) - 1):
#        for j in range (i + 1, len (balls)):
#            l = (balls [i][0] - balls [j][0])** + (balls [i][1] - balls [j][1])**
#            if  (l <= (balls [i][]))
#    }

def WallCollision (coord):

    for i in range (len (coord)):
        if coord[i][0] + coord[i][4] >= 800 and coord [i][2] > 0:
            coord[i][2] = -coord[i][2]

        if coord[i][0] - coord[i][4] <= 0 and coord [i][2] < 0:
            coord[i][2] = -coord[i][2]

        if coord[i][1] + coord[i][4] >= 800 and coord [i][3] > 0:
            coord[i][3] = -coord[i][3]

        if coord[i][1] - coord[i][4] <= 0 and coord [i][3] < 0:
            coord[i][3] = -coord[i][3]

def Anime ():
    global balls
    global t


    brushColor("white")
    rectangle(0, 0, 800, 800)

    for i in range (m):
        balls [i] = [balls [i][0] + balls [i][2], balls [i][1] + balls [i][3], balls [i][2], balls [i][3],  balls [i][4], balls [i][5]]
        Ball(balls, i)
    t += 1
    WallCollision(balls)

onTimer (Anime, 20)

run()
