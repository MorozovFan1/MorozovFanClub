from tkinter import *
from random import randrange as rnd, choice
import time
import math
import array
root = Tk()

c = Canvas(root, width=700, height=700, bg='white')
c.pack()
root.geometry('700x700')

colors = ['red','orange','yellow','green','blue']
Num = 0

m = rnd (3, 7)
n = 6

balls = [[0] * n for i in range (m)]
for i in range (m):
    balls[i][0] = rnd (50, 650)
    balls[i][1] = rnd (50, 650)
    balls[i][2] = rnd (-10, 10)
    balls[i][3] = rnd (-10, 10)
    balls[i][4] = rnd (20, 50)

def DrawBall (prop, counter):
    prop [counter][5] = c.create_oval(prop [counter][0] - prop [counter][4], prop [counter][1] - prop [counter][4], prop [counter][0] + prop [counter][4], prop [counter][1] + prop [counter][4], fill = choice (colors), width = 0)

def WallCollision ():
    global balls
    for i in range (len (balls)):
        if balls[i][0] + balls[i][4] >= 700 and balls [i][2] > 0:
            balls[i][2] = -balls[i][2]

        if balls[i][0] - balls[i][4] <= 0 and balls [i][2] < 0:
            balls[i][2] = -balls[i][2]

        if balls[i][1] + balls[i][4] >= 700 and balls [i][3] > 0:
            balls[i][3] = -balls[i][3]

        if balls[i][1] - balls[i][4] <= 0 and balls [i][3] < 0:
            balls[i][3] = -balls[i][3]

def MoveBall ():
    global balls
    for i in range (len(balls)):
        WallCollision()
        c.move (balls[i][5], balls[i][2], balls[i][3])
        balls[i][0] += balls[i][2]
        balls[i][1] += balls[i][3]


def Anime ():
    global balls
    MoveBall()
    root.after(30, Anime)

for i in range (m):
    DrawBall(balls, i)

def click (event):
    global balls
    global Num
    xe = event.x
    ye = event.y
    for i in range(len(balls)):
        if ((((xe - balls[i][0])**2) + (ye - balls[i][1])**2) <= ((balls[i][4])**2)):
            Num += 1
            print(Num)

Anime()
c.bind('<Button-1>', click)
mainloop()
