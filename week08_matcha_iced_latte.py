from turtle import *

speed(0)
bgcolor("#f5eedc")   # cream background

def draw_polygon(sides, length):
    #Draw a polygon of "sides" sides
    for i in range(sides):
        forward(length)
        right(360 / sides)

def rectangle(x, y, width, height, colour):
    penup()
    goto(x, y)
    setheading(0)        # face right
    pendown()
    fillcolor(colour)
    begin_fill()
    for i in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()

def ice_cube(x, y, angle):
    penup()
    goto(x, y)
    setheading(angle)    # tilt the cube
    pendown()
    pencolor("#ffffff")
    fillcolor("#e8f4ec")
    begin_fill()
    draw_polygon(4, 32)
    end_fill()

# milk at the bottom, matcha on top
pencolor("#c8dca0")
rectangle(-80, -120, 160, 90, "#fbf8f0")
rectangle(-80, -30, 160, 100, "#8cb45a")

# ice cubes
ice_cube(-60, 60, 20)
ice_cube(-10, 40, -15)
ice_cube(35, 55, 40)
ice_cube(-40, 0, 10)

# straw
pencolor("#466e2d")
rectangle(25, -60, 14, 230, "#466e2d")

# glass outline
pensize(4)
pencolor("#1e2b17")
penup()
goto(-80, 120)
setheading(270)          # face down
pendown()
forward(240)
left(90)
forward(160)
left(90)
forward(240)

# title
penup()
goto(0, -170)
pencolor("#1e2b17")
write("NAT'CHO MATCHA - ICED LATTE", align="center", font=("Courier New", 12, "normal"))

hideturtle()
done()