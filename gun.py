from random import randrange as rnd, choice
import tkinter as tk
import math
import time

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)


class ball():
    def __init__(self, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.g = 1
        self.lifetime = 5
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        self.live = 30

    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if not self.vx**2 + self.vy**2 < 0.001:
            self.vy += self.g

        else:
            self.vx = 0
            self.vy = 0
            self.lifetime -= 1

        if self.x + self.r >= 800 and self.vx > 0:
            self.vx = -self.vx/2
            self.vy = self.vy/2

        if self.x - self.r <= 0 and self.vx < 0:
            self.vx = -self.vx/2
            self.vy = self.vy/2

        if self.y + self.r >= 550 and self.vy > 0:
            self.vy = -self.vy/2
            self.vx = self.vx/2

        if self.y - self.r <= 0 and self.vy < 0:
            self.vy = -self.vy/2
            self.vx = self.vx/2

        self.x += self.vx
        self.y += self.vy
        self.set_coords()

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (self.x - obj.x)**2 + (self.y - obj.y)**2 < (self.r + obj.r)**2:
            return True
        return False

    def __del__(self):
        canv.delete(self.id)

class gun():
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20,450,50,420,width=7)

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = ball()
        new_ball.r += 5
        self.an = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y-450) / (event.x-20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class target():
    def __init__(self):
        self.points = 0
        self.live = 1
        self.id = canv.create_oval(0,0,0,0)
        #self.id_points = canv.create_text(30,30,text = self.points,font = '28')
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(20, 50)
        color = self.color = 'red'
        canv.coords(self.id, x-r, y-r, x+r, y+r)
        canv.itemconfig(self.id, fill=color)
        self.vx = rnd(3, 10)
        self.vy = rnd(3, 10)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)
        self.points += points
        #canv.itemconfig(self.id_points, text=self.points)

    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def move(self):
        if self.x + self.r >= 800 and self.vx > 0:
            self.vx = -self.vx
            self.vy = self.vy

        if self.x - self.r <= 0 and self.vx < 0:
            self.vx = -self.vx
            self.vy = self.vy

        if self.y + self.r >= 550 and self.vy > 0:
            self.vy = -self.vy
            self.vx = self.vx

        if self.y - self.r <= 0 and self.vy < 0:
            self.vy = -self.vy
            self.vx = self.vx


        self.x += self.vx
        self.y += self.vy
        self.set_coords()

    def __del__(self):
        canv.delete(self.id)

def Tcheck (t):
    """Проверка на наличие мячиков или целей в игре"""
    x = 0
    for i in range (len (t)):
        if t[i] != None:
            x += 1
    if x == 0:
        return 0
    else:
        return 1

def new_game(event=''):
    global screen1, balls, bullet, t
    targets_ammount = 4
    targets = [0] * targets_ammount
    for i in range(targets_ammount):
        targets[i] = target()
    screen1 = canv.create_text(400, 300, text='', font='28')
    g1 = gun()
    bullet = 0
    balls = []
    for i in range(targets_ammount):
        targets[i].new_target()
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)

    while Tcheck(targets) or Tcheck(balls):
        for t in targets:
            if t != None:
                t.move()
        for num, b in enumerate(balls):
            if b != None:
                b.move()
                for i in range(targets_ammount):
                    if targets[i] != None:
                        hittest_result = b.hittest(targets[i])
                        x = Tcheck(targets)
                        if hittest_result and x:
                            targets[i] = None
                        if Tcheck(targets) == 0:
                            canv.bind('<Button-1>', '')
                            canv.bind('<ButtonRelease-1>', '')
                            canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
                if balls[num].lifetime == 0:
                    balls[num] = None

        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
    canv.itemconfig(screen1, text='')
    canv.delete(g1.id)
    root.after(750, new_game)


new_game()

root.mainloop()
