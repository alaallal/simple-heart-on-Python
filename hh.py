import turtle
import math
t = turtle
def heart1(a):
    return 15*math.sin(a)**3
def heart2(a):
    return 12*math.cos(a)-5*math.cos(2*a)-2*math.cos(3*a)- math.cos(4*a)
t.speed(0)
t.bgcolor("black")
for i in range(6000):
    t.goto(heart1(i)*25, heart2(i)* 25)
    for j in range(1):
        t.color("red")
    t.goto(0,0)
t.done()