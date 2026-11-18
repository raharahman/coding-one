#random walker
from turtle import *
import random

speed(0)
pencolor('#466e2d')

def random_walk(steps, step_size):
    for i in range(0, steps):
        setheading(random.choice([0, 90, 180, 270]))
        forward(step_size)

random_walk(300, 10)
done()
