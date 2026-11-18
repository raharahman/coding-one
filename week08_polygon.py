from turtle import *

def draw_polygon(sides):
    #draw a polygon of "sides" sides
    # internal angle
    #(n-2) x 180 / n
    angle = 180 - ((sides - 2) * 180 / sides)

    #Draw a polygon of "sides" sides
    for i in range(0, sides):
        forward(10)
        right(angle)

penup()
pensize(5)
pencolor("green")
pendown()
#draw_polygon(4) #this draws a square
#draw_polygon(5) # this draws a pentagon
#draw_polygon(6) #this draws a hexagon
draw_polygon(40)

done()

