from turtle import *
import time 
import random
from pygame import *

colors=['cyan','yellow','blue']
n=45
speed(0)
pensize(2)
bgpic("snow.gif")

mixer.init()
mixer.music.load('jingle bells.mp3')
mixer.music.play()
penup()
goto(0, -130)
pendown()
left(90)
forward(3*n)
color=["blue"]
begin_fill()
left(126)
for i in range(5):
    forward(n/5)
    right(144)
    forward(n/5)
    left(72)
end_fill()
right(126)
color=["white"]
backward(n*4.8)
def tree(d, s):
    pensize(4)
    if d<= 0:
        return
    forward(s)
    tree(d-1, s*.8)
    right(120)
    tree(d-3, s*.6)
    right(120)
    tree(d-3, s*.6)
    right(120)
    backward(s)

def length_select():
    return random.randint(3, 8)

def stars(x,y):
    hideturtle()
    col=random.choice(color)
    l=length_select()
    color(col)
    penup()
    goto(x,y)
    pendown()
    begin_fill()
    for i in range(5):
        forward(1)
        right(144)
        forward(1)


tree(12,n)
backward(n/2)
color=["ligth yellow"]
begin_fill()
penup()
goto(-180,240)
pendown()
circle(25)
end_fill()


pensize(2)
onscreenclick(stars,1) #left mouse click
# star 2 parameter x,y
def m(col):
    speed(25)
    color=[col]
    #left(90)
    forward(30)
    right(135)
    #right(45)
    forward(25)
    left(90)
    forward(25)
    right(135)
    forward(30)

def e(col):
    penup()
    left(90)
    forward(20)
    pendown()
    color=[col]
    forward(15)
    backward(15)
    left(90)
    forward(30)
    right(90)
    forward(15)
    penup()
    right(90)
    forward(15)
    pendown()
    right(90)
    forward(15)

def r(col):
    penup()
    forward(20)
    pendown()
    color=[col]
    left(90)
    forward(30)
    right(90)
    forward(15)
    right(90)
    forward(15)
    right(90)
    forward(15)
    left(135)
    forward(21)
    left(45)

def y(col):
    penup()
    forward(25)
    pendown()
    color=[col]
    left(90)
    forward(15)
    left(45)
    forward(18)
    backward(18)
    right(90)
    forward(18)

def x(col):
    penup()
    goto(30, 170)
    pendown()
    color=[col]
    forward(38)
    backward(19)
    left(90)
    forward(19)
    backward(19)
    left(180)
    forward(19)

def a(col):
    penup()
    left(90)
    forward(18)
    pendown()
    color=[col]
    left(70)
    forward(33)
    right(140)
    forward(33)
    backward(12)
    right(110)
    forward(13)
    backward(13)
    left(110)
    forward(12)
    left(70)

def s(col):
    penup()
    forward(20)
    pendown()
    color=[col]
    forward(15)
    left(90)
    forward(15)
    left(90)
    forward(15)
    right(90)
    forward(15)
    right(90)
    forward(15)

penup()
#tree base to letter
left(90)
forward(100)
right(90)
pensize(7)
goto(-95, 235)
pendown()
m("red")

e("white")
penup()
left(90)
forward(15)
left(90)
forward(15)
pendown()

r("green")
r("red")
y("white")

x("white")
left(45)
penup()
forward(20)
left(90)
pendown()
m("red")
a("white")
s("red")
pensize(2)


done()




















