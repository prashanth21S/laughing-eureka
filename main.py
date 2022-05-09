# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings

import random
from turtle import Turtle, Screen
screen = Screen()
t = Turtle()
colors = ["light steel blue","cornflower blue","royal blue","green yellow","medium sea green","turquoise", "midnight blue", "dark sea green"]
dir = [0, 90, 180, 270]
t.shape("turtle")
t.pensize(10)
t.speed("fastest")

for i in range(200):
    t.color(random.choice(colors))
    t.forward(20)
    t.setheading(random.choice(dir))


screen.exitonclick()

