#repeated circle spirograph
from turtle import *
import random

speed(0)

def spirograph(circles, radius):
    for i in range(circles):
        pencolor(random.choice(["#466e2d", "#8cb45a", "#f0be78", "#fac8d2"]))
        circle(radius)
        left(360/circles)

spirograph(36, 80)
done()